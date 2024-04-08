import matplotlib.pyplot as plt
from math import *
from scipy.integrate import quad
from rectangle import left_rect, right_rect, central_rect, trapezoid, parabola


def f(x):
    return e**(-x)


a = 0  # начало
b = 10  # конец
n = 110  # кол-во интервалов
step = (b - a) / n  # размер шага
res = quad(f, 0, 10)  # аналитический метод решения

plotx = []
plotl = []
plotr = []
plotc = []
plott = []
plotp = []

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 6))
i = 0
while step >= 1e-11:
    plotx.append((b - a) / abs(n))
    plotl.append(abs(res[0] - left_rect(f, a,  b, n)))
    plotr.append(abs(res[0] - right_rect(f, a,  b, n)))
    plotc.append(abs(res[0] - central_rect(f, a,  b, n)))
    plott.append(abs(res[0] - trapezoid(f, a, b, step)))
    plotp.append(abs(res[0] - parabola(f, a, b, n)))
    step /= 10
    #print(abs(res[0] - central_rect(f, a,  b, n)))
    #print(abs(res[0] - trapezoid(f, a, b, n)))
    print(plotp[i])
    print(n)
    print()
    i += 1


ax1.plot(plotx, plotl, color='red', ls='--', marker='*', label='левый')
ax1.plot(plotx, plotr, color='blue', ls='-', marker='^', label='правый')
ax1.plot(plotx, plotc, color='green', ls='dotted', marker='8', label='центральный')
#ax1.plot(plotx, plotl, color='red', ls='--', marker='*', label='трапеции')
#ax1.plot(plotx, plotl, color='purple', ls='--', marker='*', label='симпсон')
ax1.set_title('Метод прямоугольников')
ax1.set_xlabel('Шаг')
ax1.set_ylabel('Отклонение')
#ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.legend()
ax1.grid(True)

ax2.plot(plotx, plott, color='red', ls='--', marker='*', label='трапеции')
ax2.set_xlabel('Шаг')
ax2.set_ylabel('Отклонение')
#ax2.set_xscale('log')
ax2.legend()
ax2.grid(True)

ax3.plot(plotx, plotp, color='purple', ls='--', marker='*', label='симпсон')
ax3.set_xlabel('Шаг')
ax3.set_ylabel('Отклонение')
ax3.legend()
ax3.grid(True)

plt.show()
