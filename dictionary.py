

tel = {'jack':1024, 'sapa':2046}

tel['guido'] = 4096
#tel.get(jack)
print(tel)

del tel['sapa']
print(tel)

print(tel.keys())
print('jack' in tel)

print(tel.get('jacks',0))
sel = dict.fromkeys(['Amy','Tony'],8888)
print(sel)

