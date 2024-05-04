import random

import numpy as np
import math


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


def generate_superincreasing_sequence(lenght):
    current_sum = 0
    sequence = []
    for i in range(lenght):
        current_elem = current_sum + np.random.randint(1, 10)
        current_sum += current_elem
        sequence.append(current_elem)
    return sequence


def get_simple_with(number):
    for i in range(number - 1, 1, -1):
        if math.gcd(i, number) == 1:
            return i
    return 1


def knapsacks(n, t):
    a = np.zeros((t, n), dtype=np.int64)
    W = np.zeros(t, dtype=np.int64)
    M = np.zeros(t, dtype=np.int64)
    a[0] = generate_superincreasing_sequence(n)
    for i in range(1, t):
        M[i] = int(sum(a[i - 1]) + np.random.randint(1, 10))
        W[i] = get_simple_with(M[i])
        for j in range(n):
            a[i][j] = a[i - 1][j] * W[i] % M[i]
    pi = [i for i in range(n)]
    random.shuffle(pi)
    public_key = a[t - 1][pi]
    private_key = {"pi": pi, "M": M, "W": W, "a": a[0]}
    print(public_key, private_key)
    return np.asarray(public_key, dtype=int), private_key


def encryption(message, public_key):
    #print("Исходное", message)
    c = 0
    for i in range(len(message)):
        c += int(message[i]) * public_key[i]
    return c


def inv_W(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = inv_W(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
    return gcd, x, y


def knap_solve(private_key, d):
    result = [0 for i in range(len(private_key))]
    for i in range(len(private_key) - 1, -1, -1):
        if d - private_key[i] >= 0:
            d = d - private_key[i]
            result[i] = 1
    return result


def dectryption(c, private_key):
    W = private_key["W"]
    M = private_key["M"]
    d = np.zeros(len(W) + 1, dtype=int)
    d = c
    for i in range(len(W), 1, -1):
        _, inv_w, _ = inv_W(W[i - 1], M[i - 1])
        if inv_w < 0:
            inv_w += M[i - 1]
        d = inv_w * d % M[i - 1]
        while d > M[i - 1]:
            d %= M[i - 1]
    #print("Суммарный вес зашифрованного сообщения", d)

    res = knap_solve(private_key["a"], d)

    r = np.asarray(res, dtype=int)
    r = r[private_key["pi"]]
    r=''.join(list(np.asarray(r,dtype=str)))
    #print("Дешифрованное", r)

    return r


def main():
    # message =text_to_bits("h")
    # print("Исходное","h")
    # public_key, private_key = knapsacks(len(message), 3)
    # c = encryption(message, public_key)
    # d = dectryption(c, private_key)
    # d= text_from_bits(d)
    # print("После дешифрования",d)
    text=''
    with open("text.txt") as file:
        text=file.read()
    text_to_encrypt = list(text)
    # message = list(format(200, 'b'))
    message = []
    for i in range(len(text_to_encrypt)):
        message.append(text_to_bits(text_to_encrypt[i]))
    print("Исходное", text)
    public_key, private_key = knapsacks(len(message[0]), 3)
    c = []
    for i in range(len(text_to_encrypt)):
        c.append(encryption(message[i], public_key))
    d = []
    result = []
    print("Зашифрованный ::::::::",c)
    for i in range(len(text_to_encrypt)):
        d.append(dectryption(c[i], private_key))
        result.append(text_from_bits(d[i]))
    result = ''.join(result)
    print("После дешифрования ::::::", result)


if __name__ == "__main__":
    main()
