import pandas as pd

print("="*50)
print("🧹 TAHAP 2: PROSES DATA CLEANING")
print("="*50)

# 1. Membaca data asli
df = pd.read_csv("heart.csv")
print(f"Total data awal: {df.shape[0]} baris")

# 2. Menghapus data duplikat
jumlah_duplikat = df.duplicated().sum()
df_clean = df.drop_duplicates()

print(f"Ditemukan dan dihapus: {jumlah_duplikat} baris duplikat")
print(f"Total data bersih    : {df_clean.shape[0]} baris unik")

# 3. Menyimpan data yang sudah bersih ke CSV baru
nama_file_baru = "heart_clean.csv"
df_clean.to_csv(nama_file_baru, index=False)

print(f"\n✅ Data bersih berhasil disimpan sebagai '{nama_file_baru}'")
print("Silakan jalankan file visualisasi selanjutnya.")