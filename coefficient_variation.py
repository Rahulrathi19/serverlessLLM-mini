import numpy as np
import matplotlib.pyplot as plt

user_ttft = {
    "user1": [1.0, 1.1, 0.9, 1.0],
    "user2": [2.0, 2.5, 2.2, 2.4],
    "user3": [4.0, 5.5, 4.8, 5.2],
    "user4": [6.0, 7.5, 6.8, 7.2]
}

cv_values = {}

for user, values in user_ttft.items():

    mean = np.mean(values)
    std = np.std(values)

    cv = std / mean
    cv_values[user] = round(cv, 2)

print(cv_values)

plt.bar(cv_values.keys(), cv_values.values())

plt.xlabel("Users")
plt.ylabel("Coefficient of Variation")
plt.title("TTFT Variability Across Users")

plt.show()