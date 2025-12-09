# Simulasi Gerak Osilasi Dua Pendulum

## Identitas
- Nama  : Contoh 
- NIM   : 00000000
- Topik : Simulasi Gerak Osilasi Dua Pendulum

## Deskripsi Singkat
Project ini mensimulasikan gerak osilasi dua pendulum yang saling terkopel dengan mempertimbangkan pengaruh gaya redaman dan kopling pegas. Tidak seperti pendulum ideal tanpa gesekan, keberadaan redaman menyebabkan energi sistem berkurang secara bertahap, sementara kopling menghasilkan interaksi dinamis antara kedua pendulum sehingga muncul pola osilasi non-linear dan pertukaran energi. Simulasi dilakukan secara numerik menggunakan metode Runge–Kutta orde 5 (RK45) untuk memperoleh evolusi sudut dan kecepatan sudut kedua pendulum secara akurat terhadap waktu.

## Tujuan
1. Memahami pengaruh gaya redaman dan kopling pegas terhadap dinamika osilasi dua pendulum terkopel.
2. Mengimplementasikan model fisika pendulum terkopel ke dalam perhitungan numerik menggunakan metode time-stepping (RK45).
3. Menampilkan grafik evolusi sudut, energi, dan pola osilasi kedua pendulum secara komputasi.
4. Melatih keterampilan penggunaan Python/Jupyter Notebook dalam fisika komputasi.

## File dalam Folder
- `GerakOsilasiDuaPendulum.ipynb` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat
Pada sistem dua pendulum terkopel, masing-masing pendulum mengalami gaya pemulih akibat gravitasi yang membuatnya berosilasi di sekitar posisi setimbang. Ketika kedua pendulum dihubungkan oleh kopling, energi dapat berpindah dari satu pendulum ke pendulum lainnya, sehingga muncul pola gerak yang khas seperti mode sinkron (keduanya bergerak bersama) dan mode anti-sinkron (bergerak berlawanan). Kehadiran gaya redaman menyebabkan energi total sistem berkurang secara perlahan, membuat amplitudo osilasi semakin mengecil seiring waktu.

## Cara Menjalankan File .ipynb di google Colab
1. Klik tombol **Open in Colab** berikut.
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/physicsedu469/project_ComputationalThinking_2025/blob/main/17_NidiaAndika_06111282227044_GerakOsilasiDuaPendulum/GerakOsilasiDuaPendulum.ipynb)
3. Notebook akan terbuka di Google Colab.  
4. Jalankan sel-sel secara berurutan untuk melihat simulasi.  
5. Anda dapat mengubah parameter (kecepatan awal, sudut tembak, koefisien drag) dan mengamati perubahan lintasan.


## Hasil Output
Notebook akan menampilkan:
- Grafik osilasi sudut pendulum pertama (θ₁) dan pendulum kedua (θ₂) terhadap waktu 
- Grafik energi sistem terhadap waktu  
- diagram fase pendulum 1 dan pendulum 2
- output angka frekuensi mode sinkron dan antisinkron

