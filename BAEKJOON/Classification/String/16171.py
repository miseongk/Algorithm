s = input()
k = input()
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for value in s:
    if value in number:
        s = s.replace(value, "")

if k in s:
    print(1)
else:
    print(0)
