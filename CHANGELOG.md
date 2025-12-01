# FTPChat (File Transfer Chatting Project)

**Encrypted FTP-Based Messaging Protocol**  
**Version 1.5 — December 2025**  
**Author:** Ahmed Omar Saad  
**Contact:** <ahmedomardev@outlook.com>

FTPChat © 2025/5/20 by Ahmed Omar Saad is licensed under **CC BY-NC-SA 4.0**.  
To view a copy of this license, visit <https://creativecommons.org/licenses/by-nc-sa/4.0/>

---

### Key Features (v1.5)

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

### New Features Added in v1.5

- Threaded FTP I/O: Both sending and reading run in background threads for smooth, non-blocking UI
- Improved Error Handling: Clear fallbacks between FTP_TLS and FTP, with user-friendly error messages
- Styled UI Elements: Buttons themed with ttkbootstrap’s `primary` style for a modern look
- Auto-Scroll Chat Window: Messages always scroll to the latest entry
- Help Menu Integration: Direct link to project documentation and exit option
- Restart-Safe Loop Control: Auto-refresh loop can be started once and remains stable
- Encryption Pipeline Refactor: Doubled 12-layer MAC encryption plus compression for symbolic resilience
