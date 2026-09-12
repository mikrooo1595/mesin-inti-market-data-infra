#!/usr/bin/env python3
"""
verify_manifest.py — check that no published file has been altered.

Anyone can run this. It re-computes the SHA-256 fingerprint of every file
listed in manifest.sha256 and compares it to the recorded value.

    python verify_manifest.py

Expected output: every line reads OK, and the last line confirms that all
files match. A file that differs, or is missing, is reported by name and
the script exits with a failure code.
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
