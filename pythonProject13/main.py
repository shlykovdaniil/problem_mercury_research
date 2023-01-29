# # 1) среднее арифметическое соседних, score=68.4925
# file = open("data.csv", "r")
# lines = file.readlines()
# file.close()
# numbers_computed = []
# numbers_expected = []
# count = 0
# d = 0
# for line in lines:
#     stroka_computed = line.split(",")[1]
#     stroka_expected = line.split(",")[2].rstrip("\n").lower()
#     print(stroka_expected)
#     if "m" in stroka_expected:
#         count = count + 1
#         numbers_expected.append(0)
#     else:
#         numbers_expected.append(float(stroka_expected))
#     numbers_computed.append(float(stroka_computed))
# print(numbers_expected)
# print(numbers_computed)
# for _, nm in enumerate(numbers_expected):
#     if nm==0:
#         if _==0:
#             numbers_expected[_] = numbers_expected[_+1]
#         elif _ == len(numbers_expected) - 1:
#             numbers_expected[_] = numbers_expected[_-1]
#         else:
#             numbers_expected[_] = (numbers_expected[_+1]+numbers_expected[_-1])/2
#         d = d + abs((numbers_expected[_] - numbers_computed[_])/numbers_expected[_])*100
# d = d/count
# final_score = 50 * max(2-d, 0)
# print(final_score)

# 2) убираю все missing и вместо них ставлю рандомное число из массива в пределах стандартного отклонения - score=0
# import random
# import numpy as np
# file = open("data.csv", "r")
# lines = file.readlines()
# file.close()
# numbers_computed = []
# numbers_expected = []
# numbers_expected2 = []
# count = 0
# d = 0
# for line in lines:
#     stroka_computed = line.split(",")[1]
#     stroka_expected = line.split(",")[2].rstrip("\n").lower()
#     if "m" in stroka_expected:
#         count = count + 1
#         numbers_expected.append(0)
#     else:
#         numbers_expected.append(float(stroka_expected))
#         numbers_expected2.append(float(stroka_expected))
#     numbers_computed.append(float(stroka_computed))
# standard_deviation = np.std(numbers_expected2)
# for _, nm in enumerate(numbers_expected):
#     if nm==0:
#         # numbers_expected[_] = random.choice(numbers_expected2) + standard_deviation
#         numbers_expected[_] = random.choice(numbers_expected2) + random.uniform(0, float(standard_deviation))
#     d = d + abs((numbers_expected[_] - numbers_computed[_])/numbers_expected[_])*100
# print(numbers_expected)
# print(numbers_computed)
# d = d/count
# final_score = 50 * max(2-d, 0)
# print(final_score)


# 3) убираю все missing и вместо них ставлю среднее число из массива в пределах стандартного отклонения - score=0
# import statistics
# import numpy as np
# file = open("data.csv", "r")
# lines = file.readlines()
# file.close()
# numbers_computed = []
# numbers_expected = []
# numbers_expected2 = []
# count = 0
# d = 0
# for line in lines:
#     stroka_computed = line.split(",")[1]
#     stroka_expected = line.split(",")[2].rstrip("\n").lower()
#     if "m" in stroka_expected:
#         count = count + 1
#         numbers_expected.append(0)
#     else:
#         numbers_expected.append(float(stroka_expected))
#         numbers_expected2.append(float(stroka_expected))
#     numbers_computed.append(float(stroka_computed))
# standard_deviation = np.std(numbers_expected2)
# for _, nm in enumerate(numbers_expected):
#     if nm==0:
#         numbers_expected[_] = statistics.mean(numbers_expected2) + standard_deviation
#     d = d + abs((numbers_expected[_] - numbers_computed[_])/numbers_expected[_])*100
# print(numbers_expected)
# print(numbers_computed)
# d = d/count
# final_score = 50 * max(2-d, 0)
# print(final_score)

# 4) среднее геометрическое соседних, scor=68.4538
# file = open("data.csv", "r")
# lines = file.readlines()
# file.close()
# numbers_computed = []
# numbers_expected = []
# count = 0
# d = 0
# for line in lines:
#     stroka_computed = line.split(",")[1]
#     stroka_expected = line.split(",")[2].rstrip("\n").lower()
#     if "m" in stroka_expected:
#         count = count + 1
#         numbers_expected.append(0)
#     else:
#         numbers_expected.append(float(stroka_expected))
#     numbers_computed.append(float(stroka_computed))
# print(numbers_expected)
# print(numbers_computed)
# for _, nm in enumerate(numbers_expected):
#     if nm==0:
#         if _==0:
#             numbers_expected[_] = numbers_expected[_+1]
#         elif _ == len(numbers_expected) - 1:
#             numbers_expected[_] = numbers_expected[_-1]
#         else:
#             numbers_expected[_] = (numbers_expected[_+1]*numbers_expected[_-1])**(1/2)
#         d = d + abs((numbers_expected[_] - numbers_computed[_])/numbers_expected[_])*100
# d = d/count
# final_score = 50 * max(2-d, 0)
# print(final_score)