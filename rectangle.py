def left_rect(f, a, b, n):
    step = (b - a) / n  # размер шага
    il = 0
    while a <= (b - step):   # проход по всем прямоугольникам с точкой с левой стороны
        il += f(a) * step
        a += step
    return il


def right_rect(f, a, b, n):
    step = (b - a) / n  # размер шага
    il = 0
    while a <= (b - step):  # проход по всем прямоугольникам с точкой с левой стороны
        il += f(a + step) * step
        a += step
    return il


def central_rect(f, a, b, step):
    step = (b - a) / n  # размер шага
    il = 0
    while a <= (b - step):  # проход по всем прямоугольникам с точкой с левой стороны
        il += f(((a + step) + a) / 2) * step
        a += step
    return il


def trapezoid(f, a, b, step):
    i_sum = 0  # сумма половин крайних оснований
    while a <= (b - step):   # проход по оставшимся трапециям
        i_sum += (f(a) + f(a + step)) * (step / 2)
        a += step
    return i_sum


def parabola(f, a, b, n):
    step = (b - a) / n  # размер шага
    i_sum = 0
    while a <= (b - step):  # проход по всем интервалам, разделяя на 3 точки по методу симпсона
        i_sum += f(a) + 4*f((a + (a + step)) / 2) + f(a + step)  #
        a += step
    print(step)
    return i_sum * (step / 6)
