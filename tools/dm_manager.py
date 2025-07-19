import argparse
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
MODULES_FILE = os.path.join(BASE_DIR, 'modules', 'modules.json')
CHAR_FILE = os.path.join(DATA_DIR, 'characters.json')


def load_json(path):
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def list_modules():
    modules = load_json(MODULES_FILE)
    for idx, mod in enumerate(modules, 1):
        print(f"{idx}. {mod['name']} - {mod['description']}")


def list_characters():
    chars = load_json(CHAR_FILE)
    if not chars:
        print('尚無角色。')
    for idx, c in enumerate(chars, 1):
        print(f"{idx}. {c['name']} ({c['race']} {c['cls']})")


def create_character(args):
    chars = load_json(CHAR_FILE)
    char = {
        'name': args.name,
        'race': args.race,
        'cls': args.cls,
        'level': args.level
    }
    chars.append(char)
    save_json(CHAR_FILE, chars)
    print(f"已創建角色 {args.name}")


def main():
    parser = argparse.ArgumentParser(description='簡易DnD DM管理工具')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('list-modules', help='列出可用模組')
    subparsers.add_parser('list-chars', help='列出角色')

    cparser = subparsers.add_parser('create-char', help='建立角色')
    cparser.add_argument('--name', required=True, help='角色名稱')
    cparser.add_argument('--race', required=True, help='種族')
    cparser.add_argument('--cls', required=True, help='職業')
    cparser.add_argument('--level', type=int, default=1, help='等級')

    args = parser.parse_args()
    if args.command == 'list-modules':
        list_modules()
    elif args.command == 'list-chars':
        list_characters()
    elif args.command == 'create-char':
        create_character(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
