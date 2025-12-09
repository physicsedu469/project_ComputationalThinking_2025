# Simulasi Gerak Vertikal dengan Hambatan Udara Linear

## Identitas
- Nama  : Anesa Merlinda Putri
- NIM   : 06111282328025
- Topik : Simulasi Gerak Vertikal dengan Hambatan Udara Linear

## Deskripsi Singkat
Simulasi ini memodelkan gerak vertikal suatu benda yang dipengaruhi dua gaya utama, yaitu gaya gravitasi dan gaya hambatan udara linear yang dirumuskan sebagai $$F_d = -cv$$. Dengan adanya hambatan udara, percepatan benda tidak lagi konstan, sehingga kecepatan dan posisi harus dihitung secara bertahap melalui pendekatan numerik. Pada setiap langkah waktu, simulasi memperbarui kecepatan dan posisi menggunakan persamaan diferensial dasar gerak, sehingga evolusi gerak benda baik saat naik maupun jatuh dapat dilihat secara realistis hingga mencapai tanah atau kecepatan terminal.

## Tujuan
1. Memahami pengaruh hambatan linear terhadap lintasan, kecepatan terminal, waktu terbang, dan ketinggian maksimum.
2. Menampilkan grafik lintasan peluru secara komputasi.
3. Melatih keterampilan penggunaan Python/Jupyter Notebook dalam fisika komputasi.

## File dalam Folder
- `Simulasi_Gerak_Vertikal_dengan_Hambatan_Udara_Linear.ipynb` → notebook berisi simulasi lengkap.
- `README.md` → penjelasan project.

## Penjelasan Fisis Singkat
Ketika sebuah benda bergerak vertikal melalui udara, ia tidak hanya dipengaruhi oleh gaya gravitasi, tetapi juga oleh gaya hambatan udara yang selalu berlawanan arah dengan geraknya. Dalam model hambatan linear, gaya hambatan diberikan oleh:

$$F_d = -cv$$

yang menunjukkan bahwa semakin besar kecepatan benda, semakin besar pula hambatannya. Gaya ini kemudian digabungkan dengan gravitasi sehingga persamaan gerak kecepatan menjadi:

$$\frac{dv}{dt} = -g - \frac{c}{m}v$$

yang berarti percepatan benda bergantung pada besar kecepatan saat itu. Ketika benda jatuh, gravitasi mempercepat gerak, namun hambatan udara menghambatnya. Seiring meningkatnya kecepatan, gaya hambatan semakin kuat sehingga percepatan menjadi semakin kecil. Pada kondisi tertentu, gaya hambatan dapat menjadi sama besar dengan gravitasi, menghasilkan kecepatan terminal, yaitu keadaan ketika percepatan bernilai nol dan benda bergerak dengan kecepatan konstan.

Selain itu, gerak vertikal tidak hanya ditentukan oleh perubahan kecepatan tetapi juga posisi. Hubungan antara posisi dan kecepatan dinyatakan oleh persamaan:

$$\frac{dy}{dt} = v$$

yang merupakan definisi dasar dalam kinematika: perubahan posisi per satuan waktu adalah kecepatan. Secara fisis, jika kecepatan bernilai positif, benda bergerak ke atas; jika negatif, benda bergerak ke bawah; dan pada titik ketika kecepatan nol, benda berada di titik balik geraknya. Persamaan inilah yang digunakan untuk memperbarui posisi benda pada setiap langkah waktu dalam simulasi numerik.

Jika benda dilempar ke atas, hambatan udara bekerja ke arah bawah, sehingga perlambatan benda lebih besar dari kasus tanpa hambatan. Benda mencapai ketinggian maksimum lebih cepat dan lebih rendah. Ketika benda mulai jatuh, hambatan udara kembali bekerja melawan arah gerak sehingga memperlambat penambahan kecepatan jatuh. Dengan menggunakan perhitungan numerik secara bertahap, seluruh dinamika ini baik pada fase naik maupun turun dapat diamati secara lengkap sesuai model hambatan linear.

## Cara Menjalankan File .ipynb di google Colab
1. Klik tombol **Open in Colab** berikut.
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/physicsedu469/project_ComputationalThinking_2025/blob/main/06_AnesaMerlindaPutri_06111282328025_GerakVertikal/SimulasiGerakVertikal.ipynb)
3. Notebook akan terbuka di Google Colab.  
4. Jalankan sel-sel secara berurutan untuk melihat simulasi.  
5. Anda dapat mengubah parameter (massa, keofisien hambatan,gravitasu, posisi awal, kecepatan awal) dan mengamati perubahan lintasan.


## Hasil Output
Notebook akan menampilkan:
- Grafik Posisi terhadap waktu  
- Grafik Kecepatan terhadap waktu 
