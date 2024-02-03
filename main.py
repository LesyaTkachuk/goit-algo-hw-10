import scipy.integrate as spi

from task_1.maximize_productivity import maximize_productivity
from task_2.find_integral_mc import find_integral_mc
from task_2.draw_graph import func, a, b


def main():
    print("-" * 70)
    # task 1
    maximize_productivity()

    print("-" * 70)
    # task 2
    # define integral with Monte-Carlo method using 1_000 points
    result = find_integral_mc(func, a, b, 1_000)
    print("Integral value using Monte-Carlo method (1_000 points): ", result)  # 35.9856

    # define integral with Monte-Carlo method using 100_000 points
    result = find_integral_mc(func, a, b, 100_000)
    print(
        "Integral value using Monte-Carlo method (100_000 points): ", result
    )  # 36.105696

    # check the integral value using scipy library
    result, error = spi.quad(func, a, b)
    print("Integral value using scipy library method: ", result)  # 38.99999999999999
    print("-" * 70)


if __name__ == "__main__":
    main()
