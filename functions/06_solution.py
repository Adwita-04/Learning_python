def sum_all(*args):
    print(args)
    for i in args:
       print(i*2)
    return sum(args)
print(sum_all(1,2,3,4,5,5,6,6,6,8,8,8,8,))
print(sum_all(1,2,3,4,5))
