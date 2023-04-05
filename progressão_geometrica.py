#progressão geométrica 3 questão b)
a1 = 4
a2 = 2
q = a1 / a2
print("razao = ", q)

pg = []
pg.append(0)
pg.append(2)

for n in range(1,10):
    an = a1 * (q ** (n - 1))
    pg.append(int(an))
    print(pg)
    