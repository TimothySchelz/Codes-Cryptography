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

# set up squeamish ossifrage
p = 3490529510847650949147849619903898133417764638493387843990820577
q = 32769132993266709549961988190834461413177642967992942539798288533
m = p*q
e = 9007
phi = (p-1)*(q-1)
d = modinv(e, phi)
M = 96869613754622061477140922254355882905759991124574319874695120930816298225145708356931476622883989628013391990551829945157815154

# convert to english
messageNumber = ""
messageNumber = messageNumber + str(pow(M, d, m))
messageString = ""
currentLetter = 0
for i in range(0, int(len(messageNumber)/2)):
	currentLetter = int(messageNumber[2*i:(2*i)+2])
	
	if currentLetter == 0:
		messageString = messageString + " "
	else:
		messageString = messageString + chr(currentLetter + 96)
	
#output
print(messageString)

# Lets do some homework

# 4a
a = 26055
p = 34807
root = pow(a,int((p+1)/4), p)
output = "4a: The root of " + str(a) + " mod " + str(p) + " is " + str(root)
check = "check: " + str(pow(root,2,p))
print(output)
print(check)

# 4b
a, p =  576031280, 5986660523
root = pow(a,int((p+1)/4), p)
output = "4b: The root of " + str(a) + " mod " + str(p) + " is " + str(root)
check = "check: " + str(pow(root,2,p))
print(output)
print(check)

# 5
a, p =  48382, 83987
root = pow(a,int((p+1)/4), p)
output = "5: The root of " + str(a) + " mod " + str(p) + " is " + str(root)
check = "check: " + str(pow(root,2,p))
print(output)
print(check)