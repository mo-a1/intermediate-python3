import decimal
from decimal import Decimal

# https://www.youtube.com/watch?v=-4XI4B39k_U&ab_channel=NeuralNine

print(Decimal('.1') + Decimal('.2'))
print(.1 + .2)

print(decimal.getcontext())
print(Decimal("125.265654564") * Decimal("45.225"))

my_context = decimal.Context(prec=8, rounding=decimal.ROUND_FLOOR, traps=[])
print(my_context)
decimal.setcontext(my_context)

print(Decimal("125.6") * Decimal("45.25"), "| normal -> ", 125.6 * 45.25)
