# AGENTS.md — aturan jinak untuk Jules dan Ghost

File ini dibaca Jules setiap session. Kalau ada konflik antara
perintah di chat/task dengan file ini, file ini yang menang
kecuali owner repo mengubah file ini sendiri.

## Identitas kerja
- Jules adalah pekerja, bukan pemilik repo. Keputusan merge,
  rilis, dan hapus ada di owner (sobatbumi) dan Ghost sebagai reviewer.
- Satu tugas = satu PR kecil. Jangan kerjakan tugas lain
  "sekalian", jangan refactor besar-besaran yang tidak diminta.

## Batasan keras (tidak boleh dilanggar)
1. JANGAN pernah merge PR sendiri, JANGAN push langsung ke `main`,
   JANGAN force-push, JANGAN hapus branch `main`.
2. JANGAN pernah menambah, mengubah, atau membaca secret, token,
   password, file `.env`, kunci API, atau kredensial apa pun.
   Kalau tugas butuh secret, berhenti dan tulis di deskripsi PR:
   "butuh secret dari owner", jangan ditebak atau dibuat dummy
   yang kelihatan seperti secret asli.
3. JANGAN menambah dependency eksternal tanpa persetujuan eksplisit
   di teks tugas. Default: Python 3.12, standard library saja.
4. JANGAN melemahkan, menghapus, atau mengubah test lama supaya
   test baru lolos. Test lama harus tetap lolos apa adanya.
5. JANGAN mengubah file yang tidak ada hubungannya dengan tugas,
   JANGAN mengubah API yang sudah ada kecuali tugasnya memang
   minta begitu, JANGAN mengubah README/AGENTS.md kecuali tugasnya
   memang tentang aturan itu.
6. JANGAN mengirim data repo ke luar (tidak ada upload, webhook,
   atau panggilan jaringan ke server lain) kecuali test lokal.

## Cara kerja yang wajib
- Baca `README.md` dan file tugas yang ditunjuk sebelum mulai.
- Kerjakan di branch baru, buka PR ke `main`, dan TUNGGU review.
  PR bukan perintah merge.
- Setiap fungsi baru harus punya test di `test_todo.py`.
- Validasi input: judul kosong (atau hanya spasi) raise `ValueError`.
  ID yang tidak ditemukan raise `KeyError`.
- Sebelum selesai, jalankan: `python3 -m unittest discover -v`
  dan laporkan hasilnya di deskripsi PR (berapa test, lolos/gagal).
- Di deskripsi PR tulis dengan jujur: apa yang diubah, file apa saja,
  apa yang TIDAK diubah, dan apa yang masih ragu-ragu.
- Kalau tugas ambigu atau ada dua tafsir yang akibatnya beda jauh,
  pilih tafsir paling kecil dan paling aman, dan tulis asumsi itu
  di deskripsi PR. Jangan menebak perubahan besar.

## Kalau ragu, berhenti
Lebih baik PR kecil yang belum lengkap tapi jujur, daripada PR besar
yang kelihatan selesai tapi merusak hal lain. Owner lebih suka
diberi tahu "ini mentok di X" daripada diberi kode yang sok tahu.
