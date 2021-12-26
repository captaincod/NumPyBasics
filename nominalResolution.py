import numpy as np
import matplotlib.pyplot as plt
import math


def max_pixel_length(start_pixels, end_pixels):
    return int(math.sqrt((end_pixels[1] - start_pixels[1]) ** 2 + (end_pixels[0] - start_pixels[0]) ** 2))


results = open('nominalResolution_results.txt', 'w')

for figure_number in range(1, 7):

    results.write(f'Фигура {figure_number}\n')

    raw = open(f'resources/figure{figure_number}.txt')
    lines = []
    for line in raw:
        try:
            lines.append([float(i) for i in line.split()])
        except ValueError:  # just for '#'
            continue

    horizontal_length = int(lines[0][0])
    results.write(f'\tМаксимальная длина по горизонтали: {horizontal_length}\n')
    pixel_length = 0
    image = np.array(lines[1:])
    start = [image.shape[1], image.shape[0]]
    end = [0, 0]
    begin = False
    for i in range(0, image.shape[0] - 1):
        if np.sum(image[i]) == 0:
            continue
        else:
            for j in range(image.shape[1]):
                if image[i][j] > 0:
                    if i < start[1]:
                        start[1] = i
                        start[0] = j
                        begin = True
                if image[i][j] > 0 and image[i][j + 1] == 0:
                    if np.sum(image[i + 1]) == 0:
                        end[0] = j
                        end[1] = i
    if begin:
        pixel_length = max_pixel_length(start, end)
    results.write(f'\tМаксимальная длина по пикселям: {pixel_length}\n')
    if pixel_length > 0:
        results.write(f'\tНоминальное разрешение: {(horizontal_length / pixel_length).__round__(2)}\n')
    else:
        results.write(f'\tНоминальное разрешение: 0\n')

    """
    plt.figure()
    plt.imshow(image)
    plt.show()
    """
    
results.close()
