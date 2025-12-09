# Simulasi Pemuaian Linear pada Benda Padat

## Identitas
- Nama  : Yasmine Altira
- NIM   : 06111282227056
- Topik : Simulasi Pemuaian Linear pada Benda Padat

## Deskripsi Singkat
Project ini mensimulasikan bagaimana panjang sebuah batang logam berubah ketika suhunya dinaikkan. Proses ini disebut pemuaian linear, yaitu kondisi ketika benda padat bertambah panjang secara proporsional terhadap kenaikan suhu. 
Simulasi dilakukan yaitu meningkatkan suhu sedikit demi sedikit, kemudian menghitung panjang baru pada setiap langkah. Hasilnya ditampilkan dalam bentuk tabel dan grafik sehingga hubungan antara panjang dan suhu dapat diamati dengan jelas.

## Tujuan
1. Memahami konsep dasar pemuaian linear pada benda padat.
2. Mengimplementasikan model fisika ke dalam perhitungan numerik.
3. Membuat simulasi yang menunjukkan perubahan panjang terhadap suhu dalam bentuk tabel dan grafik.
4. Membandingkan pemuaian beberapa material berbeda berdasarkan koefisien muainya.

## File dalam Folder
- `Simulasi_Pemuaian_Linear.ipynb` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat
Gaya hambatan udara dimodelkan sebagai:

$\vec{F}_d = -k\vec{v} $

yang menyebabkan perlambatan pada arah kecepatan. Persamaan gerak diselesaikan secara numerik
untuk memperoleh lintasan (trajectory) peluru.

## Cara Menjalankan File .ipynb di google Colab
1. Klik tombol **Open in Colab** berikut.
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/physicsedu469/project_ComputationalThinking_2025/blob/main/00_Ani_xxxx_Contoh/gerakPeluru_drag.ipynb)
3. Notebook akan terbuka di Google Colab.  
4. Jalankan sel-sel secara berurutan untuk melihat simulasi.  
5. Anda dapat mengubah parameter (kecepatan awal, sudut tembak, koefisien drag) dan mengamati perubahan lintasan.


## Hasil Output
Notebook akan menampilkan:
- Grafik lintasan peluru dengan hambatan udara.  
- Perbandingan antara gerak ideal (tanpa hambatan) dan gerak dengan drag.  
- Variasi lintasan berdasarkan sudut tembak dan koefisien drag.
