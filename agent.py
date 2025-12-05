import pandas as pd

def process_sales(df: pd.DataFrame) -> dict:
    df['tanggal'] = pd.to_datetime(df['tanggal'])
    df['bulan'] = df['tanggal'].dt.to_period('M').astype(str)

    summary = {}
    
    summary["total_sales"] = df["harga_total"].sum()
    summary["avg_sales"] = df["harga_total"].mean()
    summary["top_product"] = df.groupby("produk")["harga_total"].sum().idxtop()
    summary["top_region"] = df.groupby("region")["harga_total"].sum().idxtop()
    
    monthly = df.groupby("bulan")["harga_total"].sum()
    summary["monthly"] = monthly
    
    growth = monthly.pct_change() * 100
    summary["growth"] = growth
    
    return summary

def build_prompt(summary: dict) -> str:
    return f"""
Berikut hasil analisis penjualan:

Total Sales: {summary['total_sales']}
Rata-rata Penjualan: {summary['avg_sales']}
Produk Terlaris: {summary['top_product']}
Wilayah Terbaik: {summary['top_region']}

Penjualan Bulanan:
{summary['monthly']}

Growth Penjualan per Bulan (%):
{summary['growth']}

Tolong berikan:
1. Analisis kondisi penjualan
2. Tren penjualan dan penyebab potensial
3. Rekomendasi strategi penjualan
Tulis dalam Bahasa Indonesia.
"""
