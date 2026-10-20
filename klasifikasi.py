import pandas as pd

# ==================================================
# 1. LOAD DATA
# ==================================================
# Membaca dataset
df = pd.read_csv("heart.csv")

# Memisahkan nama-nama kolom berdasarkan jenis datanya
kolom_kategorikal = ["sex", "cp", "fbs", "restecg", "exang", "slope", "ca", "thal", "target"]
kolom_numerikal = ["age", "trestbps", "chol", "thalach", "oldpeak"]


# ==================================================
# OUTPUT 1: RINGKASAN UTAMA
# ==================================================
print("\n" + "="*50)
print("📊 1. RINGKASAN DATASET: heart.csv")
print("="*50)
print(f"Total Baris       : {df.shape[0]}")
print(f"Total Kolom       : {df.shape[1]}")
print(f"Data Duplikat     : {df.duplicated().sum()} baris")
print(f"Total Data Null   : {df.isnull().sum().sum()} nilai")
print(f"Kolom Kategorikal : {len(kolom_kategorikal)} kolom")
print(f"Kolom Numerikal   : {len(kolom_numerikal)} kolom")


# ==================================================
# OUTPUT 2: STATUS SETIAP KOLOM (TIPE DATA & NULL)
# ==================================================
print("\n" + "="*50)
print(" 2. DETAIL INFORMASI KOLOM")
print("="*50)

# Membuat dataframe baru khusus untuk ringkasan agar tampil rapi seperti tabel
df_info = pd.DataFrame({
    'Tipe Data': df.dtypes,
    'Total Null': df.isnull().sum(),
    'Total Unik': df.nunique() # Melihat jumlah variasi isi data
})
print(df_info.to_string())


# ==================================================
# OUTPUT 3: DATA KATEGORIKAL & NUMERIKAL
# ==================================================
print("\n" + "="*50)
print(" 3. PEMBAGIAN KATEGORIKAL VS NUMERIKAL")
print("="*50)

# Menampilkan data kategorikal
print("📌 KOLOM KATEGORIKAL:")
print(", ".join(kolom_kategorikal))
print("\nContoh Data Kategorikal (3 baris pertama):")
print(df[kolom_kategorikal].head(3))

print("\n" + "-"*50)

# Menampilkan data numerikal
print("📌 KOLOM NUMERIKAL:")
print(", ".join(kolom_numerikal))
print("\nContoh Data Numerikal (3 baris pertama):")
print(df[kolom_numerikal].head(3))


# ==================================================
# OUTPUT 4: STATISTIK DESKRIPTIF
# ==================================================
print("\n" + "="*50)
print("📈 4. STATISTIK DATA NUMERIKAL")
print("="*50)

# Hanya menampilkan kolom numerikal dan membulatkan 2 angka di belakang koma
print(df[kolom_numerikal].describe().round(2))


# ==================================================
# OUTPUT 5: CONTOH SELURUH DATA
# ==================================================
print("\n" + "="*50)
print(" 5. TAMPILAN KESELURUHAN DATA (3 BARIS AWAL)")
print("="*50)
print(df.head(3))
print("\n")