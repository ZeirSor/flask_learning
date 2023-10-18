import sys


args = sys.argv


def add():
    print('add')

def delete():
    print('delete')

def modify():
    print('modify')


func_dict = {
    "add": add,
    "del": delete,
    "modify": modify
}

print(len(args), args)


for i in range(1, len(args)):
    func_dict[args[i]]()