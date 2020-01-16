from mpmath import fp, mp



# * Initializing accuracy level and value of const_k
mp.dps = 100
const_k = fp.fmul(8.9875518, 10**9)


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
    r_1 = fp.sqrt(fp.fsub(fp.fadd(fp.power(r, 2), fp.power(a, 2)), fp.fmul(2, fp.fmul(a, fp.fmul(r, fp.cos(fp.radians(theta)))))))
    r_2 = fp.sqrt(fp.fadd(fp.fadd(fp.power(r, 2), fp.power(a, 2)), fp.fmul(2, fp.fmul(a, fp.fmul(r, fp.cos(fp.radians(theta)))))))
    
    # Calculating final result
    result = fp.fmul(fp.fmul(charge, const_k), fp.fsub(fp.fdiv(1, r_1), fp.fdiv(1, r_2)))
    
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
    result = fp.fdiv(fp.fmul(const_k, fp.fmul(charge, fp.fmul(2, fp.fmul(a, fp.cos(fp.radians(theta)))))), fp.power(r,2))
    
    # returning final result
    return result


if __name__ == "__main__":
    print(fp) # Configurations of fpmath

    # Testing Values
    r = 1.0      # in meters
    theta = 60   # in degrees
    charge = 1.0   # in coulombs
    a = 10**(-9) # in meters

    exact  = dipole(r, theta, charge, a) # Exact Electric Potential due to Dipole
    approx = dipole_approx(r, theta, charge, a) # Approx Electric Potential to Dipole

    diff = fp.fsub(approx, exact) # Error

    # Printing Results
    print('Exact Result  : ', exact)
    print('Approx Result : ', approx)
    print('Difference    : ', diff)
