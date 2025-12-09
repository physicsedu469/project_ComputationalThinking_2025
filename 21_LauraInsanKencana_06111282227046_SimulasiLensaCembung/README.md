# Simulasi Lensa cembung

## Identitas
- Nama  : Laura Insan Kencana
- NIM   : 06111282227046
- Topik : Simulasi Lensa Cembung

## Deskripsi Singkat
Proyek ini mensimulasikan pembentukan bayangan oleh lensa cembung menggunakan pendekatan komputasi. 
Dengan memanfaatkan rumus lensa tipis dan pembesaran simulasi ini menunjukkan bagaimana posisi dan 
ukuran bayangan berubah sesuai dengan jarak benda terhadap lensa. Grafik yang dihasilkan menggambarkan 
zona bayangan nyata (terbalik) dan maya (tegak), serta perilaku ekstrem saat benda mendekati titik fokus.

## Tujuan
1. Memahami hubungan antara posisi benda, posisi bayangan, dan pembesaran pada lensa cembung.
2. Mengimplementasikan rumus fisika optik ke dalam perhitungan numerik.
3. Menampilkan grafik posisi bayangan dan pembesaran secara komputasi.
4. Melatih keterampilan penggunaan Python/Jupyter Notebook dalam fisika komputasi.

## File dalam Folder
- `LensaCembung.ipynb` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat
Lensa cembung memfokuskan cahaya sejajar ke satu titik fokus. 
Ketika sebuah benda ditempatkan di depan lensa, bayangan terbentuk 
dengan karakteristik yang bergantung pada jarak benda terhadap lensa. 

Hubungan antara jarak benda (\(s\)), jarak bayangan (\(s'\)), dan panjang fokus (\(f\)) dinyatakan oleh:
\[
\frac{1}{f} = \frac{1}{s} + \frac{1}{s'}
\]

Bayangan nyata terbentuk jika \(s' > 0\), berada di sisi berlawanan dari benda dan bersifat terbalik.  
Bayangan maya terbentuk jika \(s' < 0\), berada di sisi yang sama dengan benda dan tampak tegak.  

Pembesaran bayangan dihitung dengan:
\[
M = -\frac{s'}{s}
\]

Simulasi dilakukan secara numerik untuk menampilkan grafik posisi bayangan dan pembesaran terhadap jarak benda.

## Cara Menjalankan File .ipynb di google Colab
1. Klik tombol **Open in Colab** berikut.
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/laurakencana13/project_ComputationalThinking_2025/blob/main/21_LauraInsankencana_06111282227046_SimulasiLensaCembung/LensaCembung.ipynb)
3. Notebook akan terbuka di Google Colab.  
4. Jalankan sel-sel secara berurutan untuk melihat simulasi.  
5. Anda dapat mengubah parameter (misalnya panjang fokus atau rentang jarak benda) dan mengamati perubahan grafik.

## Hasil Output
Notebook akan menampilkan:
- Grafik posisi bayangan (\(s'\)) terhadap jarak benda (\(s\)), menunjukkan zona bayangan nyata dan maya.
- Grafik pembesaran (\(M\)) terhadap jarak benda, memperlihatkan orientasi dan ukuran bayangan.
- Perbedaan karakteristik bayangan berdasarkan posisi benda terhadap titik fokus.
- Visualisasi numerik yang mendukung pemahaman konsep optik lensa cembung.
