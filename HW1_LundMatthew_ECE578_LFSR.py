#Matthew Lund
#mtlund@wpi.edu
#ECE 578 Homework 1

import numpy as np
from pylfsr import LFSR

seed = [1,0,0,0,0,1,1,0,0,1] #z9 to z0 (seed goes from z9 to z0)
#state = [1,0,0,1,1,0,0,0,0,1] #z0 to z9 (IGNORE THIS)

fpoly = [2,5,6,7,8,10]
# P(x) = x^10 + x^8 + x^6 + x^5 + x^2 + 1

L = LFSR(fpoly=fpoly,initstate = seed, conf = 'fibonacci', seq_bit_index= 9)
# Generate K-bits
k=512
seq_k  = L.runKCycle(k)

#Gives us the 512 Bitstream
print('-'*128)
print('512 Bitstream of LFSR')   
print(L.arr2str(seq_k))
print('-'*128)



#32 bit keystream XOR'd with given plaintext for ciphertext
plaintext = [1,1,1,0,1,1,0,0,0,0,0,1,1,0,1,1,1,0,1,1,0,1,0,0,1,1,1,1,1,0,1,0]
print('32-bit Plaintext')
print('11101100000110111011010011111010')

L.reset()
seq_keystream = L.runKCycle(32)
print('32-bit Keystream')
print(L.arr2str(seq_keystream))

ciphertext = plaintext ^ seq_keystream
print('32-bit Ciphertext (Plaintexted XOR Keystream)')
print(L.arr2str(ciphertext))
print('-'*128)

decrypted_text = ciphertext ^ seq_keystream
print(L.arr2str(decrypted_text))
print('-'*128)

#To show initial Circuit Diagram
L.reset()
L.info()
L.Viz(show=True, show_labels=False,title='10-Bit LFSR')
