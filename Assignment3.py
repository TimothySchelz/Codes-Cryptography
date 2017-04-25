import math

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def jacobi(a,b):
	num = int(a%b)
	den = int(b)
	
	if num == 1 or num ==0 :
		return 1;
	
	if num == 2 :
		if den%8 == 1 or den%8 ==-1 :
			return 1
		else :
			return -1
			
	if num == den-1 :
		if den%4 == 1 :
			return 1
		else :
			return -1
		
	if num%4 == 1 or den%4 == 1 :
		return jacobi(den, num)
	else :
		return -1*jacobi(den, num)
		
def primefactorization(a):
	num = int(a)
	
	output = ""
	
	isprime = 1
	for i in range(2, num - 1) :
		if num%i == 0 :
			output += str(i)
			output += "*"
			output += primefactorization(num/i)
			isprime = 0
			break
	
	if isprime == 1 :
		output += str(num)
		
	return output 
	
#Assignment 3

#Q1
print("\n\nQ1")
#Factoring m using Fermat Factorization Method

# Find a close square
M = 8059008699
e = 113
m = 10993522499
for i in range(1, 100) :
	number = m + i**2
	root = math.sqrt(number)
	
	#Check if square
	if root**2 == number:
		factor = egcd(m, root - i)[0]
		break
		
print("A factor!:\t" + str(factor))
print("The other one:\t" + str(factor + 2))

mod = (factor-1)*(factor+1)
d = int(modinv(e, mod))
message = pow(M,d,m)

print("The decoder is:\t" + str(d))
print("The message is:\t" + str(message))

#Q2
print("\n\nQ2")
m = 64777
a = pow(255, 2, m)
b = pow(317, 2, m)
print("255^2 = " + str(a))
print("217^2 = " + str(b))

c = 255*317%m
c = (c - ((2**5)*3*31)%m)%m

factor = egcd(c, m)[0]
print("Factor!:\t" + str(factor))
print("Another one:\t" + str(m/factor))

#Q3
print("\n\nQ3")

n = 46698343
rootn = math.floor(math.sqrt(n))

for i in range(50) :
	number = rootn + i
	square = pow(number, 2, n)
	factorization = primefactorization(square)
	print(str(number) + "^2 = " + str(square) + " = " + factorization)
	
something = 6845*6861-2*3*3*31*433
hopefully = egcd(something, n)[0]

print("\n" + str(hopefully))

	
#Q5
print("\n\nQ5")

n = 3599
for i in range(2, 20) :
	jac = jacobi(i,n)
	euler = pow(i,int((n-1)/2), n)
	
	if jac%n != euler :
		print("Found mismatch!")
		print("a = " + str(i) + "\tjacobi = " + str(jac) + "\tEuler = " + str(euler))
		

	
#Q6
print("\n\nQ6")

p = 5643653
a = 1892117
number = (2*a*pow(4*a, int((p-5)/8), p))%p
other = (-1* number)%p
print(str(number) + " , " + str(other))

#Q10
print("\n\nQ10")

for i in range(0, 19) :
	num = (pow(i,3,19) + 8)%19
	jac = jacobi(num, 19)
	
	root1 = "--"
	root2 = "--"
	if jac == 1 :
		root1 = pow(i,5,19)
		root2 = (-root1)%19
	
	print(str(i) + "\t" + str(num) + "\t" + str(root1) + ", " + str(root2))