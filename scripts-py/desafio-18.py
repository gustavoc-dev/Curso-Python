#Seno e conseno

import math

ang = int(input('Angulo:\n'))
rad = math.radians(ang)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print('Seno:{:.2f}, Cosseno:{:.2f}, Tangente:{:.2f}'.format(seno,cosseno,tangente))