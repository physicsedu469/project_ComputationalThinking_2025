# Simulasi Bandul Teredam dengan Hambatan Udara

## Identitas
Nama : Alifah Ratna Aristia

NIM : 06111282227030

Topik : Simulasi Bandul Teredam dengan Hambatan Udara

## Deskripsi Singkat
Proyek ini mensimulasikan gerak bandul sederhana yang mengalami gaya hambatan udara.
Akibat adanya hambatan, energi bandul tidak lagi konstan dan amplitudo sudut berangsur menurun.
Perhitungan dilakukan secara numerik dengan metode Euler sehingga gerakan bandul dapat divisualisasikan melalui grafik sudut dan energi terhadap waktu.

## Tujuan
- Memahami efek gaya hambatan terhadap osilasi bandul
- Membandingkan energi mekanik terhadap waktu
- Melatih pemrograman fisika menggunakan Python di Google Colab
  
## File dalam Folder
- bandul_teredam.ipynb → notebook simulasi lengkap
- README.md → penjelasan proyek

## Penjelasan Fisis Singkat
Gerakan bandul dipengaruhi oleh dua gaya utama:
1. Gaya gravitasi (mg) → mengembalikan bandul ke titik keseimbangan
2. Gaya hambatan udara (drag) → berlawanan dengan arah kecepatan sudut
Persamaan dinamika bandul teredam adalah:

θ'' + (b/m)θ' + (g/L) sin(θ) = 0

Akibat adanya hambatan:
- Energi mekanik berkurang → gerak semakin lambat
- Amplitudo sudut makin kecil hingga berhenti pada titik keseimbangan
Ini menunjukkan terjadinya konversi energi mekanik menjadi energi panas melalui hambatan udara.

## Cara Menjalankan File .ipynb di google Colab
1. Buka Google Colab: 
2. Notebook akan terbuka di Google Colab
3. Jalankan sel-sel secara berurutan untuk melihat simulasi
4. Ubah parameter (massa, panjang, redaman) untuk melihat perubahan grafik

## Hasil Output
- Grafik sudut vs waktu
- Grafik energi vs waktu
