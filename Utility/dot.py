

def dot(a,b):
    if isinstance(a,list) and isinstance(b,list):
        return dot_list(a,b)
    elif isinstance(a,(int,float)) and isinstance(b,(int,float)):
        return dot_num(a,b)
    else:
        raise ValueError('a and b must be list or int or float')


def dot_list(a=[],b=[]):
    len_a = len(a)
    len_b = len(b)
    if len_a != len_b:
        raise ValueError("Lengths of arrays do not match")
    sum = 0
    for i in range(len_b):
        sum += a[i]*b[i]
    return sum

def dot_num(a=0,b=0):
    return a*b
