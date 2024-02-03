import matplotlib.pyplot as plt
import numpy as np


# function definition
def func(x):
    return 4 * x**3 - 2 * x**2 + 2 * x + 9


# integration boundaries
a = -1  # lower boundary
b = 2  # upper boundary

# x values range creation
x = np.linspace(a, b, 100)

y = func(x)

# graph creation
fig, ax = plt.subplots()

# draw the function y
ax.plot(x, y, color="blue", linewidth=2)

# fill the area under the function curve
fill_x = np.linspace(a, b)
fill_y = func(fill_x)
ax.fill_between(fill_x, fill_y, color="yellow", alpha=0.3)

# add boundaries
ax.axvline(x=a, color="gray", alpha=0.5, linestyle="--")
ax.axvline(x=b, color="gray", alpha=0.5, linestyle="--")


# add labels and title
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title(
    f"Integration graph for f(x)=4x^3 - 2x^2 + 2x + 9 in range from {a} to {b}"
)

# draw the graph
plt.grid()
plt.show()
