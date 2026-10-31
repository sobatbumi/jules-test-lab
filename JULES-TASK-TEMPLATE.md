# Template tugas buat Jules (copy-paste ini setiap kali)

Jangan kasih tugas kabur seperti "bikin jadi bagus" atau
"bangun aplikasinya". Pakai format ini supaya Jules jinak:

```
Repo: sobatbumi/jules-test-lab
Branch dasar: main

TUGAS (satu saja, spesifik):
[Tulis satu fitur / satu bug / satu refactor, dengan nama
fungsi/file yang jelas]

YANG BOLEH DIUBAH:
[file-file yang boleh disentuh saja]

YANG TIDAK BOLEH DIUBAH:
[API lama, file lain, main, secret, dependency]

KRITERIA SELESAI (bisa dicek):
1. [Perilaku yang diharapkan, termasuk edge case]
2. Test baru di test_todo.py untuk kriteria di atas
3. Semua test lama tetap lolos:
   python3 -m unittest discover -v

ATURAN:
- Standard library saja, tanpa dependency baru
- Kerja di branch baru, buka PR ke main, JANGAN merge
- Tunggu review Ghost/owner sebelum merge
- Kalau ambigu, pilih perubahan paling kecil dan tulis
  asumsinya di deskripsi PR
```

Contoh tugas yang jinak: "Tambah method X ke file Y dengan
perilaku Z + test". Contoh tugas yang LIAR dan jangan dipakai:
"Bangun ulang aplikasi ini jadi lebih modern" tanpa batas file,
tanpa kriteria selesai, tanpa larangan merge.
