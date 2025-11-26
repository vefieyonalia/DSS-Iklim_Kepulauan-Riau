import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ================================
# 🎨 CUSTOM THEME WARNA COKLAT MUDA
# ================================
st.markdown("""
    <style>
    /* Background utama */
    .stApp {
        background-color: #F5E6D3; /* Beige / coklat muda lembut */
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #E8D3B8 !important;
        border-right: 2px solid #D6C1A1;
    }

    /* Container isi */
    .block-container {
        background-color: #FAF3E7;
        padding: 2rem 2rem;
        border-radius: 15px;
        border: 1px solid #E0CBB0;
    }

    /* Judul */
    h1, h2, h3 {
        color: #5C3B1E;
        font-weight: 700;
    }

    /* Text umum */
    p, label, span {
        color: #4E3A28 !important;
    }

    /* Tombol */
    .stButton>button {
        background-color: #C9A77C;
        color: white;
        border-radius: 10px;
        border: 1px solid #A4835B;
        padding: 0.6rem 1rem;
        font-size: 16px;
    }

    .stButton>button:hover {
        background-color: #B8936B;
        border-color: #8A6A4C;
    }

    /* Input box */
    .stTextInput>div>div input,
    .stSelectbox div[data-baseweb="select"] {
        background-color: #FAF3E7 !important;
        border-radius: 8px !important;
        border: 1px solid #D6C1A1 !important;
        color: #4E3A28 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ================================
# 📂 Fungsi Load Data
# ================================
@st.cache_data
def load_data():
    df = pd.read_excel("Data.xlsx", sheet_name="Data Harian - Table")
    return df

# ================================
# 🧊 Sidebar
# ================================
st.sidebar.title("📁 Menu Navigasi")
menu = st.sidebar.selectbox(
    "Pilih Halaman:",
    ["Dashboard", "Visualisasi", "Statistik"]
)

# ================================
# 📊 MAIN PAGE
# ================================
st.title("📊 Dashboard Iklim — Kepulauan Riau (Tema Coklat Muda Estetik)")

df = load_data()

if menu == "Dashboard":
    st.subheader("Ringkasan Data")
    st.write(df.head())

    st.write("Jumlah Data:", len(df))

elif menu == "Visualisasi":
    st.subheader("Visualisasi Curah Hujan")

    kolom = st.selectbox("Pilih Kolom Curah Hujan:", df.columns)

    fig, ax = plt.subplots()
    ax.plot(df[kolom])
    ax.set_title(f"Grafik {kolom}")
    ax.set_xlabel("Index")
    ax.set_ylabel("Nilai")
    st.pyplot(fig)

elif menu == "Statistik":
    st.subheader("Statistik Dasar")
    st.write(df.describe())

