def factorital(fac):
    if fac == 1:
        return(1)
    else:
        return(fac * factorital(fac-1))

fac = 7
print(factorital(fac))