"""
FTPChat - Encrypted FTP-based Messaging Protocol
Version 1.4 — November 2025
Type: Custom-styled MIT LICENSE
Author: Ahmed Omar Saad
Contact: ahmedomardev@outlook.com
FTPChat  © 2025/5/20 by Ahmed Omar Saad is licensed under CC BY-NC-SA 4.0. To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/4.0/

*Permission is hereby granted, free of charge, to any person obtaining a copy
*of this software and associated documentation files (the “Software”), to deal
*in the Software without restriction, including without limitation the rights
*to use, copy, modify, merge, publish, distribute, and/or sublicense copies of
*the Software, subject to the following conditions:

*- The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*- **Commercial use of this software requires prior written permission from the author.**
*- **The author reserves the right to relicense this software as closed-source or commercial at any time.**
*- All rights to the name “FTPChat” and its project specification are retained by Ahmed Omar Saad.

*THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
*INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE
*AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
*DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
*OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

*Notes:
*The author may offer separate commercial licenses for enterprise or closed-source use. Contact ahmedomardev@outlook.com for inquiries.
*This license applies to all source code, documentation, and project specifications included in the FTPChat project.
"""

from datetime import datetime
from ftplib import FTP, FTP_TLS
from threading import Thread
from webbrowser import open as open_link

from ttkbootstrap import (
    Window,
    Button,
    Label,
    Entry,
    Menu,
    NORMAL,
    DISABLED,
    StringVar,
    ScrolledText,
)
from tkinter import messagebox
from zlib import compress, decompress
from base64 import b64encode, b64decode


def help_func():
    open_link("ahmed-omar-software-projects.mydurable.com")


# !The start of the characters list and key for mac encryption layers


CHARACTERS = (
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "!",
    '"',
    "#",
    "$",
    "%",
    "&",
    "'",
    "(",
    ")",
    "*",
    "+",
    ",",
    "-",
    ".",
    "/",
    ":",
    ";",
    "<",
    "=",
    ">",
    "?",
    "@",
    "[",
    "\\",
    "]",
    "^",
    "_",
    "`",
    "{",
    "|",
    "}",
    "~",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
)
KEY_FOR_MAC_1 = (
    "!",
    ")",
    ".",
    "3",
    "(",
    "J",
    "b",
    "C",
    "A",
    ";",
    "n",
    "_",
    "$",
    "0",
    ",",
    "Z",
    "B",
    "c",
    "|",
    "g",
    "7",
    "^",
    '"',
    "I",
    "v",
    "P",
    "Y",
    "M",
    "i",
    "O",
    "k",
    "L",
    "%",
    "y",
    "D",
    "#",
    "@",
    "<",
    "9",
    "r",
    "K",
    "2",
    "-",
    "t",
    "8",
    "H",
    "=",
    "+",
    "`",
    "o",
    "T",
    "u",
    "s",
    "p",
    "U",
    "S",
    "Q",
    "~",
    "'",
    "G",
    "*",
    "&",
    ">",
    "X",
    "a",
    "N",
    "4",
    "d",
    "m",
    "l",
    "V",
    "w",
    "z",
    ":",
    "q",
    "?",
    "5",
    "x",
    "{",
    "/",
    "F",
    "j",
    "]",
    "6",
    "W",
    "f",
    "R",
    "1",
    "}",
    "e",
    "[",
    "\\",
    "h",
    "E",
)
KEY_FOR_MAC_2 = (
    "$",
    "i",
    "o",
    "c",
    "&",
    "L",
    "/",
    "~",
    "O",
    "@",
    "(",
    "[",
    "Q",
    "v",
    "a",
    "Y",
    "7",
    "3",
    "*",
    "X",
    "x",
    "8",
    "{",
    "K",
    "E",
    "4",
    "M",
    "q",
    "|",
    "J",
    "0",
    "<",
    "Z",
    "e",
    "_",
    "V",
    "H",
    "m",
    "G",
    "A",
    "d",
    "y",
    "T",
    ".",
    "S",
    "j",
    "I",
    "#",
    "]",
    "p",
    "\\",
    "F",
    "b",
    '"',
    "W",
    "k",
    ";",
    "5",
    "N",
    "s",
    "2",
    "l",
    "1",
    ":",
    "r",
    "-",
    "`",
    "h",
    ">",
    "t",
    "}",
    "^",
    "+",
    "U",
    "B",
    "!",
    "6",
    ")",
    ",",
    "P",
    "g",
    "=",
    "C",
    "D",
    "?",
    "R",
    "9",
    "z",
    "'",
    "n",
    "w",
    "f",
    "%",
    "u",
)
KEY_FOR_MAC_3 = (
    "h",
    "R",
    "-",
    "I",
    "4",
    "$",
    "Z",
    "c",
    "/",
    "Q",
    "O",
    "a",
    "E",
    "V",
    "_",
    "q",
    "A",
    "!",
    ",",
    "X",
    "N",
    "H",
    "`",
    ".",
    "K",
    "e",
    "*",
    "v",
    "\\",
    "T",
    "k",
    "M",
    "Y",
    "^",
    "6",
    "l",
    "j",
    "G",
    "'",
    "m",
    "x",
    "7",
    "3",
    "L",
    ";",
    "C",
    "1",
    "p",
    "2",
    "S",
    "]",
    "r",
    "%",
    "g",
    "@",
    "0",
    ")",
    "}",
    "B",
    "W",
    "|",
    "t",
    "=",
    "?",
    ">",
    "{",
    "b",
    "d",
    '"',
    "u",
    "f",
    "+",
    "P",
    ":",
    "z",
    "i",
    "F",
    "~",
    "[",
    "(",
    "&",
    "o",
    "n",
    "D",
    "#",
    "5",
    "8",
    "J",
    "w",
    "s",
    "U",
    "9",
    "<",
    "y",
)
KEY_FOR_MAC_4 = (
    "_",
    "(",
    "H",
    "7",
    "~",
    "t",
    "F",
    "D",
    "j",
    "5",
    "C",
    "#",
    "o",
    "^",
    "X",
    "z",
    "9",
    "-",
    "k",
    '"',
    "N",
    "E",
    "+",
    "q",
    "P",
    "/",
    ";",
    "S",
    "W",
    "h",
    "s",
    "f",
    ".",
    "A",
    "4",
    "'",
    "\\",
    "Q",
    ",",
    "m",
    "e",
    "$",
    "6",
    "p",
    "i",
    "y",
    "|",
    "U",
    "a",
    "3",
    "L",
    "g",
    "c",
    "]",
    "0",
    ")",
    "v",
    "x",
    "8",
    "T",
    "l",
    "u",
    "b",
    "[",
    "V",
    ":",
    "M",
    "r",
    "B",
    "G",
    "1",
    "K",
    "d",
    ">",
    "O",
    "`",
    "*",
    "I",
    "?",
    "2",
    "}",
    "n",
    "@",
    "<",
    "&",
    "Z",
    "{",
    "R",
    "%",
    "!",
    "Y",
    "w",
    "=",
    "J",
)
KEY_FOR_MAC_5 = (
    "W",
    "f",
    "v",
    "l",
    '"',
    "h",
    "@",
    "C",
    ";",
    "!",
    "a",
    "8",
    "5",
    "S",
    "G",
    "X",
    "-",
    "{",
    "^",
    "~",
    "|",
    "m",
    "=",
    "&",
    "H",
    "O",
    "M",
    "Q",
    "0",
    "d",
    "I",
    "g",
    "6",
    "J",
    "9",
    "E",
    "z",
    "K",
    "L",
    "?",
    "/",
    ">",
    "o",
    "]",
    "n",
    "Y",
    "F",
    "t",
    "i",
    "D",
    "w",
    "#",
    "(",
    "`",
    "y",
    "%",
    "r",
    "[",
    "p",
    "*",
    "b",
    "j",
    "<",
    "}",
    "'",
    "\\",
    ",",
    "B",
    "R",
    "q",
    "U",
    "x",
    ")",
    "$",
    "_",
    "1",
    "+",
    "T",
    "N",
    "s",
    "7",
    "c",
    "k",
    ":",
    "4",
    "3",
    "e",
    "Z",
    "V",
    "P",
    "2",
    ".",
    "u",
    "A",
)
KEY_FOR_MAC_6 = (
    "}",
    "X",
    "j",
    "%",
    "I",
    "T",
    "L",
    "s",
    "^",
    "m",
    "d",
    "K",
    ")",
    "-",
    "B",
    "D",
    "o",
    "E",
    "@",
    "Z",
    "`",
    "2",
    "f",
    "a",
    "6",
    "q",
    "e",
    "n",
    "*",
    "R",
    "[",
    ";",
    "V",
    '"',
    "z",
    "y",
    "+",
    "S",
    "W",
    "7",
    "x",
    "&",
    "<",
    "9",
    "U",
    "N",
    "]",
    "#",
    "=",
    "b",
    "Q",
    "Y",
    "(",
    "r",
    "\\",
    "M",
    "A",
    "v",
    "H",
    "{",
    "w",
    "p",
    "3",
    ",",
    "k",
    "'",
    "t",
    ":",
    "u",
    "J",
    "8",
    "F",
    ">",
    "i",
    "G",
    "P",
    "0",
    "/",
    "~",
    "|",
    "h",
    "O",
    "g",
    "_",
    "c",
    "l",
    "C",
    "4",
    "?",
    "1",
    ".",
    "!",
    "$",
    "5",
)
KEY_FOR_MAC_7 = (
    "U",
    "F",
    ".",
    "T",
    "n",
    "}",
    ")",
    "E",
    "I",
    "S",
    "{",
    "\\",
    ">",
    "B",
    "a",
    "j",
    "Z",
    "/",
    "<",
    "P",
    "e",
    "O",
    "|",
    ",",
    "i",
    "0",
    "l",
    "6",
    "@",
    ";",
    "X",
    "M",
    "J",
    "#",
    "2",
    "7",
    "+",
    "s",
    "]",
    "h",
    "x",
    "&",
    "y",
    "-",
    "`",
    "G",
    "3",
    ":",
    "(",
    "L",
    "=",
    "f",
    "*",
    "H",
    "Q",
    "R",
    "8",
    "4",
    "z",
    "[",
    "^",
    "5",
    "g",
    "D",
    "Y",
    "!",
    "W",
    "$",
    "q",
    "9",
    "K",
    "k",
    '"',
    "d",
    "p",
    "A",
    "u",
    "w",
    "C",
    "_",
    "o",
    "b",
    "'",
    "r",
    "t",
    "N",
    "v",
    "?",
    "m",
    "1",
    "c",
    "%",
    "V",
    "~",
)
KEY_FOR_MAC_8 = (
    "u",
    "5",
    "_",
    "Y",
    "l",
    "p",
    "D",
    "L",
    "b",
    "k",
    "@",
    "9",
    "O",
    "0",
    "*",
    "}",
    "f",
    "w",
    "C",
    "d",
    '"',
    "g",
    "t",
    "K",
    "&",
    ";",
    "s",
    "v",
    "o",
    "=",
    "7",
    "I",
    "]",
    ".",
    "R",
    "c",
    "?",
    "a",
    "^",
    "V",
    "x",
    "%",
    "n",
    "\\",
    "z",
    "B",
    "'",
    "Q",
    "U",
    "+",
    "m",
    "1",
    ",",
    "F",
    "M",
    "$",
    "T",
    "3",
    "N",
    ")",
    "r",
    "y",
    ">",
    "8",
    "P",
    "q",
    "2",
    "<",
    "|",
    "`",
    "4",
    "~",
    "/",
    "A",
    ":",
    "J",
    "{",
    "(",
    "H",
    "-",
    "h",
    "i",
    "j",
    "G",
    "S",
    "X",
    "[",
    "6",
    "Z",
    "E",
    "W",
    "#",
    "e",
    "!",
)
KEY_FOR_MAC_9 = (
    ",",
    "T",
    "g",
    "B",
    "5",
    "n",
    "f",
    "s",
    "G",
    "W",
    "V",
    "`",
    "M",
    "[",
    "!",
    "e",
    "L",
    "-",
    "_",
    "Q",
    "9",
    "^",
    ")",
    "P",
    "0",
    "j",
    "2",
    "v",
    "?",
    "E",
    "Y",
    "Z",
    "1",
    "|",
    ".",
    "#",
    "w",
    "D",
    "J",
    "l",
    "O",
    "@",
    "t",
    "{",
    "x",
    "+",
    "4",
    "S",
    ";",
    "u",
    "F",
    "~",
    "q",
    "}",
    "<",
    "N",
    "o",
    "(",
    "K",
    "/",
    "z",
    "a",
    "\\",
    "p",
    "3",
    '"',
    "i",
    "8",
    "7",
    "%",
    "6",
    "U",
    ">",
    "C",
    "X",
    "$",
    "R",
    "&",
    "d",
    "c",
    "I",
    "y",
    "H",
    "=",
    "'",
    "h",
    "r",
    "m",
    "*",
    "b",
    ":",
    "A",
    "]",
    "k",
)
KEY_FOR_MAC_10 = (
    "0",
    "R",
    "h",
    "C",
    "~",
    "o",
    "i",
    "g",
    ",",
    "k",
    "8",
    "H",
    "Q",
    "p",
    "9",
    "v",
    "$",
    "u",
    "5",
    "-",
    "a",
    "{",
    '"',
    "s",
    "A",
    ";",
    "[",
    "Y",
    "^",
    "r",
    "M",
    "b",
    "G",
    "_",
    "m",
    "e",
    "x",
    "I",
    "T",
    "n",
    ">",
    "<",
    "P",
    "J",
    "U",
    "2",
    "3",
    "4",
    "#",
    "W",
    ":",
    "w",
    "D",
    "|",
    "(",
    "z",
    "q",
    "K",
    "V",
    "B",
    "L",
    "j",
    "d",
    "&",
    "!",
    "1",
    "+",
    "\\",
    "X",
    "/",
    "?",
    "@",
    "*",
    "t",
    "c",
    "}",
    "Z",
    "%",
    ".",
    ")",
    "E",
    "`",
    "f",
    "N",
    "y",
    "6",
    "7",
    "O",
    "=",
    "]",
    "F",
    "l",
    "S",
    "'",
)
KEY_FOR_MAC_11 = (
    "S",
    "}",
    "!",
    "N",
    "\\",
    "C",
    "M",
    "[",
    "z",
    "?",
    "%",
    "7",
    "q",
    "Y",
    ".",
    "$",
    "l",
    "D",
    "G",
    "f",
    "+",
    "/",
    "6",
    "#",
    "5",
    "w",
    "P",
    "O",
    "U",
    "*",
    "X",
    "d",
    "=",
    "3",
    ":",
    "i",
    "y",
    "h",
    "v",
    "(",
    "R",
    "W",
    "x",
    '"',
    "1",
    "c",
    "A",
    "<",
    "J",
    "_",
    "L",
    "|",
    "T",
    "^",
    ">",
    "H",
    "2",
    "`",
    "I",
    ";",
    "0",
    "k",
    "-",
    "u",
    "o",
    "&",
    "Z",
    "j",
    "p",
    ")",
    ",",
    "r",
    "9",
    "'",
    "Q",
    "4",
    "]",
    "m",
    "t",
    "B",
    "a",
    "F",
    "V",
    "b",
    "8",
    "E",
    "n",
    "g",
    "@",
    "e",
    "s",
    "~",
    "{",
    "K",
)


# !The end of the characters list and key for mac encryption layers


# !---The start for the all encryption and decryption functions---


def reverser(text):
    """This function reverses the text"""
    return text[::-1]


# ---The end of reverser function.---


def mac_encode(text, key):
    """Generic Mono-Alphabetic cipher encoder with given key."""
    result = []
    for char in text:
        if char in CHARACTERS:
            index = CHARACTERS.index(char)
            result.append(key[index])
        else:
            result.append(char)
    return "".join(result)


def mac_decode(text, key):
    """Generic Mono-Alphabetic cipher decoder with given key."""
    result = []
    for char in text:
        if char in key:
            index = key.index(char)
            result.append(CHARACTERS[index])
        else:
            result.append(char)
    return "".join(result)


def all_mac_encryption(text):
    """12 Layers combined MAC encryption"""
    text = mac_encode(text, KEY_FOR_MAC_5)
    text = reverser(text)
    text = mac_encode(text, KEY_FOR_MAC_4)
    text = mac_encode(text, KEY_FOR_MAC_2)
    text = mac_encode(text, KEY_FOR_MAC_1)
    text = mac_encode(text, KEY_FOR_MAC_3)
    text = mac_encode(text, KEY_FOR_MAC_8)
    text = mac_encode(text, KEY_FOR_MAC_7)
    text = mac_encode(text, KEY_FOR_MAC_9)
    text = mac_encode(text, KEY_FOR_MAC_6)
    text = mac_encode(text, KEY_FOR_MAC_11)
    return mac_encode(text, KEY_FOR_MAC_10)


def all_mac_decryption(text):
    """12 Layers combined MAC decryption"""
    text = mac_decode(text, KEY_FOR_MAC_10)
    text = mac_decode(text, KEY_FOR_MAC_11)
    text = mac_decode(text, KEY_FOR_MAC_6)
    text = mac_decode(text, KEY_FOR_MAC_9)
    text = mac_decode(text, KEY_FOR_MAC_7)
    text = mac_decode(text, KEY_FOR_MAC_8)
    text = mac_decode(text, KEY_FOR_MAC_3)
    text = mac_decode(text, KEY_FOR_MAC_1)
    text = mac_decode(text, KEY_FOR_MAC_2)
    text = mac_decode(text, KEY_FOR_MAC_4)
    text = reverser(text)
    return mac_decode(text, KEY_FOR_MAC_5)


def encrypt(text: str) -> str:
    """Doubled 12 Layer MAC encryption + compression"""
    encrypted = all_mac_encryption(all_mac_encryption(text))
    compressed = compress(encrypted.encode("utf-8"))
    return b64encode(compressed).decode("utf-8")


def decrypt(text: str) -> str:
    """Doubled 12 Layer MAC decryption + decompression"""
    compressed = b64decode(text.encode("utf-8"))
    encrypted = decompress(compressed).decode("utf-8")
    return all_mac_decryption(all_mac_decryption(encrypted))


# !---The sending and reading messages functions---


def send_message_non(username, message):
    msg_e = encrypt(
        f"{datetime.now().strftime('%Y-%m-%d %H:%M')}:{username}: {message}"
    )
    msg.delete("1.0", "end")
    ftp_host = FTP_HOST.get()
    ftp_user = FTP_USER.get()
    ftp_pass = FTP_PASS.get()
    chat_name = f"{chat_file_name.get()}.txt"
    local_temp = "chat_temp.txt"

    try:
        try:
            ftp = FTP_TLS(ftp_host)
            ftp.login(ftp_user, ftp_pass)
        except Exception:
            ftp = FTP(ftp_host)
            ftp.login(ftp_user, ftp_pass)

        try:
            with open(local_temp, "wb") as f:
                ftp.retrbinary(f"RETR " + chat_name, f.write)
        except Exception:
            pass

        with open(local_temp, "w", encoding="utf-8") as f:
            f.write(f"{msg_e}\n")

        with open(local_temp, "rb") as f:
            ftp.storbinary(f"APPE " + chat_name, f)

        ftp.quit()
        read_messages()

    except Exception as error:
        messagebox.showerror("Error sending message", str(error))


def send_messages(username, message):
    Thread(target=send_message_non, args=(
        username, message), daemon=True).start()


def read_messages_non():
    ftp_host = FTP_HOST.get()
    ftp_user = FTP_USER.get()
    ftp_pass = FTP_PASS.get()
    chat_name = f"{chat_file_name.get()}.txt"
    local_temp = "chat_temp.txt"

    try:
        try:
            ftp = FTP_TLS(ftp_host)
            ftp.login(ftp_user, ftp_pass)
        except Exception as e:
            ftp = FTP(ftp_host)
            ftp.login(ftp_user, ftp_pass)

        with open(local_temp, "wb") as file:
            ftp.retrbinary(f"RETR {chat_name}", file.write)
        ftp.quit()

        with open(local_temp, "r", encoding="utf-8") as file:
            lines = file.readlines()

        out_lines = []
        for line in lines:
            try:
                out_lines.append(decrypt(line.strip()))
            except Exception:
                out_lines.append(line.strip())

        message_text = "\n".join(
            out_lines) if out_lines else "No messages yet."

        chat_notes.config(state=NORMAL)
        chat_notes.delete("1.0", "end")
        chat_notes.insert("end", message_text)
        chat_notes.see("end")
        chat_notes.config(state=DISABLED)

    except Exception as error:
        messagebox.showerror("Error reading messages", str(error))


def read_messages():
    Thread(target=read_messages_non, daemon=True).start()


def auto_refresh_func():
    if FTP_HOST.get() and FTP_USER.get() and FTP_PASS.get() and chat_file_name.get():
        read_messages()
        main.after(5000, auto_refresh_func)
    else:
        messagebox.showwarning("Warning", "Please, fill in all details")


def start_loop():
    send_butt.config(state=NORMAL)
    auto_refresh_func()
    done_butt.config(state=DISABLED)
    done_butt.config(text="Loop Started")


main = Window(themename="darkly")
main.title("FTPChat")
main.geometry("1920x1080")
main.state("zoomed")
menubar = Menu(main)
main.config(menu=menubar)

# Menubar
accessibility_menu = Menu(menubar, tearoff=False)
accessibility_menu.add_command(label="Help", command=help_func)
accessibility_menu.add_command(label="Exit", command=lambda: main.destroy())
menubar.add_cascade(label="Accessibility", menu=accessibility_menu)

# Widgets

FTP_HOST = StringVar()
Label(main, text="Host:").place(x=5, y=5)
Entry(main, textvariable=FTP_HOST, width=225).place(x=100, y=5)

FTP_USER = StringVar()
Label(main, text="FTP User:").place(x=5, y=40)
Entry(main, textvariable=FTP_USER, width=225).place(x=100, y=40)

FTP_PASS = StringVar()
Label(main, text="Password:").place(x=5, y=75)
Entry(main, textvariable=FTP_PASS, width=225, show="*").place(x=100, y=75)

username_var = StringVar()
Label(main, text="Username:").place(x=5, y=110)
Entry(main, textvariable=username_var, width=225).place(x=100, y=110)

chat_file_name = StringVar()
Label(main, text="Chat File:").place(x=5, y=146)
Entry(main, textvariable=chat_file_name, width=201).place(x=100, y=146)

done_butt = Button(
    main,
    text="Done",
    command=lambda: start_loop(),
    width=20,
    bootstyle="primary",
)
done_butt.place(x=1730, y=146)

Label(main, text="Chat:").place(x=5, y=180)
chat_notes = ScrolledText(main, width=233, height=16)
chat_notes.place(x=5, y=210)
chat_notes.see("end")
chat_notes.config(state=DISABLED)

Label(main, text="Message:").place(x=5, y=547)
msg = ScrolledText(main, width=233, height=16)
msg.place(x=5, y=575)

send_butt = Button(
    main,
    text="Send",
    command=lambda: send_messages(username_var.get(), msg.get("1.0", "end")),
    width=235,
    bootstyle="primary",
    state=DISABLED
).place(x=5, y=920)

main.mainloop()
