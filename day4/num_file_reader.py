def read_num_file(fn):
    f = open(fn, 'r')
    # print(f, type(f))
    text = f.read()
    # print(text, type(text))
    a = text.split('\n')
    # print(a)
    a = a[0:-1]
    # print(a)
    b = []
    for i in range(len(a)):
        # print(a[i])
        b.append(int(a[i]))
    # print(b)
    # print(fn, min(b), max(b), sum(b)/len(b))
    return [min(b), max(b), sum(b)/len(b)]

def read_num_file_list(fn):
    f = open(fn, 'r')
    text = f.read()
    a = text.split('\n')    # list of string
    a = a[:-1]              # a[:-1] = a[0:-1]
    b = []                  # list of int
    for i in a:
        b.append(int(i))
    return b

# read_num_file('in.txt')
# read_num_file('in2.txt')
# read_num_file_list('./pt1_data/IT_ARU_0.txt')
