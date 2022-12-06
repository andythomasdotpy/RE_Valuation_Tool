# lamda_var = lambda x: x + 1
# print(lamda_var(6))
#
# for i in range(10):
#     print(lamda_var(i+1))

# x = { 1: 2,   6: 4,   5: 3}
#   ((0, 1), (0, 1), (0, 1))

x = {1: {2: 10, 9: 20}, 6: {4: 19, 5: 30}, 4: {7: 12, 8: 50}}
#   (0,((0,  1),0,  1), 0, (0,  1),   0, (  0,     1))

print(dict(sorted(x.items(), key=lambda item: item[0][1])))



