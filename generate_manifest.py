#!/usr/bin/env python3
"""
generate_manifest.py
---------------------
Membuat daftar "sidik jari" (sha256) untuk setiap file di folder ini,
lalu menyimpannya ke manifest.sha256.

CARA PAKAI (di komputer Anda, setelah semua file final ada di folder repo):
    python generate_manifest.py

Jalankan ini SEKALI setelah semua file (report, gambar, README) sudah final,
lalu commit manifest.sha256 ke GitHub bersama file lainnya.
Siapa pun yang mendownload repo ini bisa menjalankan verify_manifest.py
untuk membuktikan tidak ada file yang berubah/dipalsukan sejak dipublikasikan.
"""
import hashlib
from pathlib import Path

ROOT = Path(__file__).parent
SKIP_NAMES = {"manifest.sha256", "generate_manifest.py", "verify_manifest.py", "read_report.py", ".git"}

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    entries = []
    for path in sorted(ROOT.rglob("*")):
        if path.is_dir():
            continue
        if path.name in SKIP_NAMES:
            continue
        if ".git" in path.parts:
            continue
        rel = path.relative_to(ROOT)
        digest = sha256_of(path)
        entries.append(f"{digest}  {rel.as_posix()}")
        print(f"  ok  {rel.as_posix()}")

    manifest_path = ROOT / "manifest.sha256"
    manifest_path.write_text("\n".join(entries) + "\n", encoding="utf-8")
    print(f"\nSelesai. {len(entries)} file dicatat ke manifest.sha256")

if __name__ == "__main__":
    main()
