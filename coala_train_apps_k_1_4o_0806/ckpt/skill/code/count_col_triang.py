
def are_collinear(p1, p2, p3):
    # Calculate the determinant to check if points are collinear
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0

def calculate_triangles(points):
    count = 0
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if not are_collinear(points[i], points[j], points[k]):
                    count += 1
    return count

def count_col_triang(a):
    total_points = len(a)
    color_groups = {}
    
    for point, color in a:
        if color not in color_groups:
            color_groups[color] = []
        color_groups[color].append(point)
    
    total_colors = len(color_groups)
    total_triangles = 0
    max_triangles = 0
    color_with_max_triangles = []
    
    for color, points in color_groups.items():
        num_triangles = calculate_triangles(points)
        total_triangles += num_triangles
        
        if num_triangles > max_triangles:
            max_triangles = num_triangles
            color_with_max_triangles = [color]
        elif num_triangles == max_triangles:
            color_with_max_triangles.append(color)
    
    color_with_max_triangles.sort()
    
    if max_triangles == 0:
        return [total_points, total_colors, total_triangles, []]
    else:
        return [total_points, total_colors, total_triangles, color_with_max_triangles + [max_triangles]]
