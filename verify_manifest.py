#!/usr/bin/env python3
"""
verify_manifest.py
--------------------
Ini skrip yang PALING PENTING untuk kredibilitas Anda.

Siapa pun (calon pembeli, reviewer, klien) bisa download repo ini lalu
jalankan skrip ini untuk MEMBUKTIKAN SENDIRI bahwa tidak ada file yang
diubah/dipalsukan sejak Anda mempublikasikannya -- tanpa perlu percaya
begitu saja pada kata-kata Anda.

CARA PAKAI:
    python verify_manifest.py

Hasil yang diharapkan: semua baris "OK", dan baris terakhir
"SEMUA FILE COCOK -- tidak ada yang berubah."
"""
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).parent
MANIFEST = ROOT / "manifest.sha256"

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    if not MANIFEST.exists():
        print("manifest.sha256 tidak ditemukan. Jalankan generate_manifest.py dulu.")
        sys.exit(1)

    ok, mismatch, missing = 0, 0, 0
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        expected_hash, rel_path = line.split("  ", 1)
        path = ROOT / rel_path
        if not path.exists():
            print(f"  HILANG    {rel_path}")
            missing += 1
            continue
        actual_hash = sha256_of(path)
        if actual_hash == expected_hash:
            print(f"  OK        {rel_path}")
            ok += 1
        else:
            print(f"  BERBEDA!  {rel_path}")
            mismatch += 1

    print()
    if mismatch == 0 and missing == 0:
        print(f"SEMUA FILE COCOK -- tidak ada yang berubah. ({ok} file diverifikasi)")
    else:
        print(f"PERINGATAN: {mismatch} file berbeda, {missing} file hilang, {ok} file cocok.")
        sys.exit(1)

if __name__ == "__main__":
    main()
