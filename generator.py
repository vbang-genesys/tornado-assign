
def simpleGeneratorFun(): 
	yield 1
	yield 2
	yield 3

x = simpleGeneratorFun() 

print(x.__next__())
print(next(x))

for i in x:
	print(i)