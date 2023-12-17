import sys
import math

# Считываем координаты центра окружности и его радиус из первого файла
with open(sys.argv[1], 'r') as file1:
    center_x, center_y = map(float, file1.readline().split())
    radius = float(file1.readline())

# Считываем координаты точек из второго файла
with open(sys.argv[2], 'r') as file2:
    for line in file2:
        point_x, point_y = map(float, line.split())
        distance = math.sqrt((point_x - center_x)**2 + (point_y - center_y)**2)
        if distance < radius:
            print("1")
        elif distance == radius:
            print("0")
        else:
            print("2")
