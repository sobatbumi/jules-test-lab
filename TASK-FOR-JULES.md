# Tugas pertama untuk Jules (scoped, kecil)

Tambahkan dua fitur ke `TodoList` di `todo.py`, tanpa mengubah perilaku
fungsi yang sudah ada:

1. `remove(item_id)` — hapus item dengan id tersebut, return item yang
   dihapus. Kalau id tidak ditemukan, raise `KeyError`.
2. `search(keyword)` — return list item yang judulnya mengandung keyword,
   case-insensitive. Keyword kosong return semua item.

Syarat:
- Standard library saja, tanpa dependency baru.
- Tambahkan test untuk kedua fitur itu di `test_todo.py`.
- Semua test lama harus tetap lolos: `python3 -m unittest discover -v`
- Kerjakan di branch baru, lalu buka pull request ke `main` untuk di-review.
