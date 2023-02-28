# Лабораторная работа №7, Овчинников Никита, вариант 5
# Импорт
import numpy as np
import csv
import matplotlib.pyplot as plt
import random
import time
from math import sin, cos

title1 = 'Положение дроссельной заслонки (%)'
title2 = 'Массовый расход воздуха (кг\ч)'

# Функция, наглядно показывающая разницу в скотрости работы списков и массивов
def difference():
    # Создание списков
    a, b, c = [], [], []

    for i in range(10**6):
        a.append(random.randint(0, 1000))
        b.append(random.randint(0, 1000))

    # Перемножение, замер времени, вывод для списков
    time_start = time.perf_counter()
    for i in range(10**6):
        c.append(a[i] * b[i])
    all_time = time.perf_counter() - time_start
    print(f'{all_time} - время перемножения стандартных списков')

    a = np.array(a, int)
    b = np.array(b, int)

    # Перемножение, замер времени, вывод для массивов
    time_start = time.perf_counter()
    np.multiply(a, b)
    all_time = time.perf_counter() - time_start

    print(f'{all_time} - время перемножения NumPy массивов')

# Функция выводтит графики зависимости от времени и график корреляции
def graph_time():
    # Создание и заполнение списков с данными из таблицы
    time = []
    a, b = [], []
    with open('data1.csv') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            time.append(float(row['Время']))
            a.append(float(row[title1]))
            b.append(float(row[title2]))
    # Создание массивов
    time = np.array(time, float)
    a = np.array(a, float)
    b = np.array(b, float)

    # Построение первого графика
    fig = plt.figure()
    ax = fig.add_subplot(121)
    ax.set(title='Зависимость от времени',
           xlabel='Время, с',
           ylabel=title1+', Желтый график')
    ax.plot(time, a,
            color='orange')

    # Построение второго графика
    ax1 = ax.twinx()
    ax1.set(ylabel=title2+', Черный график')
    ax1.plot(time, b,
             color='black',
             linewidth=0.5)

    noise = np.random.normal(0, 0.3, size=len(a))
    a_jitter = a + noise

    # Построение графика корреляции
    ax2 = fig.add_subplot(122)
    ax2.set(title='График корреляции',
            xlabel=title1,
            ylabel=title2)
    ax2.plot(a_jitter, b, 'o', alpha=0.3, markersize = 4)
    plt.show()

def graph_3d():

    # Создаине и заполнение области значения и области определения
    x = np.linspace(np.pi*(-1), np.pi, 100)
    y = np.zeros(len(x), float)
    for i in range(len(x)):
        y[i] = sin(x[i])*cos(x[i])
    z = np.zeros(len(x), float)
    for i in range(len(x)):
        z[i] = sin(x[i])

    # Вывод трехмерного графика функции
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    plt.show()

word = int(input("""Чтобы сравнить скорость работы обычных списков и NumPy массивов введите 1
Чтобы вывести графики зависимости от времени и график корреляции введите 2
Чтобы вывести трехмерный график введите 3\n"""))

match word:
    case 1:
        difference()
    case 2:
        graph_time()
    case 3:
        graph_3d()

