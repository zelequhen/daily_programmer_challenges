def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def cdr(c):
	return c(lambda _, x : x)

def car(c):
	return c(lambda x, _ : x)
