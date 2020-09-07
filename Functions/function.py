import sympy as sp
import random

common_variables = sp.symbols("a x y z theta", real=True)
variables = sp.symbols("a b c d k m n p q r s t w alpha beta gamma", real=True)
variable_weights = [0.3, 0.7]  # variables : common variables

randomVar = lambda: random.choices([random.choice(common_variables), random.choice(variables)], weights=variable_weights, k=1)[0]

# Some functions
random_functions = {  # weight : func
	10: sp.exp,  # e**x
	5: sp.log,
	10: sp.sin,
	10: sp.cos,
	5: sp.tan,
	5: sp.cot,
	3: sp.sec,
	3: sp.csc,
	3: sp.asin,
	3: sp.acos,
	3: sp.atan,
	3: sp.acot,
	1: sp.asec,
	1: sp.acsc,
	10: (lambda x: x ** ( random.choices([2, 3, 4, 5, 6, 7, 8, 9, 10], weights=[10, 6, 6, 6, 5, 4, 3, 3, 3], k=1)[0] )),  # x**a
	5: (lambda x: random.choice([-1, 1]) * random.randint(1, 10))  # random constant term 
}

def randomFuncNoComp(inner):
	return ( random.choices(list(random_functions.values()), weights=list(random_functions.keys()), k=1)[0] )(inner)


def randomFunc(variable, recur=0.67):
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

variable = randomVar()

f = randomFunc(variable)
df = sp.diff(f, variable)

print(sp.latex(sp.simplify(f)))
print(sp.latex(sp.simplify(df)))

