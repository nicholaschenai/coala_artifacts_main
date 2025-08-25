
def count_col_triang(points):
    from collections import defaultdict
    from itertools import combinations

    # Step 1: Organize points by color
    color_points = defaultdict(list)
    for point in points:
        color_points[point[1]].append(point[0])

    # Step 2: Initialize variables for results
    total_points = len(points)
    unique_colors = len(color_points)
    total_triangles = 0
    triangle_counts = {}

    # Step 3: Calculate triangles for each color
    for color, pts in color_points.items():
        num_points = len(pts)
        if num_points >= 3:
            # Calculate the number of combinations of 3 points
            triangles = 0
            for comb in combinations(pts, 3):
                # Check for collinearity using the determinant method
                x1, y1 = comb[0]
                x2, y2 = comb[1]
                x3, y3 = comb[2]
                if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) != 0:
                    triangles += 1
            triangle_counts[color] = triangles
            total_triangles += triangles

    # Step 4: Determine the maximum triangle count and colors
    max_triangles = 0
    max_colors = []
    for color, count in triangle_counts.items():
        if count > max_triangles:
            max_triangles = count
            max_colors = [color]
        elif count == max_triangles:
            max_colors.append(color)

    # Step 5: Prepare the final output
    if total_triangles == 0:
        return [total_points, unique_colors, total_triangles, []]
    
    max_color_count = triangle_counts[max_colors[0]] if max_colors else 0
    return [total_points, unique_colors, total_triangles, [*sorted(max_colors), max_color_count]]

