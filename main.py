import matplotlib.pyplot as plt
import pandas as pd 
# Beispiel-Daten: Zahlen von 0 bis 9, Quadrat- und Kubikzahlen
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # Zahlen  
y = [i**2 for i in x]              # Quadratzahlen
z = [i**3 for i in x]              # Kubikzahlen

# Liniendiagramm erstellen
plt.plot(x, y, label='Quadratzahlen')
plt.plot(x, z, label='Kubikzahlen' )

# Titel und Achsenbeschriftungen hinzufügen
plt.title('Quadrat- und Kubikzahlen von 0 bis 9')
plt.xlabel('x')
plt.ylabel('y', rotation='horizontal') 

# Legende anzeigen
plt.legend()

# Diagramm als PNG-Datei sppeichern
plt.savefig('diagramm.png',dpi=300) 
# Diagramm anzeigen
plt.show()


# DataFrame erstellen
df = pd.DataFrame({'Zahl':x,'Quadrat':y,'Kubik':z})
df.to_csv('zahlen.csv',index=False)