#!/usr/bin/env python
# coding: utf-8

# In[17]:





# In[71]:


#Generacion De Dados
from random import randint
import matplotlib.pyplot as plot
resultado = list()
tiros = int(input("Ingresar La Cantidad De Tiros: "))
dado1 = [randint(1, 6) for p in range(1, tiros+1)]
print(dado1)
dado2 = [randint(1, 6) for p in range(1, tiros+1)]
print(dado2)
for x in range(0,len(dado1)):
    #print ('Sumatoria en el Lanzamiento',x+1,' :',dado1[x]+dado2[x])
    resultado.append(dado1[x]+dado2[x])   
print('Resultado: ',resultado)
intervalos = range(min(resultado), max(resultado) + 2) 

plot.hist(x=resultado, bins=intervalos, color='#F2AB6D', rwidth=0.85)
plot.title('Histograma')
plot.xlabel('Sumatoria')
plot.ylabel('Frecuencia')
plot.xticks(intervalos)
plot.show() #dibujamos el histograma


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




