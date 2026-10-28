# Data simulasi

- Versi data: v1
- Tanggal dibuat: 28 Okt 2026
- Seed: 32260302
- Data tidak disimpan di repo. Dibuat ulang (hasil identik) dengan:

```
pip install numpy pandas openpyxl Faker reportlab Pillow   # sesuai impor skrip
python scripts/generate_fleet.py
```

- Hasil di `data/sim/`: `fleet.csv` (40 pesawat), `ground_truth.json`.
- Uji determinisme: dijalankan 2x, SHA-256 semua berkas identik. Daftar hash ada di repo DataCenter, `simulasi/fingerprints/project-32.sha256`.
