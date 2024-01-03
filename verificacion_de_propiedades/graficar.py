#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from os.path import exists
import json
import matplotlib.pyplot as plt
import numpy as np


def cargar():
    ar = 'db.json'
    if not exists(ar):
        return {}

    with open(ar, 'r') as f:
        return json.load(f)


dat = cargar()


plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()


claves = ['es_n_divertido_a1', 'es_n_divertido_b1', 'es_n_divertido_c']
colores = ['blue', 'red', 'green']
marcas = ['o', 'P', 'D']

for i, k in enumerate(claves):
    x = [v[0] for v in dat[k][1]]
    y = [v[1] for v in dat[k][1]]
    ax.scatter(x, y, c=colores[i], alpha=0.6, marker=marcas[i])
    ax.set(xlim=(0, 8), xticks=np.arange(1, 160),
           ylim=(0, 8), yticks=np.arange(1, 15))


plt.subplots_adjust(
    top=0.971,
    bottom=0.048,
    left=0.028,
    right=0.979,
    hspace=0.2,
    wspace=0.2)


plt.show()
