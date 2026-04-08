import matplotlib.pyplot as plt

users = ["user1", "user2", "user3", "user4"]
ttft = [1.2, 2.1, 3.4, 4.0]

plt.bar(users, ttft)

plt.xlabel("Users")
plt.ylabel("TTFT (seconds)")
plt.title("Real Multi-User TTFT")

for i, value in enumerate(ttft):
    plt.text(i, value + 0.1, str(value))

plt.show()