import timeit
from collections import defaultdict

def xor(data1, data2):
    return [x ^ y for x, y in zip(data1, data2)]

def xor2(data1, data2):
    for i in range(len(data1)):
        data1[i] ^= data2[i]
    return data1   
def xor3(data1, data2):
    res = defaultdict(int)
    for i in range(len(data1)):
        res[i] = data1[i] ^ data2[i]
    return res

# Prepare some data
data1 = [1, 2, 3, 4, 5] * 100000
data2 = [6, 7, 8, 9, 10] * 100000

# Time the function
start_time = timeit.default_timer()
res = xor(data1, data2)
end_time = timeit.default_timer()

# Print the time taken
print(f"Time taken: {end_time - start_time} seconds")

# Initialize a list to store the times
times = []

# Run the function 10 times
for _ in range(10):
    start_time = timeit.default_timer()
    xor3(data1, data2)
    end_time = timeit.default_timer()
    times.append(end_time - start_time)

# Print the time taken for each run
for i, time_taken in enumerate(times, 1):
    print(f"Time taken in run {i}: {time_taken} seconds")

# Calculate and print the average time
average_time = sum(times) / len(times)
print(f"Average time taken: {average_time} seconds")