from src.calculators.calculator_4 import Calculator4
from src.drivers.numpy_handler import NumpyHandler

def calculator_4_factory():
    numpyhandler = NumpyHandler()
    calc = Calculator4(numpyhandler)
    return calc