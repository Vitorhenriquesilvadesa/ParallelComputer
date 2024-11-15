import time
from Algorithms.RadixSort import generate_random_array
from RadixSort import radix_sort

if __name__ == '__main__':
    test_length = [100, 1000, 10000, 100000, 1000000, 10000000]

    for length in test_length:
        values = generate_random_array(length, 1 << 31)

        start = time.time()
        sorted_values = radix_sort(values).tolist()
        end = time.time()

        print(f'Length: {length} | Time: {(end - start):.4f} seconds')
