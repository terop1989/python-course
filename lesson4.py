dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
new_dict = {}

for k, v in dict.items():
    if v >= 3 :
        new_dict[k] = v

print(new_dict)