"""Todo list in-memory yang sederhana, tanpa dependency eksternal."""


class TodoList:
    def __init__(self):
        self._items = []
        self._next_id = 1

    def add(self, title):
        title = title.strip() if isinstance(title, str) else ""
        if not title:
            raise ValueError("title tidak boleh kosong")
        item = {"id": self._next_id, "title": title, "done": False}
        self._items.append(item)
        self._next_id += 1
        return dict(item)

    def list_all(self):
        return [dict(item) for item in self._items]

    def complete(self, item_id):
        for item in self._items:
            if item["id"] == item_id:
                item["done"] = True
                return dict(item)
        raise KeyError(f"todo id {item_id} tidak ditemukan")
