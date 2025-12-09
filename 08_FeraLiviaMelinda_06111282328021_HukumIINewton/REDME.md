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
3. Menghasilkan visualisasi gerak benda terhadap waktu

# 3. Penjelasan Fisika

Simulasi yang dibuat pada proyek ini didasarkan pada **Hukum II Newton**, yang menyatakan bahwa:

\[
F = m \cdot a
\]

Artinya, percepatan suatu benda sebanding dengan gaya total yang bekerja padanya dan berbanding terbalik dengan massanya. Dari persamaan tersebut dapat diturunkan:

\[
a = \frac{F}{m}
\]

Jika gaya yang diberikan bernilai **konstan**, maka percepatan juga akan konstan atau tidak berubah terhadap waktu.

Dalam konteks gerak lurus, hubungan antara percepatan, kecepatan, dan posisi dapat dituliskan sebagai:

- Perubahan kecepatan terhadap waktu:
\[
v(t + \Delta t) = v(t) + a \cdot \Delta t
\]

- Perubahan posisi terhadap waktu:
\[
x(t + \Delta t) = x(t) + v(t) \cdot \Delta t
\]

