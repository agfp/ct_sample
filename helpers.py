import matplotlib.pyplot as plt

def fit_edges(imageCoords, image_width, image_height):
    coords = []
    for i in range(0,len(imageCoords)):
        x = imageCoords[i][0]
        if (x < 0): x = 0
        if (x > image_width): x = image_width

        y = imageCoords[i][1]
        if (y < 0): y = 0
        if (y > image_height): y = image_height

        coords.append([x, y])
    return coords


def trim(coords, image_width, image_height):
    filteredCoords = []
    for idx in range(0, len(coords)):
        if idx != 0 and idx != len(coords)-1:
            if ((coords[idx][0]  == 0 and 
                coords[idx-1][0] == 0 and 
                coords[idx+1][0] == 0) 
                or
                (coords[idx][0]  == image_width and 
                coords[idx-1][0] == image_width and 
                coords[idx+1][0] == image_width) 
                or
                (coords[idx][1]  == 0 and 
                coords[idx-1][1] == 0 and 
                coords[idx+1][1] == 0) 
                or
                (coords[idx][1]  == image_height and 
                coords[idx-1][1] == image_height and 
                coords[idx+1][1] == image_height)):
                continue
        filteredCoords.append(coords[idx])
    return filteredCoords


def plot(image_path, results):
    x = []
    y = []
    for result in results:
        for i in range(0,len(result)):
            x.append(result[i][0])
            y.append(result[i][1])

    plt.plot(x, y)
    plt.title(image_path)
    img = plt.imread(image_path)
    imgplot = plt.imshow(img)
    plt.show()