import math
num = int(input('Digite o angulo que voçê deseja: '))

seno = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))
print('cos = {} , sin = {:.2f} , tang = {}'.format(cos,seno,tan))
