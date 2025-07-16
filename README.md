Payload Obfuscator – XOR + Base64 Hybrid

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

## Usage

Generate a secure XOR key:

    python obfuscator.py genkey

Encode a file:

    python obfuscator.py encode --input ../samples/payload.txt --output ../outputs/encoded.b64 --key deadbeef

Decode the file:

    python obfuscator.py decode --input ../outputs/encoded.b64 --output ../outputs/decoded.txt --key deadbeef

---

## Notes

This tool is intended for red team development, detection testing, and educational purposes.  
Do not use in unauthorized environments.
