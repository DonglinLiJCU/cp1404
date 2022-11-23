"""
Word Occurrences
Estimate: 5 minutes
Actual:   4 minutes
"""

text = input("Text: ")
res = text.split(' ')
my_dict = dict()
out = []
max_len = -1
for i in res:
    if i not in my_dict:
        my_dict[i] = 1
        if len(i) > max_len:
            max_len = len(i)
    else:
        my_dict[i] += 1

for item in my_dict.items():
    out.append(f"{item[0]:{max_len}} : {item[1]}")

out.sort()
for i in out:
    print(i)