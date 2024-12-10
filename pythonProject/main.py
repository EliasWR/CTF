import numpy as np

mask = np.array([
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0]
])

pattern = np.array([
    [0, 0, 0, 2, 2, 2, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 1, 2, 1, 0, 0, 0],
    [0, 0, 1, 2, 2, 2, 1, 0, 0],
    [0, 1, 1, 2, 2, 2, 1, 1, 0],
    [0, 1, 1, 2, 2, 2, 1, 1, 0],
    [0, 1, 1, 2, 2, 2, 1, 1, 0],
    [0, 1, 2, 2, 2, 2, 1, 1, 0],
    [0, 1, 2, 2, 3, 2, 1, 1, 0],
    [0, 1, 2, 3, 3, 2, 1, 1, 0],
    [0, 1, 2, 3, 3, 2, 1, 1, 0],
    [0, 1, 2, 3, 3, 2, 1, 1, 0],
    [0, 1, 2, 2, 3, 2, 1, 1, 0],
    [0, 2, 1, 2, 2, 2, 1, 2, 0],
    [0, 3, 1, 1, 2, 1, 1, 3, 0],
    [0, 0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 2, 0, 2, 1, 0, 0],
    [0, 0, 1, 2, 0, 2, 1, 0, 0],
    [0, 0, 2, 2, 0, 2, 2, 0, 0],
    [0, 0, 2, 3, 0, 3, 2, 0, 0],
    [0, 0, 2, 3, 0, 3, 2, 0, 0],
    [0, 0, 2, 3, 0, 3, 2, 0, 0],
    [0, 0, 2, 3, 0, 3, 2, 0, 0],
    [6, 3, 3, 2, 0, 2, 3, 3, 6]
])

def apply_mask(matrix, mask, x, y):
    """
    Beregn poeng for å legge masken på en gitt posisjon.
    """
    rows, cols = mask.shape
    return np.sum(matrix[x:x + rows, y:y + cols] * mask)


def find_best_mask_position(matrix, mask):
    """
    Finn den beste plasseringen for masken for maksimal score.
    """
    max_score = 0
    best_position = (0, 0)

    rows, cols = matrix.shape
    mask_rows, mask_cols = mask.shape

    for i in range(rows - mask_rows + 1):
        for j in range(cols - mask_cols + 1):
            score = apply_mask(matrix, mask, i, j)
            if score > max_score:
                max_score = score
                best_position = (i, j)

    return best_position, max_score


best_position, max_score = find_best_mask_position(pattern, mask)

print(f"Beste posisjon: {best_position}")
print(f"Høyeste poengsum: {max_score}")