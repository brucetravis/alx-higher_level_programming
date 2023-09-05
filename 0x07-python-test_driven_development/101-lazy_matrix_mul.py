#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    try:
        np_a = np.array(m_a)
        np_b = np.array(m_b)
        result = np.dot(np_a, np_b)
        return result.tolist()  # Convert the result back to a nested list
    except (ValueError, TypeError):
        raise ValueError("m_a and m_b can't be multiplied")

# Example usage
if __name__ == "__main__":
    m1 = [[1, 2], [3, 4]]
    m2 = [[1, 2], [3, 4]]
    result = lazy_matrix_mul(m1, m2)
    print(result)
