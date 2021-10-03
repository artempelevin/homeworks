import matplotlib.pyplot as plt

from dichotomy import J


def draw_graph(a: int, b: int) -> None:
    u = range(a, b+1)
    y = [J(u_) for u_ in u]

    plt.plot(u, y)
    plt.show()


def _main() -> None:
    draw_graph(a=-100, b=100)


if __name__ == '__main__':
    _main()
