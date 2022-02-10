import email
import smtplib, ssl
import re

# to add a dictionary (smtp settings) of popular email service like google or yahoo
# when user type in their email the program will check the email domain against the dictionary
# if the email domain is in the dictioinary then the program will prompt user of their password
# if the email domain is not in the dictionary then the program will inform user and ask them to retry

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def prompt_email():
    correct_email = False

    while not correct_email:
        r_email = input("Please input receiver's email: ")
        correct_email = validate_email_format(r_email)
        if correct_email == False:
            print("Error")
        else:
            correct_email = False
            break
    
    while not correct_email:
        s_email = input("Please input your email address: ")
        correct_email = validate_email_format(s_email)
        if correct_email == False:
            print("Error")
        else:
            break

    password = input("Please enter your email password : ")
    
    return r_email, s_email, password

def validate_email_format(email):
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

def main():
    r_email, s_email, password = prompt_email()
    print({r_email})
    print({s_email})
    print({password})

if __name__ == '__main__':
    main()