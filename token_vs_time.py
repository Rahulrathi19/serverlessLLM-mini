import matplotlib.pyplot as plt

user_token_times = {
    "user1": [1, 2, 3, 4],
    "user2": [1.5, 2.8, 4.1, 5.3],
    "user3": [2, 4, 6, 8],
    "user4": [3, 5, 7, 10]
}

for user, times in user_token_times.items():

    tokens = [1, 2, 3, 4]

    plt.plot(tokens, times, marker="o", label=user)

plt.xlabel("Token Number")
plt.ylabel("Time (seconds)")
plt.title("Token vs Time for Multiple Users")
plt.legend()

plt.show()