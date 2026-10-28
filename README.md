[← Back to portfolio](https://bagusbernadi.github.io/)

# Project 32: AD Applicability Checker

**Status: Design (rancangan).**

**Tujuan:** Membangun alat yang mengubah aturan applicability di dokumen Airworthiness Directive (PDF) menjadi tabel terstruktur dan mencocokkannya dengan daftar armada, untuk menemukan pesawat yang terkena setiap AD dan mengukur akurasi ekstraksinya.

Halaman rancangan: https://bagusbernadi.github.io/Project-32-AD-Applicability-Checker/

| | |
|---|---|
| Kategori | Penerbangan / compliance |
| Tingkat | Sulit |
| Data | PDF AD publik EASA (A320 family) + daftar armada simulasi |
| Tools | Python (pandas, PyMuPDF, Pydantic), LLM structured extraction (Claude atau Gemini, sekali jalan), DuckDB + SQL, Streamlit + Plotly |

## 1. Problem
Pesawat mana dalam armada yang terkena AD tertentu, berapa jumlahnya per AD dan per model, dan seberapa akurat ekstraksi aturan dari PDF dibanding label manual?

## 2. Data
- Sumber data: [here](https://ad.easa.europa.eu/) (Versi: ±15 AD A320 family, nomor AD dan revisi diisi saat Tahap B; Tanggal akses: diisi saat PDF diunduh)
- Armada: data simulasi ±40 pesawat (A319, A320, A321), dibuat oleh `scripts/generate_fleet.py` (Versi: v1; Tanggal dibuat: 28 Okt 2026; Seed: 32260302).
- Ukuran dokumen adalah perkiraan, belum diverifikasi.

## 3. Analysis
Belum dikerjakan. Rencana langkah ada di bagian Work Plan pada halaman rancangan.

## 4. Recommendation
Belum dikerjakan.

## 5. Impact
Belum dikerjakan. Angka dampak nanti diberi label `estimated` / `simulated`.

## Batasan yang sudah diketahui
- Hanya portofolio, tidak untuk keputusan kepatuhan nyata.
- AD bisa direvisi; setiap aturan menyimpan nomor revisi.
- Applicability yang merujuk ke Service Bulletin lain diberi status "Perlu dicek manual".
- Dengan ±15 AD, satu kesalahan bisa mengubah precision/recall beberapa poin.

## Struktur repository
```
index.html          # halaman rancangan (GitHub Pages)
README.md
extract/            # (rencana) teks PDF, prompt, schema, ekstraksi
data/               # (rencana) label manual, tabel aturan
scripts/            # (rencana) generator armada
sql/                # (rencana) query applicability
dashboard/          # (rencana) aplikasi Streamlit
```
