# FTPChat  
Encrypted FTP-based Messaging Protocol  
Version 1.2 — September 2025  
Author: Ahmed Omar Saad  
Contact: ahmedomardev@outlook.com

---

## What is FTPChat?

FTPChat is a lightweight, encrypted messaging protocol built entirely in Python.  
It transmits messages by reading and writing to a shared file on an FTP server.  

Designed for legacy-class deployment, FTPChat runs on low-power routers with USB and FTP capabilities, making it suitable for constrained environments or stealth setups.

---

## Features

- 24-layer encryption for secure payloads  
- File-based transport over FTP  
- Fully functional in a single `.py` file  
- Designed for legacy-class deployment  
- Compatible with low-power routers (USB + FTP support) 
- Saving Power, Saving environment
---

## How It Works

Messages are written to and read from a shared file on an FTP server.  
Each message includes a timestamp, username, and encrypted content.  
The protocol handles:
- Conflict-safe message writing  
- Encrypted message formatting  
- Lightweight file-based communication

Note: FTPChat does not include auto-refresh or background polling.

---

## License 

FTPChat is released under a custom MIT-style license.  
Commercial use is prohibited without written permission from the author.  
All rights to the name “FTPChat” and its protocol specification are retained by Ahmed Omar Saad.

See the full license in the `LICENSE` file.
