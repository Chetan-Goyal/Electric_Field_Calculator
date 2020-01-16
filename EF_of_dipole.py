from mpmath import mp
from math import cos, radians

# * Initializing accuracy level and value of const_k
mp.dps = 100
const_k = mp.fmul(8.9875518, 10**9)

def dipole_moment(charge, a):

    # Editing Value of charge as per the unit
    print(type(charge), type(a))

    if charge[1] in ('Coulomb', 'C'):
        charge = charge[0]
    elif charge[1] in ('microCoulomb', 'uC'):
        charge = mp.fmul(charge[0], 10**(-6) )
    elif charge[1] in ('milliCoulomb', 'mC'):
        charge = mp.fmul(charge[0], 10**(-3) )
    elif charge[1] in ('electronCharge', 'eC'):
        charge = mp.fmul(charge[0], mp.fmul(1.60217646, mp.fmul(10, -19) ) )                                             # 1.60217646⋅10-19
    elif charge[1] in ('nanoCoulomb', 'nC'):
        charge = mp.fmul(charge[0], mp.power(10, -10) )
    elif charge[1] in ('picoCoulomb', 'pC'):
        charge = mp.fmul( charge[0], mp.power(10, -12) )

    # Editing value of a as per the unit
    if a[1].lower() in ('meters', 'm'):
        a = a[0]
    elif a[1].lower() in ('centimeters', 'cm'):
        a = mp.fmul(a[0], 10**(-2) )
    elif a[1].lower() in ('millimeters', 'mm'):
        a = mp.fmul(a[0], 10**(-3) )
    elif a[1].lower() in ('angstroms', 'a', 'A'):
        a = mp.fmul(a[0], 10**(-10) )

    return mp.fmul(charge, mp.fmul(2, a))


def dipole(r, theta, charge, a):
    '''
    Purpose      : To calculate Electric Potential due to Dipole considering very small values

    Formula Used :

            (q/const_k)*(1/r_1 - 1/r_2)

                   where,
                        r_1     = distance between negative charge and point of observation
                                = (r^2 + a^2 - 2*a*Cos(theta))^0.5
                        r_2     = distance between positive charge and point of observation
                                = (r^2 + a^2 + 2*a*Cos(theta))^0.5
                        const_k = 4*pi*epsilon_not
                                = 8.9875518 x 10^9

    Parameters   :
                   a) r      - distance between center of the dipole and point of observation
                   b) theta  - Angle between positive charge and point of observation
                   c) charge - either charge irrespective of sign
                   d) a      - distance between either charge and center of dipole
    '''



    '''
    Editing Values of the arguments as per the values received by this function
    '''

    print('Values Received by dipole function')
    print(r, a, theta, charge)

    # Editing value of r as per the unit
    if r[1].lower() in ('meters', 'm'):
        r = r[0]
    elif r[1].lower() in ('centimeters', 'cm'):
        r = mp.fmul(r[0], 10**(-2) )
    elif r[1].lower() in ('millimeters', 'mm'):
        r = mp.fmul(r[0], 10**(-3) )
    elif r[1].lower() in ('angstroms', 'a', 'A'):
        r = mp.fmul(r[0], 10**(-10) )

    # Editing value of a as per the unit
    if a[1].lower() in ('meters', 'm'):
        a = a[0]
    elif a[1].lower() in ('centimeters', 'cm'):
        a = mp.fmul(a[0], 10**(-2) )
    elif a[1].lower() in ('millimeters', 'mm'):
        a = mp.fmul(a[0], 10**(-3) )
    elif a[1].lower() in ('angstroms', 'a', 'A'):
        a = mp.fmul(a[0], 10**(-10) )

    # Calculating Value of Cos(theta)
    if theta[1].lower() == 'radians':
        cos_theta = round( mp.cos(theta[0]), 5 )
    elif theta[1].lower() == 'degrees':
        cos_theta = round( mp.cos(mp.radians(theta[0])), 5 )

    # Editing Value of charge as per the unit
    if charge[1] in ('Coulomb', 'C'):
        charge = charge[0]
    elif charge[1] in ('microCoulomb', 'uC'):
        charge = mp.fmul(charge[0], 10**(-6) )
    elif charge[1] in ('milliCoulomb', 'mC'):
        charge = mp.fmul(charge[0], 10**(-3) )
    elif charge[1] in ('electronCharge', 'eC'):
        charge = mp.fmul(charge[0], mp.fmul(1.60217646, mp.fmul(10, -19) ) )                                         # 1.60217646⋅10-19
    elif charge[1] in ('nanoCoulomb', 'nC'):
        charge = mp.fmul(charge[0], mp.power(10, -10) )
    elif charge[1] in ('picoCharge', 'pC'):
        charge = mp.fmul( charge[0], mp.power(10, -12) )


    theta = round( mp.cos(mp.radians(theta[0])), 5 )
    print('Charge=', charge)
    print('a=', a)
    print('r=', r)
    print('theta=', theta)
    print('cos theta=', cos_theta)


    r_1 = mp.sqrt(mp.fsub(mp.fadd(mp.power(r, 2), mp.power(a, 2)), mp.fmul(2, mp.fmul(a, mp.fmul(r, cos_theta)))))
    r_2 = mp.sqrt(mp.fadd(mp.fadd(mp.power(r, 2), mp.power(a, 2)), mp.fmul(2, mp.fmul(a, mp.fmul(r, cos_theta)))))
    
    # Calculating final result
    result = mp.fmul(mp.fmul(charge, const_k), mp.fsub(mp.fdiv(1, r_1), mp.fdiv(1, r_2)))

    print('exact: ',result)

    # returning final result
    return result


def dipole_approx(r, theta, charge, a):
    '''
    Purpose      : To calculate Electric Potential due to Dipole neglecting very small value of a^2

    Formula Used :
            q*2*a*cos(theta)/( const_k*(r^2) )
                   where,
                    const_k = 4*pi*epsilon_not
                            = 8.9875518 x 10^9

    Parameters   :
                   a) r      - distance between center of the dipole and point of observation
                   b) theta  - Angle between positive charge and point of observation
                   c) charge - either charge irrespective of sign
                   d) a      - distance between either charge and center of dipole
    '''


    '''
    Editing Values of the arguments as per the values received by this function
    '''
    # Editing value of r as per the unit
    if r[1].lower() in ('meters', 'm'):
        r = r[0]
    elif r[1].lower() in ('centimeters', 'cm'):
        r = mp.fmul(r[0], 10**(-2) )
    elif r[1].lower() in ('millimeters', 'mm'):
        r = mp.fmul(r[0], 10**(-3) )
    elif r[1].lower() in ('angstroms', 'a', 'A'):
        r = mp.fmul(r[0], 10**(-10) )

    # Editing value of a as per the unit
    if a[1].lower() in ('meters', 'm'):
        a = a[0]
    elif a[1].lower() in ('centimeters', 'cm'):
        a = mp.fmul(a[0], 10**(-2) )
    elif a[1].lower() in ('millimeters', 'mm'):
        a = mp.fmul(a[0], 10**(-3) )
    elif a[1].lower() in ('angstroms', 'a', 'A'):
        a = mp.fmul(a[0], 10**(-10) )

    # Calculating Value of Cos(theta)
    if theta[1].lower() == 'radians':
        cos_theta = round( cos(theta[0]), 5 )
    elif theta[1].lower() == 'degrees':
        cos_theta = round( cos(mp.radians(theta[0])), 5 )

    # Editing Value of charge as per the unit
    if charge[1] in ('Coulomb', 'C'):
        charge = charge[0]
    elif charge[1] in ('microCoulomb', 'uC'):
        charge = mp.fmul(charge[0], 10**(-6) )
    elif charge[1] in ('milliCoulomb', 'mC'):
        charge = mp.fmul(charge[0], 10**(-3) )
    elif charge[1] in ('electronCharge', 'eC'):
        charge = mp.fmul(charge[0], mp.fmul(1.60217646, mp.fmul(10, -19) ) )                                         # 1.60217646⋅10-19
    elif charge[1] in ('nanoCoulomb', 'nC'):
        charge = mp.fmul(charge[0], mp.power(10, -10) )
    elif charge[1] in ('picoCharge', 'pC'):
        charge = mp.fmul( charge[0], mp.power(10, -12) )

    # Applying Formula to given parameters
    result = mp.fdiv(mp.fmul(const_k, mp.fmul(charge, mp.fmul(2, mp.fmul(a, cos_theta)))), mp.power(r,2))
    print('approx', result)

    # returning final result
    return result


def diff(EP:float, AP:float):
    return mp.fsub(EP, AP)


if __name__ == "__main__":
    print(mp) # Configurations of mpmath

    # Testing Values
    r = (float(1)  , 'meters')    # in meters
    theta = (float(60), 'degrees' )  # in degrees
    charge = (float(1), 'Coulomb')   # in coulombs
    a = (float(1), 'meters') # in meters

    exact  = dipole(r, theta, charge, a) # Exact Electric Potential due to Dipole
    approx = dipole_approx(r, theta, charge, a) # Approx Electric Potential to Dipole

    error = diff(exact, approx) # Error

    # Printing Results
    print('Exact Result  : ', exact)
    print('Approx Result : ', approx)
    print('Difference    : ', error)