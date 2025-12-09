# Simulasi Gerak Peluru dengan Hambatan Udara

## Identitas
- Nama  : Nur Kayla Lekati
- NIM   : 06111282328026
- Topik : Simulasi Gerak Peluru tanpa Hambatan Udara

## Deskripsi Singkat
Proyek ini mensimulasikan lintasan gerak peluru (projectile motion) tanpa hambatan udara menggunakan metode numerik.
Simulasi dilakukan dengan menerapkan metode Euler dan metode Runge–Kutta orde empat (RK4) 
untuk menyelesaikan sistem persamaan diferensial yang menggambarkan posisi dan kecepatan peluru sebagai fungsi waktu. 
Hasil simulasi divisualisasikan dalam bentuk grafik lintasan untuk membandingkan performa kedua metode numerik.

## Tujuan
1. Menganalisis gerak peluru tanpa hambatan udara dengan pendekatan metode numerik.
2. Membandingkan hasil simulasi gerak peluru menggunakan metode Euler dan metode Runge–Kutta orde empat (RK4).
3. Menampilkan grafik lintasan peluru secara komputasi.
4. Melatih keterampilan penggunaan Python/Jupyter Notebook dalam fisika komputasi.

## File dalam Folder
- `Gerak_Peluru_Tanpa_Hambatan_Udara.ipynb` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat
Pada gerak peluru tanpa hambatan udara, gaya yang bekerja pada benda hanyalah gaya gravitasi, yaitu

$$
\vec{F} = m\vec{g}
$$

dengan arah percepatan gravitasi ke bawah. Akibatnya, percepatan gerak peluru diberikan oleh

$$
a_x = 0, \qquad a_y = -g
$$

Persamaan gerak diselesaikan secara numerik untuk memperoleh lintasan (*trajectory*) gerak peluru.

## Cara Menjalankan File .ipynb di google Colab
1. Klik tombol **Open in Colab** berikut.
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/physicsedu469/project_ComputationalThinking_2025/blob/main/00_Ani_xxxx_Contoh/gerakPeluru_drag.ipynb)
3. Notebook akan terbuka di Google Colab.  
4. Jalankan sel-sel secara berurutan untuk melihat simulasi.  
5. Anda dapat mengubah parameter (kecepatan awal, sudut tembak, koefisien drag) dan mengamati perubahan lintasan.


## Hasil Output
Notebook akan menampilkan:
- Grafik lintasan gerak peluru hasil metode Euler.
- Grafik lintasan gerak peluru hasil metode Runge–Kutta orde empat (RK4).
- Perbandingan lintasan antara metode Euler dan RK4
