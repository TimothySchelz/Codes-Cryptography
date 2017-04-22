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


# Q1

p, g, X, y = 103, 2, 58, 31
Y = pow(g, y, p)
k = pow(X, y, p)
M1, M2 = (83*k)%p, (72*k)%p
print("Y = "+ str(Y))
print("k = "+ str(k))
print("The encoded message is: " + str(M1) + ", " + str(M2))
print("Also, Y = " + str(Y))


#Q2
print("phi of 103 = 102")
result = pow(2, 51, 103)
print("2^51 = " + str(result) + " mod 103 so 2 is not a generator")


#Q3

print("exponent" + "\t" + "Baby Steps" + "\t" + "Giant X" + "\t\t" + "Giant Y")
babysteps = []
Xsteps = []
Ysteps = []
gnegm = modinv(pow(2,21,421), 421)
print(str(gnegm))

for i in range(0,22):
	baby = pow(2,i,421)
	giantpow = pow(gnegm, i, 421)
	giantX = (229*giantpow)%421
	giantY = (247*giantpow)%421
	babysteps.append(baby);
	Xsteps.append(giantX);
	Ysteps.append(giantY);
	print("" + str(i) + "\t\t" + str(baby) + "\t\t" + str(giantX) + "\t\t" + str(giantY))

# check for any matches
# go through each element of baby steps and check if it matches with anything in Xsteps or Ysteps
for i in range(0,22) :
	for j in range(0,22) :
		if babysteps[i] == Xsteps[j] or babysteps[i] == Ysteps[j]:
			print("Match found: baby step exp = " + str(i) + " giant step exp = " + str(j))

print("done trying to match with baby steps")

for i in range(0,22) :
	for j in range(0,22) :
		if Xsteps[i] == Ysteps[j]:
			print("Match found: Xstep exp = " + str(i) + " Ystep exp = " + str(j))

print("Done matching between x and y")

result1 = pow(247, 200, 421)
result2 = pow(229, 300, 421)

print(str(result1) +"\t" + str(result2))


#Q8
n = 38200901201
k = 4
q = 2387556325
print("a" + "\t\t" + "i" + "\t\t" + "current result")
for a in range(2,4):
	for i in range(0,k):
		currentresult = pow(a, q*2**i,n)
		#if i == 0 and currentresult == -1:
		print(str(a) + "\t\t" + str(i) + "\t\t" + str(currentresult)) 
		
		#if currentresult == 1:
		print(str(a) + "\t\t" + str(i) + "\t\t" + str(currentresult)) 
		
		
		
#Q9
print("\n\n\n\n\n\n\n\n")
something = egcd(18, 12)
print("" + str(something))

n = 9991


for j in range(2, 10):

	a = j
	nflag = 1
	i = 1
	exp = 1
	while nflag == 1:
		a = pow(a,i)
		thing = a-1
		list = egcd(thing, n)
		reglebugle = list[0]
		i = i+1
		
		if reglebugle == n :
			nflag = 0
		
		if reglebugle != 1 and reglebugle != n :
			print("a = " + str(j) + "\t\t"+ "i = " + str(i) + "\t\t"+"factor:\t" + str(reglebugle))
			nflag = 0
		

#Q10
print("\n\n\n\nProblem 10")

n = 35
z = 1+2j

print(str(z.real))
print(str(z.imag))

norm = (z*z.conjugate()).real
gcdlist = egcd(round(norm), n)
gcd = gcdlist[0]

if gcd != 1:
	print("Yo this shit is fucked")
	
nflag = 1
i = 1
left = z
while nflag == 1 and i <= 100:
	left = (left**i)
	realmodded = round(left.real)%n
	imagmodded = round(left.imag)%n
	
	left = complex(realmodded, imagmodded)
	resultlist = egcd(round(left.imag),n)
	result = resultlist[0]
	
	if result == n :
		nflag = 0
	
	
	print("i = " + str(i) +"\t\t" + str(left) +  "\t\t" + str(result))
	
	i = i + 1
	

x = input('What is your name? ')