import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# Smallest number in line 1 is 5, largest is 20
# Smallest number in line 1 is 3, largest is 9, line 2 couldn't produce a 4
# Smallest number I have seen is 2.669010466739309, largest is 5.3518785695962928

print(random.uniform(1, 100))
