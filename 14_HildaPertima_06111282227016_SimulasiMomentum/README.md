# Simulasi Momentum

## Identitas
- Nama  : Hilda Pertima 
- NIM   : 06111282227016
- Topik : Simulasi Momentum

## Deskripsi Singkat
Project ini mensimulasikan momentum liniear dan tumbukan dua benda untuk mempelajari konsep momentum dan hukum kekekalan momentum. Dalam sistem tertutup tanpa gaya luar (gaya gesek dan hambatan udara), momentum total sistem akan tetap konstan, baik pada tumbukan lenting sempurna, tumbukan lenting sebagian dan tumbukan tidak lenting sempurna.Simulasi ini dilakukan menggunakan metode langkah-waktu (time stepping) dan divisualisasikan dengan animasi posisi dua benda yang bertumbukan. 

## Tujuan
1. Memahami konsep momentum.
2. Membedakan karakteristik tumbukan lenting sempurna, tumbukan lenting sebagian dan tumbukan tidak lenting sempurna.
3. Mengimplementasikan model fisika ke dalam perhitungan numerik di Python.
4. Menampilkan grafik momentum dan animasi tumbukan.

## File dalam Folder
- `simulasimomentum.py` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat
Momentum didefinisikan sebagai hasil kali massa dan kecepatan :
$p = m . v$
Pada saat dua benda bertumbukan, akan berlaku hukum kekekalan momentum :
$\frac{1}{2}m_1v_1^2 + \frac{1}{2}m_1v_2^2$

Tumbukan dibagi menjadi 3 macam 

Tumbukan Lenting Sempurna:

Momentum dan energi kinetik total kekal dengan koefisien resistusi $e=1$ yang terjadi pada benda sangat elastis seperti partikel atom atau bola baja.

Tumbukan Lenting Sebagian:

Momentum total kekal, energi kinetik sebagian hilang menjadi panas, bunyi, atau deformasi dengan Koefisien restitusi

Tumbukan Lenting Tidak Sempurna:

Dua benda menyatu setelah tumbukan, momentum total kekal, energi kinetik hilang sebagian besar dengan koefisien restitusi

## Cara Menjalankan File .ipynb di google Colab
1. Klik tombol **Open in Colab** berikut.
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/physicsedu469/project_ComputationalThinking_2025/blob/main/14_HildaPertima_06111282227016_SimulasiMomentum/simulasimomentum.py)
3. Notebook akan terbuka di Google Colab.  
4. Jalankan sel-sel secara berurutan untuk melihat simulasi.  
5. Anda dapat mengubah parameter (kecepatan awal, sudut tembak, koefisien drag) dan mengamati perubahan lintasan.


## Hasil Output
Notebook akan menampilkan:
- Grafik momentum terhadap kecepatan
- Grafik momentum terhadap massa
- Animasi tumbukan lenting sempurna
- Animasi tumbukan lenting sebagian
- Animasi tumbukan tidak lenting sempurna
