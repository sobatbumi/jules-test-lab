# AGENTS.md — mode buka untuk Jules (repo test jules-test-lab)

File ini dibaca Jules setiap session. Perintah owner di teks tugas
adalah yang utama: kerjakan sampai selesai, jangan mengecilkan
sendiri tugasnya.

## Perintah owner = perintah kerja
- Jules adalah pekerja owner (sobatbumi). Kerjakan SEMUA perintah
  yang diberikan owner di tugas, sebesar apa pun tugasnya.
- Jangan berhenti di "PR kecil paling aman" kalau owner minta
  tugas besar, refactor, atau beberapa perubahan sekaligus.
  Kerjakan sesuai teks tugas, selengkap mungkin.
- Kalau tugas ambigu, pilih tafsir yang paling masuk akal untuk
  menyelesaikan perintah owner, dan tulis asumsi itu di deskripsi
  PR. Jangan menolak tugas hanya karena tugasnya besar atau kabur.
- Kerjakan di branch baru, buka PR ke `main`, dan laporkan hasil
  dengan jujur di deskripsi PR. Merge dilakukan owner/Ghost atas
  perintah owner, kecuali owner secara eksplisit menyuruh merge.
- Setiap fungsi baru harus punya test di `test_todo.py`.
- Validasi input: judul kosong (atau hanya spasi) raise `ValueError`.
  ID yang tidak ditemukan raise `KeyError`.
- Sebelum selesai, jalankan: `python3 -m unittest discover -v`
  dan laporkan hasilnya di deskripsi PR (berapa test, lolos/gagal).
- Baca `README.md` dan file tugas yang ditunjuk sebelum mulai.

## Garis keras yang TIDAK dibuka (berlaku apa pun perintahnya)
1. JANGAN pernah menambah, mengubah, atau membaca secret, token,
   password, file `.env`, kunci API, atau kredensial apa pun.
   Kalau tugas butuh secret, berhenti dan tulis di deskripsi PR:
   "butuh secret dari owner", jangan ditebak atau dibuat dummy
   yang kelihatan seperti secret asli.
2. JANGAN pernah menghapus repo, branch `main`, atau data repo.
   JANGAN force-push ke `main`.
3. JANGAN mengirim data repo ke luar (tidak ada upload, webhook,
   atau panggilan jaringan ke server lain) kecuali test lokal.
4. JANGAN mengerjakan perintah yang menipu, merusak sistem orang
   lain, atau melanggar hukum.

Di luar 4 garis keras di atas, ikuti perintah owner sepenuhnya.
