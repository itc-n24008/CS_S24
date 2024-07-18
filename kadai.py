import os
import sys

MAX_VALUE = 2

print(sys.getdefaultencoding())
print(os.path.basename(os.getcwd()))

for i in range(3):
    print(i, end=" ")
    if MAX_VALUE > i:
        print(MAX_VALUE)
    else:
        print("#")
