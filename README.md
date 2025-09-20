# FTPChat  
**Encrypted FTP-Based Messaging Protocol**  
**Version 1.2 — September 2025**  
**Author:** Ahmed Omar Saad  
**Contact:** ahmedomardev@outlook.com

---

## Overview

FTPChat is a lightweight, encrypted messaging protocol implemented entirely in Python.  
It facilitates secure communication by reading and writing messages to a shared file hosted on an FTP server.

FTPChat is specifically designed for deployment in legacy environments, including low-power routers equipped with USB and FTP capabilities. This makes it an ideal solution for resource-constrained scenarios or discreet operations.

---

## Key Features

- 24-layer encryption ensuring robust payload security  
- File-based transport mechanism utilizing FTP  
- Fully operational within a single `.py` file  
- Optimized for legacy hardware and low-power devices  
- Compatible with routers supporting USB and FTP  
- Energy-efficient and environmentally conscious design

---

## Protocol Operation

Messages are exchanged via a shared file on an FTP server.  
Each message contains a timestamp, username, and encrypted content.  
The protocol provides:
- Conflict-safe message writing  
- Encrypted message formatting  
- Lightweight, file-based communication

**Note:** FTPChat does not support auto-refresh or background polling.

---

## Usage Instructions

1. Download `FtpChat.exe` for Windows, or run the Python script on macOS or Linux.
2. Activate your FTP server. Refer to `Documentation/Quick Start Guide (Making FTP Server).md` for detailed setup instructions.
3. Enter your credentials as prompted.
4. Please review the `Notes Before Starting` section prior to use.

---

## License

FTPChat is distributed under a custom MIT-style license.  
Commercial use is strictly prohibited without written permission from the author.  
All rights to the name “FTPChat” and its protocol specification are reserved by Ahmed Omar Saad.

For full license details, refer to the `LICENSE