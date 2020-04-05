n1 = int(input('Digite um nr '))
n2 = int(input('Digite um nr '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

mod = n1 % n2

print('O resultado é s = {}, m = {}, d = {:.3f}, di = {}, e = {} mod ={} '.format(s,m,d,di,e, mod), end=' ###')
