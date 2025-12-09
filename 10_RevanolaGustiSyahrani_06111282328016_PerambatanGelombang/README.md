# Simulasi Perambatan Gelombang 2D Dengan Metode Finite Difference

## Identitas
- Nama  : Revanola Gusti Syahrani
- NIM   : 06111282328016
- Topik : Simulasi Perambatan Gelombang 2D Dengan Metode Finite Difference

## Deskripsi Singkat
Project ini mensimulasikan perambatan gelombang 2D pada suatu medium menggunakan metode Finite Difference (FDTD / Finite Difference Time Domain).
Model numerik ini digunakan untuk menghitung evolusi gelombang dari waktu ke waktu berdasarkan persamaan gelombang 2D.

## Tujuan
1. Memahami konsep dasar perambatan gelombang 2D.
2. Mengimplementasikan persamaan gelombang ke bentuk numerik dengan metode Finite Difference.
3. Menampilkan grafik perubahan parameter seperti redaman (α), kecepatan gelombang (c), dan Courant number (r).
4. Melatih keterampilan pemrograman Python/Jupyter Notebook dalam fisika komputasi.

## File dalam Folder
- `10_RevanolaGustiSyahrani_06111282328016_PerambatanGelombang.ipynb` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project dan petunjuk penggunaan.

## Penjelasan Fisis Singkat
Simulasi didasarkan pada persamaan gelombang 2D:

```math
\frac{\partial^2 u}{\partial t^2}
=
c^2\left(
\frac{\partial^2 u}{\partial x^2}
+
\frac{\partial^2 u}{\partial y^2}
\right)
```

Pendekatan numerik menggunakan skema central difference pada ruang dan waktu:

```math
u^{k+1}_{i,j}
=
2u^k_{i,j} - u^{k-1}_{i,j}
+
\frac{c^2 (\Delta t)^2}{h^2}
\left(
u^k_{i+1,j}
+
u^k_{i-1,j}
+
u^k_{i,j+1}
+
u^k_{i,j-1}
-
4u^k_{i,j}
\right)
```

Dengan parameter Courant:
```math
b = \frac{c^2 (\Delta t)^2}{h^2}
```

Model juga memasukkan faktor redaman (α) untuk mensimulasikan kehilangan energi pada medium.

## Cara Menjalankan File .ipynb di google Colab
1. Klik tombol **Open in Colab** berikut.
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/physicsedu469/project_ComputationalThinking_2025/blob/main/10_RevanolaGustiSyahrani_06111282328016_PerambatanGelombang.ipynb)
3. Notebook akan terbuka di Google Colab.  
4. Jalankan sel-sel secara berurutan untuk melihat simulasi.  
5. Anda dapat mengubah parameter (kecepatan gelombang c, redaman α, courant number r), bentuk kondisi awal lalu amati perubahannya.


## Hasil Output
Notebook akan menampilkan:
- Perbandingan gelombang untuk berbagai redaman α = (0, 0.01, 0.05).  
- Perbandingan gelombang untuk c berbeda c = (0.5, 1.0, 2.0).  
- Perbedaan pola gelombang berdasarkan Courant Number r = (0.2, 0.5, 0.7).

