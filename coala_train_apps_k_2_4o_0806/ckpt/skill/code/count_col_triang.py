
def are_collinear(p1, p2, p3):
    # Calculate the determinant to check if points are collinear
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0

def count_col_triang(points):
    from itertools import combinations
    
    # Step 1: Count total points
    total_points = len(points)
    
    # Step 2: Group points by color
    color_groups = {}
    for point, color in points:
        if color not in color_groups:
            color_groups[color] = []
        color_groups[color].append(point)
    
    # Step 3: Count total colors
    total_colors = len(color_groups)
    
    # Step 4: Calculate triangles for each color
    max_triangles = 0
    max_colors = []
    total_triangles = 0
    
    for color, points_of_color in color_groups.items():
        num_points = len(points_of_color)
        triangles = 0
        
        # Check all combinations of 3 points
        for p1, p2, p3 in combinations(points_of_color, 3):
            if not are_collinear(p1, p2, p3):
                triangles += 1
        
        total_triangles += triangles
        
        # Update max triangles and colors
        if triangles > max_triangles:
            max_triangles = triangles
            max_colors = [color]
        elif triangles == max_triangles:
            max_colors.append(color)
    
    # Step 5: Sort max colors alphabetically
    max_colors.sort()
    
    # Step 6: Return the result
    if max_triangles == 0:
        return [total_points, total_colors, total_triangles, []]
    else:
        return [total_points, total_colors, total_triangles, max_colors + [max_triangles]]

