import math

e = 1 / (10**4)             # Точность
alpha = -0.1; betta = 4.0   # Константы для 17-го варианта


def J(u: float) -> float:
    return u**4 + alpha * math.atan(betta*u)


def provide_u1(a: float, b: float) -> float:
    return a + (3 - math.sqrt(5)) * (b - a) / 2


def provide_u2(a: float, b: float) -> float:
    return a + (math.sqrt(5) - 1) * (b - a) / 2


def provide_u(a: float, b: float, u2: float) -> float:
    return a + b - u2


def _main() -> None:
    a_k = -100; b_k = 100
    iter_ = 0

    u1, u2 = provide_u1(a_k, b_k), provide_u2(a_k, b_k)

    while abs(b_k - a_k) > e:
        if J(u1) <= J(u2):
            b_k = u2
            u2 = u1
        else:
            a_k = u1

        u1 = provide_u(a_k, b_k, u2)
        if u1 > u2:
            u1, u2 = u2, u1

        iter_ += 1

    print(f"u* = {(a_k+b_k)/2}\tJ* = {J((a_k+b_k)/2)}\tДлина отрезка = {b_k - a_k}")
    print(f"iterations: {iter_}")


if __name__ == '__main__':
    _main()