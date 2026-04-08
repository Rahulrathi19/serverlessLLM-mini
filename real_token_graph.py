import matplotlib.pyplot as plt

tokens = [1, 2, 3, 4, 5]
times = [0.6, 1.1, 1.6, 2.1, 2.6]

plt.plot(tokens, times, marker="o")

plt.xlabel("Token Number")
plt.ylabel("Time (seconds)")
plt.title("Real Token vs Time")

plt.show()