import math
def eulerImp(func, range, step, y0):
    """
        Uses the euler method of numerical solving. Returns the solution
        Arguments:
            func: lambda expression defining y'[x]
            range: tuple with min and max x
            step: decimal step size
            y0: decimal y starting position
    """
    x = range[0]
    newX = x + step
    if newX > range[1]:
        return y0
    else:
        slope = func(x, y0)
        newY = y0 + (step/2)*(slope + func(newX, y0+step*slope))
        return eulerImp(func, (newX, range[1]), step, newY)

def euler(func, range, step, y0):
    """
        Uses the euler method of numerical solving. Returns the solution
        Arguments:
            func: lambda expression defining y'[x]
            range: tuple with min and max x
            step: decimal step size
            y0: decimal y starting position
    """
    x = range[0]
    newX = x + step
    if newX > range[1]:
        return y0
    else:
        slope = func(x, y0)
        newY = y0 + step*slope
        return euler(func, (newX, range[1]), step, newY)
def rungeKutta(func, range, step, y0):
    x = range[0]
    newX = x + step
    if newX > range[1]:
        return y0
    else:
        k1 = func(x, y0)
        k2 = func(x + 0.5 * step, y0 + 0.5 * step * k1)
        k3 = func(x + 0.5 * step, y0 + 0.5 * step * k2)
        k4 = func(x + step, y0 + step * k3)
        newY = y0 + (step / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        return rungeKutta(func, (newX, range[1]), step, newY)


print(rungeKutta(lambda y : 32-(0.125/4)*(y**2), (0, 5), 1, 0))
