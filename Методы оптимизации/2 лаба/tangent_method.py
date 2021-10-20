import math
from random import uniform
from typing import List

import numpy as np
import matplotlib.pyplot as plt

#  Константы для 17-го варианта
a = -0.3879;   b = 0        # Берём отрезок где функция выпукла
alpha = 4.330
betta = 4.008
sigma = 3.5
e = 0.0001

step = 0.001    # Расстояние между 2мя точками графика


def J(u: float) -> float:       # Исходная функция
    return alpha * math.sin(betta * u) - sigma * u


def J_(u: float) -> float:      # Производная
    return alpha * betta * math.cos(betta * u) - sigma


def g(u: float, v: float) -> float:   # Касательная
    return J(v) + J_(v) * (u - v)


def provide_max_g(g1: List[float], g2: List[float]) -> List[float]:
    return [max(g1_, g2_) for g1_, g2_ in zip(g1, g2)]


def provide_min_p(p: List[float], u: List[float]) -> float:
    min_ = p[0]
    u_min = u[0]

    for i, u_ in enumerate(u):
        if min_ > p[i]:
            min_ = p[i]
            u_min = u_

    return u_min


def _main() -> None:
    u = list(np.arange(a, b, step))     # Все точки на отрезке [a, b], отличающиеся на step
    u0 = a                              # Выбираем начальную точку = точке a

    p1 = [g(u_, u0) for u_ in u]        # Строим касательную в точке u0
    u1 = provide_min_p(p1, u)           # Находим точку минимума ломанной

    iter_ = 0
    while abs(u1 - u0) > e:
        p2 = [g(u_, u1) for u_ in u]        # Строим вторую касательные
        p2 = provide_max_g(p1, p2)          # Объединяем ломанные (по правилу максимума)

        u0 = u1
        u1 = provide_min_p(p2, u)
        p1 = p2

        iter_ += 1

    print(f"u* = {(u1)}\tJ* = {J((u1))}\t"f"Разница |J(u0) - J(u1)| = {abs(J(u0) - J(u1))}")
    print(f"iterations: {iter_}")

    y = [J(u) for u in u]

    plt.plot(u, y, 'g')         # График функции
    plt.plot(u, p2, 'y')        # График ломанной
    plt.plot(u1, J(u1), '.r')   # Точка минимума
    plt.show()


if __name__ == '__main__':
    _main()