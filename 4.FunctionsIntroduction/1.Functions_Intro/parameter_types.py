def func(p1, p2, *args, k, **kwargs):
    print("Positional-or-keyword:...{}, {}".format(p1, p2))
    print("Var-positional (*args):..{}".format(args))
    print("Keyword:.................{}".format(k))
    print("Var-keyword:.............{}".format(kwargs))
    

func(1, 2, 3, 4, 5, 9, k=6, key1=7, k2=8)