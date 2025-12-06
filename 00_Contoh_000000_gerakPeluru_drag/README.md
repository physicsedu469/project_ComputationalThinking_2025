# Simulasi Gerak Peluru dengan Hambatan Udara

## Identitas
- Nama  : Contoh 
- NIM   : 00000000
- Topik : Simulasi Gerak Peluru dengan Hambatan Udara

## Deskripsi Singkat
Project ini mensimulasikan lintasan gerak peluru (projectile motion) yang dipengaruhi oleh
gaya hambatan udara. Tidak seperti gerak peluru ideal tanpa hambatan, gaya drag menyebabkan
objek kehilangan energi sehingga lintasannya menjadi lebih pendek dan melengkung secara non-linear.
Simulasi dilakukan secara numerik menggunakan metode time-stepping.

## Tujuan
1. Memahami pengaruh gaya hambatan udara terhadap gerak peluru.
2. Mengimplementasikan model fisika ke dalam perhitungan numerik.
3. Menampilkan grafik lintasan peluru secara komputasi.
4. Melatih keterampilan penggunaan Python/Jupyter Notebook dalam fisika komputasi.

## File dalam Folder
- `Gerak_Peluru_dengan_hambatan_udara.ipynb` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat
Gaya hambatan udara dimodelkan sebagai:

$\vec{F}_d = -k\vec{v} $

yang menyebabkan perlambatan pada arah kecepatan. Persamaan gerak diselesaikan secara numerik
untuk memperoleh lintasan (trajectory) peluru.

## Cara Menjalankan File .ipynb di google Colab
1. Klik tombol **Open in Colab** berikut.
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/physicsedu469/project_ComputationalThinking_2025/blob/main/00_Contoh_000000_gerakPeluru_drag/gerakPeluru_drag.ipynb)
3. Notebook akan terbuka di Google Colab.  
4. Jalankan sel-sel secara berurutan untuk melihat simulasi.  
5. Anda dapat mengubah parameter (kecepatan awal, sudut tembak, koefisien drag) dan mengamati perubahan lintasan.


## Hasil Output
Notebook akan menampilkan:
- Grafik lintasan peluru dengan hambatan udara.  
- Perbandingan antara gerak ideal (tanpa hambatan) dan gerak dengan drag.  
- Variasi lintasan berdasarkan sudut tembak dan koefisien drag.
