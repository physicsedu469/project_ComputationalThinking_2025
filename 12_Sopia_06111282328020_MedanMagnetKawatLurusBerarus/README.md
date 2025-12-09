# Simulasi Medan Magnet Kawat Lurus Berarus

## Identitas
- Nama  : Sopia
- NIM   : 06111282328020
- Topik : Simulasi Medan Magnet Kawat Lurus Berarus

## Deskripsi Singkat
Project ini mensimulasikan perhitungan medan magnet yang dihasilkan oleh sebuah kawat lurus panjang yang dialiri arus listrik. Tidak seperti analisis sederhana yang hanya menggunakan persamaan langsung, project ini memanfaatkan pendekatan komputasi untuk menghitung integral medan magnet pada rentang jarak tertentu dari kawat. Besarnya medan magnet yang bergantung pada jarak dihitung menggunakan metode numerik trapezoidal, sehingga menghasilkan pendekatan integral yang akurat meskipun fungsi memiliki perubahan nilai yang tajam pada jarak kecil. Selain itu, simulasi dilakukan menggunakan Colab, yang memungkinkan visualisasi grafik medan magnet terhadap jarak serta analisis galat (error) antara hasil numerik dan solusi analitik.

## Tujuan
1. Memahami hubungan antara besar medan magnet dan jarak dari kawat berarus melalui visualisasi grafik
2.Mengimplementasikan persamaan fisika medan magnet ke dalam perhitungan integral numerik menggunakan metode trapezoidal untuk memperoleh nilai integral pada rentang jarak tertentu.
3. Membandingkan hasil perhitungan numerik dan hasil analitik untuk menilai tingkat akurasi dari metode trapezoidal.
4. Menganalisis pengaruh jumlah pembagian interval (n) terhadap besar error dengan menampilkan grafik error metode trapezoidal secara komputasi.
5. Melatih keterampilan penggunaan Jupyter Notebook dalam melakukan simulasi fisika komputasi, visualisasi grafik, dan evaluasi error numerik.

## File dalam Folder
- `SOPIA_06111282328020_MedanMagnetKawatLurusBerarus (1).ipynb` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat
Medan magnet di sekitar kawat lurus panjang yang dialiri arus listrik diberikan oleh persamaan:
$B(r)=\frac{\mu_0 I}{2\pi r}$")

yang menunjukkan bahwa besar medan magnet berbanding terbalik dengan jarak r dari kawat. Hal ini berarti bahwa semakin dekat suatu titik ke kawat, medan magnet yang dirasakan semakin kuat, dan sebaliknya medan magnet akan melemah ketika titik pengamatan menjauh dari kawat.

Untuk memperoleh nilai integral medan magnet pada suatu rentang jarak tertentu, perhitungan dilakukan secara numerik menggunakan metode trapezoidal. Metode ini membagi interval jarak menjadi banyak segmen kecil dan menghampiri luas di bawah kurva B(r). Dengan pendekatan numerik ini, nilai integral dapat dihitung meskipun fungsi tidak diselesaikan secara analitik, sekaligus memungkinkan analisis akurasi dengan membandingkan hasil numerik dan hasil teoritis.

## Cara Menjalankan File .ipynb di google Colab
   1.Klik tombol **Open in Colab** berikut.
     [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/physicsedu469/project_ComputationalThinking_2025/main/12_Sopia_06111282328020_MedanMagnetKawatLurusBerarus/SOPIA_06111282328020_MedanMagnetKawatLurusBerarus%20(1).ipynb)

2. Notebook akan terbuka di Google Colab.  
3. Jalankan sel-sel secara berurutan untuk melihat simulasi.  
4. Anda dapat mengubah parameter (kecepatan awal, sudut tembak, koefisien drag) dan mengamati perubahan lintasan.


## Hasil Output
Notebook akan menampilkan:
- grafik hubungan antara jarak r terhadap besar medan magnet B(r) 
- Perbandingan hasil metode trapezoidal dan hasil analitik
- Pengaruh jumlah pembagian (n) terhadap besar error metode trapezoidal, grafik error terhadap n.
