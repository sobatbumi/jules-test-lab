# jules-test-lab

Repo percobaan kecil untuk ngetes workflow Ghost + Jules.

Tujuannya bukan aplikasinya, tapi prosesnya:
1. Repo ini jadi titik awal yang sudah jalan dan sudah ada testnya.
2. Jules dikasih satu tugas kecil yang jelas (lihat `TASK-FOR-JULES.md`).
3. Jules mengerjakan di branch-nya sendiri dan membuka pull request.
4. Ghost me-review PR itu, menjalankan test, lalu merge kalau lolos.

## Penggunaan Baru
Berikut adalah contoh singkat penggunaan fitur-fitur baru di TodoList:

```python
from todo import TodoList

todos = TodoList()
item = todos.add("Belajar")

# 1. Update title
todos.update(item["id"], "Belajar Python")

# 2. Lihat statistik
stats = todos.stats()
print(stats) # Output: {'total': 1, 'completed': 0, 'pending': 1}

# 3. Clear completed
todos.complete(item["id"])
removed = todos.clear_completed()
print(f"Dihapus: {removed}") # Output: Dihapus: 1
```

## Cara jalanin test

```bash
python3 -m unittest discover -v
```

Tidak ada dependency eksternal, cukup Python 3.12 dan standard library.
