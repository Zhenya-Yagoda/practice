def root2(n2):
    return round(n2**0.5,5)
def root3(n3):
    if n3>=0:
        return round(n3**(1/3),5)
    else:
        return round(-(-n3)**(1/3),5 )
