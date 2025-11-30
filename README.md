# FTPChat (File Transfer Chatting Project)

**Encrypted FTP-Based Messaging Protocol**  
**Version 1.5 — December 2025**  
**Author:** Ahmed Omar Saad  
**Contact:** <ahmedomardev@outlook.com>  

FTPChat © 2025/5/20 by Ahmed Omar Saad is licensed under **CC BY-NC-SA 4.0**.  
To view a copy of this license, visit <https://creativecommons.org/licenses/by-nc-sa/4.0/>  

---

### Overview

FTPChat is a lightweight, encrypted messaging protocol implemented entirely in Python.  
It facilitates secure communication by reading and writing messages to a shared file hosted on an FTP server.  

FTPChat is specifically designed for deployment in legacy environments, including low-power routers equipped with USB and FTP capabilities. This makes it an ideal solution for resource-constrained scenarios or discreet operations.

---

### Key Features (v1.4)

- 24-layer encryption ensuring robust payload security  
- File-based transport mechanism utilizing FTP/FTPS fallback  
- Single `.py` file deployment for simplicity  
- Optimized for legacy hardware and low-power devices  
- International chatting via [SFTPCloud Tool](https://sftpcloud.io/tools/free-ftp-server)  
- Local LAN support with `Documentation/Quick Start Guide (Making FTP Server).md`  
- Threaded send/receive — no UI freezing during FTP operations  
- Auto-refresh loop with restart-safe scheduling  
- Modern UI with ttkbootstrap (dark theme, styled buttons)  
- Blue primary buttons for clarity and aesthetics  
- Non-editable chat history with scrollable view  
- Modular encryption pipeline (easy to extend with new ciphers)  

---

### New Features Added in v1.4

- Threaded FTP I/O: Both sending and reading run in background threads for smooth, non-blocking UI  
- Improved Error Handling: Clear fallbacks between FTP_TLS and FTP, with user-friendly error messages  
- Styled UI Elements: Buttons themed with ttkbootstrap’s `primary` style for a modern look  
- Auto-Scroll Chat Window: Messages always scroll to the latest entry  
- Help Menu Integration: Direct link to project documentation and exit option  
- Restart-Safe Loop Control: Auto-refresh loop can be started once and remains stable  
- Encryption Pipeline Refactor: Doubled 12-layer MAC encryption plus compression for symbolic resilience  

---

### Protocol Operation

Messages are exchanged via a shared file on an FTP server.  
Each message contains a timestamp, username, and encrypted content.  

The protocol provides:
- Conflict-safe message writing  
- Encrypted message formatting  
- Lightweight, file-based communication  

---

### Usage Instructions

1. Download `FtpChat.exe` for Windows 10/11, or run the Python script on macOS/Linux.  
2. Activate your FTP server. Refer to `Documentation/Quick Start Guide (Making FTP Server).md`.  
3. Enter your credentials as prompted.  
4. Review the `Notes Before Starting` section prior to use.  

---

### License

FTPChat is distributed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)**.  
Commercial use is strictly prohibited without written permission from the author.  
All rights to the name “FTPChat” and its protocol specification are reserved by Ahmed Omar Saad.  
