# Simulasi Penyebaran Gelombang Bunyi

## Identitas
- Nama   : Dea Amalia
- NIM    : 06111282328015
- Topik  : Simulasi Penyebaran Gelombang Bunyi Di Ruangan 2D Secara Numerik

## Deskripsi Singkat
Proyek ini mensimulasikan penyebaran gelombang bunyi di dalam ruang dua dimensi menggunakan metode FDTD (Finite Difference Time Domain). Melalui model akustik linier, tekanan 
p(x,y,t) dihitung pada setiap grid sehingga proses perambatan, pantulan dari dinding, hingga interferensi dapat terlihat secara jelas. Persamaan gelombang yang digunakan berasal dari gabungan persamaan momentum dan kontinuitas, kemudian disederhanakan menjadi bentuk diskrit yang dapat dieksekusi secara numerik. Simulasi ini memungkinkan kita mengamati bagaimana gelombang yang diberikan pada sebuah titik sumber menyebar ke seluruh domain, mengalami pemantulan pada batas ruangan, dan membentuk pola tekanan yang berubah seiring waktu. Selain pola ruang, juga ditampilkan sinyal tekanan pada titik tertentu serta evolusi energi sistem, yang memberi gambaran apakah metode yang dipakai stabil dan apakah pantulan dalam domain mempengaruhi dinamika energi.

## Tujuan
1. Memahami proses fisik penyebaran gelombang bunyi dalam ruang 2D
2. Menerapkan metode FDTD untuk menyelesaikan persamaan gelombang akustik
3. Mengamati pola tekanan, profil tekanan per-penampang, dan energi total
4. Melatih implementasi komputasi fisika menggunakan Python/Colab

## File dalam Folder
- `SimulasiPenyebaranGelombangBunyi.ipynb` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat
**1. Persamaan Dasar**

Model akustik linier dibangun dari dua hukum fluida:

a. Persamaan momentum (Euler linier)

$$\rho_0 \frac{\partial \mathbf{v}}{\partial t} = - \nabla p$$

b. Persamaan kontinuitas

$$\frac{\partial \rho'}{\partial t} = - \rho_0 \nabla \cdot \mathbf{v}$$

   Dengan:
   $p$      = tekanan akustik
   $v$      = kecepatan partikel
   $\rho_0$ = densitas udara
   $\rho'$  = perubahan densitas


**2. Persamaan Keadaan Linier**

$$p = c^{2}\rho'$$

dengan 
$𝑐$ adalah kecepatan rambat bunyi.

**3. Eliminasi Variabel Menjadi Persamaan Gelombang**
Gabungan momentum + kontinuitas + keadaan:

$$\frac{\partial^{2} p}{\partial t^{2}} = c^{2} \nabla^{2} p + s(x,y,t)$$

Persamaan ini menjadi dasar metode FDTD.

**4. Diskritisasi Ruang 2D**

Operator Laplace 2D disederhanakan menjadi skema lima-titik:

$$\nabla^{2} p \approx \frac{1}{h^{2}}
\left( p_{i+1,j} + p_{i-1,j} + p_{i,j+1} + p_{i,j-1} - 4p_{i,j} \right)$$

**5. Diskritisasi Waktu Orde-2**

$$\frac{\partial^{2} p}{\partial t^{2}}
\approx
\frac{1}{\Delta t^{2}}
\left( p_{i,j}^{\,n+1} - 2p_{i,j}^{\,n} + p_{i,j}^{\,n-1} \right)$$

**6. Skema FDTD Final**

$p_{i,j}^{\,n+1} = 2p_{i,j}^{\,n} - p_{i,j}^{\,n-1} + \lambda^{2}\left( p_{i+1,j}^{\,n} + p_{i-1,j}^{\,n} + p_{i,j+1}^{\,n} + p_{i,j-1}^{\,n} - 4p_{i,j}^{\,n} \right) + s_{i,j}^{\,n}(\Delta t)^{2}$

dengan 

$$\lambda = \frac{c \, \Delta t}{h}$$




## Cara Menjalankan File .ipynb di google Colab
1. Klik tombol *Open in Colab* berikut.
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/physicsedu469/project_ComputationalThinking_2025/blob/main/13_DeaAmalia_06111282328015_SimulasiPenyebaranGelombangBunyi/SimulasiPenyebaranGelombangBunyi.ipynb)
4. Jalankan sel-sel secara berurutan untuk melihat simulasi.  
5. Anda dapat mengubah parameter (kecepatan awal, sudut tembak, koefisien drag) dan mengamati perubahan lintasan.


## Hasil Output
Notebook menampilkan beberapa visualisasi utama:
1. Tekanan pada Titik Sumber
Grafik memperlihatkan respons impuls: gelombang langsung, pantulan, serta interferensi.
2. Distribusi Tekanan pada Penampang Horizontal
Profil tekanan pada waktu akhir menggambarkan pola gelombang di sepanjang ruangan.
3. Energi Total vs Waktu
Menunjukkan stabilitas metode FDTD dan pengaruh pantulan terhadap energi sistem.
