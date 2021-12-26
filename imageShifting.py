import numpy as np
import matplotlib.pyplot as plt


def shifting_pixels(first_pixels, second_pixels):
    x = second_pixels[0] - first_pixels[0]
    y = second_pixels[1] - first_pixels[1]
    return [x, y]


results = open('imageShifting_results.txt', 'w')
first_start = []
second_start = []
shifting = 0

for figure_number in range(1, 3):

    raw = open(f'resources/img{figure_number}.txt')
    lines = []
    for line in raw:
        try:
            lines.append([float(i) for i in line.split()])
        except ValueError:  # just for '#'
            continue

    horizontal_length = int(lines[0][0])
    image = np.array(lines[1:])

    start = [image.shape[1], image.shape[0]]
    for i in range(0, image.shape[0] - 1):
        if np.sum(image[i]) == 0:
            continue
        else:
            for j in range(image.shape[1]):
                if image[i][j] > 0:
                    if i < start[1]:
                        start[1] = i
                        start[0] = j

    if figure_number == 1:
        first_start = start
    elif figure_number == 2:
        second_start = start
        shifting = shifting_pixels(first_start, second_start)
        results.write(f'Смещение: {shifting}\n')

    """
    plt.figure()
    plt.imshow(image)
    plt.show()
    """

results.close()
