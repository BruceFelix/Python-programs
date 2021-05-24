from verify_email import verify_email
email = input("Enter email to verify: ")

if verify_email(email):
    print("Yes, This is a Valid email address")
else:
    print("No this is not valid")