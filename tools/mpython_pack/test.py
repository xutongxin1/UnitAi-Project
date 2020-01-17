from mpython import *

p1=MPythonPin(1,PinMode.OUT)
p2=MPythonPin(2,PinMode.IN)
p1.write_digital(1)
if p2.read_digital()==1:
    print(123)







