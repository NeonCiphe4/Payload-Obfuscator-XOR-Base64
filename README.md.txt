----------------------------------------------
Filename: README.md
----------------------------------------------

# Payload Obfuscator – XOR + Base64 Hybrid

Status: In Progress  
Version: v0.1  
Created: July 2025

---

## Overview

This tool performs hybrid payload obfuscation using XOR encryption followed by Base64 encoding. It supports both encoding and decoding of arbitrary binary files or payloads.

It is designed to simulate real-world red team obfuscation workflows and AV evasion behavior during file delivery or staging operations.

---

## Features

- XOR encryption with user-defined or randomly generated key
- Base64 encoding layered on top of XOR
- Works on any file type: .exe, .ps1, .sh, .txt, shellcode, etc.
- Command-line interface for fast integration
- Decoder restores full original content

---

## MITRE ATT&CK Techniques

| Technique Name                      | ID     |
|------------------------------------|--------|
| Obfuscated Files or Information    | T1027  |
| Deobfuscate/Decode Files or Info   | T1140  |

---

## Project Structure

Payload-Obfuscator-XOR-Base64/
├── scripts/
│   └── obfuscator.py  
├── samples/
│   └── payload.txt  
├── outputs/
│   ├── encoded.b64  
│   └── decoded.txt  
├── screenshots/
│   └── demo_encode_decode.png  
└── README.md  

---

## Usage

Generate a secure XOR key:

    python obfuscator.py genkey

Encode a file:

    python obfuscator.py encode --input ../samples/payload.txt --output ../outputs/encoded.b64 --key deadbeef

Decode the file:

    python obfuscator.py decode --input ../outputs/encoded.b64 --output ../outputs/decoded.txt --key deadbeef

---

## Screenshot Example

Screenshot usage demonstration:  
`screenshots/demo_encode_decode.png`

---

## Notes

This tool is intended for red team development, detection testing, and educational purposes.  
Do not use in unauthorized environments.