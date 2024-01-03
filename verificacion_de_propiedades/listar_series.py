#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from os.path import exists
from controles import *
import json

def listar(nmin, nmax, n, fn):
    result = []
    for b in range(nmin,nmax):
        est, val = fn(b,n)
        if est:
            print(f'{val}')
            result.append(val)

    return [fn, result]

def almacenar(dat):
    ar = 'db.json'
    if not exists(ar):
        with open(ar, 'w') as f:
            f.write(json.dumps({}))

    with open(ar, 'r') as f:
        db = json.load(f)
        if not db:
            db = {}

    if not dat[0].__name__ in db:
        db[dat[0].__name__] = [dat[0].__doc__, dat[1]]
    else:
        db[dat[0].__name__][1] += dat[1]
        db[dat[0].__name__][1] = unicos(db[dat[0].__name__][1])

    with open(ar, 'w') as f:
        f.write(json.dumps(db))

def unicos(ll):
    r = []
    for l in ll:
        if not l in r:
            r.append(l)
    return r

nmin = 1
nmax = 100000


nombres = [k[3:] for k in locals().keys() if(k.startswith('es_n_'))]
ignorar = ['n_algo_c']

print(nombres)


for nomb in nombres:
    if not nomb in ignorar:
        fn = locals()[f'es_{nomb}'.lower()]

        print(f'\nSon {fn.__name__.upper()}, "{fn.__doc__}" : ')

        almacenar(listar(nmin, nmax, 2, fn))
        almacenar(listar(nmin, nmax, 3, fn))
        almacenar(listar(nmin, nmax, 4, fn))
        almacenar(listar(nmin, nmax, 5, fn))
        almacenar(listar(nmin, nmax, 6, fn))
        almacenar(listar(nmin, nmax, 7, fn))
        almacenar(listar(nmin, nmax, 8, fn))
        almacenar(listar(nmin, nmax, 9, fn))
        almacenar(listar(nmin, nmax, 10, fn))
        almacenar(listar(nmin, nmax, 11, fn))
        almacenar(listar(nmin, nmax, 12, fn))
        almacenar(listar(nmin, nmax, 13, fn))
