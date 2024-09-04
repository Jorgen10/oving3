from math import log
from lib import parseFloat

def f(m, n):
    return m*log(m) + n*log(n)

m = parseFloat("Skriv inn m: ")
n = parseFloat("Skriv inn n: ")

print(f(m, n))