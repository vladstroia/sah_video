import geometrieSah as gs
import matplotlib.pyplot as plt

# aici trebuie sa pui coordonatele colturilor
corners = [gs.Point(5,4),gs.Point(8,2),gs.Point(10,3.6),gs.Point(7,5)]

# asta e variabila in care vor fi coordonatele centrelor patratelor
patrate = gs.getInnerSquareCoordinates(corners)


######################################
    ###Plotting
####################################
for i in range(8):
  for j in range(8):
    patrate[i][j].plot()
plt.show()
