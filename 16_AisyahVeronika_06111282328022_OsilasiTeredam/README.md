# Simulasi Gerak Osilasi Teredam

## Identitas
- Nama  : Aisyah Veronika
- NIM   : 06111282328022
- Topik : Simulasi Gerak Osilasi Teredam

## Deskripsi Singkat
Project ini mensimulasikan gerak osilator harmonik teredam yang dipengaruhi oleh gaya
redaman. Berbeda dengan osilasi harmonik ideal tanpa redaman, keberadaan gaya
redaman menyebabkan amplitudo getaran berkurang seiring waktu hingga sistem
berhenti. Simulasi dilakukan secara numerik menggunakan metode Runge–Kutta orde
empat (RK4) untuk menyelesaikan persamaan diferensial gerak.

## Tujuan
1. Memahami pengaruh gaya redaman terhadap perilaku osilasi.
2. Mengimplementasikan model fisika osilator teredam ke dalam perhitungan numerik.
3. Menampilkan grafik posisi terhadap waktu secara komputasi.
4. Melatih keterampilan penggunaan Python/Jupyter Notebook dalam fisika komputasi.

## File dalam Folder
- `Simulasi_Gerak_Osilasi_Teredam.ipynb` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat
Gerak osilasi teredam merupakan gerak periodik suatu benda yang amplitudonya semakin mengecil seiring
waktu akibat adanya gaya hambatan dari lingkungan. Dalam model ini, gaya hambatan dianggap sebanding
dengan kecepatan benda dan arahnya berlawanan dengan arah geraknya, sehingga dapat dituliskan sebagai:

$\vec{F_d} = -b\vec{v}$

Persamaan gerak sistem tidak diselesaikan secara analitik, melainkan secara numerik menggunakan pendekatan
time-stepping. Pada pendekatan ini, posisi dan kecepatan benda dihitung secara bertahap untuk setiap selang
waktu kecil menggunakan metode Runge–Kutta orde empat (RK4).

Pendekatan numerik ini memungkinkan simulasi dilakukan secara fleksibel untuk berbagai nilai parameter fisika,
sehingga pengaruh gaya redaman terhadap perubahan amplitudo simpangan dapat diamati melalui grafik hasil simulasi.


## Cara Menjalankan File .ipynb di google Colab
1. Klik tombol **Open in Colab** berikut.
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aisyahvrnka/project_ComputationalThinking_2025/blob/main/16_AisyahVeronika_06111282328022_OsilasiTeredam/Simulasi_Gerak_Osilasi_Teredam.ipynb)
3. Notebook akan terbuka di Google Colab.  
4. Jalankan sel-sel secara berurutan untuk melihat simulasi.  
5. Anda dapat mengubah parameter (massa, konstanta pegas, koefisien redaman, kondisi awal) untuk melihat perubahan grafik.

## Hasil Output
Notebook akan menampilkan:
- Grafik posisi terhadap waktu pada osilator teredam.
- Grafik kecepatan terhadap waktu. 
- Perbandingan pengaruh redaman kecil dan besar.
