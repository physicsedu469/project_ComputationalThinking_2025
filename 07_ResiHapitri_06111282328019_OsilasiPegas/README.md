# Simulasi Osilasi Pegas
## Identitas
- Nama    : Resi Hapitri
- NIM     : 06111282328019
- Topik   : Simulasi Osilasi Pegas
  
## Deskripsi Singkat
Proyek ini membuat simulasi gerak osilasi pegas berdasarkan Hukum Hooke menggunakan metode komputasi numerik Finite Difference (Euler Method). Simulasi menampilkan grafik hubungan antara perpindahan (x) dan waktu (t) untuk melihat bagaimana massa pada pegas bergerak naik–turun secara periodik. Pada sistem pegas-massa, jika sebuah massa ditarik dari posisi keseimbangan dan dilepaskan, benda akan bergerak bolak-balik (osilasi). Secara teori, gerakan ini dapat dihitung menggunakan persamaan diferensial. Namun dalam simulasi komputasi, gerak pegas dihitung sedikit demi sedikit dengan metode numerik finite difference, bukan langsung menggunakan persamaan analitik.

## Tujuan
Proyek simulasi ini bertujuan untuk memberikan pemahaman yang lebih mendalam tentang bagaimana sistem pegas bekerja dan bagaimana gerakan osilasi dapat dianalisis melalui pendekatan komputasi. Dengan melakukan simulasi menggunakan metode numerik finite difference, mahasiswa dapat mengamati secara langsung perubahan posisi suatu massa pada pegas dari waktu ke waktu, tanpa harus menggunakan alat laboratorium fisik.

## File dalam Folder
- `Simulasi_Osilasi_Pegas.ipynb` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisika
Pada sistem pegas, ketika sebuah benda ditarik menjauh dari posisi awalnya kemudian dilepaskan, pegas akan berusaha kembali ke posisi semula. Karena pegas menarik benda kembali, benda tersebut tidak langsung berhenti di titik tengah, tetapi malah bergerak melewati titik tersebut dan terus bergerak ke sisi yang berlawanan. Setelah itu, gaya dari pegas kembali menarik benda lagi ke posisi awal.
Akibat dari saling tarik menarik antara gaya pegas dan gerakan benda, benda akan bergerak naik dan turun secara teratur. Gerakan ini disebut osilasi atau getaran berulang, mirip seperti pergerakan per atau pegas di pulpen, shockbreaker motor, atau ayunan tempat tidur yang digoyang.
Kecepatan benda akan berubah-ubah: paling cepat ketika melewati posisi tengah, dan paling lambat ketika mencapai titik paling jauh. Gerakan seperti ini terjadi terus menerus selama tidak ada hambatan udara atau gesekan. Bila ada gesekan atau redaman, gerakannya akan semakin melemah dan akhirnya berhenti.
Simulasi komputer digunakan untuk meniru gerakan ini dari waktu ke waktu sehingga kita bisa melihat bentuk getaran dalam grafik, tanpa harus melakukan percobaan langsung di laboratorium.

Gaya pegas mengikuti Hukum Hooke:

$$ F = -kx $$

Karena Hukum Newton II:

$$ F = ma $$

Maka:

$$ ma = -kx $$

Percepatan adalah turunan kecepatan terhadap waktu:

$$ a = \frac{dv}{dt} $$

Sehingga persamaan geraknya menjadi:

$$ \frac{dv}{dt} = -\frac{k}{m}x $$

Gerak ini menghasilkan **osilasi harmonik sederhana**, yaitu gerak periodik yang berulang-ulang.

## Cara Menjalankan File .ipynb di google Colab
1. Klik tombol **Open in Colab** berikut.
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/physicsedu469/project_ComputationalThinking_2025/blob/main/00_Contoh_000000_gerakPeluru_drag/gerakPeluru_drag.ipynb)
3. Notebook akan terbuka di Google Colab.  
4. Jalankan sel-sel secara berurutan untuk melihat simulasi.  
5. Anda dapat mengubah parameter (konstanta pegas, massa benda, posisi awal, kecepatan awal, langkah waktu dan durasi simulasi)

## Hasil Output
Notebook akan menampilkan:
- bergerak bolak–balik di sekitar titik setimbang
- membentuk osilasi periodik
- amplitudo tampak berkurang sedikit karena efek numerik metode Euler
