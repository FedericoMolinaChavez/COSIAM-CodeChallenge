#Scrypt para encontrar patrones en el consumo energetico en Corinto y compararlos con los valores promedios de los otros departamentos.
import pandas as pd

c = pd.read_csv("./Electrificacion.csv")
#print(c.head())

for i,row in c.iterrows():
	print(i,row)