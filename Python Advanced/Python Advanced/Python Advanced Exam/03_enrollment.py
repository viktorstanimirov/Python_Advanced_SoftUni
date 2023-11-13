def gather_credits(credits_need, *args):
    total_credits = 0
    passed_course = []

    for el in args:

        if total_credits >= credits_need:
            break

        if el[0] not in passed_course:
            total_credits += el[1]
            passed_course.append(el[0])

        else:
            continue


    if credits_need > total_credits:
        total_credits = credits_need - total_credits
        return f"You need to enroll in more courses! You have to gather {total_credits} credits more."

    elif credits_need <= total_credits:

        return f"Enrollment finished! Maximum credits: {total_credits}.\n" \
               f"Courses: {', '.join(sorted(passed_course))}"

# print(gather_credits(
#     60,
#     ("Basics", 27),
#     ("Basics", 27),
#     ("Aaundamentals", 27),
#     ("Advanced", 30),
#     ("Aandamentals", 27),
#     ("Web", 30)
#
# ))
