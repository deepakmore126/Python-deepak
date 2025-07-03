import random

count_1 = 0
count_2 = 0
for i in range(10000):
    num = random.random()
    #print(f"random {i+1}: {num}")
    if(num <= 0.5):
        count_1 = count_1 + 1
    else:
        count_2 = count_2 + 1
    print(count_1)
    print(count_2)
