import sounddevice as sd
from threading import Thread
import numpy as np
import turtle as tt
import math as m


# объект эквалайзер
class Sub:
    # инициализация переменных
    def __init__(self, cols, dwr):
        self.dwr = dwr
        self.dwr.pensize(10)

        self.dwr.left(90)

        self.colors = cols

        self.g = 0
        self.t = 0

    # запуск измерения громкости звука через микрофон
    def run_callback(self):

        duration = 10

        # Функция получения громкости звука
        def audio_callback(indata, frames, time, status):
            volume_norm = np.linalg.norm(indata) * 10

            self.g = int(volume_norm)

        stream = sd.InputStream(callback=audio_callback)

        # функция запуска
        def o():
            with stream:
                sd.sleep(duration**8)

        # запуск отдельного потока для проверки громкости звука
        thre = Thread(target=o)
        thre.start()

    # Прорисовка эквалайзера
    def draw(self):
        self.dwr.clear()

        num = 60
        st = (num - 1) // 2
        dist = 10
        all_dist = st * dist

        f = -170
        g = 0

        if self.t < self.g:
            self.t += abs(self.g - self.t) / 3
        else:
            self.t -= abs(self.g - self.t) / 3

        for k in range(num):
            if k - 1 == num // 2:
                f = 110
                g = 100

            x = abs(-all_dist + dist * k + f)
            self.dwr.up()
            self.dwr.goto(-all_dist + dist * k + f, -350)
            self.dwr.down()

            try:
                self.dwr.color(
                    self.colors[int(self.t * (st - abs(k - st)) / 4)])
            except:
                self.dwr.color(self.colors[-1])

            self.dwr.fd(self.t * m.sqrt((x / 5) ** 2) - g)
