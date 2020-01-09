from math import pow, sqrt, cos, radians, pi
from mpmath import mp

mp.dps = 50

def dipole(r, theta, charge, a):
    '''
    v = c(a + b)
    '''
    
    a = mp.power( mp.fsub(mp.fadd(1, mp.fdiv(mp.power(a, 2), mp.power(r, 2))), mp.fdiv(mp.fmul(mp.fmul(mp.fmul(2, a), r), mp.cos(radians(theta))), r) ), -0.5 )
    b = mp.power( mp.fadd(mp.fadd(1, mp.fdiv(mp.power(a, 2), mp.power(r, 2))), mp.fdiv(mp.fmul(mp.fmul(mp.fmul(2, a), r), mp.cos(radians(theta))), r) ), -0.5 )
    c = mp.fdiv(mp.fmul(9, mp.power(10, 9)), r)
    result = mp.fmul(c, mp.fadd(a, b))
    print(result)

def dipole_approx(r, theta, charge, a):
    result = mp.fdiv(mp.fmul(9, mp.fmul(mp.power(10,9), mp.fmul(charge, mp.fmul(2, mp.fmul(a, mp.cos(radians(theta))))))), mp.power(r,2))
    print(result)

print(mp)
dipole(0.1, 60, 1, mp.power(10, -9))
dipole_approx(0.1, 60, 1, mp.power(10, -9))

