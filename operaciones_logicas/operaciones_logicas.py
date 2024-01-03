# Operaciones lóginas

# https://en.wikipedia.org/wiki/Boolean_algebra
# https://es.wikipedia.org/wiki/L%C3%B3gica_binaria

def neg(n):
    # negación
    return 1 - n

def y (n,m):
    # y, conjunción
    return n * m

def o(n,m):
    # o inclusivo, disynción
    return n + m - n * m

def imp(n, m):
    # implicación
    return neg(n * neg(m))

def ide(n, m):
    # identidad, equivalencia
    return o(y(n,m), y(neg(n),neg(m)))

def con(n,m):
    # contradicción, o exclusivo
    return y(o(n,m), neg(y(n,m)))
