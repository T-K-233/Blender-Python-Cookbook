import math

import numpy as np

def getXYZFromMatrix(matrix):
    """
    Extract Euler angles (rotation around x, y, and z axis) from a 4x4 rotation matrix.
    This is with XYZ order, and Y must be in range (-90deg, 90deg)
    
    @param matrix: np.array - A 4x4 numpy array representing the rotation matrix.

    @return: tuple - A tuple containing the Euler angles (rot_x, rot_y, rot_z) in degrees.
    """

    # Ensure the matrix is a numpy array
    matrix = np.array(matrix)

    # Threshold for numerical stability
    threshold = 1e-6

    # Extract angles based on XYZ rotation order
    if abs(matrix[2, 1]) < 1 - threshold:
        rot_x = np.arctan2(matrix[2, 1], matrix[2, 2])
        rot_y = np.arcsin(-matrix[2, 0])
        rot_z = np.arctan2(matrix[1, 0], matrix[0, 0])
    else:
        # Gimbal lock occurs
        rot_z = 0  # Arbitrarily set
        if matrix[2, 1] < -1 + threshold:
            rot_x = -np.pi / 2
            rot_y = np.arctan2(matrix[0, 1], matrix[1, 1])
        else:
            rot_x = np.pi / 2
            rot_y = np.arctan2(-matrix[0, 1], -matrix[1, 1])

    # Convert the angles from radians to degrees
    rot_x = math.degrees(rot_x)
    rot_y = math.degrees(rot_y)
    rot_z = math.degrees(rot_z)

    return rot_x, rot_y, rot_z