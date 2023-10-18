from os.path import *

ABS_PATH = abspath(__file__)
BASE_PATH = dirname(ABS_PATH)
BASE_BASE_PATH = dirname(BASE_PATH)
BASE_BASE_BASE_PATH =  dirname(BASE_BASE_PATH)

print(ABS_PATH)
print(BASE_PATH)
print(BASE_BASE_PATH)
print(BASE_BASE_BASE_PATH)
# print(dirname(BASE_BASE_BASE_PATH))