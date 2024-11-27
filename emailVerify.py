import re

email_condition = re.compile(r'[a-z]+[\._]?+[a-z 0-9]+[@]\w+[.]{2,3}$')
user_email = input('enter your email: ')
if re.search(email_condition,user_email):
    print('right email')
else:
    print('right email')