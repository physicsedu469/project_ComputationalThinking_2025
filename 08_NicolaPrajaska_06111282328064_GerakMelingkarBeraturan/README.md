# Simulasi Gerak Melingkar Beraturan

## Identitas
- Nama  : M. Nicola Prajaska
- NIM   : 06111282328064
- Topik : Simulasi Gerak Melingkar Beraturan

## Deskripsi Singkat
Simulasi ini bertujuan untuk membantu memahami konsep dasar dinamika benda yang bergerak melingkar dengan kecepatan sudut konstan. Pada Gerak Melingkar Beraturan (GMB), besar kecepatan benda tetap, namun arah kecepatannya selalu berubah sehingga menghasilkan lintasan berbentuk lingkaran.
Model komputasi dibuat menggunakan Google Colab dengan bantuan Python untuk memvisualisasikan perubahan nilai fisik melalui grafik. Tidak seperti perhitungan manual, simulasi memungkinkan pengguna melakukan uji coba dengan variabel bebas yang dapat diatur sendiri (mode uji 1–4).

## Tujuan
1. Mempelajari hubungan antara variabel-variabel utama dalam Gerak Melingkar Beraturan.
2. Mengimplementasikan persamaan GMB ke dalam komputasi Python.
3. Menyediakan mode uji yang memungkinkan pengguna memasukkan variabel bebas (r, ω, v, f).
4. Memvisualisasikan hubungan fisik GMB menggunakan grafik v–r, v–ω, a–v, dan v–f.
5. Melatih keterampilan pemrograman dan berpikir komputasional dalam konteks fisika dasar.

## File dalam Folder
  - `Simulasi_Gerak_Melingkar_Beraturan.ipynb` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat
1. Kecepatan Sudut:

$$\omega = \frac{2\pi}{T}$$

2. Kecepatan Linear:

$$v = \omega r$$


3. Kecepatan Linear (Tangensial):

   

yang menyebabkan perlambatan pada arah kecepatan. Persamaan gerak diselesaikan secara numerik
untuk memperoleh lintasan (trajectory) peluru.

## Mode Uji dalam Simulasi

Simulasi terdiri dari 4 mode, yaitu:

- Mode 1 — Uji Jari-jari (r)

Mengamati pengaruh perubahan jari-jari terhadap kecepatan linear dan percepatan sentripetal.

- Mode 2 — Uji Kecepatan Sudut (ω)

Melihat bagaimana kecepatan sudut memengaruhi kecepatan linear dan percepatan sentripetal.

- Mode 3 — Uji Kecepatan Linear (v)

Menginvestigasi efek kecepatan linear terhadap percepatan sentripetal dan kecepatan sudut.

- Mode 4 — Uji Frekuensi (f)

Mengamati hubungan f dengan T, ω, dan v.

Setiap mode menghasilkan grafik dan tabel data untuk memudahkan analisis.

## Cara Menjalankan File .ipynb di google Colab
1. Klik tombol **Open in Colab** berikut.
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/physicsedu469/project_ComputationalThinking_2025/blob/main/00_Contoh_000000_gerakPeluru_drag/gerakPeluru_drag.ipynb)
3. Notebook akan terbuka di Google Colab.  
4. Jalankan sel-sel secara berurutan untuk melihat simulasi.  
5. Anda dapat mengubah parameter (kecepatan awal, sudut tembak, koefisien drag) dan mengamati perubahan lintasan.


## Hasil Output
Notebook akan menampilkan:
- Grafik hubungan GMB.  
- Tabel nilai fisika (contoh sampel data).
- Simulasi mode uji dengan variabel bebas yang diinput pengguna.
