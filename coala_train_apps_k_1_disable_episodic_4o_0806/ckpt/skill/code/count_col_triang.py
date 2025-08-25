
def are_points_collinear(p1, p2, p3):
    # Calculate the determinant to check if points are collinear
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0

def count_col_triang(points):
    from itertools import combinations
    
    # Step 1: Categorize points by color
    color_points = {}
    for point, color in points:
        if color not in color_points:
            color_points[color] = []
        color_points[color].append(point)
    
    # Step 2: Count triangles for each color
    triangle_counts = {}
    total_triangles = 0
    for color, pts in color_points.items():
        if len(pts) < 3:
            triangle_counts[color] = 0
            continue
        
        count = 0
        for p1, p2, p3 in combinations(pts, 3):
            if not are_points_collinear(p1, p2, p3):
                count += 1
        
        triangle_counts[color] = count
        total_triangles += count
    
    # Step 3: Find the color(s) with the maximum number of triangles
    max_triangles = max(triangle_counts.values(), default=0)
    max_colors = [color for color, count in triangle_counts.items() if count == max_triangles]
    max_colors.sort()
    
    # Step 4: Prepare the result
    total_points = len(points)
    total_colors = len(color_points)
    
    if max_triangles > 0:
        result = [total_points, total_colors, total_triangles, max_colors + [max_triangles]]
    else:
        result = [total_points, total_colors, total_triangles, []]
    
    return result
