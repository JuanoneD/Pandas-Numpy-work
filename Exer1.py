import pandas as pd
import numpy as np
from matplotlib import pyplot as plt 


df = pd.read_csv("Salary_Data.csv").to_numpy()
print("media de salario: "+str(df.mean(0)[1]))
print("media de tempo de trabalho: "+str(df.mean(0)[0]))
print("media de salario de funcionarios com mais de 5 anos: "+str(np.mean(df[df[:,0]>5,1])))

plt.bar(df[:,0],df[:,1],align="center")
plt.title('Grafico Salario por Tempo') 
plt.ylabel('Salario') 
plt.xlabel('Anos')  
plt.show()

print(df[:,1]*1.1)




