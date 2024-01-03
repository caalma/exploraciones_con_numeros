from math import ceil
from utiles import *

debug = False

def es_n_algo_d1c(n,i):
    """| sum(p_digitos_pos_par) * dif(p_digitos_pos_impar) | + i == n^(1/i)"""
    p = n ** i
    x1 = (sum([int(d) if j % 2 else 0 for j, d in enumerate(str(p)[::-1])]))
    x2 = (sum([0 if j % 2 else int(d) for j, d in enumerate(str(p)[::-1])]))
    x = abs(x1 * x2) + i
    if debug : print(n, i, p, x)
    return [x == n, [n, i, p, x]]

def es_n_algo_d1b(n,i):
    """| sum(p_digitos_pos_par) * dif(p_digitos_pos_impar) | - i == n^(1/i)"""
    p = n ** i
    x1 = (sum([int(d) if j % 2 else 0 for j, d in enumerate(str(p)[::-1])]))
    x2 = (sum([0 if j % 2 else int(d) for j, d in enumerate(str(p)[::-1])]))
    x = abs(x1 * x2) - i
    if debug : print(n, i, p, x)
    return [x == n, [n, i, p, x]]

def es_n_algo_d1a(n,i):
    """| sum(p_digitos_pos_par) * dif(p_digitos_pos_impar) | == n^(1/i)"""
    p = n ** i
    x1 = (sum([int(d) if j % 2 else 0 for j, d in enumerate(str(p)[::-1])]))
    x2 = (sum([0 if j % 2 else int(d) for j, d in enumerate(str(p)[::-1])]))
    x = abs(x1 * x2)
    if debug : print(n, i, p, x)
    return [x == n, [n, i, p, x]]

def es_n_algo_c(n,i):
    """n ^ i = i ^ n"""
    p = n ** i
    x = i ** n
    return [x == p, [n, i, p, x]]

def es_n_algo_b2c(n,i):
    """sum(p_digitos) * i * 3 == n^(1/i)"""
    p = n ** i
    x = int(sum([int(d) for d in str(p)]) * i * 3)
    if debug : print(n, i, p, x)
    return [x == n, [n, i, p, x]]

def es_n_algo_b2b(n,i):
    """sum(p_digitos) * i * 2 == n^(1/i)"""
    p = n ** i
    x = int(sum([int(d) for d in str(p)]) * i * 2)
    if debug : print(n, i, p, x)
    return [x == n, [n, i, p, x]]

def es_n_algo_b2a(n,i):
    """sum(p_digitos) * i == n^(1/i)"""
    p = n ** i
    x = int(sum([int(d) for d in str(p)]) * i)
    if debug : print(n, i, p, x)
    return [x == n, [n, i, p, x]]

def es_n_algo_b1c(n,i):
    """sum(p_digitos) / i * 3 == n^(1/i)"""
    p = n ** i
    x = int(sum([int(d) for d in str(p)]) / i * 3)
    if debug : print(n, i, p, x)
    return [x == n, [n, i, p, x]]

def es_n_algo_b1b(n,i):
    """sum(p_digitos) / i * 2 == n^(1/i)"""
    p = n ** i
    x = int(sum([int(d) for d in str(p)]) / i * 2)
    if debug : print(n, i, p, x)
    return [x == n, [n, i, p, x]]

def es_n_algo_b1a(n,i):
    """sum(p_digitos) / i == n^(1/i)"""
    p = n ** i
    x = int(sum([int(d) for d in str(p)]) / i)
    if debug : print(n, i, p, x)
    return [x == n, [n, i, p, x]]

def es_n_algo_a1c(n,i):
    """sum(p_digitos_pos_par) + dif(p_digitos_pos_impar) + i == n^(1/i)"""
    p = n ** i
    x = abs(sum([int(d)*-1 if j % 2 else int(d)
        for j, d in enumerate(str(p)[::-1])])) + i
    if debug : print(n, i, p, x)
    return [x == n, [n, i, p, x]]

def es_n_algo_a1b(n,i):
    """sum(p_digitos_pos_par) + dif(p_digitos_pos_impar) - i == n^(1/i)"""
    p = n ** i
    x = abs(sum([int(d)*-1 if j % 2 else int(d)
        for j, d in enumerate(str(p)[::-1])])) - i
    if debug : print(n, i, p, x)
    return [x == n, [n, i, p, x]]

def es_n_algo_a1a(n,i):
    """| sum(p_digitos_pos_par) + dif(p_digitos_pos_impar) | == n^(1/i)"""
    p = n ** i
    x1 = (sum([int(d) if j % 2 else 0 for j, d in enumerate(str(p)[::-1])]))
    x2 = (sum([0 if j % 2 else int(d) for j, d in enumerate(str(p)[::-1])]))
    x = abs(x1 - x2)
    if debug : print(n, i, p, x)
    return [x == n, [n, i, p, x]]

def es_n_divertido_c(n,i):
    """sum(p_digitos) == n^(1/i)"""
    p = n ** i
    x = sum([int(d) for d in str(p)])
    if debug : print(n, i, p, x)
    return [x == n, [n, i, p, x]]

def es_n_divertido_b2(n,i):
    """sum(p_digitos) + (2*i) == n^(1/i)"""
    p = n ** i
    x = sum([int(d) for d in str(p)]) + (2*i)
    if debug : print(n, i, p, x)
    return [x == n, [n, i, p, x]]

def es_n_divertido_b1(n,i):
    """sum(p_digitos) + i == n^(1/i)"""
    p = n ** i
    x = sum([int(d) for d in str(p)]) + i
    if debug : print(n, i, p, x)
    return [x == n, [n, i, p, x]]

def es_n_divertido_a2(n,i):
    """sum(p_digitos) - (2*i) == n^(1/i)"""
    p = n ** i
    x = sum([int(d) for d in str(p)]) - (2*i)
    if debug : print(n, i, p, x)
    return [x == n, [n, i, p, x]]

def es_n_divertido_a1(n,i):
    """sum(p_digitos) - i == n^(1/i)"""
    p = n ** i
    x = sum([int(d) for d in str(p)]) - i
    if debug : print(n, i, p, x)
    return [x == n, [n, i, p, x]]
