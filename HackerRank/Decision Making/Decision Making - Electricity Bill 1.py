n = int(input())
if n <= 200:
    print(f"Rs.{int(n*0.5)}")
elif n <= 400:
    print(f"int(n*0.65)+100")
elif n <= 600:
    print(f"Rs.{int(n*0.8)+200}")
else:
    print(f"{int(n*1.25)+425}")
