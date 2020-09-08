import sympy as sp
import random

common_variables = sp.symbols("a x y z theta", real=True)
variables = sp.symbols("a b c d k m n p q r s t w alpha beta gamma", real=True)
variable_weights = [0.3, 0.7]  # variables : common variables

randomVar = lambda: random.choices([random.choice(common_variables), random.choice(variables)], weights=variable_weights, k=1)[0]

# Some functions
random_functions = {  # weight : func
	50: sp.exp,  # e**x
	30: sp.log,
	50: sp.sin,
	50: sp.cos,
	15: sp.tan,
	15: sp.cot,
	10: sp.sec,
	10: sp.csc,
	10: sp.asin,
	10: sp.acos,
	10: sp.atan,
	10: sp.acot,
	2: sp.asec,
	2: sp.acsc,
	10: sp.sinh,
	10: sp.cosh,
	5: sp.tanh,
	5: sp.coth,
	2: sp.sech,
	2: sp.csch,
	1: sp.asinh,
	1: sp.acosh,
	1: sp.atanh,
	1: sp.acoth,
	1: sp.asech,
	1: sp.acsch,
	25: sp.sqrt,
	25: sp.cbrt,
	50: (lambda x: x ** ( random.choices([2, 3, 4, 5, 6, 7, 8, 9, 10], weights=[10, 6, 6, 6, 5, 4, 3, 3, 3], k=1)[0] )),  # x**a
	30: (lambda x: random.choice([-1, 1]) * random.randint(1, 10)),  # random constant term
	30: (lambda x: random.randint(2, 10) ** x),  # random constant term
	10: (lambda x: sp.real_root(x, random.randint(4, 10)))
}

def randomFuncNoComp(inner):
	return ( random.choices(list(random_functions.values()), weights=list(random_functions.keys()), k=1)[0] )(inner)


def randomFunc(variable, recur=0.67):
	assert recur < 1
	if random.uniform(0.001, 1) < recur:  # Recursion
		chance = random.randint(1, 20)
		if chance <= 4:
			return randomFunc(variable, recur=recur) + randomFunc(variable, recur=recur)
		elif chance <= 10:
			return randomFunc(variable, recur=recur) - randomFunc(variable, recur=recur)
		elif chance <= 15:
			return randomFunc(variable) * randomFunc(variable, recur=(recur*0.8))
		elif chance <= 19:
			return (randomFunc(variable))/(randomFunc(variable, recur=(recur*0.6)))
		elif chance == 20:
			return randomFunc(randomFunc(variable, recur=recur*recur))
	else:
		return ( random.choices(list(random_functions.values()), weights=list(random_functions.keys()), k=1)[0] )(variable)


# print(sp.latex(sp.simplify(random.choices(list(random_functions.items()), weights=list(random_functions.keys()), k=1)[0](randomVar()))))

def randomProblem(recur=0.67, simplify=False):
	variable = randomVar()
	f = randomFunc(variable, recur=recur)
	df = sp.diff(f, variable)
	if simplify:
		return (sp.latex(sp.Derivative(sp.simplify(f))), sp.latex(sp.simplify(df)))
	else:
		return (sp.latex(sp.Derivative(f)), sp.latex(df))


if __name__ == "__main__":
	for i in range(10):
		print(randomProblem())

