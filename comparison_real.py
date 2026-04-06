import time

start = time.time()

# simulate without migration
time.sleep(7)

without_migration = time.time() - start

start = time.time()

# simulate with migration
time.sleep(3)

with_migration = time.time() - start

print("Without migration:", round(without_migration, 2), "seconds")
print("With migration:", round(with_migration, 2), "seconds")

improvement = without_migration / with_migration

print("Improvement:", round(improvement, 2), "x faster")