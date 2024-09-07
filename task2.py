import sys

path1, path2 = sys.argv[1], sys.argv[2]
file1 = open(path1, 'r')
file2 = open(path2, 'r')
circle = file1.read().split("\n")
points = file2.read().split("\n")
circle_points = circle[0].split(' ')
circle_radius_sqr = float(circle[1])**2
for point in points:
    point = point.split(' ')
    point_expression = (float(point[0]) - float(circle_points[0]))**2 + (float(point[1]) - float(circle_points[1]))**2
    if point_expression < circle_radius_sqr:
        print('1')
    elif point_expression == circle_radius_sqr:
        print('0')
    else:
        print('2')