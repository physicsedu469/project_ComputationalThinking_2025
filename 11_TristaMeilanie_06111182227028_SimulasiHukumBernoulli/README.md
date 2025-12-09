# Simulasi Hukum Bernoulli : Efek Venturi 

## Identitas
- Nama  : Trista Meilanie
- NIM   : 06111182227028
- Topik : Efek Venturi dalam aliran fluida

## Deskripsi Singkat
Project ini mensimulasikan Efek Venturi, yaitu fenomena ketika fluida yang mengalir melalui pipa menyempit mengalami kenaikan kecepatan dan penurunan tekanan. Fenomena ini merupakan penerapan dari Hukum Bernoulli dan Persamaan Kontinuitas. Simulasi dilakukan secara komputasi untuk menghitung perubahan kecepatan dan tekanan pada berbagai ukuran luas penampang. Output utama berupa grafik hubungan luas penampang terhadap kecepatan serta grafik tekanan terhadap kecepatan. Simulasi dijalankan menggunakan Python melalui Google Colab.

## Tujuan
1. Memahami hubungan antara luas penampang, kecepatan, dan tekanan pada aliran fluida.
2. Mengimplementasikan Persamaan Kontinuitas dan Hukum Bernoulli secara numerik.
3. Menampilkan grafik perubahan tekanan dan kecepatan pada pipa Venturi.

## File dalam Folder
- `.ipynb` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat
Efek Venturi berdasarkan dua hukum utama:

1. Persamaan Kontinuitas

   $$A_1 v_1 = A_2 v_2$$

   Semakin kecil luas penampang $$(A_2 < A_1)$$, kecepatan fluida meningkat.

3. Hukum Bernoulli
   dengan prinsip Bernoulli, perbedaan tekanan dapat dihitung sebagai:

   $$P_1 - P_2 = \frac{1}{2}\rho (v_2^2 - v_1^2)$$

   Dengan demikian, kita dapat menghitung kecepatan dan tekanan pada berbagai titik dalam pipa sesuai dengan perubahan luas penampang.

## Cara Menjalankan File .ipynb di google Colab
1. Klik tombol **Open in Colab** berikut.
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/physicsedu469/project_ComputationalThinking_2025/blob/main/11_TristaMeilanie_06111182227028_SimulasiHukumBernoulli/Simulasi_Hukum_Bernoulli.ipynb)
3. Notebook akan terbuka di Google Colab.  
4. Jalankan sel-sel secara berurutan untuk melihat simulasi.  



## Hasil Output
Notebook akan menampilkan:
1. Grafik Kecepatan terhadap Luas Penampang
2. Grafik Tekanan terhadap Luas Penampang
3. Grafik Tekanan vs Kecepatan (P–v)
