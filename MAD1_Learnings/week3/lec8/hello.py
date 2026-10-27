# print("you are in file => hello.py")
# name = input('enter your name: ')
# print("hello", name)

import sys

print("प्रोग्राम का नाम:", sys.argv[0])
print("पहला पैरामीटर:", sys.argv[1])
print("दूसरा पैरामीटर:", sys.argv[2])
print(len(sys.argv))