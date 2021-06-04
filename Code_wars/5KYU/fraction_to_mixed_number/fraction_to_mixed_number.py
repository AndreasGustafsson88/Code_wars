from fractions import Fraction

"""
Task:

Given a string representing a simple fraction x/y, your function must return a string representing the corresponding mixed fraction in the following format: [sign]a b/c
where a is integer part and b/c is irreducible proper fraction. There must be exactly one space between a and b/c.
Provide [sign] only if negative (and non zero) and only at the beginning of the number (both integer part and fractional part must be provided absolute).

If the x/y equals the integer part, return integer part only. If integer part is zero, return the irreducible proper fraction only.
In both of these cases, the resulting string must not contain any spaces.

Division by zero should raise an error (preferably, the standard zero division error of your language).
"""


def mixed_fraction(s):
    numerator, denominator = [int(x) for x in s.split('/')]
    sign = "-" if numerator/denominator < 0 else ""
    fraction = Fraction(abs(numerator / denominator)).limit_denominator(abs(denominator))
    integer = fraction.numerator // fraction.denominator

    if integer:
        return f'{sign}{fraction.numerator // fraction.denominator} {fraction.numerator % fraction.denominator}/{fraction.denominator}' if fraction.numerator % fraction.denominator else f'{sign}{fraction.numerator // fraction.denominator}'
    else:
        return f'{sign}{fraction.numerator % fraction.denominator}/{fraction.denominator}' if fraction.numerator % fraction.denominator else f'0'

print(mixed_fraction('-4327409/9302624'))
# '-4327409/9302624'
print(mixed_fraction('42/9'))
# # '4 2/3'
print(mixed_fraction('6/3'))
# # '2'
print(mixed_fraction('4/6'))
# # '2/3'
print(mixed_fraction('0/18891'))
# '0'
print(mixed_fraction('-10/7'))
# '-1 3/7'
print(mixed_fraction('-22/-7'))
# '3 1/7'
