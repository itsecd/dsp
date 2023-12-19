from typing import Tuple

import numpy as np
from scipy.signal import convolve, deconvolve

# g[n] = f[n] * h[n] * h[-n]


def unstable(g: np.ndarray, h: np.ndarray) -> Tuple[np.ndarray, float]:
    # alternative:
    # p, r1 = deconvolve(g, h)
    # f, r2 = deconvolve(p, np.flip(h))
    # return f, max(np.max(np.abs(r1)), np.max(np.abs(r2)))
    f, r = deconvolve(g, convolve(h, np.flip(h)))
    return f, np.max(np.abs(r))


def stable(g: np.ndarray, h: np.ndarray) -> Tuple[np.ndarray, float]:
    p, r1 = deconvolve(g, h)
    f, r2 = deconvolve(np.flip(p), h)
    f = np.flip(f)
    return f, max(np.max(np.abs(r1)), np.max(np.abs(r2)))


def main() -> None:
    np.random.seed(0)

    # generate

    f = np.array((0, 1, 2, 3, 2, 1, 0), dtype=np.float64)
    h = np.array((1, 0.5), dtype=np.float64)
    g = convolve(f, convolve(h, np.flip(h)))
    g = g + np.random.normal(0, 0.1, len(g))

    # restore

    f1, e1 = unstable(g, h)
    f2, e2 = stable(g, h)

    # print

    np.set_printoptions(formatter={"float": lambda value: f"{value:6.2f}"})

    print(f"original: {f}")
    print(f"unstable: {f1}   max_remainder={e1:.2f}")
    print(f"stable:   {f2}   max_remainder={e2:.2f}")


if __name__ == "__main__":
    main()
