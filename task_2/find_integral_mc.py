import numpy as np
import matplotlib.pyplot as plt


def find_integral_mc(func, x_min, x_max, num_points, show_points=True):
    y_min = func(x_min)
    y_max = func(x_max)

    # random points generation
    x = np.random.uniform(x_min, x_max, num_points)
    y = np.random.uniform(y_min, y_max, num_points)

    # points that targeted under the function curve
    under_curve = y < func(x)

    # find an area
    area = (x_max - x_min) * (y_max - y_min) * np.sum(under_curve) / num_points

    def draw_points():
        plt.figure(figsize=(8, 8))
        plt.scatter(x[under_curve], y[under_curve], color="blue", s=1)
        plt.scatter(x[~under_curve], y[~under_curve], color="red", s=1)
        plt.show()

    if show_points:
        draw_points()

    return area
