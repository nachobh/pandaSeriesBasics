import numpy as np
import pandas as pd


def compute(elements):
    x = elements[0:5]
    print(x)
    print(type(x))
    print(pd.Series(x))
    ser = pd.Series(x, [200, 201, 202, 203, 204], str, "Alphabets")
    print(ser)
    map_ser = pd.Series({1: 1, 2: 4, 3: 9, 4: 16}, [1, 2, 4, 5, 6], str, "Squares")
    print(map_ser)
    another_series = pd.Series(1, [0, 1, 2, 3, 4])
    print(pd.DataFrame(another_series, [0, 1, 2, 3, 5], [3]))
    another_series2 = pd.Series([[0, 0], [1, 1], [2, 4], [9, 27], [16, 64]], [0, 1, 2, 3, 4])
    print(pd.DataFrame(another_series2, [0, 1, 2, 3]))
    another_series3 = [[0, 0], [1, 1], [4, 8], [9, 27], [16, 64]]
    print(pd.DataFrame(another_series3, [0, 1, 2, 3, 4], ["^2", "^3"]))
    super_series = {"Name:": ["name1", "name2"], "Age": [33, 34]}
    print(super_series)
    print(pd.DataFrame(super_series, [1, 2]))
    print(pd.DataFrame(super_series, ["name1", "name2"], ["Number", "Age"]))


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    inputs = np.array(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    compute(inputs)
