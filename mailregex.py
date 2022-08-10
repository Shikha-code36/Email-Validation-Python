'''
Conditions:
a-z test@gmail.com
0-9
'.''_'time.1
.@. time.1
'.' 2,3
'''

import re
email_conditions = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email= input("Enter Your Email Address:")

if re.search(email_conditions,user_email):
    print("Email is Verified")
else:
    print("Email is incorrect! Kindly check")