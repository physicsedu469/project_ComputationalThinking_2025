# Simulasi Rangkaian Listrik dengan Hukum Ohm

## Identitas
- Nama  : Muhammad Putra Aririyansyah
- NIM   : 06111282227054
- Topik : Simulasi Rangkaian Listrik dengan Hukum Ohm

## Deskripsi Singkat
Project ini mensimulasikan hubungan antara tegangan, arus, dan hambatan pada rangkaian listrik berdasarkan prinsip Hukum Ohm. Tidak seperti analisis teoritis yang hanya mengandalkan persamaan langsung, simulasi ini memperlihatkan bagaimana perubahan salah satu variabel menghasilkan perilaku listrik yang berbeda melalui visualisasi grafik. Dengan melakukan variasi nilai tegangan dan hambatan, terlihat bahwa arus listrik merespons secara linier terhadap tegangan pada hambatan tetap, serta menurun ketika hambatan diperbesar pada tegangan konstan. Seluruh proses perhitungan dilakukan secara numerik melalui pendekatan step-by-step sehingga perubahan nilai dapat diamati secara bertahap dan menyeluruh. Simulasi ini memberikan gambaran yang lebih intuitif mengenai penerapan Hukum Ohm dalam sistem listrik sederhana maupun dalam kondisi dengan parameter yang bervariasi.

## Tujuan
1. Memahami hubungan antara tegangan, arus, dan hambatan berdasarkan Hukum Ohm.
2. Mengimplementasikan model kelistrikan ke dalam perhitungan numerik secara sistematis.
3. Menampilkan grafik perubahan tegangan, arus, dan hambatan sebagai visualisasi komputasi.
4. Melatih keterampilan penggunaan Python/Jupyter Notebook dalam analisis rangkaian listrik secara komputasional.

## File dalam Folder
- `Proyek_UAS_Berpikir_Komputasii_Muhammad_Putra_Aririyansyah_06111282227054.ipynb` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat
Sebuah rangkaian listrik sederhana terdiri dari sumber tegangan $V$, hambatan listrik $R$, dan arus listrik $I$ yang mengalir dalam rangkaian. Pada rangkaian ideal, hubungan antara tegangan, arus, dan hambatan dapat dijelaskan menggunakan Hukum Ohm. Hukum ini menyatakan bahwa besar arus listrik yang mengalir sebanding dengan tegangan yang diberikan dan berbanding terbalik dengan hambatan rangkaian.

Secara matematis, Hukum Ohm dinyatakan sebagai:

$V = I . R$

## Cara Menjalankan File .ipynb di google Colab
1. Klik tombol **Open in Colab** berikut.
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iteng744/project_ComputationalThinking_2025/blob/main/21_Muhammad Putra Aririyansyah_06111282227054_Simulasi_Rangkaian_Listrik_dengan_Hukum_Ohm_drag/Simulasi_Rangkaian_Listrik_dengan_Hukum_Ohm.ipynb)
3. Notebook akan terbuka di Google Colab.  
4. Jalankan sel-sel secara berurutan untuk melihat simulasi.  
5. Anda dapat mengubah parameter (kecepatan awal, sudut tembak, koefisien drag) dan mengamati perubahan lintasan.


## Hasil Output
Notebook akan menampilkan:
- Grafik Hubungan Tegangan dan Arus dengan Hambatan tetap dan Variabel 
- Grafik Hubungan Arus terhadap Tegangan engan Hambatan tetap dan Variabel
- Grafik Hubungan Hambatan terhadap tegangan dengan I bervariabel dan V bervariabel
- Grafik Perbandingan Arus Listrik Terhadap Waktu
- Grafik Perubahan Tegangan Terhadap Waktu
