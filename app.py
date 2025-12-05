import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from agent import process_sales, build_prompt
from groq_client import ask_groq

st.title("📊 AI Agent - Sales Analysis")

uploaded = st.file_uploader("Upload Data Sales CSV", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    st.subheader("Data Sales")
    st.dataframe(df)

    if st.button("Analisis Data"):
        summary = process_sales(df)
        
        st.subheader("Hasil Analisis Sales")
        st.write(f"Total Sales: Rp {summary['total_sales']:,}")
        st.write(f"Rata-rata Transaksi: Rp {summary['avg_sales']:,}")
        st.write(f"Produk Terlaris: {summary['top_product']}")
        st.write(f"Wilayah Terbaik: {summary['top_region']}")
        
        # Grafik
        st.subheader("Grafik Penjualan Bulanan")
        fig, ax = plt.subplots()
        summary["monthly"].plot(kind="bar", ax=ax)
        ax.set_title("Penjualan per Bulan")
        st.pyplot(fig)

        # Growth
        st.subheader("Growth (%)")
        st.dataframe(summary["growth"])
        
        # Groq
        if st.button("Analisis AI (Groq)"):
            prompt = build_prompt(summary)
            ai = ask_groq(prompt)
            st.subheader("Hasil Analisis dari Groq")
            st.write(ai)
