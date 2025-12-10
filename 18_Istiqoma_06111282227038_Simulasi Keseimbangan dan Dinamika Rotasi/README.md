# Simulasi Keseimbangan dan Dinamika Rotasi

## Identitas
- Nama  : Istiqoma
- NIM   : 06111282227038
- Topik : Simulasi Keseimbangan dan Dinamika Rotasi

## Deskripsi Singkat
Dinamika Rotasi adalah ilmu yang mempelajari tentang pergerakan benda yang berputar pada porosnya atau titik tumpunya.Dinamika Rotasi ini dipengaruhi oleh beberapa hal diantaranya yaitu massa benda,gaya,kecepatan,percepatan,torsi dan masih banyak lagi.Sebenarnya,benda yang bergerak secara berotasi akan menggunakan konsep hukum II Newton (ΣF=m.a),namun karena benda berotasi pada porosnya dan dipengaruhi oleh torsi,maka diberlakukan rumus:

Στ = I. α

Keterangan:

ΣF : Resultan gaya (N)

m : Massa/ukuran kelembaman (kg)

a : Percepatan (m/s2)

Στ : Momen torsi (Nm)

I : Momen inersia (kgm2)

α : Percepatan sudut (rad/s)

Benda tegar adalah benda yang tidak mengalami perubahan bentuk jika diberi gaya F tertentu pada benda tersebut. Hal ini karena benda tegar memiliki banyak partikel yang mengaitkan satu sama lain dan membentuk sebuah ukuran tertentu.Maka dalam hal ini, keseimbangan benda tegar berkaitan dengan Hukum Newton I dengan menggunakan konsep ΣF=0 dan Στ=0 atau keseimbangan translasi. Jadi, kesetimbangan benda tegar adalah ketika benda dinilai sebagai
bagian titik dengan ΣF=0, artinya benda tersebut seimbang. Contohnya misal seorang pemain akrobat yang tengah berdiri di atas tali dengan membawa tongkat yang panjang. Pemain ini memegang tongkat tepat di tengah-tengah. Akibatnya, gaya berat tongkat pada setiap sisi sama besar.Gaya ini menimbulkan momen gaya pada sumbu putar (tubuh pemain akrobat) sama besar dengan arah berlawanan, sehingga terjadi keseimbangan rotasi. Ini
menyebabkan pemain lebih mudah berjalan di atas tali.

## Tujuan
1. Memahami konsep torsi (momen gaya), momen inersia, serta hubungan antara torsi dan percepatan sudut.
2. Menganalisis kondisi keseimbangan rotasi pada benda tegar melalui prinsip ∑τ = 0 dan ∑F = 0.
3. Mengimplementasikan model fisika ke dalam perhitungan numerik di Python.
4. Menampilkan animasi dan grafik perubahan sudut, kecepatan sudut, torsi, dan energi rotasi untuk mengamati dinamika rotasi dan kondisi keseimbangan.

## File dalam Folder
- ` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat
1. Keseimbangan Benda Tegar
Dalam sistem partikel, benda dianggap sebagai suatu titik materi. Semua gaya yang bekerja pada benda dianggap bekerja pada titik materi tersebut, sehingga gaya yang bekerja dapat menyebabkan gerak translasi (tidak menyebabkan gerak rotasi). Oleh karena itu, syarat keseimbangan pada sistem partikel hanya berlaku untuk keseimbangan translasi:
 ∑F = 0 

 2. Dinamika Rotasi
Dinamika rotasi adalah ilmu yang mempelajari tentang gerak rotasi (berputar) dengan memperhatikan aspek penyebabnya, yaitu momen gaya. Momen gaya atau yang lebih dikenal dengan torsi ini akan menyebabkan terjadinya percepatan sudut. Suatu benda dikatakan melakukan gerak rotasi (berputar) jika semua bagian benda bergerak mengelilingi poros atau sumbu putar. Sumbu putar benda terletak
pada salah satu bagian dari benda tersebut.

## Cara Menjalankan File .ipynb di google Colab
1. Klik tombol **Open in Colab** berikut.
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/physicsedu469/project_ComputationalThinking_2025/blob/main/018_Istiqoma_06111282227038_SimulasiKeseimbangandanDinamikaRotasi/keseimbangan_dan_dinamika_rotasi.ipynb)

2. Notebook akan terbuka di Google Colab.  
3. Jalankan sel-sel secara berurutan untuk melihat simulasi.  
4. Anda dapat mengubah parameter engubah parameter (gaya besar, posisi gaya kerja terhadap poros, momen inersia, atau kondisi awal rotasi) dan mengamati bagaimana torsi mempengaruhi sudut percepatan, kecepatan sudut, serta tercapainya keseimbangan rotasi.

## Hasil Output

Perhitungan torsi, momen gaya, dan momen inersia pada berbagai sistem rotasi sederhana.
Simulasi dan grafik hubungan antara torsi dan percepatan sudut sesuai Hukum II Newton untuk rotasi.
Grafik perbandingan kondisi seimbang dan tidak seimbang pada benda tegar (∑τ = 0 vs ∑τ ≠ 0).


