import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [1, 3, 6, 10]

plt.plot(x, y1, label="expence")
plt.plot(x, y2, label="income")
plt.legend(loc="upper left")  # Add legend at the top-left corner
plt.grid()
plt.title('ultimate')
plt.show()
