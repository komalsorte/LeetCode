def prefixString(a,b):
    items = dict()
    string_s = ''
    new_string = ''
    flag = False
    for j in range(len(a)):
        if string_s == '':
            string_s = a[j]
        else:
            string_s = string_s + a[j]
            items[string_s] = string_s
    for ele in b:
        new_string += ele

    if new_string in items.keys():
        flag = True
    return flag
if __name__ == '__main__':
    a = ["One", "Two","Three"]
    b= ["Two"]
    prefixString(a,b)