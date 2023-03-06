def avg(marks):
    return sum(marks) / len(marks)


def grade(average):
    if average >= 80:
        return "A"
    elif 60 <= average < 80:
        return "B"
    elif 50 <= average < 60:
        return "C"
    elif average < 50:
        return "F"


marks = [55, 64, 75, 80, 65, 69]
for i in marks:
    print(f"{marks[i]} {grade(marks[i])}")
print("Average:", avg(marks), ", Grade:", grade(avg(marks)))
