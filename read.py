import os

username = os.getenv('USERNAME_ENV')
password = os.getenv('PASSWORD_ENV')

print(username)
print(password)

if username == 'admin':
    print('valir')
else:
    print('invalid')
