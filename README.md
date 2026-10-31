# jules-test-lab

Repo percobaan kecil untuk ngetes workflow Ghost + Jules.

Tujuannya bukan aplikasinya, tapi prosesnya:
1. Repo ini jadi titik awal yang sudah jalan dan sudah ada testnya.
2. Jules dikasih satu tugas kecil yang jelas (lihat `TASK-FOR-JULES.md`).
3. Jules mengerjakan di branch-nya sendiri dan membuka pull request.
4. Ghost me-review PR itu, menjalankan test, lalu merge kalau lolos.

## Cara jalanin test

```bash
python3 -m unittest discover -v
```

Tidak ada dependency eksternal, cukup Python 3.12 dan standard library.
