# input
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# output :
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ
def wrap(string, max_width):
    counter = 0
    wrapped_str = ""
    for i in string:
        if counter == max_width:
            counter = 0
            wrapped_str = wrapped_str + "\n"
        wrapped_str = wrapped_str + i
        counter = counter + 1
    return wrapped_str


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
