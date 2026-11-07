#!/usr/bin/env bash
# Install Manim Community and its system-level build dependencies in the
# Manus sandbox (Ubuntu 22.04 base). Idempotent: safe to run multiple times.
#
# Usage:
#   bash /home/ubuntu/skills/manim/scripts/setup.sh
#
# On success, `manim --version` prints the installed ManimCE version.
set -euo pipefail

echo "[manim/setup] Checking existing install..."
if python3 -c "import manim" 2>/dev/null; then
    VERSION=$(python3 -c "import manim; print(manim.__version__)")
    echo "[manim/setup] Already installed (manim==${VERSION}). Skipping."
    manim --version || true
    exit 0
fi

echo "[manim/setup] Installing system build dependencies..."
# Pango / Cairo headers are required to build the manimpango and pycairo
# wheels from source. Python.h is required for the same reason. ffmpeg is
# required at runtime to assemble per-frame PNGs into MP4.
sudo apt-get update -qq
sudo apt-get install -y --no-install-recommends \
    libpango1.0-dev \
    libcairo2-dev \
    pkg-config \
    build-essential \
    python3.11-dev \
    python3-dev \
    ffmpeg

echo "[manim/setup] Installing Manim Community and frame-extraction deps via pip..."
# opencv-python-headless powers scripts/extract_frames.py; numpy comes with manim.
sudo pip3 install --quiet manim opencv-python-headless

echo "[manim/setup] Verifying installation..."
python3 -c "import manim; print('OK:', manim.__version__)"
manim --version

echo "[manim/setup] Done. LaTeX (texlive-latex-extra / texlive-fonts-extra /"
echo "[manim/setup] texlive-science) is NOT installed by default. Install on"
echo "[manim/setup] demand if a scene uses MathTex or Tex:"
echo "[manim/setup]   sudo apt-get install -y --no-install-recommends \\"
echo "[manim/setup]     texlive-latex-extra texlive-fonts-extra texlive-science"
