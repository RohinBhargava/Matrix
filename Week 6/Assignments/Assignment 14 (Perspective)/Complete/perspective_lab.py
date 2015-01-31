from image_mat_util import *

from mat import Mat
from vec import Vec
from matutil import *

from solver import solve

## Task 1
def move2board(v): 
    '''
    Input:
        - v: a vector with domain {'y1','y2','y3'}, the coordinate representation of a point q.
    Output:
        - A {'y1','y2','y3'}-vector z, the coordinate representation
          in whiteboard coordinates of the point p such that the line through the 
          origin and q intersects the whiteboard plane at p.
    '''
    return Vec({'y1','y2','y3'}, { i : v.f[i]/v.f['y3'] for i in v.D })

## Task 2
def make_equations(x1, x2, w1, w2): 
    '''
    Input:
        - x1 & x2: photo coordinates of a point on the board
        - y1 & y2: whiteboard coordinates of a point on the board
    Output:
        - List [u,v] where u*h = 0 and v*h = 0
    '''
    domain = {(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}
    u = Vec(domain, {('y3', 'x1') : w1 * x1, ('y3', 'x2') : w1 * x2, ('y3', 'x3') : w1, ('y1', 'x1') : -x1, ('y1', 'x2') : -x2, ('y1', 'x3') : -1})
    v = Vec(domain, {('y3', 'x1') : w2 * x1, ('y3', 'x2') : w2 * x2, ('y3', 'x3') : w2, ('y2', 'x1') : -x1, ('y2', 'x2') : -x2, ('y2', 'x3') : -1})
    return [u, v]


## Task 3
h = solve(rowdict2mat(make_equations(358, 36, 0, 0) + make_equations(329, 597, 0, 1) + make_equations(592, 157, 1, 0) + make_equations(580, 483, 1, 1) + [Vec({(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}, { ('y1', 'x1') : 1 })]), Vec({i for i in range(9)}, {8 : 1}))
H = Mat( ({'y1', 'y2', 'y3'}, {'x1', 'x2', 'x3'}), { i : h.f[i] for i in h.D })

## Task 4
def mat_move2board(Y):
    '''
    Input:
        - Y: Mat instance, each column of which is a 'y1', 'y2', 'y3' vector 
          giving the whiteboard coordinates of a point q.
    Output:
        - Mat instance, each column of which is the corresponding point in the
          whiteboard plane (the point of intersection with the whiteboard plane 
          of the line through the origin and q).
    '''
    return coldict2mat({v[0] : move2board(v[1]) for v in mat2coldict(Y).items()})

## For Fun
def translate_rectangle_in_image(LT, LB, RT, RB, Scale, Image):
    '''
    Translates an image to make one thing in it viewable.
    Input:
        - LT: Left Top of distorted part of image in tuple form ('x1', 'x2') representing the position from the origin of the image.
        - LB: Left Bottom of distorted part of image in tuple form ('x1', 'x2') representing the position from the origin of the image.
        - RT: Right Top of distorted part of image in tuple form ('x1', 'x2') representing the position from the origin of the image.
        - RB: Right Bottom of distorted part of image in tuple form ('x1', 'x2') representing the position from the origin of the image.
        - Scale: The distance from the origin in terms of the z-axis in an int or float form.
        - Image: The filename of the image to open in string form.
    '''
    (XCoor, colors) = file2mat(Image, ('x1', 'x2', 'x3'))
    h = solve(rowdict2mat(make_equations(LT[0], LT[1], 0, 0) + make_equations(LB[0], LB[1], 0, 1) + make_equations(RT[0], RT[1], 1, 0) + make_equations(RB[0], RB[1], 1, 1) + [Vec({(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}, { ('y1', 'x1') : Scale })]), Vec({i for i in range(9)}, {8 : 1}))
    YCoor = Mat( ({'y1', 'y2', 'y3'}, {'x1', 'x2', 'x3'}), { i : h.f[i] for i in h.D }) * XCoor
    YScreen = mat_move2board(YCoor)
    mat2display(YScreen, colors, ('y1', 'y2', 'y3'), scale=1000, xmin=None, ymin=None)
