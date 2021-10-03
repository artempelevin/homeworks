import math
from random import uniform
from typing import Tuple


e = 1 / (10**4)             # Точность
alpha = -0.1; betta = 4.0   # Константы для 17-го варианта


def J(u: float) -> float:
    return u**4 + alpha * math.atan(betta*u)


def provide_u12(a_i: float, b_i: float, sigma: float) -> Tuple[float, float]:
    return (a_i + b_i - sigma) / 2, (a_i + b_i + sigma) / 2


def _main() -> None:
    a_k = -100; b_k = 100
    sigma = uniform(0, b_k - a_k)  # Случайное число sigma
    iter_ = 0

    while abs(b_k - a_k) > e:
        u1, u2 = provide_u12(a_k, b_k, sigma)
        if J(u1) < J(u2):
            b_k = u2
        else:
            a_k = u1
        sigma = uniform(0, b_k - a_k)

        iter_ += 1

    print(f"u* = {(a_k+b_k)/2}\tJ* = {J((a_k+b_k)/2)}\tДлина отрезка = {b_k - a_k}")
    print(f"iterations: {iter_}")


if __name__ == '__main__':
    _main()