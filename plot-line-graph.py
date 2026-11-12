import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5, 6]
y = [10, 15, 13, 18, 16, 20]

plt.plot(x, y, marker='o', linestyle='-', color='blue', label="Sales")

plt.title("Sales Over Time")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)

plt.show()
