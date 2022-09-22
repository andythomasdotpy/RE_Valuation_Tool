import random
from math import floor, ceil

#Constant Percent to Filter
FILTER_PERCENT = .2

#Data
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
print(my_list)

#Randomize Data for Testing
random.shuffle(my_list)
print(my_list)

#How Many to Filter
#If total number in dataset is less than 20, round down to filter less
if len(my_list) < 20:
    filter_how_many = floor(len(my_list) * FILTER_PERCENT)
    print(f"Filter the top and bottom {filter_how_many}")

#If total number in dataset is 20 or more, round up to filter more
else:
    filter_how_many = ceil(len(my_list) * FILTER_PERCENT)
    print(f"Filter the top and bottom {filter_how_many}")

#Sort List
sorted_list = []
for i in range(len(my_list)):
    if len(sorted_list) == 0:
        sorted_list.append(my_list[i])
    else:
        for n in range(len(sorted_list)):
            if my_list[i] > sorted_list[n]:
                if n == (len(sorted_list) - 1):
                    sorted_list.append(my_list[i])
            elif my_list[i] < sorted_list[n]:
                sorted_list.insert(n, my_list[i])
                break

print(sorted_list)

filtered_sorted_list_front = sorted_list[filter_how_many:]
print(filtered_sorted_list_front)

filtered_sorted_list_back = filtered_sorted_list_front[:-filter_how_many]
print(len(my_list), len(filtered_sorted_list_back), filtered_sorted_list_back)