#Scrypt para encontrar patrones en el consumo energetico en Corinto y compararlos con los valores promedios de los otros departamentos.
import pandas as pd

c = pd.read_csv("./Electrificacion.csv")
#print(c.head())

meanUsers = c["Total suscriptores urbanos"].mean()
meanUsage = c["Consumo total rural estrato 01"].mean()

#print(meanUsers)
#print(meanUsage)

CorintoRow = c[c.Municipio == "Corinto"]
#print(CorintoRow)
meanUsersR = CorintoRow["Total suscriptores urbanos"].mean()
meanUsageR = CorintoRow["Consumo total rural estrato 01"].mean()
#print(meanUsersR)
#print(meanUsageR)
differenceUsage = meanUsageR-meanUsage
differenceHabitants = meanUsersR-meanUsers
print(differenceUsage)
print(differenceHabitants)