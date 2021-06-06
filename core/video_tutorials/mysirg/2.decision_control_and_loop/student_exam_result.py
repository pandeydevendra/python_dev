SUBJECTS = ["Hindi", "English", "Maths", "Physics", "Chemistry"]
TOTAL_MARKS = 500


def get_grade(percent):
    """

    @param percent: float
    @return: str
    """
    grade = []
    if percent >= 60:
        grade = "1st"
    elif 45 <= percent < 60:
        grade = "2nd"
    elif percent >= 30:
        grade = "3rd"
    else:
        grade = "4rth"
        print("It should fall in FAILED category..")
    return grade


def get_result(marks_data):
    total_obtained_marks = sum(marks_data)
    percentage = total_obtained_marks * 100 / TOTAL_MARKS
    grade = get_grade(percentage)
    print(total_obtained_marks, percentage, grade)

marks_sheet = []
for subject in SUBJECTS:
    marks = int(input(f"Enter marks obtained in {subject}: "))
    marks_sheet.append(marks)

i = 0
for mark in marks_sheet:
    if mark < 30:
        print("FAIL")
        break
else:
    get_result(marks_sheet)
    print("PASS")
