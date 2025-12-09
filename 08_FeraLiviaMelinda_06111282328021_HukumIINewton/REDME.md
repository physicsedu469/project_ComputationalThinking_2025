# Simulasi Penerapan Hukum II Newton pada Gerak Lurus Berpercepatan Konstan

## Identitas
- Nama  : Fera Livia Melinda 
- NIM   : 06111282328021
- Topik : Simulasi Penerapan Hukum II Newton pada Gerak Lurus Berpercepatan Konstan
  
## Deskripsi Singkat
Proyek ini merupakan simulasi komputasi berbasis Python untuk memodelkan gerak benda menggunakan Hukum II Newton (F = m × a). Simulasi dilakukan di dalam lingkungan Jupyter Notebook dengan metode numerik sederhana, yaitu Euler Method, untuk menghitung perubahan posisi dan kecepatan benda setiap interval waktu kecil (Δt).Pada simulasi ini, gaya diberikan konstan terhadap benda, sehingga percepatan juga bernilai konstan. Hasil simulasi divisualisasikan dalam bentuk grafik posisi dan kecepatan terhadap waktu, sehingga hubungan antara gaya, massa, dan percepatan dapat diamati secara jelas.

## Tujuan
1. Memahami hubungan antara gaya, massa, dan percepatan.
2. Menerapkan metode numerik dalam pemodelan gerak.
3. Menghasilkan visualisasi gerak benda terhadap waktu.

## File dalam Folder
- `Gerak_Peluru_dengan_hambatan_udara.ipynb` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat
## Penjelasan Fisika

Simulasi ini didasarkan pada Hukum II Newton:

$$
F = m \cdot a
$$

Sehingga percepatan benda dapat dihitung:

$$
a = \frac{F}{m}
$$

Jika gaya konstan, maka percepatan juga konstan. Perubahan kecepatan dan posisi terhadap waktu dihitung dengan metode Euler:

$$
v(t + \Delta t) = v(t) + a \cdot \Delta t
$$

$$
x(t + \Delta t) = x(t) + v(t) \cdot \Delta t
$$

Ketika gaya konstan menyebabkan percepatan konstan, kecepatan meningkat secara linear terhadap waktu, dan posisi meningkat secara kuadratik terhadap waktu.


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
