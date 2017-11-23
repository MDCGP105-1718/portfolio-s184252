class Fraction:
	def __init__(self, num, denom):
		self.num = num
		self.denom = denom

	def __add__(self, other):
		self_num = self.num * other.denom
		new_denom = self.denom * other.denom
		other_num = other.num * self.denom
		return Fraction(self_num + other_num, new_denom)

	def __sub__(self, other):
		pass

	def __mul__(self, other):
		pass

	def __truediv__(self, other):
		pass

	def __invert__(self, other):
		pass

	def __str__(self):
		return f"{self.num}/{self.denom}"

frac1 = Fraction(1, 2)
frac2 = Fraction(1, 3)

print(frac1 + frac2)