data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 102, 108
        ]
    
min_valid = 100
max_valid = 200

# for index in range(len(data) - 1, -1, -1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data)
#         del data[index]

for index, value in enumerate(reversed(data)):
    print(index, value)

print(data)