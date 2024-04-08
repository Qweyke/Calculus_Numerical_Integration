"""
                                        Методы численного интегрирования.
Метод прямоугольников (метод левых, правых и центральных прямоугольников):
Идея заключается в приближении площади под кривой прямоугольниками.
Прямоугольники размещаются под кривой, и их площади суммируются для приближенного вычисления интеграла.
В методе левых прямоугольников используются значения функции на левом конце каждого интервала, в правых - на правом,
 а в центральных - посередине.

Метод трапеций:
Кривая аппроксимируется сегментами трапеции.
Вычисляется накопленная сумма площадей трапеций, полученных делением интервала на сегменты - трапеции под функцией
Метод трапеций точнее метода прямоугольников.

Использует квадратичные полиномы для аппроксимации кривой.
Интеграл разбивается на несколько сегментов, для каждого из которых используется квадратичный полином (парабола),
 проходящий через три точки (левый конец, правый конец и середина интервала).
Этот метод часто дает более точные результаты, чем методы прямоугольников и трапеций.

Бояршинов МГ, 2006 -- Численные методы.ч4
"""

import matplotlib.pyplot as plt
from math import *
from scipy.integrate import quad
from rectangle import left_rect, right_rect, central_rect, trapezoid, parabola


def f(x):
    return e**(-x)


a = 0  # начало
b = 10  # конец
n = 10  # кол-во интервалов
step = (b - a) / n  # размер шага

res = quad(f, 0, 10)  # аналитический метод решения

plotx = []
plotl = []
plotr = []
plotc = []
plott = []
plotp = []

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 6))

while step >= 1e-5:  # отклонения
    plotx.append(step)
    plotl.append(abs(res[0] - left_rect(f, a,  b, step)))
    plotr.append(abs(res[0] - right_rect(f, a,  b, step)))
    plotc.append(abs(res[0] - central_rect(f, a,  b, step)))
    plott.append(abs(res[0] - trapezoid(f, a, b, step)))
    plotp.append(abs(res[0] - parabola(f, a, b, step)))
    step /= 10

ax1.plot(plotx, plotl, color='red', ls='--', marker='*', label='левый')
ax1.plot(plotx, plotr, color='blue', ls='-', marker='^', label='правый')
ax1.plot(plotx, plotc, color='green', ls='dotted', marker='8', label='центральный')
# ax1.plot(plotx, plott, color='orange', ls='--', marker='*', label='трапеции')
# ax1.plot(plotx, plotp, color='purple', ls='--', marker='*', label='симпсон')
ax1.set_title('Метод прямоугольников')
ax1.set_xlabel('Шаг')
ax1.set_ylabel('Отклонение')
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.legend()
ax1.grid(True)

ax2.plot(plotx, plott, color='red', ls='--', marker='*', label='трапеции')
ax2.set_xlabel('Шаг')
ax2.set_ylabel('Отклонение')
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.legend()
ax2.grid(True)

ax3.plot(plotx, plotp, color='purple', ls='--', marker='*', label='симпсон')
ax3.set_xlabel('Шаг')
ax3.set_ylabel('Отклонение')
ax3.legend()
ax3.set_yscale('log')
ax3.set_xscale('log')
ax3.grid(True)

plt.show()
