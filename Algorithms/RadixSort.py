import numpy as np

def generate_random_array(size, max_value):
    return np.random.randint(0, max_value, size)

def radix_sort(values: np.ndarray) -> np.ndarray:
    max_bits = int(values.max()).bit_length()

    for i in range(max_bits):
        mask = (values >> i) & 1
        zero_bucket = values[mask == 0]
        one_bucket = values[mask == 1]
        values = np.concatenate((zero_bucket, one_bucket))

    return values
