# Simulasi Rangkaian Listrik dengan Hukum Ohm

## Identitas
- Nama  : Muhammad Putra Aririyansyah
- NIM   : 06111282227054
- Topik : Simulasi Rangkaian Listrik dengan Hukum Ohm

## Deskripsi Singkat
Project ini mensimulasikan hubungan antara tegangan, arus, dan hambatan pada rangkaian listrik berdasarkan prinsip Hukum Ohm. Tidak seperti analisis teoritis yang hanya mengandalkan persamaan langsung, simulasi ini memperlihatkan bagaimana perubahan salah satu variabel menghasilkan perilaku listrik yang berbeda melalui visualisasi grafik. Dengan melakukan variasi nilai tegangan dan hambatan, terlihat bahwa arus listrik merespons secara linier terhadap tegangan pada hambatan tetap, serta menurun ketika hambatan diperbesar pada tegangan konstan. Seluruh proses perhitungan dilakukan secara numerik melalui pendekatan step-by-step sehingga perubahan nilai dapat diamati secara bertahap dan menyeluruh. Simulasi ini memberikan gambaran yang lebih intuitif mengenai penerapan Hukum Ohm dalam sistem listrik sederhana maupun dalam kondisi dengan parameter yang bervariasi.

## Tujuan
1. Memahami pengaruh gaya hambatan udara terhadap gerak peluru.
2. Mengimplementasikan model fisika ke dalam perhitungan numerik.
3. Menampilkan grafik lintasan peluru secara komputasi.
4. Melatih keterampilan penggunaan Python/Jupyter Notebook dalam fisika komputasi.

## File dalam Folder
- `Proyek_UAS_Berpikir_Komputasii_Muhammad_Putra_Aririyansyah_06111282227054.ipynb` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat
Sebuah rangkaian listrik sederhana terdiri dari sumber tegangan $V$, hambatan listrik $R$, dan arus listrik $I$ yang mengalir dalam rangkaian. Pada rangkaian ideal, hubungan antara tegangan, arus, dan hambatan dapat dijelaskan menggunakan Hukum Ohm. Hukum ini menyatakan bahwa besar arus listrik yang mengalir sebanding dengan tegangan yang diberikan dan berbanding terbalik dengan hambatan rangkaian.

Secara matematis, Hukum Ohm dinyatakan sebagai:

$V = I . R$

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
