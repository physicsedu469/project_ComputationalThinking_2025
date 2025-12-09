# Pengaruh Panjang Gelombang Terhadap Pola Difraksi

## Identitas
- Nama  : Anisa Qoriq Atun Nasiroh
- NIM   : 06111282328017
- Topik : Pengaruh Panjang Gelombang Terhadap Pola Difraksi

## Deskripsi Singkat
Project ini mensimulasikan pola difraksi cahaya yang melewati kisi difraksi berdasarkan variasi panjang gelombang. Difraksi terjadi ketika cahaya melewati celah atau kisi sempit, sehingga gelombang cahaya menyebar dan membentuk pola maksimum dan minimum intensitas pada layar. Dalam simulasi ini, pola difraksi dihitung secara numerik menggunakan persamaan difraksi kisi dan divisualisasikan dalam bentuk grafik untuk beberapa panjang gelombang berbeda. Hasil visualisasi menunjukkan bahwa posisi maksimum difraksi bergantung langsung pada panjang gelombang cahaya. Semakin besar panjang gelombang, pola difraksi semakin melebar dan titik puncaknya bergeser lebih jauh dari pusat.

## Tujuan
1. Memahami pengaruh panjang gelombang cahaya terhadap pola difraksi pada kisi.
2. Mengimplementasikan model fisika difraksi ke dalam perhitungan numerik.
3. Menampilkan grafik pola difraksi secara komputasi.
4. Melatih keterampilan penggunaan Python/Notebook dalam simulasi fisika.

## File dalam Folder
- `Pengaruh_Panjang_Gelombang_Terhadap_Pola_Difraksi.ipynb` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat

Ketika cahaya melewati celah, maka digunkan rumus:

$$I_{\text{single}} = I_0 \left(\frac{\sin \beta}{\beta}\right)^2, \quad \beta = \frac{\pi a x}{\lambda L}$$

$$I_{\text{multi}} =\left(\frac{\sin(N\alpha)}{\sin(\alpha)}\right)^2, \quad \alpha = \frac{\lambda L \pi}{dx}$$

sehingga didapat $I_{\text{total}}$

$$\mathbf{I_{\text{total}} =  I_{\text{single}} \times I_{\text{multi}}}$$

Normalisasikan $I_{\text{total}}$ sehingga didapat

$$I_{\text{norm}} = \frac{I_{\text{single}} \cdot I_{\text{multi}}}{\max(I_{\text{single}} \cdot I_{\text{multi}})}$$


## Cara Menjalankan File .ipynb di google Colab
1. Klik tombol **Open in Colab** berikut.
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/physicsedu469/project_ComputationalThinking_2025/blob/main/05_AnisaQoriqAtunNasiroh_06111282328017_SimulasiDifraksi_drag/SimulasiDifraksi_drag.ipynb)
3. Notebook akan terbuka di Google Colab.  
4. Jalankan sel-sel secara berurutan untuk melihat simulasi.  
5. Anda dapat mengubah parameter (panjang gelombang (λ), konstanta kisi (d), lebar celah tiap garis (a), jumlah celah (N)) dan mengamati perubahan pola difraksi.

## Hasil Output
Notebook akan menampilkan:
- Grafik pola difraksi.  
- Perbandingan antara antara beberapa variasi panjang gelombang.  
- Variasi lebar dan posisi puncak saat mengubah beberapa parameter (d, a, N, L).
