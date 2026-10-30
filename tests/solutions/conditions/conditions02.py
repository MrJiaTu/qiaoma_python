taxable = 5000
if taxable <= 3000:
    tax = taxable * 0.03
elif taxable <= 12000:
    tax = taxable * 0.10
else:
    tax = taxable * 0.20
