"""Week 4 Tutorial exercise"""
# Firstly we are looking at converting from different number bases
# Binary (base 2), Octal (base 8), Decimal (base 10), Hexadecimal (base 16)
# For reference, first 5 bases

for i in range(1, 6):
    print(f"{2 ** i} , {8 ** i} , {16 ** i}")

# Why Octal? Because 8 = 2*2*2 = (1000)base2 UNIX
# Hex is (10000)base2, also HTML colours!
# Both are legible with recognisable characters


def basechange(x, y, z):
    old_value = int(x, y)
    new_value = int(old_value, z)
    print(f"{x} in base {y} is {new_value} in base {z}")


basechange(1200, 3, 10)
