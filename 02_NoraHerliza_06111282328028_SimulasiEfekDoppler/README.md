# Simulasi Efek Doppler dengan Sumber Bergerak Melengkung

## Identitas
- Nama  : Nora Herliza 
- NIM   : 06111282328028
- Topik : Simulasi Efek Doppler dengan Sumber Bergerak Melengkung

## Deskripsi Singkat
Project ini mensimulasikan perubahan frekuensi teramati akibat sumber bunyi bergerak pada lintasan melengkung di bidang 2D dan pengamat tetap diam di satu titik. Simulasi memakai pendekatan numerik dengan posisi sumber disimulasikan secara diskret, kecepatan diperoleh dengan beda hingga, kemudian kecepatan radial dihitung untuk setiap langkah agar diperoleh frekuensi teramati $f(t)$.

## Tujuan 
Tujuan utama dari program ini adalah menganalisis bagaimana frekuensi bunyi yang diterima pengamat berubah ketika sumber bunyi bergerak pada lintasan melengkung di bidang 2D. Dengan menggunakan pendekatan numerik, simulasi ini memungkinkan kita menghitung perubahan posisi, kecepatan, dan terutama komponen radial kecepatan yang menentukan besar efek Doppler dari waktu ke waktu.

## File dalam Folder 
- `Efek_Doppler.ipynb` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat 
Simulasi ini tentang efek Doppler dengan sumber bunyi yang bergerak mengikuti lintasan melengkung di bidang dua dimensi, sementara pengamat berada pada posisi tetap. Dalam kondisi seperti ini, perubahan frekuensi yang diterima pengamat tidak hanya bergantung pada besar kecepatan sumber, tetapi juga pada komponen kecepatan radial.
Posisi sumber sebagai fungsi waktu dinyatakan sebagai

$$x(t) = R \cos\left( \frac{\pi t}{T} \right)$$

$$y(t) = R\sin\left(\frac{\pi t}{T}\right)$$

karena simulasi dilakukan secara numerik, kecepatan sumber dihitung menggunakan metode beda hingga:

$$\vec{v}_i \approx \dfrac{\vec{r}_i -\vec{r}_{i-1}}{\Delta t}$$

Untuk menentukan frekuensi yang diterima pengamat, hanya komponen kecepatan sumber yang searah dengan garis sumber–pengamat yang berpengaruh, yaitu kecepatan radial

$$v_{\text{rad}}(t) = \vec{v}(t)\cdot\hat{r}(t)$$

dengan $\hat{r}(t)$ adalah vektor satuan dari sumber menuju pengamat.

Sehingga frekuensi teramati pada setiap waktu adalah

$$f'(t)= f_0\\frac{v}{v - v_{\text{rad}}(t)}$$

dengan $v$ sebagai laju rambat bunyi diudara dan $f_0$ adalah frekuensi asli.

Jika $v_{\text{rad}}(t) < 0$, sumber secara radial menjauhi pengamat sehingga $f'(t)$ menurun. Sebaliknya, jika $v_{\text{rad}}(t) > 0$, sumber bergerak mendekat sehingga $f'(t)$ meningkat. 

## Cara Menjalankan File .ipynb di google Colab 
1. Klik tombol **Open in Colab** berikut.
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/physicsedu469/project_ComputationalThinking_2025/blob/main/02_NoraHerliza_06111282328028_SimulasiEfekDoppler/Efek_Doppler.ipynb)
3. Notebook akan terbuka di Google Colab.  
4. Jalankan sel secara berurutan untuk melihat simulasi.  
5. Anda dapat mengubah parameter (posisi pengamat, waktu simulasi, jari-jari lintasan, frekuensi asli) dan mengamati lintasan sumber dan perubahan frekuensi yang teramati.

## Hasil Output 
Notebook akan menampilkan:
- Grafik lintasan sumber dengan gerak melengkung  
- Grafik perubahan frekuensi yang teramati 
