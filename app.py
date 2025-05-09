import streamlit as st
import joblib
import numpy as np
import datetime

# Load model, encoder, dan scaler
model = joblib.load('linear_regression_model.joblib')
label_encoder = joblib.load('encoder_pasar.pkl')
scaler = joblib.load('scaler.pkl')

# Tampilkan logo di atas judul (ganti path jika perlu)
st.image('logo.png', width=1000)  # Sesuaikan nama file dan ukuran logo

st.title('Prediksi Harga Beras Medium')

# Dropdown nama pasar
pasar_list = label_encoder.classes_
selected_pasar = st.selectbox('Pilih Pasar', pasar_list)

# Input tanggal menggunakan kalender
tanggal = st.date_input('Pilih Tanggal', value=datetime.date.today())

# Ekstrak tahun, bulan, hari dari tanggal
tahun = tanggal.year
bulan = tanggal.month
hari = tanggal.day

# Encode pasar
pasar_encoded = label_encoder.transform([selected_pasar])[0]

if st.button('Prediksi'):
    X = np.array([[tahun, bulan, hari, pasar_encoded]])
    X_scaled = scaler.transform(X)
    prediction = model.predict(X_scaled)
    st.success(f'Prediksi Harga Beras: Rp {prediction[0]:,.2f}')
