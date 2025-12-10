# Simulasi Pemuaian Linear

## Identitas
- Nama  : Yasmine Altira
- NIM   : 06111282227056
- Topik : Simulasi Pemuaian Linear

## Deskripsi Singkat
Project ini mensimulasikan bagaimana panjang suatu benda padat berubah ketika suhunya dinaikkan. Fenomena ini disebut pemuaian linear, yaitu kondisi ketika panjang benda bertambah secara proporsional terhadap kenaikan suhu.

Jika kenaikan suhu cukup besar, perbedaan panjang yang awalnya kecil bisa menjadi signifikan, terutama pada material yang memiliki koefisien muai tinggi. Simulasi ini menghitung perubahan panjang pada rentang suhu tertentu, kemudian menampilkannya dalam bentuk tabel dan grafik.

Metode perhitungan menggunakan pendekatan langkah-suhu (temperature stepping), di mana setiap perubahan suhu dihitung satu per satu untuk memperoleh pemahaman visual terhadap pola pemuaian.

## Tujuan
1. Menjelaskan hubungan antara perubahan suhu dan pemuaian panjang suatu benda padat.
2. Mengimplementasikan persamaan pemuaian linear ke dalam perhitungan numerik.
3. Menampilkan grafik perubahan panjang terhadap suhu.
4. Melatih penggunaan Jupyter Notebook untuk membuat simulasi fisika sederhana.

## File dalam Folder
- `Simulasi_Pemuaian_Linear.ipynb` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat

L0 : panjang awal

alpha : koefisien muai panjang

T0 : suhu awal

T : suhu akhir yang ingin dihitung

L : panjang setelah mengalami pemuaian

Rumus ini menunjukkan bahwa semakin besar alpha atau semakin besar perubahan suhu dT, maka pertambahan panjang akan semakin besar. Grafik hubungan ini berbentuk garis lurus karena sifat pemuaiannya linear.

## Cara Menjalankan File .ipynb di google Colab
1. Klik tombol **Open in Colab** berikut.
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/physicsedu469/project_ComputationalThinking_2025/blob/main/24_YasmineAltira_06111282227056_SimulasiPemuaianLinear/Simulasi_Pemuaian_Linear.ipynb)
3. Notebook akan terbuka di Google Colab.  
4. Jalankan sel-sel secara berurutan untuk melihat simulasi.  
5. Ubah parameter seperti panjang awal, koefisien muai, atau suhu akhir untuk melihat pengaruhnya terhadap grafik pemuaian.


## Hasil Output
Notebook akan menampilkan:
1. Tabel perubahan panjang pada setiap kenaikan suhu.
2. Grafik pemuaian linear untuk satu material.
3. Grafik perbandingan pemuaian beberapa material (misalnya baja, aluminium, tembaga).
4. Interpretasi grafik mengenai material mana yang paling cepat memuai.
