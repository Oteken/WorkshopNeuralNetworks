# De Numpy package helpt bij het uitvoeren van matrix en array operaties.
import numpy as np

def getRandom():
    return np.random.random(1)[0]

# Dit zijn 4 stukken aan input data, overigens alle mogelijke opties met een logic operation.
# De eerste +1 is een verplichtte waarde
inputData = np.array([[+1, -1, -1],
                   [+1, -1, +1],
                   [+1, +1, -1],
                   [+1, +1, +1]])
# Dit zijn de verwachtte outputs per stuk aan input data. Hier zien we een voorbeeld van een AND operation.
# Alleen de laatste input combinatie is een True, +1.
desiredOutputs = np.array([-1, -1, -1, +1])

# De learningRate(leerTempo) zorgt ervoor dat onze netwerk op een comfortabele oplossing komt en niet blijft overschieten.
learningRate = 0.2

# Dit zijn de gewichten van het netwerk. We hebben drie verbindingen waarvan het gewicht bijgehouden moet worden.
weights = np.array([getRandom(), getRandom(), getRandom()])

# Deze functie geeft aan of onze net waarde aan het einde een true of een false is.
def activationFunction(netValue):
    if(netValue > 0):
        return True
    else:
        return False

# De predict functie berekent de net waarde aan de hand van gegeven inputs en gewichten.
def predict(inputs, weights):
    return inputs.dot(weights)

# De error functie geeft de foutmarge terug.
def errorFunction(desiredOutput, netValue):
    return desiredOutput - netValue

# De train functie geeft de verandering terug die uitgevoerd moet worden op de input verbindingen.
def train(inputs, desiredOutput, weights):
    weightAdjustments = np.array([0.0, 0.0, 0.0])
    prediction = predict(inputs, weights)
    i = 0
    for input in inputs:
        error = errorFunction(desiredOutput, prediction)
        weightAdjustments[i] = (error * learningRate * input)
        i = i + 1
    return weightAdjustments

# De train multiple functie neemt meerdere input waardes en geeft de verandering terug die uitgevoerd moet worden.
def trainMultiple(inputData, desiredOutputData, weights):
    weightAdjustments = np.zeros(shape=(inputData.size, 3))
    # We gaan nu een effectievere manier van trainen uitvoeren.
    # In plaats van dat we met elke input aan data gaan leren, pakken we meerdere inputs.
    # Met deze inputs gaan we vervolgens kijken wat de verandering is en per verbinding het gemiddelde pakken en dit returnen
    meanWeightAdjustment = "Dit is de array die gevuld moet worden tijdens deze functie"

    return meanWeightAdjustment

# De iterations variabele geeft aan hoe vaak we het netwerk willen trainen met dezelfde data.
iterations = 1000

print("Starting weights = ", weights)
for i in range(0, iterations):
    weightAdjustment = trainMultiple(inputData, desiredOutputs, weights)
    weights = weights + weightAdjustment
print("Adjusted weights = ", weights)

# Uitkomst voor input rij één
print(activationFunction(predict(inputData[0], weights)))
# Uitkomst voor input rij twee
print(activationFunction(predict(inputData[1], weights)))
# Uitkomst voor input rij drie
print(activationFunction(predict(inputData[2], weights)))
# Uitkomst voor input rij vier
print(activationFunction(predict(inputData[3], weights)))

# Als de uitkomsten kloppen met de het verwachtte resultaat, dan ben je klaar.
# Dus bij een AND operation is dit False False False True