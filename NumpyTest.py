import numpy as np

randomNumber = np.random.random(1)[0]

matrix = np.array([[+1, randomNumber, -1],
                   [+1, -1, -1]])

net = matrix[0].dot([randomNumber, 2, 3])

print("Done")
