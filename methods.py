from math import*
from scipy.integrate import quad


def left_rect(f, a, b, step, arr, ilf):
    il = 0
    while a <= (b - step):   # проход по всем прямоугольникам с точкой с левой стороны прямоугольника
        il += f(a) * step
        arr.append(il - ilf(a))
        print(ilf)
        print(il)
        print()
        a += step
    return il


def right_rect(f, a, b, step, arr, ilf):
    il = 0
    while a <= (b - step):  # проход по всем прямоугольникам с точкой с левой стороны
        il += f(a + step) * step
        arr.append(il - ilf(a))
        a += step
    return il


def central_rect(f, a, b, step, arr, ilf):
    il = 0
    while a <= (b - step):  # проход по всем прямоугольникам с точкой с левой стороны
        il += f(((a + step) + a) / 2) * step
        arr.append(il - ilf(a))
        a += step
    return il


def trapezoid(f, a, b, step, arr, ilf):
    i_sum = 0  # сумма половин крайних оснований
    while a <= b - step:   # проход по оставшимся трапециям
        i_sum += (f(a) + f(a + step)) * (step / 2)
        arr.append(i_sum - ilf(a))
        a += step
    return i_sum


def parabola(f, a, b, step, arr, ilf):
    i_sum = 0
    while a <= b - step:  # проход по всем интервалам, разделяя на 3 точки по методу симпсона
        i_sum += (f(a) + 4*f((a + (a + step)) / 2) + f(a + step)) * (step / 6)
        arr.append(i_sum - ilf(a))
        a += step
    return i_sum

