coordinates = input("Please enter points (format: x1,y1;x2,y2;...): ")
result = coordinates.split(';')

squared_values = []

for point in result:
    coords = point.split(',')
    x = float(coords[0])
    y = float(coords[1])
    
    squared_x = x ** 2
    squared_y = y ** 2
    
    squared_values.append({'squared_x': squared_x, 'squared_y': squared_y})

for i in range(len(squared_values)):
    print(f"Point {i + 1}: {squared_values[i]}")
