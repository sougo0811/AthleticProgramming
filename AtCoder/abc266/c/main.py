import numpy as np
import sys
input = sys.stdin.readline

Ax,Ay = map(int,input().split())
Bx,By = map(int,input().split())
Cx,Cy = map(int,input().split())
Dx,Dy = map(int,input().split())

triangle_ABC = [[Ax,Ay],[Bx,By],[Cx,Cy]]
triangle_BCD = [[Bx,By],[Cx,Cy],[Dx,Dy]]
triangle_CDA = [[Cx,Cy],[Dx,Dy],[Ax,Ay]]
triangle_DAB = [[Dx,Dy],[Ax,Ay],[Bx,By]]

def in_triangle(triangle,point_x,point_y):
  a = (triangle[0][0], triangle[0][1])
  b = (triangle[1][0], triangle[1][1])
  c = (triangle[2][0], triangle[2][1])
  d = (point_x, point_y)

  vector_a = np.array(a)
  vector_b = np.array(b)
  vector_c = np.array(c)
  vector_d = np.array(d)

  vector_ab = vector_b - vector_a
  vector_ad = vector_d - vector_a
  vector_bc = vector_c - vector_b
  vector_bd = vector_d - vector_b
  vector_ca = vector_a - vector_c
  vector_cd = vector_d - vector_c

  vector_cross_ab_ad = np.cross(vector_ab, vector_ad)
  vector_cross_bc_bd = np.cross(vector_bc, vector_bd)
  vector_cross_ca_cd = np.cross(vector_ca, vector_cd)

  return vector_cross_ab_ad > 0 and vector_cross_bc_bd > 0 and vector_cross_ca_cd > 0

if in_triangle(triangle_ABC,Dx,Dy) or in_triangle(triangle_BCD,Ax,Ay) or in_triangle(triangle_CDA,Bx,By) or in_triangle(triangle_DAB,Cx,Cy):
  print("No")
else:
  print("Yes")