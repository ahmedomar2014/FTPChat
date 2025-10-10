from datetime import datetime
from ftplib import FTP
from tkinter import (DISABLED, END, NORMAL, Button, Entry, Label, Menu,
                     StringVar, messagebox, scrolledtext)
from webbrowser import open as open_link

from ttkbootstrap import END, Button, Menu, Window


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


def mac1_encode(text):
    """Encryption layer for Mono-Alphabetic cipher - Number (1)."""
    result = []
    for char in text:
        if char in CHARACTERS:
            index = CHARACTERS.index(char)
            result.append(KEY_FOR_MAC_1[index])
        else:
            result.append(char)
    return "".join(result)


def mac1_decode(text):
    """Decryption layer for Mono-Alphabetic cipher - Number (1)."""
    result = []
    for char in text:
        if char in KEY_FOR_MAC_1:
            index = KEY_FOR_MAC_1.index(char)
            result.append(CHARACTERS[index])
        else:
            result.append(char)
    return "".join(result)


# ---The end for the encryption and decryption functions - Number (1)---


def mac2_encode(text):
    """Encryption layer for Mono-Alphabetic cipher - Number (2)."""
    result = []
    for char in text:
        if char in CHARACTERS:
            index = CHARACTERS.index(char)
            result.append(KEY_FOR_MAC_2[index])
        else:
            result.append(char)
    return "".join(result)


def mac2_decode(text):
    """Decryption layer for Mono-Alphabetic cipher - Number (2)."""
    result = []
    for char in text:
        if char in KEY_FOR_MAC_2:
            index = KEY_FOR_MAC_2.index(char)
            result.append(CHARACTERS[index])
        else:
            result.append(char)
    return "".join(result)


# ---The end for the encryption and decryption functions - Number (2)---


def mac3_encode(text):
    """Encryption layer for Mono-Alphabetic cipher - Number (3)."""
    result = []
    for char in text:
        if char in CHARACTERS:
            index = CHARACTERS.index(char)
            result.append(KEY_FOR_MAC_3[index])
        else:
            result.append(char)
    return "".join(result)


def mac3_decode(text):
    """Decryption layer for Mono-Alphabetic cipher - Number (3)."""
    result = []
    for char in text:
        if char in KEY_FOR_MAC_3:
            index = KEY_FOR_MAC_3.index(char)
            result.append(CHARACTERS[index])
        else:
            result.append(char)
    return "".join(result)


# ---The end for the encryption and decryption functions - Number (3)---


def mac4_encode(text):
    """Encryption layer for Mono-Alphabetic cipher - Number (4)."""
    result = []
    for char in text:
        if char in CHARACTERS:
            index = CHARACTERS.index(char)
            result.append(KEY_FOR_MAC_4[index])
        else:
            result.append(char)
    return "".join(result)


def mac4_decode(text):
    """Decryption layer for Mono-Alphabetic cipher - Number (4)."""
    result = []
    for char in text:
        if char in KEY_FOR_MAC_4:
            index = KEY_FOR_MAC_4.index(char)
            result.append(CHARACTERS[index])
        else:
            result.append(char)
    return "".join(result)


# ---The end for the encryption and decryption functions - Number (4)---


def mac5_encode(text):
    """Encryption layer for Mono-Alphabetic cipher - Number (5)."""
    result = []
    for char in text:
        if char in CHARACTERS:
            index = CHARACTERS.index(char)
            result.append(KEY_FOR_MAC_5[index])
        else:
            result.append(char)
    return "".join(result)


def mac5_decode(text):
    """Decryption layer for Mono-Alphabetic cipher - Number (5)."""
    result = []
    for char in text:
        if char in KEY_FOR_MAC_5:
            index = KEY_FOR_MAC_5.index(char)
            result.append(CHARACTERS[index])
        else:
            result.append(char)
    return "".join(result)


# ---The end for the encryption and decryption functions - Number (5)---


def mac6_encode(text):
    """Encryption layer for Mono-Alphabetic cipher - Number (6)."""
    result = []
    for char in text:
        if char in CHARACTERS:
            index = CHARACTERS.index(char)
            result.append(KEY_FOR_MAC_6[index])
        else:
            result.append(char)
    return "".join(result)


def mac6_decode(text):
    """Decryption layer for Mono-Alphabetic cipher - Number (6)."""
    result = []
    for char in text:
        if char in KEY_FOR_MAC_6:
            index = KEY_FOR_MAC_6.index(char)
            result.append(CHARACTERS[index])
        else:
            result.append(char)
    return "".join(result)


# ---The end for the encryption and decryption functions - Number (6)---


def mac7_encode(text):
    """Encryption layer for Mono-Alphabetic cipher - Number (7)."""
    result = []
    for char in text:
        if char in CHARACTERS:
            index = CHARACTERS.index(char)
            result.append(KEY_FOR_MAC_7[index])
        else:
            result.append(char)
    return "".join(result)


def mac7_decode(text):
    """Decryption layer for Mono-Alphabetic cipher - Number (7)."""
    result = []
    for char in text:
        if char in KEY_FOR_MAC_7:
            index = KEY_FOR_MAC_7.index(char)
            result.append(CHARACTERS[index])
        else:
            result.append(char)
    return "".join(result)


# ---The end for the encryption and decryption functions - Number (7)---


def mac8_encode(text):
    """Encryption layer for Mono-Alphabetic cipher - Number (8)."""
    result = []
    for char in text:
        if char in CHARACTERS:
            index = CHARACTERS.index(char)
            result.append(KEY_FOR_MAC_8[index])
        else:
            result.append(char)
    return "".join(result)


def mac8_decode(text):
    """Decryption layer for Mono-Alphabetic cipher - Number (8)."""
    result = []
    for char in text:
        if char in KEY_FOR_MAC_8:
            index = KEY_FOR_MAC_8.index(char)
            result.append(CHARACTERS[index])
        else:
            result.append(char)
    return "".join(result)


# ---The end for the encryption and decryption functions - Number (8)---


def mac9_encode(text):
    """Encryption layer for Mono-Alphabetic cipher - Number (9)."""
    result = []
    for char in text:
        if char in CHARACTERS:
            index = CHARACTERS.index(char)
            result.append(KEY_FOR_MAC_9[index])
        else:
            result.append(char)
    return "".join(result)


def mac9_decode(text):
    """Decryption layer for Mono-Alphabetic cipher - Number (9)."""
    result = []
    for char in text:
        if char in KEY_FOR_MAC_9:
            index = KEY_FOR_MAC_9.index(char)
            result.append(CHARACTERS[index])
        else:
            result.append(char)
    return "".join(result)


# ---The end for the encryption and decryption functions - Number (9)---


def mac10_encode(text):
    """Encryption layer for Mono-Alphabetic cipher - Number (10)."""
    result = []
    for char in text:
        if char in CHARACTERS:
            index = CHARACTERS.index(char)
            result.append(KEY_FOR_MAC_10[index])
        else:
            result.append(char)
    return "".join(result)


def mac10_decode(text):
    """Decryption layer for Mono-Alphabetic cipher - Number (10)."""
    result = []
    for char in text:
        if char in KEY_FOR_MAC_10:
            index = KEY_FOR_MAC_10.index(char)
            result.append(CHARACTERS[index])
        else:
            result.append(char)
    return "".join(result)


# ---The end for the encryption and decryption functions - Number (10)---


def mac11_encode(text):
    """Encryption layer for Mono-Alphabetic cipher - Number (11)."""
    result = []
    for char in text:
        if char in CHARACTERS:
            index = CHARACTERS.index(char)
            result.append(KEY_FOR_MAC_11[index])
        else:
            result.append(char)
    return "".join(result)


def mac11_decode(text):
    """Decryption layer for Mono-Alphabetic cipher - Number (11)."""
    result = []
    for char in text:
        if char in KEY_FOR_MAC_11:
            index = KEY_FOR_MAC_11.index(char)
            result.append(CHARACTERS[index])
        else:
            result.append(char)
    return "".join(result)


# ---The end for the encryption and decryption functions - Number (11)---


# !---The end for the all encryption and decryption functions---


def all_mac_encryption(text):
    """12 Layers combined MAC encryption"""
    layer1 = mac5_encode(text)
    layer2 = reverser(layer1)
    layer3 = mac4_encode(layer2)
    layer4 = mac2_encode(layer3)
    layer5 = mac1_encode(layer4)
    layer6 = mac3_encode(layer5)
    layer7 = mac8_encode(layer6)
    layer8 = mac7_encode(layer7)
    layer9 = mac9_encode(layer8)
    layer10 = mac6_encode(layer9)
    layer11 = mac11_encode(layer10)
    return str(mac10_encode(layer11))


def all_mac_decryption(text):
    """12 Layers combined MAC decryption"""
    layer1 = mac10_decode(text)
    layer2 = mac11_decode(layer1)
    layer3 = mac6_decode(layer2)
    layer4 = mac9_decode(layer3)
    layer5 = mac7_decode(layer4)
    layer6 = mac8_decode(layer5)
    layer7 = mac3_decode(layer6)
    layer8 = mac1_decode(layer7)
    layer9 = mac2_decode(layer8)
    layer10 = mac4_decode(layer9)
    layer11 = reverser(layer10)
    return str(mac5_decode(layer11))


def encrypt(text):
    """Doubled 12 Layer MAC encryption"""
    return str(all_mac_encryption(all_mac_encryption(text)))


def decrypt(text):
    """Doubled 12 Layer MAC decryption"""
    return str(all_mac_decryption(all_mac_decryption(text)))


# !---The sending and reading messages functions---


def send_message(username, message):
    msg = f"{datetime.now()}:{username}: {message}"
    ftp_host = FTP_HOST.get()
    ftp_user = FTP_USER.get()
    ftp_pass = FTP_PASS.get()
    if not ftp_host or not ftp_user or not ftp_pass:
        messagebox.showerror("Error", "Please enter FTP credentials.")
        return

    ftp = FTP()
    ftp.connect(ftp_host)
    ftp.login(ftp_user, ftp_pass)

    chat_content = ""
    try:
        with open(CHAT_FILE, "wb") as file:
            ftp.retrbinary(f"RETR {CHAT_FILE}", file.write)
        with open(CHAT_FILE, "r", encoding="utf-8") as file:
            chat_content = file.read()
            if chat_content:
                chat_content = decrypt(chat_content)
    except Exception:
        chat_content = ""

    chat_content += msg
    encrypted_content = encrypt(chat_content)

    with open(CHAT_FILE, "w", encoding="utf-8") as file:
        file.write(encrypted_content)
    with open(CHAT_FILE, "rb") as file:
        ftp.storbinary(f"STOR {CHAT_FILE}", file)

    ftp.quit()


def read_messages():
    ftp_host = FTP_HOST.get()
    ftp_user = FTP_USER.get()
    ftp_pass = FTP_PASS.get()
    if not ftp_host or not ftp_user or not ftp_pass:
        messagebox.showerror("Error", "Please enter FTP credentials.")
        return

    ftp = FTP()
    ftp.connect(ftp_host)
    ftp.login(ftp_user, ftp_pass)

    try:
        with open(CHAT_FILE, "wb") as file:
            ftp.retrbinary(f"RETR {CHAT_FILE}", file.write)
        with open(CHAT_FILE, "r", encoding="utf-8") as file:
            content = file.read()
            if content:
                content = decrypt(content)
                chat_notes.config(state=NORMAL)
                chat_notes.delete("1.0", END)
                chat_notes.insert(END, content)
                chat_notes.config(state=DISABLED)
    except Exception:
        chat_notes.delete("1.0", END)
        chat_notes.insert(END, "No messages yet.")

    ftp.quit()


main = Window(themename="superhero")
main.title("TLock")
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
Label(main, text="FTP User:").place(x=5, y=32)
Entry(main, textvariable=FTP_USER, width=225).place(x=100, y=32)

FTP_PASS = StringVar()
Label(main, text="Password:").place(x=5, y=59)
Entry(main, textvariable=FTP_PASS, width=225, show="*").place(x=100, y=59)

username_var = StringVar()
Label(main, text="Username:").place(x=5, y=86)
Entry(main, textvariable=username_var, width=225).place(x=100, y=86)

chat_file_name = StringVar()
Label(main, text="Chat File:").place(x=5, y=112)
Entry(main, textvariable=chat_file_name, width=225).place(x=100, y=112)
CHAT_FILE = f"{chat_file_name.get()}.txt"

Label(main, text="Chat:").place(x=5, y=140)
chat_notes = scrolledtext.ScrolledText(main, width=233, height=17)
chat_notes.place(x=5, y=170)

Label(main, text="Message:").place(x=5, y=524)
msg = scrolledtext.ScrolledText(main, width=233, height=17)
msg.place(x=5, y=552)

Button(
    main,
    text="Send",
    command=lambda: send_message(username_var.get(), msg.get("1.0", END)),
    width=115,
).place(x=965, y=920)

Button(
    main,
    text="Read",
    command=read_messages,
    width=115,
).place(x=5, y=920)

main.mainloop()
