import numpy as np
from pylfsr import LFSR

state = [1,0,0,0,0,1,1,0,0,1]
fpoly = [10,4,3,1]
L = LFSR(initstate=state,fpoly=fpoly)
L.Viz(show=True, show_labels=False,title='R1')
print('count \t state \t\toutbit \t seq')
print('-'*128)
for _ in range(512):
    print(L.count,L.state,'',L.outbit,sep='\t')
    L.next()
print('-'*128)
print('Output: ',L.seq)