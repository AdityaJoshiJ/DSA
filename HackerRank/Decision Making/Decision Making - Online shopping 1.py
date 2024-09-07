fPrice = int(input())
fDiscount = int(input())
fChargs = int(input())
sPrice = int(input())
sDiscount = int(input())
sChargs = int(input())
aPrice = int(input())
aDiscount = int(input())
aChargs = int(input())
fFinal = (int(fPrice-(fPrice*fDiscount/100)+fChargs))
sFinal = (int(sPrice-(sPrice*sDiscount/100)+sChargs))
aFinal = (int(aPrice-(aPrice*aDiscount/100)+aChargs))
print(f"In Flipkart: Rs.{fFinal}")
print(f"In Snapdeal: Rs.{sFinal}")
print(f"In Amazon: Rs.{aFinal}")
if fFinal <= sFinal:
    if fFinal <= aFinal:
        print("Choose Flipkart")
    else:
        print("Choose Amazon")
else:
    if sFinal <= aFinal:
        print("Choose Snapdeal")
    else:
        print("Choose Amazon")
