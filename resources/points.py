from random import choice
from resources.variables import *

MAIN_POINTS = [(WIDTH // 3, HEIGHT * 2 // 3), (WIDTH * 2 // 3, HEIGHT * 2 // 3), (WIDTH // 2, HEIGHT // 3)]


def midpoint(pt1=choice(MAIN_POINTS[:2]), pt2=MAIN_POINTS[2]):
    return (pt1[0] + pt2[0]) // 2, (pt1[1] + pt2[1]) // 2


midpoints = [midpoint()]
