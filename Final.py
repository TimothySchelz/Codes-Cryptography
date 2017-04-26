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

n = 9999999900000001
nmin1 = n-1
rootn = math.sqrt(n)
Factors = factor(nmin1)
print(str(Factors))

print("sqrt(n) = " + str(rootn))

#construct s and r
s = 1
r = 1
i = 0
sFactors = []
rFactors = []
length = len(Factors)
for i in range(1, length + 1):
	if(s<=rootn):
		s = s*Factors[length - i]
		sFactors.append(Factors[length - i])
	else:
		r = r*Factors[length - i]
		rFactors.append(Factors[length - i])

print("s = " + str(s) + " = " + str(sFactors))
print("r = " + str(r) + " = " + str(rFactors))

for i in range(2, 1000000):
	a = pow(i,r,n)
	power = pow(a,s,n)

	gcd1 = egcd(pow(a,s/5,n)-1, n)[0]
	gcd2 = egcd(pow(a,s/11,n)-1, n)[0]
	gcd3 = egcd(pow(a,s/73,n)-1, n)[0]
	gcd4 = egcd(pow(a,s/101,n)-1, n)[0]
	gcd5 = egcd(pow(a,s/137,n)-1, n)[0]


	if (power == 1 and gcd1 == 1 and gcd2 == 1 and gcd3 == 1 and gcd4 == 1 and gcd5 == 1):	
		print("a = " + str(a))
		print("a^s mod n = " + str(power))
		print("gcd(pow(a,s/5,n)-1, n) = " + str(gcd1))
		print("gcd(pow(a,s/11,n)-1, n) = " + str(gcd2))
		print("gcd(pow(a,s/73,n)-1, n) = " + str(gcd3))
		print("gcd(pow(a,s/101,n)-1, n) = " + str(gcd4))
		print("gcd(pow(a,s/137,n)-1, n) = " + str(gcd5))
		print("\n\nn is prime!\n\n")
		break



# Question 6
print("\nQuestion 6\n")



print("Done")
