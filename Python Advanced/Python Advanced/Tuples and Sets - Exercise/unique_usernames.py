usernames_count = int(input())



all_usernames = set()

for _ in range(usernames_count):
    username = input()

    all_usernames.add(username)

print(*all_usernames, sep="\n")