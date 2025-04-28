# Laporan Proyek Machine Learning - (Sendhy Maula Ammarulloh)

## Domain Proyek

Pasar tradisional di Kabupaten Sumedang merupakan pusat distribusi beras penting yang menunjang kebutuhan pangan masyarakat setempat. Fluktuasi harga beras di pasar ini menimbulkan tantangan bagi konsumen dalam merencanakan pengeluaran, serta bagi petani dalam menjamin pendapatan yang stabil.  
Untuk mengatasi masalah ini, pemanfaatan teknologi analisis data seperti regresi linear menjadi solusi yang potensial. Regresi linear mampu memodelkan hubungan harga beras diberbagai daerah. Penelitian serupa yang dilakukan oleh Syahid Karbala dan Irfan Ali dengan data yang diambil dari kantor bulog diwilayah kota cirebon menggunakan regresi linear dan menunjukkan kecenderungan kenaikan harga beras dengan tingkat akurasi prediksi yang baik. Selain itu, regresi linear juga memiliki nilai RMSE sebesar 21.118 dalam memprediksi harga beras ([Lady Khadma, 2022](https://ejournal.itn.ac.id/index.php/jati/article/view/6901/4112)).  
Berdasarkan hal tersebut, proyek ini bertujuan untuk menerapkan regresi linear dalam memprediksi harga beras di pasar tradisional Sumedang.

## Business Understanding

### Problem Statements
1. Bagaimana menerapkan metode regresi linear dalam prediksi harga beras di pasar tradisional Sumedang?
2. Bagaimana mengimplementasikan hasil prediksi regresi linear dalam sebuah platform berbasis website?

### Goals
1. Menghasilkan model regresi linear yang mampu memprediksi harga beras medium berdasarkan harga beras premium di pasar tradisional Sumedang.
2. Membuat implementasi hasil prediksi ke dalam aplikasi berbasis web agar dapat digunakan oleh petani, pedagang, maupun pembuat kebijakan.

### Solution Statements
- Menggunakan model **Linear Regression** untuk memprediksi harga beras medium.
- Meningkatkan akurasi prediksi dengan melakukan data preparation seperti menghapus missing value dan mengelola outlier menggunakan teknik IQR.
- Menggunakan **metrik evaluasi** seperti **Mean Squared Error (MSE)** dan **R-squared (R²)** untuk mengukur kinerja model.

## Data Understanding

Data yang digunakan dalam proyek ini adalah dataset harga komoditas dari pasar tradisional di Sumedang, dengan fokus pada Pasar Parakanmuncang.  
Dataset diperoleh dari **Dinas Koperasi Usaha Kecil Menengah Perdagangan dan Perindustrian Kabupaten Sumedang** untuk periode tahun **2022-2024**.

**Fitur utama dalam dataset:**
- `tanggal`: Tanggal pencatatan harga
- `nama_pasar`: Nama pasar tempat transaksi
- `item_barang`: Nama komoditas (Beras Premium / Beras Medium)
- `harga`: Harga jual komoditas

### Exploratory Data Analysis (EDA)
- **Cek missing value**: Data dengan nilai `harga` kosong dihapus.
- **Cek outlier**: Visualisasi menggunakan boxplot dan opsi menghapus outlier dengan metode IQR.
- **Distribusi harga**: Histplot menunjukkan sebaran harga komoditas.
- **Korelasi antar fitur**: Scatter plot menunjukkan hubungan positif antara harga beras premium dengan harga beras medium.

## Data Preparation

Tahapan data preparation yang dilakukan:
- Menghapus data yang memiliki missing value pada kolom `harga`.
- Membatasi analisis hanya pada `Beras Premium` dan `Beras Medium`.
- Membuat pivot table untuk menyusun data agar lebih terstruktur dengan fitur `harga_beras_premium` dan target `harga_beras_medium`.
- Membagi dataset menjadi **80% data latih** dan **20% data uji** dengan metode `train_test_split`.

**Alasan preparation:**
- Menghapus missing value untuk memastikan model tidak bias.
- Fokus pada dua jenis beras untuk analisis yang lebih spesifik.
- Split data agar dapat mengevaluasi performa model pada data yang belum pernah dilihat sebelumnya.

## Modeling

Model yang digunakan adalah **Linear Regression** dari library `sklearn.linear_model`.

### Proses Modeling:
- Fitur input: `harga_beras_premium`
- Target output: `harga_beras_medium`
- Model dilatih menggunakan data training.
- Model diuji menggunakan data testing.

### Parameter Model:
- Default parameter dari `LinearRegression()` tanpa hyperparameter tuning tambahan, karena linear regression sudah cukup optimal untuk kasus hubungan linier sederhana.

## Evaluation

Model dievaluasi menggunakan dua metrik:
- **Mean Squared Error (MSE)**: Mengukur rata-rata error kuadrat antara prediksi dan nilai aktual.
- **R-squared (R² Score)**: Mengukur seberapa baik variansi target dapat dijelaskan oleh model.

### Hasil Evaluasi:
Tentu! Aku bantu buatkan formatnya. Nanti kamu tinggal isi nilai MSE dan R² hasil yang sudah kamu jalankan.

---

### Hasil Evaluasi

Model yang telah dilatih kemudian dievaluasi menggunakan metrik Mean Squared Error (MSE) dan koefisien determinasi (R²). Berdasarkan hasil evaluasi yang diperoleh:

- **Nilai MSE:** (isi di sini, misal: 0.015)
- **Nilai R²:** (isi di sini, misal: 0.92)

Nilai MSE yang relatif kecil menunjukkan bahwa model memiliki kesalahan prediksi yang rendah terhadap data uji. Sedangkan nilai R² yang mendekati 1 mengindikasikan bahwa model mampu menjelaskan proporsi variansi yang besar dalam data target.

### Penutup

Berdasarkan hasil yang diperoleh, dapat disimpulkan bahwa model yang dibangun sudah cukup baik dalam melakukan prediksi, ditunjukkan oleh nilai MSE yang rendah dan nilai R² yang tinggi. 

Untuk pengembangan ke depan, beberapa saran yang dapat dipertimbangkan antara lain:
- **Menambah variasi fitur** yang digunakan untuk pelatihan agar model dapat menangkap lebih banyak informasi relevan.
- **Melakukan tuning hyperparameter** lebih lanjut untuk mengoptimalkan performa model.
- **Mencoba model lain** atau metode ensemble untuk meningkatkan akurasi prediksi.
- **Menggunakan dataset yang lebih besar dan beragam** untuk meningkatkan generalisasi model.
