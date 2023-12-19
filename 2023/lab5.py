# pylint: disable=invalid-name
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import unittest

import numpy as np
from scipy.signal import stft, istft
from scipy.fft import ifft


def idft(x: np.ndarray) -> np.ndarray:
    # TODO #1: Implement complex-data inverse DFT
    return x


def real_istft(spectrum: np.ndarray, segment: int, overlap: int) -> np.ndarray:
    assert len(spectrum.shape) == 2
    assert spectrum.shape[0] == segment // 2 + 1

    # TODO #2: Implement inverse STFT

    return np.zeros(1)


class Test(unittest.TestCase):
    class Params:
        def __init__(self, n: int, segment: int, overlap: int) -> None:
            self.n = n
            self.segment = segment
            self.overlap = overlap

        def __str__(self) -> str:
            return f"n={self.n} segment={self.segment} overlap={self.overlap}"

    def test_idft(self) -> None:
        for n in (10, 11, 12, 13, 14, 15, 16):
            with self.subTest(n=n):
                np.random.seed(0)
                x = np.random.rand(n) + 1j * np.random.rand(n)
                actual = idft(x)
                expected = ifft(x)
                self.assertTrue(np.allclose(actual, expected))

    @unittest.skip
    def test_istft_unmodified(self) -> None:
        self._test_istft(False)

    @unittest.skip
    def test_istft_modified(self) -> None:
        self._test_istft(True)

    def _test_istft(self, modify: bool) -> None:
        params_list = (
            Test.Params(50, 10, 5),
            Test.Params(50, 10, 6),
            Test.Params(50, 10, 7),
            Test.Params(50, 10, 8),
            Test.Params(50, 10, 9),
            Test.Params(101, 15, 7),
            Test.Params(101, 15, 8),
        )

        for params in params_list:
            with self.subTest(params=str(params)):
                np.random.seed(0)

                x = np.random.rand(params.n)

                _, _, s = stft(
                    x,
                    boundary=None,
                    nperseg=params.segment,
                    noverlap=params.overlap,
                    padded=False,
                    window="boxcar",
                )

                assert isinstance(s, np.ndarray)

                if modify:
                    low_pass_filter = np.concatenate(
                        (
                            np.ones(s.shape[0] // 2),
                            np.zeros(s.shape[0] - s.shape[0] // 2),
                        )
                    )
                    for column in np.arange(s.shape[1]):
                        s[:, column] = s[:, column] * low_pass_filter

                _, expected = istft(
                    s,
                    boundary=None,
                    nperseg=params.segment,
                    noverlap=params.overlap,
                    window="boxcar",
                )

                assert isinstance(expected, np.ndarray)

                actual = real_istft(s * params.segment, params.segment, params.overlap)

                self.assertTrue(np.allclose(actual, expected))


def main() -> None:
    unittest.main()

    # TODO #3: Implement robotic effect using scipy's stft/istft


if __name__ == "__main__":
    main()
