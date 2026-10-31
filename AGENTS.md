# AGENTS.md — untuk Jules dan Ghost

- Bahasa: Python 3.12, standard library saja, tanpa dependency eksternal.
- Jangan ubah API yang sudah ada kecuali tugasnya memang minta begitu.
- Setiap fungsi baru harus punya test di `test_todo.py`.
- Validasi input: judul kosong (atau hanya spasi) harus raise `ValueError`.
- ID yang tidak ditemukan harus raise `KeyError`.
- Sebelum selesai, jalankan: `python3 -m unittest discover -v`
- Jangan menambahkan file konfigurasi, secret, atau token apa pun ke repo ini.
