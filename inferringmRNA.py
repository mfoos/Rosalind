string = raw_input("Protein Sequence: ")
R = L = S = 6
A = G = P = T = V = 4
I = 3
N = D = H = E = Y = K = F = C = Q = 2
M = W = 1

answer = 3
#because it will have to be multiplied by stop codon possibilities and start codon possibilities, which is 1 x 3
for i in string:
	answer = answer * eval(i)

print answer % 1000000
