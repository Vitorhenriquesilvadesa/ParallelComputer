import numpy as np
import time


def generate_random_array(size):
    return np.random.randint(0, 100, size)


def reduce_serial(array):
    result = 0
    for value in array:
        result += value
    return result


def hillis_steele_scan(array):
    n = len(array)
    result = array.copy()
    steps = int(np.ceil(np.log2(n)))
    for step in range(steps):
        offset = 2 ** step
        temp_result = result.copy()
        for i in range(offset, n):
            temp_result[i] += result[i - offset]
        result = temp_result
    return result


def blelloch_scan(array):
    n = len(array)
    result = array.copy()

    offset = 1
    while offset < n:
        for i in range(offset, n, offset * 2):
            result[i + offset - 1] += result[i - 1]
        offset *= 2

    offset = n // 2
    while offset > 0:
        for i in range(offset, n, offset * 2):
            temp = result[i + offset - 1]
            result[i + offset - 1] = result[i - 1]
            result[i - 1] += temp
        offset //= 2

    return result


array_sizes = [100, 1000, 10000, 100000, 1000000, 10000000]

print("Teste para Reduce Serial:")
times_serial = []
for size in array_sizes:
    test_array = generate_random_array(size)
    start_time = time.time()
    reduce_serial(test_array)
    end_time = time.time()
    times_serial.append(end_time - start_time)
    print(f"Tamanho do array: {size}, Tempo de execução: {end_time - start_time:.6f} segundos")

print("\nTeste para Hillis-Steele:")
times_hillis_steele = []
for size in array_sizes:
    test_array = generate_random_array(size)
    start_time = time.time()
    hillis_steele_scan(test_array)
    end_time = time.time()
    times_hillis_steele.append(end_time - start_time)
    print(f"Tamanho do array: {size}, Tempo de execução: {end_time - start_time:.6f} segundos")

print("\nTeste para Blelloch:")
times_blelloch = []
for size in array_sizes:
    test_array = generate_random_array(size)
    start_time = time.time()
    blelloch_scan(test_array)
    end_time = time.time()
    times_blelloch.append(end_time - start_time)
    print(f"Tamanho do array: {size}, Tempo de execução: {end_time - start_time:.6f} segundos")
