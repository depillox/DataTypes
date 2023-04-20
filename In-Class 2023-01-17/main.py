#In-class work 2023-01-17

epsilon = 123
zeta = 456
iota = epsilon + zeta
print(iota)

beta = "123"
delta = "456"
gamma = beta + delta #'add' a string and an integer
print(gamma)

x=42
y=1.5
z=x+y
print(z)

zeta = True
foo = zeta + 1 
print(foo)

gamma = True
eta = gamma + 1.5 #Can I add a boolean to a float?
print(eta)

#can I add a boolean to a string? NO!
gamma = True 
beta = 123
delta = gamma + beta
print(delta)

#Store a float in variable epsilon
#Store a float in variable nu
#Divide epsilon by nu, store the result in sigma
#Print the value of sigma to 2 decimal places
epsilon = 1.3
nu = 2.7
sigma = epsilon / nu
print("{:.2f}".format(sigma))


#Introduce the % operator (integer remainder operator/ 'mod' or modulo. Used for data encryption
a = 100
b = 30
c = a % b #c is the remainder of a / b
print("c=", c)

a = 30
b = 100
c = a % b #Integer remainder of 30/100
print("c=", c) 