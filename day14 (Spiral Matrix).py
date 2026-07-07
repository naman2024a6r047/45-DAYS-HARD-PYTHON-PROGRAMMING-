import sys

def spiralOrder(mat):
    if not mat or not mat[0]:
        return []
        
    lis = []
    top = 0
    bottom = len(mat) - 1
    left = 0
    right = len(mat[0]) - 1
    
    while top <= bottom and left <= right:
        # 1. Traverse Right (Top Row)
        for j in range(left, right + 1):
            lis.append(mat[top][j])
        top += 1  # Move top boundary down
        
        # 2. Traverse Down (Right Column)
        for i in range(top, bottom + 1):
            lis.append(mat[i][right])
        right -= 1  # Move right boundary left
        
        # 3. Traverse Left (Bottom Row) - check if row still exists
        if top <= bottom:
            for j in range(right, left - 1, -1):
                lis.append(mat[bottom][j])
            bottom -= 1  # Move bottom boundary up
            
        # 4. Traverse Up (Left Column) - check if column still exists
        if left <= right:
            for i in range(bottom, top - 1, -1):
                lis.append(mat[i][left])
            left += 1  # Move left boundary right
            
    return lis
