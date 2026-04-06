without_migration = 7
with_migration = 3

print("Without migration:", without_migration, "seconds")
print("With migration:", with_migration, "seconds")

improvement = without_migration / with_migration

print("Improvement:", round(improvement, 2), "x faster")