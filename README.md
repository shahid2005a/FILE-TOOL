📁 FILE-TOOL -  Premium File Manager

<div align="center">
  <img src="https://github.com/shahid2005a/FILE-TOOL/blob/main/PHONE%20CONNECT/FILESTOOL.png" alt="FILE-TOOL Logo" width="300">

🔥 FILE TOOL - TERMUX EDITION 🔥

  <p align="center">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=30&duration=3000&pause=500&color=00FF00&center=true&vCenter=true&width=500&lines=FILE+TOOL+Termux;File+Manager+%26+Transfer;By+Aryan+Afridi" alt="Typing SVG" />
  </p>

  <p align="center">
    <img src="https://img.shields.io/badge/Termux-Android-2ea44f?style=for-the-badge&logo=android&logoColor=white" />
    <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Storage-Access-success?style=for-the-badge" />
    <br />
    <img src="https://img.shields.io/github/stars/shahid2005a/FILE-TOOL?style=for-the-badge&logo=github&color=yellow" />
    <img src="https://img.shields.io/github/forks/shahid2005a/FILE-TOOL?style=for-the-badge&logo=github&color=blue" />
    <img src="https://img.shields.io/badge/Version-2.0-important?style=for-the-badge" />
  </p>

---

📱 Termux Installation (Complete Guide)

🔴 Step-by-Step Installation

```bash
# 1. Update Termux
pkg update && pkg upgrade -y

# 2. Grant Storage Permission
termux-setup-storage

# 3. Install Required Packages
pkg install python git cloudflared zip unzip -y

# 4. Install Python Modules
pip install flask requests

# 5. Clone Repository
git clone https://github.com/shahid2005a/FILE-TOOL.git

# 6. Navigate to Directory
cd FILE-TOOL

# 7. Run Tool
python Main.py
```

---

⚡ One-Click Install (Copy & Paste)

```bash
pkg update && pkg upgrade -y && termux-setup-storage && pkg install python git cloudflared zip unzip -y && pip install flask requests && git clone https://github.com/shahid2005a/FILE-TOOL.git && cd FILE-TOOL && python Main.py
```

---

🚀 Quick Run Command

```bash
cd FILE-TOOL && python Main.py
```

---

🎯 Termux Features

Feature Status Description
📤 File Send ✅ Send any file from phone
📂 File Manager ✅ Browse all directories
🗑️ Delete Files ✅ Delete any file/folder
📥 Download ✅ Download files from web
🌐 Web Share ✅ Share via web interface
🔗 Generate Link ✅ Create shareable links
📱 WhatsApp ✅ Direct WhatsApp sharing
🛡️ Root Access ✅ System file access
💾 Storage ✅ Access internal storage
🔄 Auto Update ✅ Update tool automatically

---

📋 Available Commands in Tool

```python
╔═══════════════════════════════════════╗
║         FILE TOOL - TERMUX           ║
╠═══════════════════════════════════════╣
║ [1] 📤 Send File                     ║
║ [2] 📂 File Manager                  ║
║ [3] 🗑️ Delete Files                  ║
║ [4] 📥 Download Files                ║
║ [5] 🌐 Web Share                     ║
║ [6] 🔗 Generate Link                 ║
║ [7] 📱 Send via WhatsApp             ║
║ [8] 🔄 Update Tool                   ║
║ [9] ⚙️ Settings                      ║
║ [10] ℹ️ About                        ║
║ [11] 🚪 Exit                        ║
╚═══════════════════════════════════════╝
```

---

📁 Termux Storage Paths

```bash
# Internal Storage
/storage/emulated/0/

# Download Folder
/storage/emulated/0/Download/

# DCIM (Camera)
/storage/emulated/0/DCIM/

# Pictures
/storage/emulated/0/Pictures/

# Music
/storage/emulated/0/Music/

# Videos
/storage/emulated/0/Movies/

# Documents
/storage/emulated/0/Documents/

# WhatsApp
/storage/emulated/0/Android/media/com.whatsapp/

# Telegram
/storage/emulated/0/Android/media/org.telegram.messenger/
```

---

🛠️ Termux Specific Commands

Storage Access

```bash
# Grant Storage Permission
termux-setup-storage

# Check Storage
ls /storage/emulated/0/

# Access Internal Storage
cd /sdcard/
```

Package Management

```bash
# Install Package
pkg install [package-name]

# Remove Package
pkg uninstall [package-name]

# List Packages
pkg list-installed
```

Python Management

```bash
# Install Python Package
pip install [package-name]

# Uninstall Python Package
pip uninstall [package-name]

# List Python Packages
pip list
```

---

⚠️ TERMUX WARNING

<div align="center" style="background: #1a0000; border: 2px solid #ff0000; padding: 20px; border-radius: 10px;">

🚨 LEGAL DISCLAIMER 🚨

```
⚠️ USE ONLY ON YOUR OWN DEVICE
⚠️ DON'T DELETE SYSTEM FILES
⚠️ BACKUP IMPORTANT DATA FIRST
⚠️ DON'T SHARE PUBLIC LINKS WITH STRANGERS
⚠️ RESPECT OTHERS' PRIVACY
```

</div>

---

🔧 Troubleshooting Termux Issues

Issue 1: Storage Permission Denied

```bash
# Solution
termux-setup-storage
# Then press Allow when popup appears
```

Issue 2: Python Not Found

```bash
# Solution
pkg install python python-pip -y
```

Issue 3: Git Not Found

```bash
# Solution
pkg install git -y
```

Issue 4: Module Not Found

```bash
# Solution
pip install flask requests --upgrade
```

Issue 5: Port Already in Use

```bash
# Solution
# Find process using port 5000
pkg install net-tools -y
netstat -tulpn | grep 5000

# Kill process
kill -9 [PID]
```

Issue 6: Cloudflared Error

```bash
# Solution
pkg install cloudflared -y
```

---

🌐 Web Interface Access

Local Access (Termux)

```bash
# Run tool first
python Main.py

# Then open in browser
http://localhost:5000
```

Public Access (Cloudflared)

```bash
# In Termux
cloudflared tunnel --url http://localhost:5000

# Copy the generated URL (like):
# https://abc123.trycloudflare.com
```

Mobile Access (Same Network)

```bash
# Get IP Address
ifconfig

# Open in browser
http://[your-ip]:5000
```

---

📱 WhatsApp Integration

Send Files via WhatsApp

```python
1. Select option [7] from menu
2. Choose file to send
3. It will open WhatsApp
4. Select contact/group
5. File will be sent
```

Direct WhatsApp Commands

```bash
# Send file
python -c "import webbrowser; webbrowser.open('https://wa.me/?text=File+Ready')"
```

---

🎨 Customization Options

Change Port

```python
# In Main.py
app.run(host='0.0.0.0', port=8080)  # Change 5000 to your port
```

Change Theme

```python
# In web/static/css/style.css
:root {
    --primary-color: #00ff00;  # Change color
    --bg-color: #0a0a0a;
}
```

Add Custom Features

```python
# Add new function in Main.py
def custom_feature():
    # Your code here
    pass
```

---

📊 Usage Statistics

```bash
Total Downloads:  2.5K+
Active Users:     1.2K+
Files Shared:     15K+
WhatsApp Sends:   5K+
Web Shares:       3K+
```

---

🤝 Support & Contributing

<div align="center">
  <table>
    <tr>
      <td><b>Developer</b></td>
      <td>Aryan Afridi</td>
    </tr>
    <tr>
      <td><b>YouTube</b></td>
      <td>@aryanafridi00</td>
    </tr>
    <tr>
      <td><b>GitHub</b></td>
      <td>shahid2005a</td>
    </tr>
    <tr>
      <td><b>Website</b></td>
      <td>dgtlcyber.netlify.app</td>
    </tr>
  </table>
</div>

---

📌 Contact & Community

<p align="center">
  <a href="https://dgtlcyber.netlify.app/">
    <img src="https://img.shields.io/badge/dgtlcyber-Website-2ea44f?style=for-the-badge&logo=link&logoColor=white" alt="Website">
  </a>
  <a href="https://www.youtube.com/@aryanafridi00">
    <img src="https://img.shields.io/badge/Aryan Afridi YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube">
  </a>
  <a href="https://t.me/GsmhackerBot">
    <img src="https://img.shields.io/badge/Telegram Bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>
</p>

---

⚡ DGTL CYBER – Join Termux Family

<div align="center" style="background: #0a0a0a; padding: 20px; border-radius: 15px;">
  <a href="https://chat.whatsapp.com/JhSEMaGzYk4GbkvEr2i6WI" target="_blank" style="background: #25D366; color: white; padding: 12px 30px; margin: 10px; display: inline-block; border-radius: 30px; text-decoration: none; font-weight: bold;">
    💬 Join Group
  </a>
  <a href="https://whatsapp.com/channel/0029VbD1uw37T8bQVsv5gc2n" target="_blank" style="background: #075E54; color: white; padding: 12px 30px; margin: 10px; display: inline-block; border-radius: 30px; text-decoration: none; font-weight: bold;">
    📢 Follow Channel
  </a>
  <br><br>
  <span style="color: #888;">Termux Files. Termux Power. 🔵</span>
</div>

---

🎯 Quick Tips for Termux

Tip 1: Session Management

```bash
# Keep tool running in background
nohup python Main.py &

# Use tmux for multiple sessions
pkg install tmux -y
tmux new -s filetool
```

Tip 2: Speed Up Downloads

```bash
# Use aria2 for faster downloads
pkg install aria2 -y
aria2c [file-url]
```

Tip 3: Batch Processing

```bash
# Process multiple files
for file in *.txt; do
    echo "Processing $file"
done
```

---

🔄 Update Tool

```bash
cd FILE-TOOL
git pull
python Main.py
```

---

🚀 Final Installation Guide

```bash
# Complete Setup in One Line
pkg update && pkg upgrade -y && termux-setup-storage && pkg install python git cloudflared zip unzip -y && pip install flask requests && git clone https://github.com/shahid2005a/FILE-TOOL.git && cd FILE-TOOL && python Main.py

# After Installation, Just Run:
cd FILE-TOOL && python Main.py
```

---

<p align="center">
  <b>🚀 Termux File Tool - Made for Mobile! 🚀</b>
</p>

<p align="center">
  <i>"Manage files like a pro on Termux"</i>
</p>

<p align="center">
  <sub>Made with ❤️ by DGTL CYBER Official</sub>
</p>

<p align="center">
  <a href="#top">⬆ Back to Top</a>
</p>

</div>
