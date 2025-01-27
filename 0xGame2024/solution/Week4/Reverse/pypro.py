import base64
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes

key = 0x554B134A029DE539438BD18604BF114


def PKCS5_pad(data):
    if len(data) < 48:
        length = 48 - len(data)
        return data.ljust(48, length.to_bytes())


def main():
    cipher = AES.new(long_to_bytes(key, 16), AES.MODE_ECB)
    c = "2e8Ugcv8lKVhL3gkv3grJGNE3UqkjlvKqCgJSGRNHHEk98Kd0wv6s60GpAUsU+8Q"
    c = base64.b64decode(c.encode("utf-8"))
    m = cipher.decrypt(c)
    print(m.decode("utf-8"))


if __name__ == "__main__":
    main()
