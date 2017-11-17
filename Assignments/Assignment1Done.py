# De Numpy package helpt bij het uitvoeren van matrix en array operaties.
import numpy as np

def getRandom():
    return np.random.random(1)[0]

# Dit zijn 4 stukken aan input data, overigens alle mogelijke opties met een logic operation.
# De eerste +1 is een verplichtte waarde
inputData = np.array([
                   [+1, -1, -1],
                   [+1, -1, +1],
                   [+1, +1, -1],
                   [+1, +1, +1]])
# Dit zijn de verwachtte outputs per stuk aan input data. Hier zien we een voorbeeld van een AND operation.
# Alleen de laatste input combinatie is een True, +1.
desiredOutputs = np.array([-1, -1, -1, +1])

# De learningRate(leerTempo) zorgt ervoor dat onze netwerk op een comfortabele oplossing komt en niet blijft overschieten.
learningRate = 0.2

# Dit zijn de gewichten van het netwerk. We hebben drie verbindingen waarvan het gewicht bijgehouden moet worden.
weights = np.array([-0.5, 0.5, 0.5])

# Deze functie geeft aan of onze net waarde aan het einde een true of een false is.
def activationFunction(netValue):
    if(netValue > 0):
        return True
    else:
        return False

# De predict functie berekent de net waarde aan de hand van gegeven inputs en gewichten.
def predict(inputs, weights):
    return inputs.dot(weights)

# Dit zijn de net waardes. Reken hier de voorspellingen voor de inputs uit.
prediction1 = predict(inputData[0], weights)
prediction2 = predict(inputData[1], weights)
prediction3 = predict(inputData[2], weights)
prediction4 = predict(inputData[3], weights)

# Uitkomst Alle rijen.
output1 = activationFunction(prediction1)
output2 = activationFunction(prediction2)
output3 = activationFunction(prediction3)
output4 = activationFunction(prediction4)

# Aan het einde van de opdracht print het programma een aantal True en False uit. Om uit te testen of de ingevulde velden goed zijn kan je de
# gewichten invullen als np.array([-0.5, 0.5, 0.5]). De uitkomst is dan uiteindelijk False False False True.
print(output1)
print(output2)
print(output3)
print(output4)

