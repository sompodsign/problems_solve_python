brl = 1/2.43
print(format(brl, '0.4f'))

print('1 BRL = {rate:0.2f}'.format(rate=brl))


from datetime import datetime

now = datetime.now()
print(format(now, '%H:%M:%S'))

print("It's now {:%H:%M:%S %p}".format(now))
