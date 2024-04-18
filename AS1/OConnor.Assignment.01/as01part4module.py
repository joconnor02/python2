SALESTAX = 0.06

def calcSalesTax(total):
    temp = total * SALESTAX
    return round(temp, 2)

def calcTotalAfterTax(total):
    return round(total + calcSalesTax(total), 2)
