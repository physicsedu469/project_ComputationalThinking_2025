# Simulasi Gelombang Bunyi

## Identitas
- Nama  : Maria Callista Ayu Nathaniela
- NIM   : 06111282227034
- Topik : Simulasi Gelombang Bunyi

## Deskripsi Singkat
Simulasi ini dibuat untuk memvisualisasikan gelombang bunyi sebagai gelombang mekanik longitudinal yang merambat melalui udara. Gelombang bunyi direpresentasikan sebagai fungsi perubahan tekanan terhadap posisi dan waktu. Melalui grafik statis, animasi, dan kontrol interaktif (frekuensi dan amplitudo), pengguna dapat memahami bagaimana karakteristik bunyi berubah berdasarkan parameter fisiknya.

## Tujuan
1. Menunjukkan bentuk gelombang bunyi secara grafis pada domain ruang.
2. ⁠Mendeskripsikan hubungan antara frekuensi, amplitudo, panjang gelombang, dan cepat rambat bunyi.
3. ⁠Menyediakan animasi untuk melihat propagasi gelombang bunyi terhadap waktu.
4. ⁠Memberikan simulasi interaktif sehingga pengguna dapat mengubah frekuensi dan amplitudo secara langsung.
5. ⁠Membantu memahami gelombang bunyi sebagai gelombang longitudinal melalui tampilan rapatan–regangan (ditampilkan sebagai fungsi sinus).

## File dalam Folder
- `simulasi_gelombang_bunyi` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat
Bunyi merupakan gelombang mekanik longitudinal, artinya rambatannya terjadi melalui rapatan dan regangan partikel udara. Secara matematis, gelombang bunyi dapat dituliskan:

y(x,t)=Asin(kx−ωt) 

Interpretasi fisis:
• Semakin besar frekuensi, semakin rapat gelombangnya → nada lebih tinggi.
• ⁠Semakin besar amplitudo, semakin besar energi gelombang → bunyi terdengar lebih keras.
• ⁠Gelombang sinus hanyalah representasi matematis; secara fisik, bunyi adalah osilasi tekanan udara.

## Cara Menjalankan File .ipynb di google Colab
1. Klik tombol **Open in Colab** berikut.
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/physicsedu469/project_ComputationalThinking_2025/blob/main/018_Istiqoma_06111282227038_SimulasiKeseimbangandanDinamikaRotasi/keseimbangan_dan_dinamika_rotasi.ipynb)

2. Notebook akan terbuka di Google Colab.  
3. Jalankan sel-sel secara berurutan untuk melihat simulasi.  
4. Anda dapat mengubah parameter engubah parameter (gaya besar, posisi gaya kerja terhadap poros, momen inersia, atau kondisi awal rotasi) dan mengamati bagaimana torsi mempengaruhi sudut percepatan, kecepatan sudut, serta tercapainya keseimbangan rotasi.

## Hasil Output
- Grafik bentuk gelombang bunyi dalam domain ruang.
- ⁠Animasi propagasi gelombang bunyi terhadap waktu.
- ⁠Simulasi interaktif perubahan frekuensi dan amplitudo.
- ⁠Visualisasi perubahan bentuk gelombang saat frekuensi dan amplitudo diubah.

## Catatan
Notebook ini menggunakan ipywidgets (slider interaktif).
Fitur interaktif berjalan dengan baik di Google Colab,
namun tidak dapat ditampilkan langsung di GitHub.
