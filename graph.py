import matplotlib.pyplot as plt

labels = ["Without Migration", "With Migration"]
values = [7, 3]

plt.bar(labels, values)
plt.ylabel("Time (seconds)")
plt.title("ServerlessLLM Improvement")
plt.show()