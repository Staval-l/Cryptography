import math
import scipy
import numpy as np


def read_all(path_to_sequence, path_to_pi, path_to_exp):
    with open(path_to_sequence, 'r') as f:
        sequence = f.read(1000000)
    with open(path_to_pi, 'r') as f:
        pi = f.read(1000000)
    with open(path_to_exp, 'r') as f:
        exp = f.read(1000000)
    return sequence, pi, exp


def universal_statistical(input):
    L = 7
    nblocks = int(math.floor(len(input) / L))
    Q = 10 * (2 ** L)
    K = nblocks - Q
    nsymbols = (2 ** L)
    T = [0 for x in range(nsymbols)]
    for i in range(0, Q):
        pattern = input[i * L:(i + 1) * L]
        idx = int(pattern, 2)
        T[idx] = i + 1
    sum = 0
    for i in range(Q, nblocks):
        pattern = input[i * L:(i + 1) * L]
        j = int(pattern, 2)
        dist = i + 1 - T[j]
        T[j] = i + 1
        sum = sum + math.log(dist, 2)
    f_n = sum / K
    expectedValue = 6.1962507
    variance = 3.125
    mag = abs((f_n - expectedValue) / (
            (0.7 - (0.8 / L) + (4 + 32 / L) * ((pow(K, -3 / L)) / 15)) * (math.sqrt(variance / K) * math.sqrt(2))))
    p_val = scipy.special.erfc(mag)
    if p_val < 0.01:
        print(f"P-value = {p_val}")
        print("Последовательность неслучайна! Тест не пройден")

    else:
        print(f"P-value = {p_val}")
        print("Последовательность случайна! Тест пройден")


def cumulative_sums(sequence, mode=0):
    seq = []
    n = len(sequence)
    for i in range(len(sequence)):
        seq.append(2 * int(sequence[i]) - 1)
    if mode == 1:
        seq.reverse()
    cum_sum = np.cumsum(seq)
    z = np.max(abs(cum_sum))
    sum_a = 0.0
    k_start = int(math.floor((((-n / z) + 1.0) / 4.0)))
    k_end = int(math.floor((((n / z) - 1.0) / 4.0)))
    for k in range(k_start, k_end + 1):
        c = (((4.0 * k) + 1.0) * z) / math.sqrt(n)
        first = scipy.stats.norm.cdf(c)
        c = (((4.0 * k) - 1.0) * z) / math.sqrt(n)
        second = scipy.stats.norm.cdf(c)
        sum_a = sum_a + first - second
    sum_b = 0.0
    k_start = int(math.floor((((-n / z) - 3.0) / 4.0)))
    k_end = int(math.floor((((n / z) - 1.0) / 4.0)))
    for k in range(k_start, k_end + 1):
        c = (((4.0 * k) + 3.0) * z) / math.sqrt(n)
        first = scipy.stats.norm.cdf(c)
        c = (((4.0 * k) + 1.0) * z) / math.sqrt(n)
        second = scipy.stats.norm.cdf(c)
        sum_b = sum_b + first - second
    p_val = 1.0 - sum_a + sum_b
    if p_val < 0.01:
        print(f"P-value = {p_val}")
        print("Последовательность неслучайна! Тест не пройден")

    else:
        print(f"P-value = {p_val}")
        print("Последовательность случайна! Тест пройден")


def random_excursions_variant(sequence):
    seq = []
    for i in range(len(sequence)):
        seq.append(2 * int(sequence[i]) - 1)
    s = np.cumsum(seq)
    s = np.append(s, 0)
    s = np.insert(s, 0, 0)
    states = np.arange(1, 10)
    neg_states = -1 * states
    table = dict.fromkeys(np.concatenate((states, neg_states)), 0)
    J = np.count_nonzero(s == 0) - 1
    for key in table.keys():
        table[key] = np.count_nonzero(s == key)
    for key, value in table.items():
        p_val = math.erfc(np.abs(value - J) / np.sqrt(2 * J * (4 * np.abs(key) - 2)))
        print(f"Значение P-value для {key}: {p_val}")
        if p_val < 0.01:
            print(f"P-value = {p_val}")
            print("Последовательность неслучайна! Тест не пройден")
        else:
            print(f"P-value = {p_val}")
            print("Последовательность случайна! Тест пройден")


def main():
    path_to_sequence = r"C:\Users\vodnyy\PycharmProjects\crypta\1.txt"
    path_to_pi = r"C:\Users\vodnyy\PycharmProjects\crypta\data.pi"
    path_to_exp = r"C:\Users\vodnyy\PycharmProjects\crypta\data.e"
    sequence, pi, exp = read_all(path_to_sequence, path_to_pi, path_to_exp)
    # universal_statistical(sequence)
    # universal_statistical(pi)
    # universal_statistical(exp)
    # cumulative_sums(sequence)
    # cumulative_sums(pi)
    # cumulative_sums(exp)
    # cumulative_sums(pi, 1)
    # cumulative_sums(exp, 1)
    # random_excursions_variant(sequence)
    # random_excursions_variant(pi)
    # random_excursions_variant(exp)


if __name__ == '__main__':
    main()
