r = []
a = int(input())
e = int(input())

if a>=3 and e<=4:
    r.append("TroyMartian")
if a<=6 and e>=2:
    r.append("VladSaturnian")
if a<=2 and e<=3:
    r.append("GraemeMercurian")
for n in r:
    print(n)