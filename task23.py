txt = ['a', 'b', 'd', 'a', 'l', 'r', 'a', 'h', 'm', 'a', 'n']
good = ''.join(txt)
print(good.count('a'))
good = good.replace('d', 'c').replace('h', 'k')
print(good)
good = good.replace('l', '')
print(good)
