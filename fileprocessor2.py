#!/usr/bin/python3

import sys

user_data = []

for line in sys.stdin:
    line = line.strip()

    if line.startswith('#'):
        continue

    user_info = line.split(':')

    if len(user_info) >= 4:
        username = user_info[0]
        password = user_info[1]
        userid = user_info[2]
        groupid = user_info[3]

        user_data.append({
            'username': username,
            'password': password,
            'userid': userid,
            'groupid': groupid
        })
    else:
        print(f"Skipping invalid line: {line}")


print("Printing out User Data:")
for user in user_data:
    print(f"The user {user['username']} has a password of {user['password']} and has userid {user['userid']} and groupid {user['groupid']}")

print("End of User Data")

