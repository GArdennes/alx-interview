#!/usr/bin/python3
"""
0-rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given a square matrix rotate it 90 degrees clockwise
    """
    for i in range(len(matrix)):
        matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
