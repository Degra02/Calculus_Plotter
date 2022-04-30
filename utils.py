from functions import *


def plot(*functions, x_range=10, y_range=10):
    return 0


def compose(f, g):
    h = Function()
    try:
        h.init_func_no_input(smp.compose(f.func, g.func))
    except Exception:
        raise 'First create the functions'

    return h

