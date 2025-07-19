# DnD DM 工具範例

此倉庫包含簡易的 DnD 管理腳本，用於示範如何儲存模組與角色資料。

## 目錄結構
- `modules/`：存放冒險模組列表。
- `data/characters.json`：玩家角色資料。
- `tools/dm_manager.py`：管理腳本，可列出模組、建立角色與查看角色。

## 使用方式

列出模組：
```bash
python tools/dm_manager.py list-modules
```

建立角色：
```bash
python tools/dm_manager.py create-char --name 名稱 --race 種族 
  --cls 職業 --level 等級
```

查看現有角色：
```bash
python tools/dm_manager.py list-chars
```
