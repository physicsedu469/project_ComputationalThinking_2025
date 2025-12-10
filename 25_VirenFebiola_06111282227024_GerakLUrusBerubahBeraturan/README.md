# Simulasi Gerak Berubah beraturan

## Identitas
- Nama  : Viren Febiola
- NIM   : 06111282227024
- Topik : Gerak Berubah beraturan

## Deskripsi Singkat
Proyek ini mensimulasikan Gerak Lurus Berubah Beraturan (GLBB), yaitu gerak benda pada lintasan lurus dengan percepatan konstan. Dalam GLBB, perubahan kecepatan berlangsung secara teratur sehingga posisi dan kecepatan benda dapat diprediksi melalui persamaan kinematika. Simulasi dilakukan secara numerik menggunakan metode time stepping untuk memperlihatkan bagaimana posisi, kecepatan, dan percepatan berubah terhadap waktu.

## Tujuan
1. Memahami karakteristik Gerak Lurus Berubah Beraturan (GLBB) dan keterkaitannya dengan percepatan konstan.
2. Mengimplementasikan persamaan GLBB ke dalam perhitungan numerik berbasis waktu.
3. Menampilkan grafik perubahan posisi dan kecepatan benda sebagai fungsi waktu.
4. Melatih keterampilan penggunaan Python/Jupyter Notebook dalam analisis kinematika dasar.

## File dalam Folder
- `GerakLurusBerubahBeraturan.ipynb` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat
Pada Gerak Lurus Berubah Beraturan (GLBB), sebuah benda bergerak pada lintasan lurus dengan percepatan konstan. Percepatan ini dapat berupa percepatan positif (benda semakin cepat) atau percepatan negatif (perlambatan). Secara umum, hubungan antara posisi, kecepatan, dan percepatan dalam GLBB dapat dituliskan sebagai:
Gerak lurus berubah beraturan (GLBB) adalah gerak benda pada lintasan lurus dengan
**percepatan konstan**. Pada gerak ini, kecepatan benda tidak tetap, tetapi berubah secara
beraturan setiap selang waktu tertentu. Perubahan kecepatan yang teratur ini disebabkan
oleh percepatan \(a\), yang dapat bernilai positif (benda dipercepat) maupun negatif
(benda diperlambat atau mengalami perlambatan).

Berbeda dengan gerak lurus beraturan (GLB) yang memiliki kecepatan konstan, GLBB
menunjukkan hubungan yang lebih dinamis antara posisi, kecepatan, dan percepatan.
Perubahan kecepatan dan posisi dalam GLBB tidak dipengaruhi oleh gaya hambatan
atau faktor eksternal lain, sehingga model matematisnya dapat dianalisis secara
langsung menggunakan persamaan kinematika, tanpa memerlukan metode numerik.

Model gerak pada GLBB didasarkan pada tiga persamaan dasar berikut:
Gerak lurus berubah beraturan (GLBB) adalah gerak benda pada lintasan lurus dengan
**percepatan konstan**. Pada gerak ini, kecepatan benda tidak tetap, tetapi berubah secara
beraturan setiap selang waktu tertentu. Perubahan kecepatan yang teratur ini disebabkan
oleh percepatan \(a\), yang dapat bernilai positif (benda dipercepat) maupun negatif
(benda diperlambat atau mengalami perlambatan).

Model gerak pada GLBB didasarkan pada tiga persamaan dasar berikut:

### **1. Percepatan konstan**
$$a = \frac{dv}{dt}$$

### **2. Hubungan kecepatan terhadap waktu**
$$v(t) = v_0 + at$$

### **3. Perubahan posisi terhadap waktu**
$$
x(t) = x_0 + v_0 t + \frac{1}{2} a t^2$$

 Persamaan pertama menunjukkan bahwa percepatan adalah laju perubahan kecepatan
terhadap waktu. Persamaan kedua menggambarkan bagaimana kecepatan meningkat atau
menurun secara linear tergantung nilai percepatan. Persamaan ketiga menyatakan bahwa
posisi benda berubah secara kuadratis terhadap waktu akibat adanya percepatan.

Simulasi ini bertujuan untuk memodelkan bagaimana kecepatan dan posisi benda berubah
dari waktu ke waktu ketika benda bergerak lurus dengan percepatan konstan. Dengan
model ini, kita dapat menggambarkan grafik gerak, menghitung posisi dan kecepatan
pada setiap waktu, serta memahami karakteristik dasar GLBB secara komputasional.

Dalam simulasi komputasi, persamaan ini diselesaikan secara numerik menggunakan metode time stepping untuk memeriksa perubahan posisi dan kecepatan dari waktu ke waktu.## Cara Menjalankan File .ipynb di google Colab
1. Klik tombol **Open in Colab** berikut.
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1UxTldETp4vArC3Up2YuDz8I-31d4RAmX?usp=sharing)
3. Notebook akan terbuka di Google Colab.  
4. Jalankan sel-sel secara berurutan untuk melihat simulasi.  
5. Anda dapat mengubah parameter (kecepatan awal, sudut tembak, koefisien drag) dan mengamati perubahan lintasan.


## Hasil Output
Notebook akan menampilkan:
-Grafik posisi terhadap waktu untuk menunjukkan bagaimana posisi benda berubah secara teratur pada GLBB.
-Grafik kecepatan terhadap waktu yang memperlihatkan perubahan kecepatan akibat percepatan konstan (positif atau negatif).
-Perbandingan beberapa kondisi GLBB, misalnya:

 a. percepatan positif vs percepatan negatif,
 b. kecepatan awal berbeda,posisi awal berbeda.Variasi grafik berdasarkan perubahan parameter, seperti percepatan, kecepatan awal, atau langkah waktu, sehingga terlihat bagaimana dinamika GLBB berbeda dengan tiap konfigurasi.
