from decimal import Decimal,ROUND_HALF_UP
n=1.5
temp=str(4.5)
temp=Decimal(temp)
cut=int(temp.quantize(Decimal('0'),rounding=ROUND_HALF_UP))

print((3+4)/2)