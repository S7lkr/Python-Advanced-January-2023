def students_credits(*args):
    students_data = {}
    total_credits = 0
    result = []

    for data in (", ".join(args)).split(", "):
        subject, *info = data.split("-")
        students_data[subject] = int(info[0]) * (int(info[2]) / int(info[1]))
        total_credits += students_data[subject]

    result = '\n'.join([f"{key} - {value:.1f}" for key, value in sorted(students_data.items(), key=lambda x: -x[1])])

    if total_credits >= 240:
        return f"Diyan gets a diploma with {total_credits:.1f} credits.\n{result}"
    diff = 240 - total_credits
    return f"Diyan needs {diff:.1f} credits more for a diploma.\n{result}"


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)