# Simulasi Gerak Vertikal dengan Hambatan Udara Linear

## Identitas
- Nama  : Anesa Merlinda Putri
- NIM   : 06111282328025
- Topik : Simulasi Gerak Vertikal dengan Hambatan Udara Linear

## Deskripsi Singkat
Simulasi ini memodelkan gerak vertikal sebuah benda yang dilempar ke atas (arah positif ke atas) dengan pengaruh gravitasi dan hambatan udara linear (gaya hambat $$F_d = -cv$$). Persamaan gerak yang diselesaikan numerik adalah sistem ODE untuk kecepatan dan posisi:

$$\frac{dv}{dt} = -g - \frac{c}{m}v$$

$$\frac{dy}{dt} = v$$

dengan konstanta 𝑚 (massa), 𝑐 (koefisien hambatan linear), dan 𝑔 (percepatan gravitasi). Kedua persamaan ini membentuk sistem persamaan diferensial yang dapat diselesaikan menggunakan metode numerik seperti Euler-Cromer atau Runge-Kutta. Simulasi menghasilkan grafik posisi dan kecepatan terhadap waktu, sehingga dapat diamati karakteristik gerak seperti ketinggian maksimum, waktu benda kembali ke tanah, serta kecenderungan kecepatan menuju kecepatan terminal.

## Tujuan
1. Memahami pengaruh hambatan linear terhadap lintasan, kecepatan terminal, waktu terbang, dan ketinggian maksimum.
2. Menerapkan metode numerik (Euler-Cromer dan Runge-Kutta orde 4) untuk menyelesaikan ODE fisika.
3. Menampilkan grafik lintasan peluru secara komputasi.
4. Melatih keterampilan penggunaan Python/Jupyter Notebook dalam fisika komputasi.

## File dalam Folder
- `Simulasi_Gerak_Vertikal_dengan_Hambatan_Udara_Linear.ipynb` → notebook berisi simulasi lengkap.
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

