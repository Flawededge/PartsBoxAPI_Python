# PartsBoxAPI

PartsBoxAPI is a Python client library for interacting with the PartsBox API. It provides a modular and easy-to-use interface for managing parts, stock, projects, and more.

## Installation

```bash
pip install -e .
```

## Usage

```python
from PartsBoxAPI import PartsBoxAPI

api = PartsBoxAPI(api_key='your_api_key')
parts = api.get_all_parts()
print(parts)
```

## Modules
If it's checked, that means that the function has been implemented and has tests which work

### [Parts](https://partsbox.com/api.html#parts)
- [ ] [`part/get`](https://partsbox.com/api.html#part-get)
- [ ] [`part/all`](https://partsbox.com/api.html#part-all)
- [ ] [`part/create`](https://partsbox.com/api.html#part-create)
  - [x] `part/create` - Local part
  - [x] `part/create` - Meta part
  - [ ] `part/create` - Linked part - Not possible as of yet via API *(You will need to create a local part first then use the UI to link it manually.)*
  - [ ] `part/create` - Sub-assembly
- [ ] [`part/update`](https://partsbox.com/api.html#part-update)
- [ ] [`part/delete`](https://partsbox.com/api.html#part-delete)
- [ ] [`part/add-meta-part-ids`](https://partsbox.com/api.html#part-add-meta-part-ids)
- [ ] [`part/remove-meta-part-ids`](https://partsbox.com/api.html#part-remove-meta-part-ids)
- [ ] [`part/add-substitute-ids`](https://partsbox.com/api.html#part-add-substitute-ids)
- [ ] [`part/remove-substitute-ids`](https://partsbox.com/api.html#part-add-substitute-ids)
- [ ] [`part/update-custom-fields`](https://partsbox.com/api.html#part-remove-substitute-ids)
- [ ] [`part/delete-custom-field`](https://partsbox.com/api.html#part-update-custom-fields)
- [ ] [`part/storage`](https://partsbox.com/api.html#part-storage)
- [ ] [`part/lots`](https://partsbox.com/api.html#part-lots)
- [ ] [`part/stock`](https://partsbox.com/api.html#part-stock)

### [Stock](https://partsbox.com/api.html#stock)
- [ ] [`stock/add`](https://partsbox.com/api.html#stock-add)
- [ ] [`stock/remove`](https://partsbox.com/api.html#stock-remove)
- [ ] [`stock/move`](https://partsbox.com/api.html#stock-move)
- [ ] [`stock/update`](https://partsbox.com/api.html#stock-update)

### [Lots](https://partsbox.com/api.html#lots)
- [ ] [`lot/get`](https://partsbox.com/api.html#lot-get)
- [ ] [`lot/update`](https://partsbox.com/api.html#lot-get)
- [ ] [`lot/all`](https://partsbox.com/api.html#lot-get)

### [Storage](https://partsbox.com/api.html#storage)
- [ ] [`storage/get`](https://partsbox.com/api.html#storage-get)
- [ ] [`storage/all`](https://partsbox.com/api.html#storage-all)
- [ ] [`storage/update`](https://partsbox.com/api.html#storage-update)
- [ ] [`storage/rename`](https://partsbox.com/api.html#storage-rename)
- [ ] [`storage/change-settings`](https://partsbox.com/api.html#storage-change-settings)
- [ ] [`storage/archive`](https://partsbox.com/api.html#storage-archive)
- [ ] [`storage/restore`](https://partsbox.com/api.html#storage-restore)
- [ ] [`storage/parts`](https://partsbox.com/api.html#storage-parts)
- [ ] [`storage/lots`](https://partsbox.com/api.html#storage-lots)

### [Projects](https://partsbox.com/api.html#projects)
- [ ] [`project/get`](https://partsbox.com/api.html#project-get)
- [ ] [`project/all`](https://partsbox.com/api.html#project-all)
- [ ] [`project/create`](https://partsbox.com/api.html#project-create)
- [ ] [`project/update`](https://partsbox.com/api.html#project-update)
- [ ] [`project/delete`](https://partsbox.com/api.html#project-delete)
- [ ] [`project/get-entries`](https://partsbox.com/api.html#project-get-entries)
- [ ] [`project/add-entries`](https://partsbox.com/api.html#project-add-entries)
- [ ] [`project/update-entries`](https://partsbox.com/api.html#project-update-entries)
- [ ] [`project/delete-entries`](https://partsbox.com/api.html#project-delete-entries)
- [ ] [`project/get-builds`](https://partsbox.com/api.html#project-get-builds)
- [ ] [`project/archive`](https://partsbox.com/api.html#project-archive)
- [ ] [`project/restore`](https://partsbox.com/api.html#project-restore)
- [ ] [`build/get`](https://partsbox.com/api.html#build-get)
- [ ] [`build/update`](https://partsbox.com/api.html#build-update)

Orders
- [ ] `order/get`
- [ ] `order/all`
- [ ] `order/get-entries`
- [ ] `order/receive`

Offers
- [ ] `offer/get`

Purchase Lists
- [ ] `list/create`
- [ ] `list/add-entries`
- [ ] `list/get`
- [ ] `list/get-entries`
- [ ] `list/delete`

ID Anything™
- [ ] `id-anything-qr`

Global
- [ ] `db/download-all-data`

## Features

- Manage parts, stock, projects, and orders
- Modular design for easy extension
- Supports Python 3.6 and above

## License

MIT License