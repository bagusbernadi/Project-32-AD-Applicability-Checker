"""Project 32: daftar armada simulasi (40 pesawat keluarga A320) untuk pencocokan applicability AD. Seed tetap.

Seluruh identitas karangan: tail ID "SIM-xxx", MSN acak, kode modifikasi dan Service Bulletin "SIM" (bukan kode Airbus asli).
Varian dan mesin memakai penamaan umum keluarga A320 supaya aturan applicability (tipe, varian, rentang MSN, status mod/SB)
bisa diuji. Hanya untuk portofolio, tidak untuk keputusan kepatuhan nyata.
Hasil (data/sim/): fleet.csv, ground_truth.json. Jalankan: python scripts/generate_fleet.py   (versi data: v1)
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "sim"
SEED = 32260302
DATA_VERSION = "v1"
AS_OF = pd.Timestamp("2026-10-01")
FLEET = [  # (keluarga, varian, mesin, jumlah)
    ("A319", "A319-111", "CFM56-5B5/P", 5), ("A319", "A319-112", "CFM56-5B6/P", 3), ("A319", "A319-131", "V2522-A5", 2),
    ("A320", "A320-211", "CFM56-5A1", 4), ("A320", "A320-214", "CFM56-5B4/P", 10), ("A320", "A320-232", "V2527-A5", 6),
    ("A321", "A321-211", "CFM56-5B3/P", 6), ("A321", "A321-231", "V2533-A5", 4),
]
SIM_MODS = [f"MOD-SIM-{n}" for n in (1001, 1002, 1003, 1004, 1005, 1006)]       # modifikasi karangan
SIM_SBS = [f"SB-SIM-{c}" for c in ("57-0011", "27-0024", "32-0007", "71-0102", "53-0033")]
rng = np.random.default_rng(SEED)

rows = []
for fam, var, eng, n in FLEET:
    for _ in range(n):
        age_y = float(rng.uniform(2, 22))
        deliv = AS_OF - pd.Timedelta(days=int(age_y * 365.25))
        fh = int(age_y * rng.uniform(2800, 3600)); fc = int(fh / rng.uniform(1.4, 2.2))
        mods = [m for i, m in enumerate(SIM_MODS) if rng.random() < min(0.9, 0.15 + 0.04 * age_y) * (0.5 if i >= 4 else 1)]
        sbs = [s for s in SIM_SBS if rng.random() < min(0.85, 0.10 + 0.04 * age_y)]
        rows.append([fam, var, eng, deliv.date(), fh, fc, ";".join(mods), ";".join(sbs)])
df = pd.DataFrame(rows, columns=["type_family", "variant", "engine_type", "delivery_date", "flight_hours", "flight_cycles", "installed_mods", "sb_embodied"])
df = df.sort_values(["delivery_date", "variant"]).reset_index(drop=True)
df.insert(0, "msn", rng.choice(np.arange(1000, 9000), len(df), replace=False).tolist())
df["msn"] = sorted(df["msn"])                              # MSN naik mengikuti tanggal pengiriman
df.insert(0, "aircraft_id", [f"SIM-{i + 1:03d}" for i in range(len(df))])
df["as_of_date"] = str(AS_OF.date())
OUT.mkdir(parents=True, exist_ok=True)
df.to_csv(OUT / "fleet.csv", index=False)
(OUT / "ground_truth.json").write_text(json.dumps({
    "seed": SEED, "version": DATA_VERSION, "as_of": str(AS_OF.date()), "n_aircraft": len(df),
    "by_family": df["type_family"].value_counts().sort_index().to_dict(), "by_variant": df["variant"].value_counts().sort_index().to_dict(),
    "sim_mod_codes": SIM_MODS, "sim_sb_codes": SIM_SBS,
    "note": "identitas, MSN, modifikasi, dan SB karangan; bukan data operator atau Airbus"}, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"fleet.csv {len(df)} pesawat", df["type_family"].value_counts().sort_index().to_dict())
