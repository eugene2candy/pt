a00 = raw_input('amount of 0: ')
a11 = raw_input('amount of 1: ')
a22 = raw_input('amount of 2: ')
a33 = raw_input('amount of 3: ')
a0 = int(a00)
a1 = int(a11)
a2 = int(a22)
a3 = int(a33)

def z(a0 ,a1, a2, a3, p0 = 20, p1 = 15, p2 = 16, p3 = 6):
    zong = a0 * p0 + a1 * p1 + a2 * p2 + a3 * p3
    return zong

zong = z(a0, a1, a2, a3)
print 'payment =', zong

