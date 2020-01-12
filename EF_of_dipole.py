from mpmath import mp


# * Initializing accuracy level and value of const_k
mp.dps = 50
const_k = mp.fmul(8.9875518, 10**9)

def dipole_moment(charge:float, a:float):
        return mp.fmul(charge, mp.fmul(2, a))


def dipole(r:float, theta:float, charge:float, a:float):
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

    # Calculating values of r_1 and r_2
    r_1 = mp.sqrt(mp.fsub(mp.fadd(mp.power(r, 2), mp.power(a, 2)), mp.fmul(2, mp.fmul(a, mp.fmul(r, mp.cos(mp.radians(theta)))))))
    r_2 = mp.sqrt(mp.fadd(mp.fadd(mp.power(r, 2), mp.power(a, 2)), mp.fmul(2, mp.fmul(a, mp.fmul(r, mp.cos(mp.radians(theta)))))))
    
    # Calculating final result
    result = mp.fmul(mp.fmul(charge, const_k), mp.fsub(mp.fdiv(1, r_1), mp.fdiv(1, r_2)))
    
    # returning final result
    return result 


def dipole_approx(r:float, theta:float, charge:float, a:float):
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
    
    # Applying Formula to given parameters
    result = mp.fdiv(mp.fmul(const_k, mp.fmul(charge, mp.fmul(2, mp.fmul(a, mp.cos(mp.radians(theta)))))), mp.power(r,2))
    
    # returning final result
    return result


def diff(EP:float, AP:float):
        return mp.fsub(EP, AP)


if __name__ == "__main__":
    print(mp) # Configurations of mpmath

    # Testing Values
    r = 0.1      # in meters
    theta = 60   # in degrees
    charge = 1   # in coulombs
    a = 10**(-9) # in meters

    exact  = dipole(r, theta, charge, a) # Exact Electric Potential due to Dipole
    approx = dipole_approx(r, theta, charge, a) # Approx Electric Potential to Dipole

    error = diff(exact, approx) # Error

    # Printing Results
    print('Exact Result  : ', exact)
    print('Approx Result : ', approx)
    print('Difference    : ', error)
