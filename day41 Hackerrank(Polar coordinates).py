# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
z=complex(input())
real_part = z.real
imag_part = z.imag

magnitude = math.sqrt(real_part**2 + imag_part**2)

theta_rad = math.atan2(imag_part, real_part)
print(magnitude)
print(theta_rad)
