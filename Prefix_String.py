"""
EBAY Question 2
"""
def prefixString(a,b):
    all_possible_prefix = dict()
    string_s = ''
    flag = False
    for j in range(len(a)):
        if string_s == '':
            string_s = a[j]
            all_possible_prefix[string_s] = string_s
        else:
            string_s = string_s + a[j]
            all_possible_prefix[string_s] = string_s
            print(string_s)
    print(all_possible_prefix)

    for ele in b:
        if ele in all_possible_prefix.keys():
            flag = True
        else:
            return False
    print(flag)
    return flag
if __name__ == '__main__':
    a = ["One", "Two","Three"]
    b= ["OneTwo" , "One"]
    prefixString(a,b)