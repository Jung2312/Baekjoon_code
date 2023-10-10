dict_li = {
    "A+": 4.5,
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "D+": 1.5,
    "D": 1.0,
    "F": 0.0,
}

grade = input()

for k, v in dict_li.items():
    grade = grade.replace(k, (str(v) + " "))

avg = list(map(float, grade.split()))

print(sum(avg) / len(avg))
