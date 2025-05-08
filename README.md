# Laporan Proyek Machine Learning - Sendhy Maula Ammarulloh

## **Domain Proyek**

Beras merupakan kebutuhan pokok yang tidak tergantikan bagi mayoritas masyarakat Indonesia. Fluktuasi harga beras sangat memengaruhi stabilitas ekonomi rumah tangga, terutama di kalangan masyarakat menengah ke bawah. Fenomena kenaikan harga beras yang terjadi di Pasar Rakyat Sumedang, sebagaimana dilaporkan oleh Pemerintah Kabupaten Sumedang, menunjukkan adanya lonjakan harga yang cukup signifikan dalam waktu singkat. Harga beras kelas 1 misalnya, naik dari Rp 16.000 menjadi Rp 17.000 per kilogram hanya dalam kurun waktu satu minggu [1]. Faktor penyebab utamanya adalah kelangkaan gabah yang berdampak langsung pada rantai pasokan beras di pasar.

Secara nasional, tren harga beras memang menunjukkan peningkatan sejak Agustus 2022 hingga awal tahun 2024, berdasarkan laporan Sistem Pemantauan Pasar dan Kebutuhan Pokok (SP2KP) Kementerian Perdagangan. Hal ini terjadi meskipun produksi beras secara global mengalami peningkatan, bahkan mencetak rekor tertinggi 520,8 juta ton pada periode 2021–2022 menurut Food and Agriculture Organization (FAO). Fakta ini menunjukkan bahwa kenaikan harga bukan semata karena pasokan global, melainkan juga dipengaruhi oleh faktor domestik seperti distribusi, cuaca, dan kondisi pertanian lokal [2].

Perubahan harga beras yang terjadi secara dinamis ini berpotensi memberikan dampak signifikan terhadap inflasi dan kesejahteraan masyarakat. Oleh karena itu, diperlukan pendekatan analisis data yang mampu memprediksi harga beras secara akurat dan tepat waktu. Salah satu metode yang sudah terbukti dapat digunakan untuk tujuan ini adalah **Regresi Linear**, sebagaimana diterapkan dalam penelitian sebelumnya oleh Veri Arinal & Muhammad Azhari (2023), yang berhasil memprediksi harga beras dengan tingkat kesalahan (RMSE) sebesar 109.062 menggunakan data dari tahun 2021–2023.

Dengan adanya sistem prediksi harga beras berbasis regresi, baik pemerintah daerah maupun pelaku pasar dapat merencanakan kebijakan atau strategi penanggulangan lebih dini. Solusi ini juga berpotensi meningkatkan efisiensi distribusi dan mencegah kelangkaan akibat panic buying.

---

### **Referensi**
- E. D. Kusnaedi, "Harga Beras di Pasar Rakyat Sumedang Terus Melejit," *sumedangkab.go.id*, Feb. 15, 2024. [Online]. Available: https://sumedangkab.go.id/berita/detail/harga-beras-di-pasar-rakyat-sumedang-terus-melejit
- V. Arinal and M. Azhari, "Penerapan Regresi Linear Untuk Prediksi Harga Beras Di Indonesia," *Jurnal Sains dan Teknologi*, vol. 5, no. 1, pp. 341–346, 2023.

---

## **Business Understanding**

Bagian ini menjelaskan proses klarifikasi masalah dalam proyek prediksi harga beras, yang berfokus pada analisis data historis harga beras di Kabupaten Sumedang dan pengembangan model prediksi untuk mendukung pengambilan keputusan.

---

### **Problem Statements**

1. Harga beras di pasar rakyat Sumedang mengalami fluktuasi yang cukup signifikan dan seringkali tidak terduga, sehingga menyulitkan masyarakat dan pelaku pasar dalam merencanakan pembelian atau penjualan.

2. Belum tersedia sistem berbasis data yang dapat memprediksi harga beras secara akurat dalam jangka pendek, khususnya untuk wilayah Sumedang, sehingga pengambilan keputusan masih bersifat reaktif.

---

### **Goals**

1. Mengidentifikasi dan menganalisis tren harga beras di Kabupaten Sumedang dari data historis untuk memahami pola fluktuasinya.

2. Membangun model prediksi harga beras berbasis regresi untuk memperkirakan harga dalam jangka pendek dengan akurasi yang dapat diukur, guna mendukung pengambilan keputusan yang lebih proaktif.

---

### **Solution Statements**

1. Mengimplementasikan **Regresi Linear** sebagai baseline model untuk memprediksi harga beras menggunakan data historis lokal. Evaluasi akurasi dilakukan menggunakan beberapa metrik evaluasi regresi, yaitu:
   - **Root Mean Squared Error (RMSE)** untuk mengukur rata-rata kesalahan prediksi dalam satuan yang sama dengan data asli,
   - **Mean Absolute Error (MAE)** untuk mengetahui rata-rata besar kesalahan absolut dari prediksi,
   - **Mean Squared Error (MSE)** untuk mengukur rata-rata kuadrat dari kesalahan prediksi, dan
   - **R-squared (R²)** untuk menilai seberapa baik model menjelaskan variasi harga beras dari data historis.

2. Membandingkan hasil Regresi Linear dengan model lain seperti **Decision Tree Regressor** dan **Random Forest Regressor** untuk mengetahui model dengan performa terbaik dalam konteks data harga beras di Kabupaten Sumedang.

---

## **Data Understanding**

| id     | satuan | pasar | tanggal    | nama_item | keterangan | harga | jumlah | kebutuhan | item_barang           | satuan_item | nama_pasar           |
|--------|--------|--------|------------|------------|-------------|--------|---------|-------------|------------------------|--------------|------------------------|
| 26766 |        | 7      | 2022-01-01 | 1          | cukup       | 12000 | 0       | 0           | Beras Premium         | kg           | Pasar Parakanmuncang |
| 26767 |        | 7      | 2022-01-01 | 2          | cukup       | 11500 | 0       | 0           | Beras Medium          | kg           | Pasar Parakanmuncang |
| 26768 |        | 7      | 2022-01-01 | 3          | cukup       | 12000 | 0       | 0           | Beras Termahal        | kg           | Pasar Parakanmuncang |
| 26769 |        | 7      | 2022-01-01 | 4          | cukup       | 14000 | 0       | 0           | Gula Pasir            | kg           | Pasar Parakanmuncang |
| 26770 |        | 7      | 2022-01-01 | 8          | cukup       | 3000  | 0       | 0           | Minyak Goreng Bimoli  | liter        | Pasar Parakanmuncang |


Dataset yang digunakan dalam proyek ini bersumber langsung dari **Dinas Koperasi Usaha Kecil Menengah Perdagangan dan Perindustrian Kabupaten Sumedang** dan dapat diakses melalui [GitHub Repository](https://raw.githubusercontent.com/sendhy12/datasetd/refs/heads/main/data_produk_pasar.csv). Dataset ini berfokus pada harga produk beras di pasar-pasar rakyat Sumedang dan memiliki 7630 entri serta 12 kolom. Data ini mencakup periode dari tahun 2022 hingga 2024.

### **Struktur Dataset**

Dataset ini terdiri dari 12 kolom sebagai berikut:

1. **id**: ID unik untuk setiap entri (integer).
2. **satuan**: Informasi satuan produk, namun kolom ini berisi nilai **null** (float).
3. **pasar**: ID pasar tempat produk dijual (integer).
4. **tanggal**: Tanggal pencatatan harga produk (string).
5. **nama_item**: ID produk yang dijual (integer).
6. **keterangan**: Deskripsi atau keterangan tentang produk (string).
7. **harga**: Harga produk per satuan (integer) yang menjadi target prediksi.
8. **jumlah**: Jumlah barang yang tersedia atau terjual (integer).
9. **kebutuhan**: Jumlah kebutuhan barang (integer).
10. **item_barang**: Nama produk (string).
11. **satuan_item**: Satuan produk (string).
12. **nama_pasar**: Nama pasar tempat barang dijual (string).

### **Informasi Tambahan**
- **Jumlah Baris**: 7630 baris data.
- **Jumlah Kolom**: 12 kolom data.
- **Tipe Data**: Kombinasi antara integer, string, dan float.
- **Periode Data**: Data ini mencakup rentang waktu dari tahun 2022 hingga 2024.

### **Target Prediksi**
Kolom **harga** adalah target prediksi untuk model ini, yang merujuk pada harga beras Medium yang diperdagangkan di pasar-pasar Sumedang.

### **Variabel Penting**
Dua variabel yang dianggap paling penting untuk memprediksi harga beras Medium adalah:
- **tanggal**: Tanggal pencatatan harga yang memungkinkan adanya tren musiman atau pola berdasarkan waktu.
- **nama_pasar**: Nama pasar yang dapat memberikan wawasan tentang fluktuasi harga berdasarkan lokasi pasar.

### Eksplorasi Data dan Visualisasi

Eksplorasi data dilakukan untuk memahami karakteristik dan pola dalam dataset harga beras medium di berbagai pasar. Beberapa visualisasi berikut memberikan insight penting yang membantu dalam proses analisis dan pemilihan fitur:

* **Distribusi Harga Beras Medium:**
  Visualisasi histogram menunjukkan sebaran harga beras medium. Terlihat bahwa sebagian besar harga berada pada rentang 10.000 sampai 13.000, menunjukkan bahwa harga cenderung terkonsentrasi di kisaran tersebut.

* **Frekuensi Nama Pasar:**
  Bar chart menunjukkan variasi jumlah data yang tersedia untuk masing-masing pasar. Teridentifikasi bahwa pasar seperti *Pasar Parakamuncang* memiliki jumlah observasi tertinggi, sementara beberapa pasar lainnya memiliki data yang relatif sedikit. Hal ini perlu dipertimbangkan untuk analisis lanjutan agar tidak bias terhadap pasar tertentu.

* **Distribusi Waktu (Bulan dan Tahun):**
  Visualisasi distribusi data berdasarkan bulan dan tahun menunjukkan bahwa data tidak tersebar merata sepanjang waktu. Beberapa bulan atau tahun memiliki jumlah data yang jauh lebih tinggi, misalnya *bulan Januari dan tahun 2022*, yang bisa memengaruhi hasil analisis tren.

* **Tren Harga Beras per Tahun:**
  Line plot memperlihatkan adanya *tren peningkatan harga* dari tahun ke tahun. Ini mengindikasikan adanya pola musiman atau faktor eksternal yang memengaruhi harga beras dalam jangka panjang.

* **Harga Berdasarkan Tahun (Boxplot):**
  Boxplot harga berdasarkan tahun mengungkapkan fluktuasi dan persebaran harga dalam tiap tahun. Dapat diamati adanya *peningkatan median harga* di tahun-tahun tertentu yang mencerminkan ketidakstabilan harga.

* **Harga Berdasarkan Pasar:**
  Visualisasi boxplot antar pasar menunjukkan variasi harga antar lokasi. Beberapa pasar memiliki harga yang secara konsisten lebih tinggi atau lebih rendah dibandingkan lainnya, mengindikasikan kemungkinan perbedaan biaya distribusi, kualitas beras, atau kekuatan pasar lokal.

* **Korelasi Antar Fitur Numerik:**
  Matriks korelasi menunjukkan hubungan antar variabel numerik seperti harga, bulan, tahun, dan pasar (yang telah diubah menjadi numerik). Terdapat korelasi yang signifikan antara *harga dan tahun*, yang menunjukkan bahwa faktor waktu memiliki pengaruh terhadap perubahan harga beras.

---

## **Data Preparation**

Pada tahap ini, beberapa langkah penting dalam mempersiapkan data untuk pemodelan dilakukan agar data siap digunakan oleh algoritma pembelajaran mesin. Berikut adalah langkah-langkah yang diambil dalam proses persiapan data:

### **1. Filter Hanya Beras Medium**

* Dataset awal mengandung berbagai jenis komoditas beras. Namun, untuk fokus pada analisis yang lebih spesifik dan konsisten, hanya data dengan jenis **`Beras Medium`** yang digunakan. Ini dilakukan dengan memfilter kolom **`item_barang`**.

  ```python
  df = df[df['item_barang'] == 'Beras Medium']
  ```

### **2. Konversi Kolom Tanggal**
- Kolom **`tanggal`** yang awalnya berformat string diubah menjadi format **`datetime`** menggunakan fungsi `pd.to_datetime()`. Setelah itu, elemen waktu diekstrak menjadi dua kolom baru, yaitu **`tahun`** dan **`bulan`**, untuk mempermudah analisis musiman atau tren tahunan.

  ```python
  df['tanggal'] = pd.to_datetime(df['tanggal'])
  df['tahun'] = df['tanggal'].dt.year
  df['bulan'] = df['tanggal'].dt.month
  ```

### **3. Menghapus Kolom yang Tidak Terpakai**
- Kolom **`satuan`** memiliki banyak nilai yang hilang (missing values) dan tidak berkontribusi terhadap analisis atau prediksi harga beras. Oleh karena itu, kolom ini dihapus dari dataset.

### **4. Menghapus Outlier pada Kolom Harga**
- Untuk memastikan bahwa model tidak terpengaruh oleh nilai ekstrem yang tidak wajar, dilakukan proses deteksi dan penghapusan outlier pada kolom **`harga`** menggunakan metode **Interquartile Range (IQR)**. Data yang berada di luar rentang [Q1 - 1.5 * IQR, Q3 + 1.5 * IQR] dianggap sebagai outlier dan dihapus.

  ```python
  Q1 = df['harga'].quantile(0.25)
  Q3 = df['harga'].quantile(0.75)
  IQR = Q3 - Q1
  df = df[~((df['harga'] < (Q1 - 1.5 * IQR)) | (df['harga'] > (Q3 + 1.5 * IQR)))]
  ```

### **5. Pengkodean Variabel Kategorikal**
- Kolom **`nama_pasar`** yang merupakan variabel kategorikal, dikodekan menggunakan **LabelEncoder**. Hal ini dilakukan untuk mengonversi nama pasar menjadi representasi numerik yang bisa diterima oleh model pembelajaran mesin.

  ```python
  le = LabelEncoder()
  df['pasar_encoded'] = le.fit_transform(df['nama_pasar'])
  ```

### **6. Pemilihan Fitur**
- **Fitur untuk Model:** Dalam proses pemilihan fitur, kolom **`tahun`**, **`bulan`**, dan **`pasar_encoded`** dipilih sebagai fitur input (**X**) untuk memprediksi harga beras. Kolom **`harga`** dipilih sebagai target output (**y**).

  ```python
  X = df[['tahun', 'bulan', 'pasar_encoded']]
  y = df['harga']
  ```

### **7. Pembagian Data**
- **Split Data:** Data dibagi menjadi data latih (training) dan data uji (testing) dengan perbandingan 80:20 menggunakan fungsi `train_test_split`. Data latih digunakan untuk melatih model, sementara data uji digunakan untuk menguji akurasi model setelah pelatihan.

  ```python
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  ```

  Hasil pembagian data (setelah penghapusan outlier):
  - **Total datasets:** 7627
  - **Data Latih (Training):** ~80% dari total (6101)
  - **Data Uji (Testing):** ~20% dari total (1526)

### **8. Normalisasi Data**
- **Normalisasi untuk Regresi Linear:** Karena model regresi linear sensitif terhadap skala data, fitur input dinormalisasi menggunakan **MinMaxScaler** untuk mengubah nilai fitur menjadi rentang [0, 1]. Proses normalisasi ini dilakukan pada data latih (training) dan data uji (testing).

  ```python
  scaler = MinMaxScaler()
  scaler.fit(X_train)
  X_train_scaled = scaler.transform(X_train)
  X_test_scaled = scaler.transform(X_test)
  ```

---

## Modeling

Dalam proyek ini, digunakan tiga model regresi untuk memprediksi harga beras Medium berdasarkan data historis dari Kabupaten Sumedang, yaitu:

### Linear Regression
Linear Regression digunakan sebagai baseline model karena sifatnya yang sederhana dan interpretatif. Model ini diasumsikan memiliki hubungan linier antara fitur (tahun, bulan, dan pasar_encoded) dengan target harga. Sebelum pelatihan, fitur dilakukan normalisasi menggunakan `MinMaxScaler`.

**Kelebihan:**
- Mudah diinterpretasikan
- Cepat dilatih

**Kekurangan:**
- Tidak menangkap hubungan non-linier dengan baik

---

### Decision Tree Regressor
Model pohon keputusan digunakan untuk menangkap hubungan non-linear antar fitur. Model ini disetel dengan `max_depth=5` untuk menghindari overfitting.

**Kelebihan:**
- Dapat menangkap hubungan non-linear
- Tidak memerlukan normalisasi

**Kekurangan:**
- Rentan terhadap overfitting jika tidak dikendalikan

---

### Random Forest Regressor
Random Forest, sebagai ensembel dari banyak pohon keputusan, digunakan untuk meningkatkan performa dengan mengurangi variansi. Model ini disetel dengan `n_estimators=100` dan `max_depth=7`.

**Kelebihan:**
- Lebih stabil dan akurat dibanding satu pohon keputusan
- Mengurangi risiko overfitting

**Kekurangan:**
- Interpretasi lebih sulit
- Lebih berat secara komputasi

---

Model terbaik dipilih berdasarkan performa pada metrik evaluasi, seperti dijelaskan di bawah.

---

## **Evaluation (Evaluasi Model)**

### **1. Metrik Evaluasi dan Penjelasannya**

Untuk mengukur kinerja model prediksi harga beras, digunakan empat metrik evaluasi regresi yang relevan dengan konteks prediksi nilai numerik (harga), yaitu:

* **Mean Absolute Error (MAE)**
  MAE mengukur rata-rata selisih absolut antara nilai aktual dan nilai yang diprediksi.
  **Rumus:**

      MAE = (1/n) * Σ |yᵢ - ŷᵢ|

  MAE memberikan gambaran langsung mengenai besarnya kesalahan dalam satuan harga (Rupiah). Metrik ini sangat cocok dalam konteks bisnis karena interpretasinya yang intuitif (rata-rata seberapa meleset prediksi dari kenyataan).

* **Mean Squared Error (MSE)**
  MSE menghitung rata-rata dari kuadrat selisih antara nilai aktual dan prediksi.
  **Rumus:**

      MSE = (1/n) * Σ (yᵢ - ŷᵢ)²

  MSE menekankan kesalahan besar, sehingga berguna untuk menghindari model dengan prediksi ekstrem.

* **Root Mean Squared Error (RMSE)**
  RMSE adalah akar kuadrat dari MSE, yang menjadikannya berada dalam satuan yang sama dengan target.
  **Rumus:**

      RMSE = √MSE

  Dalam konteks ini, RMSE menunjukkan secara langsung seberapa jauh, dalam satuan rupiah, prediksi menyimpang dari nilai aktual.

* **R-squared (R² Score)**
  R² mengukur proporsi variabilitas dalam target yang bisa dijelaskan oleh model.
  **Rumus:**

      R² = 1 - (Σ (yᵢ - ŷᵢ)² / Σ (yᵢ - ȳ)²)

  Nilai R² mendekati 1 menandakan bahwa model menjelaskan hampir seluruh variasi dalam data, yang sangat penting untuk prediksi harga yang akurat.

---

### **2. Hasil Evaluasi Model**

Berikut adalah perbandingan hasil ketiga model:

| Model             | MAE        | MSE           | RMSE       | R²         |
| ----------------- | ---------- | ------------- | ---------- | ---------- |
| Linear Regression | 624.22     | 630,262.50    | 793.89     | 0.7024     |
| Decision Tree     | 257.02     | 168,816.39    | 410.87     | 0.9203     |
| Random Forest     | **152.40** | **89,048.07** | **298.41** | **0.9579** |

### **Analisis Hasil**

* **Random Forest Regressor** menunjukkan performa terbaik di seluruh metrik:

  * MAE hanya sekitar **Rp152**, yang artinya rata-rata kesalahan prediksi harga sangat kecil.
  * RMSE di bawah **Rp300**, menunjukkan stabilitas model dalam meminimalisir kesalahan besar.
  * R² sebesar **0.9579**, berarti hampir 96% variabilitas harga beras dapat dijelaskan oleh model ini.

Model ini jauh lebih baik dibandingkan baseline **Linear Regression** yang hanya memiliki R² sebesar 0.70 dan MAE lebih dari Rp600. Bahkan dibandingkan dengan **Decision Tree**, Random Forest unggul di seluruh aspek.

---

### **3. Keterkaitan dengan Business Understanding**

#### **Apakah sudah menjawab Problem Statements?**

* **Problem 1:** Fluktuasi harga beras yang tidak terduga membuat perencanaan sulit.
  ✅ *Model prediktif ini memungkinkan estimasi harga beras jangka pendek yang akurat, sehingga membantu pelaku pasar dan masyarakat merencanakan aktivitas jual beli.*

* **Problem 2:** Tidak tersedianya sistem prediksi berbasis data untuk wilayah Sumedang.
  ✅ *Dengan model Random Forest ini, tersedia sistem prediksi harga berbasis machine learning yang dirancang khusus berdasarkan data lokal Kabupaten Sumedang.*

#### **Apakah sudah mencapai Goals?**

* **Goal 1:** Mengidentifikasi tren harga beras.
  ✅ *Melalui eksplorasi data dan visualisasi tren musiman (tahun, bulan), pola harga berhasil dianalisis.*

* **Goal 2:** Membangun model prediksi harga beras jangka pendek.
  ✅ *Random Forest Regressor terbukti akurat dalam memprediksi harga beras dengan MAE < Rp200 dan R² > 0.95.*

#### **Apakah solusi yang dirancang berdampak?**

* ✅ *Solusi menggunakan regresi linear sebagai baseline dan membandingkannya dengan model yang lebih kompleks telah terbukti berdampak signifikan. Model akhir (Random Forest) memberikan hasil terbaik, melebihi ekspektasi dari baseline, dan siap digunakan dalam pengambilan keputusan strategis.*

---

### **Kesimpulan Evaluasi**

Model Random Forest Regressor memberikan hasil prediksi harga beras yang sangat akurat dan memenuhi seluruh aspek dari problem statement, goals, dan solusi proyek. Metrik evaluasi yang digunakan relevan dengan konteks bisnis (prediksi harga), dan hasil evaluasi menunjukkan bahwa proyek ini berhasil secara teknis maupun fungsional dalam mendukung stabilitas pasar beras di Kabupaten Sumedang.
