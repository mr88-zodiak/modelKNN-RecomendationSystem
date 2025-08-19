import pandas as pd
import joblib

# Load model
model = joblib.load("knn_model.pkl")

# Baca data uji
dataUji = pd.read_excel("data_uji.xlsx")

# Prediksi
prediksi = model.predict(dataUji)

# Tambahin kolom hasil prediksi ke DataFrame
dataUji["layak"] = prediksi

# Tampilkan hasil
print(dataUji)

# Kalau mau simpan ke Excel
dataUji.to_excel("hasil_prediksi.xlsx", index=False)
