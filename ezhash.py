message = input("ezhash: ") 
cMessage = ''.join(format(ord(a), '08b') for a in message) #
messageLength = len(cMessage) 
blockCount = 1 #iterates based on messageLength Ln 8
nextMultiple = (blockCount*512)-64-1
while messageLength > nextMultiple: #finding multiple of 512 higher than messageLength to determine blockcount
	blockCount += 1
	nextMultiple = (blockCount*512)-64-1 
	##print("messageLength is larger than",nextMultiple,blockCount)
padCount = (512 * blockCount) - 65 - messageLength
gMessage = cMessage + "1" + ("0"*padCount)
messageBlocks = []
for j in range(0, blockCount):
	messageBlocks.append(gMessage[(j * 512):((j+1)*512)])
messageBlocks[-1] += (format(bin(messageLength)[2:], '0>64')) #converts messageLength to 64-bit binary
##print(messageBlocks)
hashValues = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
#initializing Hash values H0-H7 for hash computation
constants = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070, 0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3, 0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]
#initializing constants K0-K63 for hash computation
def choose(x, y ,z):
	return (x & y)^(~x&z)
def majority(x, y, z):
	return (x & y)^(x & z)^(y & z)
def circularRight(x, n):
	return (x >> n) | (x << (32-n))
def logicZero(x):
	return (circularRight(x, 2) ^ circularRight(x, 13) ^ circularRight(x, 22))
def logicOne(x):
	return (circularRight(x, 6) ^ circularRight(x, 11) ^ circularRight(x, 25))
def logicTwo(x):
	return (circularRight(x, 7) ^ circularRight(x, 18) ^ (x >> 3))
def logicThree(x):
	return (circularRight(x, 17) ^ circularRight(x, 19) ^ (x >> 10))
messageSchedule = []
for p in range(0, blockCount):  #loops for each 512 bit block
	for l in range(0, 16):     #repopulates the messageSchedule
		messageSchedule.append(int(messageBlocks[p][l * 32:((l + 1) * 32)], 2))
		#print(l)
	for u in range(16, 64):  #fills rest of messageSchedule with logicFunctions
		messageSchedule.append((logicThree(messageSchedule[u-2]) + (messageSchedule[u-7]) + (logicTwo(messageSchedule[u-15])) + (messageSchedule[u-16]))%2**32)
		#print(u)
	a = hashValues[0] 
	b = hashValues[1] 
	c = hashValues[2]
	d = hashValues[3]
	e = hashValues[4]
	f = hashValues[5]
	g = hashValues[6]
	h = hashValues[7]
	for q in range(0, 64):
		tempOne = (h + logicOne(e) + choose(e, f ,g) + constants[q] + messageSchedule[q])%2**32
		tempTwo = (logicZero(a) + majority(a, b, c))%2**32
		h = g
		g = f
		f = e
		e = (d + tempOne)%2**32
		d = c
		c = b
		b = a
		a = (tempOne + tempTwo)%2**32
	hashValues[0] = (a + hashValues[0])%2**32 
	hashValues[1] = (b + hashValues[1])%2**32
	hashValues[2] = (c + hashValues[2])%2**32
	hashValues[3] = (d + hashValues[3])%2**32
	hashValues[4] = (e + hashValues[4])%2**32
	hashValues[5] = (f + hashValues[5])%2**32
	hashValues[6] = (g + hashValues[6])%2**32
	hashValues[7] = (h + hashValues[7])%2**32
messageDigest = ''.join(format(hex(v)[2:], '0>8') for v in hashValues)  #converting decimal hashValues to hex and concatenating them for printing
print(messageDigest)