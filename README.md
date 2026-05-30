```markdown
# 🎬 AMTFetch - Anime System Info Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)]()

> A beautiful system information tool with **random anime animations** and **exact system specifications** for your terminal!

---

## 📋 Table of Contents

- [Features](#-features)
- [Requirements](#-requirements)
- [Quick Installation](#-quick-installation)
- [Detailed Installation](#-detailed-installation)
- [Usage](#-usage)
- [Anime Characters](#-anime-characters)
- [System Information](#-system-information)
- [Commands Reference](#-commands-reference)
- [Troubleshooting](#-troubleshooting)
- [Uninstallation](#-uninstallation)
- [FAQ](#-faq)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎀 **Random Anime** | Different anime character every run |
| 🎬 **Animated ASCII** | Live animations in terminal |
| 📊 **Exact Specs** | Detailed CPU, GPU, RAM, Disk info |
| 🎨 **Random Colors** | New color scheme each session |
| 💬 **Anime Quotes** | Famous lines from anime |
| 🖥️ **Cross-Platform** | Windows, Linux, macOS |
| ⚡ **Fast** | Written in optimized Python |

---

## 📋 Requirements

| Requirement | Version |
|-------------|---------|
| Python | 3.8 or higher |
| pip | Latest version |
| Terminal | ANSI color support |

### Python Packages

```txt
psutil>=5.9.0
GPUtil>=1.4.0
wmi>=1.5.0  # Windows only (optional)
```

---

## 🚀 Quick Installation

### One-Line Install & Run

**Linux/macOS:**
```bash
pip install psutil GPUtil && curl -o amtfetch.py https://raw.githubusercontent.com/yourrepo/amtfetch/main/amtfetch.py && python3 amtfetch.py
```

**Windows (PowerShell):**
```powershell
pip install psutil GPUtil; Invoke-WebRequest -Uri "https://raw.githubusercontent.com/yourrepo/amtfetch/main/amtfetch.py" -OutFile "amtfetch.py"; python amtfetch.py
```

---

## 📦 Detailed Installation

### 🐧 Linux (Ubuntu/Debian/Fedora/Arch)

```bash
# Install Python packages
pip3 install psutil GPUtil

# Download AMTFetch
curl -o amtfetch.py https://raw.githubusercontent.com/yourrepo/amtfetch/main/amtfetch.py

# Make executable and run
chmod +x amtfetch.py
python3 amtfetch.py
```

### 🪟 Windows

```bash
# Install packages
pip install psutil GPUtil

# Download script
curl -o amtfetch.py https://raw.githubusercontent.com/yourrepo/amtfetch/main/amtfetch.py

# Run
python amtfetch.py
```

### 🍎 macOS

```bash
# Install packages
pip3 install psutil GPUtil

# Download script
curl -o amtfetch.py https://raw.githubusercontent.com/yourrepo/amtfetch/main/amtfetch.py

# Make executable and run
chmod +x amtfetch.py
python3 amtfetch.py
```

---

## 🎮 Usage

### Basic Commands

```bash
# Run with random anime character
python3 amtfetch.py

# List all anime characters
python3 amtfetch.py --list

# Show specific character
python3 amtfetch.py --character "Naruto"

# Show help
python3 amtfetch.py --help
```

### Make Global Command

**Linux/macOS:**
```bash
sudo mv amtfetch.py /usr/local/bin/amtfetch
amtfetch
```

**Windows (PowerShell):**
```powershell
echo "function amtfetch { python $env:USERPROFILE\amtfetch.py }" >> $PROFILE
. $PROFILE
amtfetch
```

---

## 🎭 Anime Characters

| # | Character | Anime |
|---|-----------|-------|
| 1 | Naruto Uzumaki | Naruto |
| 2 | Sailor Moon | Sailor Moon |
| 3 | Goku | Dragon Ball Z |
| 4 | Pikachu | Pokémon |
| 5 | Totoro | My Neighbor Totoro |
| 6 | Lelouch | Code Geass |
| 7 | Levi | Attack on Titan |
| 8 | Zoro | One Piece |
| 9 | Hatsune Miku | Vocaloid |
| 10 | Rem | Re:Zero |
| 11 | L | Death Note |
| 12 | Gojo | Jujutsu Kaisen |
| 13 | Tanjiro | Demon Slayer |
| 14 | Vegeta | Dragon Ball Z |
| 15 | Inuyasha | Inuyasha |

### Animated Characters

| Character | Animation |
|-----------|-----------|
| Naruto | Running |
| Goku | Kamehameha charge |
| Pikachu | Dancing |
| Levi | Cleaning |
| Gojo | Domain Expansion |

---

## 📊 System Information

| Category | Details |
|----------|---------|
| **OS** | Name, version, build |
| **CPU** | Model, cores, threads, clock speed |
| **GPU** | Model, memory, driver |
| **RAM** | Total, used, available, percentage |
| **Disk** | Total, used, free per drive |
| **Network** | Interface IP addresses |
| **Battery** | Level, charging status, time left |
| **Temperatures** | CPU/GPU temps (if available) |

---

## ⚡ Commands Reference

| Action | Command |
|--------|---------|
| Install packages | `pip install psutil GPUtil` |
| Download script | `curl -o amtfetch.py [URL]` |
| Run AMTFetch | `python3 amtfetch.py` |
| List characters | `python3 amtfetch.py --list` |
| Specific character | `python3 amtfetch.py -c "Gojo"` |
| Make global (Linux) | `sudo mv amtfetch.py /usr/local/bin/amtfetch` |
| Run globally | `amtfetch` |
| Uninstall packages | `pip uninstall psutil GPUtil` |

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| `pip: command not found` | Use `python3 -m pip install psutil GPUtil` |
| `Permission denied` | Install with `--user`: `pip3 install --user psutil GPUtil` |
| `GPUtil not working` | Install NVIDIA tools: `sudo apt install nvidia-smi` |
| Script won't run | Make executable: `chmod +x amtfetch.py` |
| No colors showing | Use terminal with ANSI color support |

### Verify Installation

```bash
# Check Python version
python3 --version

# Check installed packages
pip list | grep -E "psutil|GPUtil"

# Test imports
python3 -c "import psutil, GPUtil; print('✅ OK')"
```

---

## 🗑️ Uninstallation

### Complete Removal

**Linux/macOS:**
```bash
# Remove packages
pip3 uninstall psutil GPUtil -y

# Remove script
sudo rm /usr/local/bin/amtfetch
rm amtfetch.py
```

**Windows:**
```powershell
# Remove packages
pip uninstall psutil GPUtil wmi -y

# Remove script
del %USERPROFILE%\amtfetch.py
```

---

## ❓ FAQ

**Q: Does AMTFetch work on WSL?**
A: Yes, works perfectly on WSL1 and WSL2.

**Q: Can I add my own anime characters?**
A: Yes! Edit the script and add to `AnimeCharacters.CHARACTERS` list.

**Q: Why doesn't my GPU show?**
A: Install GPU drivers or use `--gpu-fallback` option.

**Q: How to disable animations?**
A: Use `--no-animation` flag when running.

**Q: Is there a web version?**
A: Currently terminal-only, web version planned.

---

## 📝 License

MIT License - Free to use, modify, and distribute.

---

## ⭐ Support

If you like AMTFetch, please star the repository!

---

**Made with ❤️ and 🎀 for terminal lovers and anime fans!**

*"Believe it!" - Naruto Uzumaki*

```
