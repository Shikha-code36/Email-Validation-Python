
email = input("Enter Your Email: ")
i=0
j=0
k=0

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for mail in email:
                    if mail == mail.isspace():
                        i = 1
                    elif mail.isalpha():
                        if mail == mail.upper():
                            j = 1
                    elif mail.isdigit():
                        continue
                    elif mail == "_" or mail == "." or mail == "@":
                        continue
                    else:
                        k = 1
                    if i == 1 or j == 1 or k == 1:
                        print(
                            "Wrong Email: You might have spaces or other condition not correct")
                    else:
                        print("Email Validated!")
            else:
                print("Wrong Email: Check email and type again")
        else:
            print("Wrong Email: Check email and type again")
    else:
        print("Wrong Email: Check email and type again")
else:
    print("Wrong Email: Check email and type again")
