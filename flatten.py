"""
Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]
"""


def flatten(x):
    
    for i in x:
        if isinstance(i,list): 
            flatten(i)
        else:
            empty_list.append(i)
    
    

x= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
empty_list = [] 
flatten(x)
print(empty_list)