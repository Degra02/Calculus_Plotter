import sympy as smp
from sympy import Symbol, Matrix, pprint
from sympy.abc import x, y, z, w, t, u, v, theta, p, phi
from sympy.plotting import plot3d, plot
from sympy.functions import log, exp, sin, cos, cot, tan, acot, acos, asin, sinh, cosh

symbols = [x, y, z, w, t, u, v, theta, p, phi]


class Function:
    n: int
    variables: []
    func: smp.Function
    jacobian: Matrix
    hessian: Matrix
    taylor: smp.Function

    def __init__(self):
        self.n = 0
        self.variables = []
        self.jacobian = Matrix()
        self.hessian = Matrix()

    def init(self):
        self.eval_function()
        self.calculate_jacobian()
        self.calculate_hessian()

    def init_func_no_input(self, function):
        try:
            self.func = function
            self.variables = list(self.func.free_symbols)
            self.n = len(self.variables)
            self.calculate_jacobian()
            self.calculate_hessian()
        except Exception:
            raise 'Unable to compose the given functions'

    def eval_function(self):
        string = input("Function >> ")
        try:
            self.func = smp.sympify(string)
        except Exception:
            raise 'Invalid syntax'
        self.variables = list(self.func.free_symbols)
        self.n = len(self.variables)

    def calculate_jacobian(self):
        self.jacobian = Matrix([self.func]).jacobian([var for var in self.variables])

    def calculate_hessian(self):
        self.hessian = smp.hessian(self.func, self.variables)

    def print_function(self):
        print(f'f: R^{self.n} --> R')
        print('f(', end=''), print(*self.variables, sep=',', end=') = ')
        print(self.func)
        i = 0
        print('\ngrad(f)(', end=''), print(*self.variables, sep=',', end='):\n')
        pprint(self.jacobian)

    def plot(self, x_range=5, y_range=5):
        if self.n <= 2:
            data = {
                1: (plot, (self.func, )),
                2: (plot3d, (self.func, (x, -x_range, x_range), (y, -y_range, y_range)))
            }[self.n]
            data[0](*data[1])
        else:
            raise 'Too many dimensions'

    def val_at(self, coords):
        replace = [(self.variables[i], coords[i]) for i in range(len(self.variables))]
        res = self.func.subs(replace)
        print(f'At po=(', end=''), print(*coords, sep=',', end=f') -->  {res}')
