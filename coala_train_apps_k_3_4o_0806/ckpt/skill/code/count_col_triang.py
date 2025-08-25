
def are_collinear(p1, p2, p3):
    # Calculate the determinant to check if points are collinear
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0

def count_col_triang(points):
    from itertools import combinations
    
    # Group points by color
    color_groups = {}
    for point, color in points:
        if color not in color_groups:
            color_groups[color] = []
        color_groups[color].append(point)
    
    total_points = len(points)
    total_colors = len(color_groups)
    total_triangles = 0
    max_triangles = 0
    max_color = []

    # Calculate triangles for each color
    for color, points_of_color in color_groups.items():
        num_points = len(points_of_color)
        triangles = 0

        # Check all combinations of 3 points
        for p1, p2, p3 in combinations(points_of_color, 3):
            if not are_collinear(p1, p2, p3):
                triangles += 1

        total_triangles += triangles

        # Determine if this color has the maximum number of triangles
        if triangles > max_triangles:
            max_triangles = triangles
            max_color = [color]
        elif triangles == max_triangles:
            max_color.append(color)

    # Sort colors with the maximum number of triangles
    max_color.sort()

    # If no triangles are formed, return an empty list for colors
    if max_triangles == 0:
        return [total_points, total_colors, total_triangles, []]

    return [total_points, total_colors, total_triangles, max_color + [max_triangles]]
