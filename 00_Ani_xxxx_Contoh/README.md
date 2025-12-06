# Simulasi Fourier Series untuk Gelombang Kotak

## Identitas
- Nama  : Contoh Project
- NIM   : 00000000
- Topik : Simulasi Gerak Peluru dengan Hambatan Udara

## Deskripsi Singkat
Project ini mensimulasikan lintasan gerak peluru (projectile motion) yang dipengaruhi oleh
gaya hambatan udara. Tidak seperti gerak peluru ideal tanpa hambatan, gaya drag menyebabkan
peluru kehilangan energi sehingga lintasannya menjadi lebih pendek dan melengkung secara non-linear.
Simulasi dilakukan secara numerik menggunakan metode langkah-waktu (time stepping).

## Tujuan
1. Memahami pengaruh gaya hambatan udara terhadap gerak peluru.
2. Mengimplementasikan model fisika ke dalam perhitungan numerik.
3. Menampilkan grafik lintasan peluru secara komputasi.
4. Melatih keterampilan penggunaan Python/Jupyter Notebook dalam fisika komputasi.

## File dalam Folder
- `Gerak_Peluru_dengan_hambatan_udara.ipynb` → notebook berisi simulasi lengkap.
- `gerak_peluru_drag.py` (opsional) → versi Python script.
- `plot_trajectory.png` → grafik lintasan peluru hasil simulasi.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat
Gaya hambatan udara dimodelkan sebagai:

$\vec{F}_d = -k\vec{v} $

yang menyebabkan perlambatan pada arah kecepatan. Persamaan gerak diselesaikan secara numerik
untuk memperoleh lintasan (trajectory) peluru.

## Cara Menjalankan
1. Instal Python + matplotlib + numpy.
2. Jalankan notebook:
