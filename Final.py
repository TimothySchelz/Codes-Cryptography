#Final Exam!
import math
# The first entry of the return value is the gcd
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

#finds the inverse of a mod m
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


#Calculates the jacobi symbol for (a/b)
def jacobi(a, b):
    if (b%2 == 0) or (b < 0):
        raise Exception('b must be a positive odd number')
    if (a == 0) or (a == 1): return a
    a, t = a%b, 1
    while a != 0:
        while not a & 1:
            a /= 2
            if b & 7 in (3, 5): t *= -1
        a, b = b, a
        if (a & 3 == 3) and (b & 3) == 3: t *= -1
        a %= b
    return t if b == 1 else 0

# 2nd grade factoring method
def factor(x):
  factors = []
  i = 2
  while x > 1:
    if x % i == 0:
      x = x / i
      factors.append(i)
    else:
       i = i+1
  return factors


print("!!!Final Exam!!!")


# Question 1

print("\nQuestion 1\n")

n = 601
numOfPrim = 0
primroot = 0;

for i in range(1, 601):

    isPrimitiveRoot = True

    if (pow(i, 2**3*3*5,n) == 1):
        isPrimitiveRoot = False

    if (pow(i, 2**4*5,n) == 1):
        isPrimitiveRoot = False

    if (pow(i, 2**4*3,n) == 1):
        isPrimitiveRoot = False

    if (isPrimitiveRoot):
        numOfPrim += 1
        print(str(i))

        if(primroot == 0):
            primroot = i

print("Number of primitive roots mod " + str(n) + " is : " + str(numOfPrim))
print("I found that "+str(primroot)+ " is a primitive root by taking it to " +
      "the power 600/q mod 601 for every q that divides 600");


# Question 2
print("\nQuestion 2\n")

print(str(6*12*18))

print("The number of elements in (Z/1729)^x is 1296")

n = 1729
numOfWit = 0
for i in range(1, n):
    j = jacobi(i,n)
    e = pow(i,(n-1)/2, n)
    if(j%n != (e)%n):
        print(str(i) + "\t"+str(e)+" =/= "+str(j))
        numOfWit += 1

print("The number of SS witnesses is: " + str(numOfWit))


# Question 3
print("\nQuestion 3\n")

M = 2415782808
e = 17
n=2593863379
rootn = math.floor(math.sqrt(n))

for i in range(1, 1000000):
  number=int(rootn+i);
  square = pow(number, 2, n)
  # check if we have a square
  if (math.floor(math.sqrt(square))**2) == square :

  	factors = factor(square)
  	

	# Multiply the factors of the root
	subtr = 1;
	for i in range(0, len(factors)):
		if i%2 == 0:
			subr = subtr*(factors[i])
	
	Factor = egcd(number - subr, n)[0]
	
	# Print out the successes
	if (Factor != 1 and Factor != n):
		print (number)
		print(str(factors))
		print("Possible Factor:\t\t\t" + str(Factor))

print("This shows that gcd(662051-50423, n) = 50969 and so 50969 is a factor")
p = 50969
q = 50891 #python is being stupid and randomly changing values of variables!!!
print("The other factor is: " + str(q))

pmin1 = p - 1
qmin1 = q - 1
pmin1qmin1 = pmin1*qmin1
print("p-1 = " + str(pmin1))
print("q-1 = " + str(qmin1))
d = modinv(e, pmin1qmin1)
print("d = " + str(d))
message = pow(M, d, n)
print("The message is:\n" + str(message))

# Question 4
print("\nQuestion 4\n")
# This doesn't work!!!!!!!!!!!!!!!!!

n = 7#9999999900000001
nmin1 = n-1
rootn = math.sqrt(n)
Factors = factor(nmin1)
print(str(Factors))

#construct s and r
s = 1
r = 1
i = 0
sFactors = []
rFactors = []
sFactors.append(1)
rFactors.append(1)


for i in range(0, len(Factors)):
	if(s<=rootn):
		s = s*Factors[i]
		sFactors.append(Factors[i])
	else:
		r = r*Factors[i]
		rFactors.append(Factors[i])

print("s = " + str(s))
print("r = " + str(r))

print("Before Test, after getting s,r")
# Grab "random b" and construct a
for b in range(0,3):
	a = pow(b,r)

	#check a's order
	if(pow(a,s,n) != 1):
		continue

	print("Before Inner Loop")
	gcdWorksSoFar = True
	#Check gcds
	for q in sFactors:
		print("q = " + str(q))
		if (egcd(pow(a,s/q)-1, n)[0] != 1):
			gcdWorksSoFar = False
			print("Hit Break")
			break
		print("gcd == 1")

	print("After Inner Loop")

	if(gcdWorksSoFar == False):
		continue

	print(str(n) + " is prime!")
	print("s = " + str(s) + " = " + str(sFactors))
	print("a = " + str(a))




# Question 4
print("\nQuestion 6\n")

print("Done")