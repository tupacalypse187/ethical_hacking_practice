import requests
import hashlib
# import os
# import argparse

with open('./password_file.txt', 'r') as file:
    passwords = file.readlines()
    # for pwd in passwords:
    #     print(pwd)
    for password in passwords:
        # MYHASH = "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8".upper()
        # password = "password"
        password = password.strip('\n')
        sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

        # url = f'https://api.pwnedpasswords.com/range/{MYHASH[:5]}'
        url = f'https://api.pwnedpasswords.com/range/{sha1password[:5]}'
        res = requests.get(url)
        if res.status_code != 200:
            print(res.status_code)
            raise RuntimeError(f'Error fetching: {res.status_code}, check the API docs.')
        # print(res.text)

        # print(sha1password[5:])
        if sha1password[5:] in res.text:
            for line in res.text.splitlines():
                if sha1password[5:] in line:
                    count = line.split(":")[1]
                    print(f"Your password '{password}' has been pwned {count} times. Time to get a new password.")
        else:
            print(f"Your password '{password}' has been pwned 0 times. That's a solid password. Don't tell anyone.")
