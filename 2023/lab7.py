from typing import Final

import numpy as np

MORSE_CODES: Final[dict[str, str]] = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}


def morse_encode(message: str, unit_length: int) -> np.ndarray:
    dot = np.ones(unit_length)
    dash = np.ones(3 * unit_length)
    letter_intraspace = np.zeros(unit_length)
    letter_interspace = np.zeros(3 * unit_length)
    word_interspace = np.zeros(7 * unit_length)

    encoded = np.zeros((0))
    prev_symbol_is_letter = False

    for symbol in message:
        if symbol in MORSE_CODES:
            if prev_symbol_is_letter:
                encoded = np.concatenate((encoded, letter_interspace))
            is_first = True
            for code in MORSE_CODES[symbol]:
                if is_first:
                    is_first = False
                else:
                    encoded = np.concatenate((encoded, letter_intraspace))
                if code == ".":
                    chunk = dot
                elif code == "-":
                    chunk = dash
                else:
                    msg = f'Invalid morse code "{MORSE_CODES[symbol]}" for "{symbol}".'
                    raise Exception(msg)
                encoded = np.concatenate((encoded, chunk))
            prev_symbol_is_letter = True
        else:
            encoded = np.concatenate((encoded, word_interspace))
            prev_symbol_is_letter = False

    return encoded


def build_lowpass(w: float, n: int) -> np.ndarray:
    # TODO 2.3 Рассчитать ИХ для ФР НЧ КИХ-фильтра с частотой среза w [рад/отсчёт] и размером n [отсчётов]
    return np.zeros(0)


class LowpassReconstruction:
    def __init__(self, recovered: np.ndarray) -> None:
        self.__recovered = recovered
        # Добавить допданные при необходимости

    @property
    def recovered(self) -> np.ndarray:
        return self.__recovered


def lowpass_reconstruct(y: np.ndarray, h: np.ndarray) -> LowpassReconstruction:
    # TODO 2.1 Развернуть y и h, чтобы получить оценку x
    # TODO 2.2 Определить размер одной точки Морзе в отсчётах и соответствующую частоту среза w
    # TODO 2.4 Построить и применить ФР НЧ КИХ-фильтр
    del y, h
    return LowpassReconstruction(np.zeros(0))


class SuboptimalReconstruction:
    def __init__(self, recovered: np.ndarray) -> None:
        self.__recovered = recovered
        # Добавить допданные при необходимости

    @property
    def recovered(self) -> np.ndarray:
        return self.__recovered


def suboptimal_reconstruct(
    y: np.ndarray, h: np.ndarray, v: np.ndarray
) -> SuboptimalReconstruction:
    # TODO 4.1 Оценить r_y, r_v
    # TODO 4.2 Оценить r_xy, r_x
    # TODO 4.3 Рассчитать (уравнение Винера-Хопфа) фильтр и применить фильтр
    # TODO 4.4 По r_x[0] и ИХ фильтра рассчитать оценку погрешности восстановления
    del y, v, h
    return SuboptimalReconstruction(np.zeros(0))


def main() -> None:
    # TODO 1 Загрузить данные и оценить h[n]
    # TODO 3.1 Восстановить сигнал с помощью lowpass_reconstruct и вручную/автоматически декодировать сообщение
    # TODO 3.2 С помощью morse_encode сформировать идеальный полезный сигнал и рассчитать MSE
    # TODO 5 Восстановить сигнал с помощью suboptimal_reconstruct
    pass


if __name__ == "__main__":
    main()
