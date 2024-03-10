import sys
import re


def reed_text(path: str):
    with open(path, 'r') as f:
        text = f.read()
    return text


def write_text(path: str, text: str):
    with open(path, 'w') as f:
        f.write(text)


def check_key(key: str, frst_key_len: int, scnd_key_len: int):
    key_pattern = r'^[\d\s]+$'
    if key.count('\n') != 1:
        sys.exit("Неверный ключ")
    key = key.split('\n')
    if key[0].count(' ') != frst_key_len - 1 or re.search(key_pattern, key[0]) is None:
        sys.exit("Неверный ключ")
    elif key[1].count(' ') != scnd_key_len - 1 or re.search(key_pattern, key[1]) is None:
        sys.exit("Неверный ключ")


def permutation_encrypt(text: str, key: str):
    key = key.split(' ')
    output_text = ''
    if len(text) % len(key) != 0:
        text += text[0:(len(key) - (len(text) % len(key)))]
    for i in range(0, len(text), len(key)):
        block = text[i:i + len(key)]
        crypt_block = ''
        for j in range(1, len(block) + 1):
            crypt_block += block[key.index(str(j))]
        output_text += crypt_block
    return output_text


def permutation_decrypt(encrypt_text: str, key: str):
    key = key.split(' ')
    output_text = ''
    for i in range(0, len(encrypt_text), len(key)):
        block = encrypt_text[i:i + len(key)]
        decrypt_block = ''
        for j in range(0, len(block)):
            decrypt_block += block[int(key[j]) - 1]
        output_text += decrypt_block
    return output_text


def encrypt(text: str, key: str):
    encrypt_text = text
    key = key.split('\n')
    for i in range(len(key)):
        encrypt_text = permutation_encrypt(encrypt_text, key[i])
    return encrypt_text


def decrypt(text: str, key: str):
    decrypt_text = text
    key = key.split('\n')
    for i in range(len(key)-1, 1):
        decrypt_text = permutation_decrypt(decrypt_text, key[i])
    return decrypt_text


def main():
    text = reed_text('text.txt')
    key = reed_text('key.txt')
    check_key(key, 5, 3)
    write_text('encrypt.txt', encrypt(text, key))
    write_text('decrypt.txt', decrypt(text, key))
    # print(encrypt(text, key))
    # print(decrypt(text, key))


if __name__ == '__main__':
    main()
