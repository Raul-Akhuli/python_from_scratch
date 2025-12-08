
# to figure out the type of a variable, we can use the type() function

a = 32
t = type(a)
print(t)  # <class 'int'>

b = 32.5
t = type(b)
print(t)


c = "hello"
t = type(c)
print(t)

# now go for the type conversion using int(), float(), str() --> they are called type casting functions

x = "5.78"  # it is string
print(type(x))

y = float(x)   # change to float
print(type(y))



# 😁

p = "hello"
q = float(p)   # not possible to conver string to float

print(type(q))