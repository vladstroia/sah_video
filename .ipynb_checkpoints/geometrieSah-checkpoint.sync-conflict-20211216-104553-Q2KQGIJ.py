import matplotlib.pyplot as plt
# import numpy as np
import math



class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  ## cum sa fie printat punctul
  def __str__(self):
    return str(self.x) + " " + str(self.y)
  def plot(self):
    # plt.plot(self.x,self.y, marker=".", markersize=40,'o', color='black' );
    plt.plot(self.x,self.y, marker=".", markersize= 3  );

class Line:
  def __init__(self, p1, p2):
    self.p1 = p1
    self.p2 = p2
  def eq_a(self):
    return (self.p2.y-self.p1.y)/(self.p2.x-self.p1.x) 
  def eq_b(self):
    return (self.p1.y - self.p1.x * self.eq_a())
  def plot(self):
    plt.plot([self.p1.x,self.p2.x],[self.p1.y,self.p2.y])
  # def __str__(self):
    # return self.p1 + " " + self.p2
    
# zice punctul unde se intalnesc doua linii
def punctDeFuga(line1, line2):
    x = (line2.eq_b() - line1.eq_b()) / ( line1.eq_a() - line2.eq_a() )
    y = line1.eq_a() * x + line1.eq_b()
    point = Point(x,y);
    return point;

# eq dreptei in functie de 2 puncte
# y-y0 = f'(x0)*(x-x0) 
def lineEq(p1, p2, x):
  y = ((p2.y-p1.y)/(p2.x-p1.x))*(x-p1.x)+p1.y
  return y



#ia 2 linii si returneaza unghiul dintre ele
def angleBetweenLines(line1,line2):
    angle = math.atan(line2.eq_a())-math.atan(line1.eq_a())
    # print('angle is ' + str(angle))
    return angle
#ia doua linii si returneaza un array de 9 elemente cu pantele dreptelor care incap intre cele doua linii
# (2 din cele 9 linii sunt liniile cu care am inceput)
def divideAngle(line1,line2):
    small_angle = angleBetweenLines(line1,line2) / (nr_linii -1)
    start_angle = math.atan(line1.eq_a())
    slopes = [math.tan(start_angle + i*small_angle) for i in range(nr_linii)]
    return slopes
def lineByPointAndSlope(point,slope):
    x = point.x + 1
    y = point.y+ slope
    point2 = Point(x,y)
    line = Line(point, point2)
    return line

def getInnerSquareCoordinates(corners):
    table_lines= [Line(corners[0],corners[1]),Line(corners[1],corners[2]),
              Line(corners[2],corners[3]), Line(corners[3],corners[0])]
    lines = [[],[]]
    puncte_de_fuga = [punctDeFuga(table_lines[0],table_lines[2]), punctDeFuga(table_lines[1],table_lines[3])]
    pante = [divideAngle(table_lines[0], table_lines[2]), divideAngle(table_lines[1], table_lines[3])]
    nr_linii = 17
    for i in range(nr_linii):
      if i % 2 == 1:
        lines[0].append(lineByPointAndSlope(puncte_de_fuga[0],pante[0][i]))
        lines[1].append(lineByPointAndSlope(puncte_de_fuga[1],pante[1][i]))
    patrate= [ [punctDeFuga(lines[0][i], lines[1][j]) for j in range(8)] for i in range(8)]
    return patrate




########################################
 ## INPUT VARIABLE -- corners
########################################
# corners = [Point(5,4),Point(8,2),Point(10,3.6),Point(7,5)]

# patrate = getInnerSquareCoordinates(corners)



# ######################################
#     ###Plotting
# ####################################
# for i in range(8):
#   for j in range(8):
#     patrate[i][j].plot()
# plt.subplots(figsize=(18, 18))
# # axes.set_aspect(1./axes.get_data_ratio())
# plt.axis('equal')
# # plt.plot([puncte_de_fuga[0].x,corners[1].x],[puncte_de_fuga[0].y,corners[1].y])
# # plt.plot([puncte_de_fuga[0].x,corners[2].x],[puncte_de_fuga[0].y,corners[2].y])
# # plt.plot([puncte_de_fuga[1].x,corners[0].x],[puncte_de_fuga[1].y,corners[0].y])
# # plt.plot([puncte_de_fuga[1].x,corners[1].x],[puncte_de_fuga[1].y,corners[1].y])
# plt.plot(figsize=(18, 18))
# plt.show()