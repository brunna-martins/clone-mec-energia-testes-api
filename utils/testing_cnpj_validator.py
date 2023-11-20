from cnpj_validator_util import CnpjValidator

def ct1():
    CnpjValidator.validate('58577114000189')

def ct2():
    CnpjValidator.validate('A5857711400018')

def ct3():
    CnpjValidator.validate('585771140001899')

def ct4():
    CnpjValidator.validate('58577114000159')

def ct5():
    CnpjValidator.validate('58577114000183')


print('running ct1')

try:
    ct1()
except Exception as e:
    print(e)
    pass
else:
    print('no error')

print('running ct2')
try:
    ct2()
except Exception as e:
    print(e)
    pass
else:
    print('no error')

print('running ct3')
try:
    ct3()
except Exception as e:
    print(e)
    pass
else:
    print('no error')

print('running ct4')
try:
    ct4()
except Exception as e:
    print(e)
    pass
else:
    print('no error')

print('running ct5')
try:
    ct5()
except Exception as e:
    print(e)
    pass
else:
    print('no error')

