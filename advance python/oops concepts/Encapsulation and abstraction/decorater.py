def dec_fn(fn):
    def inn_function(n1,n2):
        if n2>n1:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return inn_function

@dec_fn
def sub(n1,n2):
    return n1-n2
@dec_fn
def div(n1,n2):
    return n1/n2
print(sub(20,10))

