
import argparse
import base64
import secrets

def xor_encrypt(data: bytes, key: bytes) -> bytes:
    """Applies XOR encryption using a repeating key."""
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def encode_payload(input_path: str, output_path: str, key: str):
    """Reads a file, applies XOR + Base64, writes to output."""
    with open(input_path, 'rb') as f:
        raw_data = f.read()

    xor_key = key.encode()
    xored = xor_encrypt(raw_data, xor_key)
    encoded = base64.b64encode(xored)

    with open(output_path, 'wb') as f:
        f.write(encoded)

    print(f"[+] Payload encoded: {output_path}")

def decode_payload(input_path: str, output_path: str, key: str):
    """Reads XOR + Base64 obfuscated file, decodes to original."""
    with open(input_path, 'rb') as f:
        encoded_data = f.read()

    decoded = base64.b64decode(encoded_data)
    xor_key = key.encode()
    original = xor_encrypt(decoded, xor_key)

    with open(output_path, 'wb') as f:
        f.write(original)

    print(f"[+] Payload decoded: {output_path}")

def generate_key(length: int = 16):
    """Generates a secure random XOR key (hex format)."""
    key = secrets.token_hex(length)
    print(f"[+] XOR Key: {key}")
    return key

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Payload Obfuscator - XOR + Base64 Encoder/Decoder")
    parser.add_argument("mode", choices=["encode", "decode", "genkey"], help="Operation mode")
    parser.add_argument("--input", help="Path to input file")
    parser.add_argument("--output", help="Path to output file")
    parser.add_argument("--key", help="XOR key (hex or text)")

    args = parser.parse_args()

    if args.mode == "genkey":
        generate_key()
    elif args.mode == "encode":
        if not args.input or not args.output or not args.key:
            print("[-] Missing arguments for encode mode.")
        else:
            encode_payload(args.input, args.output, args.key)
    elif args.mode == "decode":
        if not args.input or not args.output or not args.key:
            print("[-] Missing arguments for decode mode.")
        else:
            decode_payload(args.input, args.output, args.key)
