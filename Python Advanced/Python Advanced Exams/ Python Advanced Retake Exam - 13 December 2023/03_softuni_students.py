def softuni_students(*args, **kwargs):
    students_data = {}
    courses_data = {}
    invalid_students = []

    for arg in args:
        course_id, username = arg
        students_data[username] = course_id

    for key, value in kwargs.items():
        courses_data[key] = value

    result = ""

    if students_data:

        sorted_students = sorted(students_data.keys())

        for username in sorted_students:
            course_id = students_data[username]
            if course_id in courses_data:
                result += f"*** A student with the username {username} has successfully finished the " \
                          f"course {courses_data.get(course_id)}!\n"
            else:
                invalid_students.append(username)

    if invalid_students:
        result += f"!!! Invalid course students: {', '.join(sorted(invalid_students))}\n"

    return result.strip()













