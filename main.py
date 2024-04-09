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
from methods import left_rect, right_rect, central_rect, trapezoid, parabola


def f(x):
    return sin(x)


def ilf(x):
    return 1 - cos(x)


def plotik(r, le, stepik):
    while r <= (le - stepik):
        plotx.append(r)
        r += step


a = 0  # начало
b = 10  # конец
n = 100  # кол-во интервалов
step = (b - a) / n  # размер шага

res = quad(f, 0, 10)  # аналитический метод решения
print(res)

plotx = []
plotl = []
plotr = []
plotc = []
plott = []
plotp = []

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 6))

plotik(a, b, step)
left_rect(f, a,  b, step, plotl, ilf)
right_rect(f, a,  b, step, plotr, ilf)
central_rect(f, a,  b, step, plotc, ilf)
trapezoid(f, a, b, step, plott, ilf)
parabola(f, a, b, step, plotp, ilf)

ax1.plot(plotx, plotl, color='red', ls='--', marker='*', label='левый')
ax1.plot(plotx, plotr, color='blue', ls='-', marker='^', label='правый')
ax1.plot(plotx, plotc, color='green', ls='dotted', marker='8', label='центральный')
ax1.set_title('Метод прямоугольников')
ax1.set_xlabel('Шаг')
ax1.set_ylabel('Отклонение')
#ax1.set_xscale('log')
#ax1.set_yscale('log')
ax1.legend()
ax1.grid(True)

ax2.plot(plotx, plott, color='red', ls='--', marker='*', label='трапеции')
ax2.set_xlabel('Шаг')
ax2.set_ylabel('Отклонение')
ax2.legend()
ax2.grid(True)

ax3.plot(plotx, plotp, color='purple', ls='--', marker='*', label='симпсон')
ax3.set_xlabel('Шаг')
ax3.set_ylabel('Отклонение')
ax3.legend()
ax3.grid(True)

plt.show()
