def Test(y):
    assert (y >= 0),"Less than 0"
    return y+2


def CheckAssert(x):
   assert (x >= 0),"Colder than absolute zero!"
   return ((x-273)*1.8)+32

print (CheckAssert(273))
print (int(CheckAssert(505.78)))
print (Test(-5))