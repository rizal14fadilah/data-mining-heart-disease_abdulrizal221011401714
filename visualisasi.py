import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# 1. Load Data Mentah
df = pd.read_csv("heart.csv")

# 2. Proses 'Sebelum' (hapus duplikat & data tidak valid)
df_sebelum = df.drop_duplicates()
df_sebelum = df_sebelum[(df_sebelum['ca'] != 4) & (df_sebelum['thal'] != 0)]

# 3. Proses 'Sesudah' (Capping Outlier Kolesterol di Persentil 99)
df_sesudah = df_sebelum.copy()
# Mengubah tipe data ke float agar tidak error saat diisi nilai desimal (407.1)
df_sesudah['chol'] = df_sesudah['chol'].astype(float)

q99 = df_sebelum['chol'].quantile(0.99)
df_sesudah.loc[df_sesudah['chol'] > q99, 'chol'] = q99

# 4. Proses Normalisasi (Min-Max Scaling)
scaler = MinMaxScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df_sesudah), columns=df_sesudah.columns)

# ==========================================
# 5. PEMBUATAN VISUALISASI
# ==========================================
sns.set_style("white") 
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# GRAFIK 1 (KIRI ATAS): Boxplot Sebelum
sns.boxplot(x=df_sebelum['chol'], ax=axes[0, 0], color='salmon')
axes[0, 0].set_title('1. SEBELUM CLEANING (Boxplot):\nBanyak pencilan (outlier) kolesterol di atas 400', pad=15)
axes[0, 0].set_xlabel('Kadar Kolesterol (mg/dl)')

# GRAFIK 2 (KANAN ATAS): Boxplot Sesudah
sns.boxplot(x=df_sesudah['chol'], ax=axes[0, 1], color='lightgreen')
axes[0, 1].set_title('1. SESUDAH CLEANING (Boxplot):\nOutlier dibatasi (capping) pada batas maksimal', pad=15)
axes[0, 1].set_xlabel('Kadar Kolesterol (mg/dl)')

# GRAFIK 3 (KIRI BAWAH): KDE Plot Sebelum Normalisasi
sns.kdeplot(x=df_sesudah['chol'], ax=axes[1, 0], color='blue', fill=True, label='Kolesterol')
sns.kdeplot(x=df_sesudah['age'], ax=axes[1, 0], color='orange', fill=True, label='Umur (Age)')
axes[1, 0].set_title('2. SEBELUM NORMALISASI (KDE Plot):\nSkala antar variabel sangat timpang (Umur vs Kolesterol)', pad=15)
axes[1, 0].set_xlabel('chol')
axes[1, 0].legend()

# GRAFIK 4 (KANAN BAWAH): KDE Plot Sesudah Normalisasi
sns.kdeplot(x=df_scaled['chol'], ax=axes[1, 1], color='blue', fill=True, label='Kolesterol (Scaled)')
sns.kdeplot(x=df_scaled['age'], ax=axes[1, 1], color='orange', fill=True, label='Umur (Scaled)')
axes[1, 1].set_title('2. SESUDAH NORMALISASI (KDE Plot):\nSemua variabel kini memiliki skala setara (0.0 - 1.0)', pad=15)
axes[1, 1].set_xlabel('chol')
axes[1, 1].legend()

# Menghapus garis bingkai atas dan kanan
sns.despine()

plt.tight_layout()
plt.show()