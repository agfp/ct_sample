import numpy as np

def parse(data): 
    coordinatesData = []
    for feature in data["features"]:
        coords = feature['geometry']['coordinates']
        for coordList in coords:
            i = 0
            data = np.zeros((len(coordList), 3))
            for coordPair in coordList:
                data[i][0] = coordPair[0]
                data[i][1] = coordPair[1]
                data[i][2] = coordPair[2]
                i+=1
            coordinatesData.append(data)
    return coordinatesData