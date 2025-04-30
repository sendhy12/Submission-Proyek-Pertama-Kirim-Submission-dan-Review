# Laporan Proyek Machine Learning - Sendhy Maula Ammarulloh

## Domain Proyek

Sektor pangan merupakan sektor yang sangat krusial dalam menjaga kestabilan ekonomi dan sosial, terutama di daerah yang sangat bergantung pada bahan pokok seperti beras. Di Kabupaten Sumedang, Dinas Koperasi, UKM, Perdagangan, dan Perindustrian secara rutin mengumpulkan data harga kebutuhan pokok di pasar-pasar tradisional.

Namun, fluktuasi harga Beras Medium yang sering terjadi menyebabkan ketidakpastian bagi konsumen dan pelaku usaha. Oleh karena itu, penting untuk membangun sistem prediksi harga berbasis Machine Learning yang dapat membantu pemerintah daerah dan pelaku pasar dalam merencanakan kebijakan dan strategi distribusi.

Prediksi harga ini didasarkan pada data historis yang mencakup tanggal, lokasi pasar, dan harga komoditas. Teknologi Machine Learning, terutama regresi, digunakan untuk membangun model prediktif yang andal.

**Referensi:**
- BPS Sumedang. “Harga Rata-Rata Beberapa Komoditas.” [Online]. Available: https://sumedangkab.bps.go.id
- O. Ismail et al., “Time Series Forecasting of Rice Prices Using Machine Learning Techniques,” *International Journal of Advanced Computer Science*, 2020.

---

## Business Understanding

### Problem Statements

- Bagaimana memprediksi harga *Beras Medium* berdasarkan informasi pasar dan waktu (bulan, tahun)?
- Bagaimana membangun model Machine Learning yang akurat untuk membantu prediksi harga komoditas tersebut?

### Goals

- Membuat model prediktif berbasis regresi untuk memprediksi harga *Beras Medium*.
- Mengidentifikasi fitur-fitur yang relevan dan melakukan visualisasi serta pembersihan data.

### Solution Statements

- Membangun beberapa model regresi: Linear Regression, Decision Tree, dan Random Forest untuk membandingkan performa.
- Melakukan evaluasi model dengan metrik MAE, MSE, RMSE, dan R².

---

## Data Understanding

Dataset digunakan dari [GitHub Dataset Produk Pasar Sumedang](https://raw.githubusercontent.com/sendhy12/datasetd/refs/heads/main/data_produk_pasar.csv). Dataset berisi informasi harga kebutuhan pokok dari pasar-pasar tradisional.

### Variabel pada dataset:

| Nama Variabel     | Deskripsi                                           |
|-------------------|-----------------------------------------------------|
| `id`              | ID data                                             |
| `tanggal`         | Tanggal pencatatan harga                            |
| `nama_item`       | Kode nama item                                      |
| `item_barang`     | Nama barang (contoh: Beras Medium)                  |
| `harga`           | Harga komoditas dalam rupiah                        |
| `nama_pasar`      | Nama pasar tempat pencatatan                        |
| `keterangan`      | Keterangan ketersediaan (contoh: cukup)             |
| `jumlah`, `kebutuhan` | Informasi jumlah dan kebutuhan (tidak dipakai) |
| `bulan`, `tahun`  | Fitur tambahan hasil ekstraksi dari tanggal        |
| `pasar_encoded`   | Hasil encoding nama pasar                           |

Visualisasi distribusi data juga telah dilakukan, seperti sebaran harga, distribusi bulan, tahun, dan frekuensi per pasar.

---

## Data Preparation

Tahapan persiapan data meliputi:

1. **Filtering**: Hanya mengambil data dengan `item_barang` = "Beras Medium".
2. **Konversi tanggal**: Mengubah kolom `tanggal` ke format datetime lalu mengekstrak `bulan` dan `tahun`.
3. **Drop kolom tidak penting**: Kolom `satuan` dihapus karena mengandung missing values dan tidak relevan.
4. **Handling Outlier**: Outlier pada kolom `harga` dihapus dengan metode IQR (Interquartile Range).
5. **Encoding**: Kolom `nama_pasar` diubah ke angka dengan `LabelEncoder`.

---

## Modeling

Tiga model regresi digunakan:

1. **Linear Regression**  
   - Model baseline sederhana.
   - Tidak menangani relasi non-linear dengan baik.

2. **Decision Tree Regressor**  
   - Menangani hubungan non-linear.
   - Mudah overfitting jika tidak dikontrol.

3. **Random Forest Regressor**  
   - Ensembling Decision Tree untuk performa lebih stabil dan akurat.
   - Cocok untuk dataset dengan noise dan non-linearitas.

**Fitur yang digunakan untuk prediksi**:
- `bulan`
- `tahun`
- `pasar_encoded`

Model dilatih dengan pembagian data 80% training dan 20% testing.

---

## Evaluation

### Metrik Evaluasi:

- **MAE (Mean Absolute Error)**: Rata-rata selisih absolut antara nilai aktual dan prediksi.
- **MSE (Mean Squared Error)**: Rata-rata kuadrat dari selisih.
- **R² Score (Coefficient of Determination)**: Seberapa baik model menjelaskan variansi data.

### Hasil Evaluasi:

| Model                  | MAE   | MSE   | R² Score |
|------------------------|-------|-------|----------|
| Linear Regression      | 456.1 | 371820.3 | 0.48     |
| Decision Tree Regressor | 235.4 | 167243.8 | 0.76     |
| Random Forest Regressor| 196.2 | 122321.5 | **0.83** |

**Kesimpulan**:
Random Forest memberikan performa terbaik dengan R² tertinggi dan error terkecil. Oleh karena itu, dipilih sebagai model akhir untuk prediksi harga *Beras Medium*.
