import geometrieSah
import matplotlib.pyplot as plt


corners = [Point(5,4),Point(8,2),Point(10,3.6),Point(7,5)]

patrate = getInnerSquareCoordinates(corners)



######################################
    ###Plotting
####################################
for i in range(8):
  for j in range(8):
    patrate[i][j].plot()
plt.subplots(figsize=(18, 18))
# axes.set_aspect(1./axes.get_data_ratio())
plt.axis('equal')
# plt.plot([puncte_de_fuga[0].x,corners[1].x],[puncte_de_fuga[0].y,corners[1].y])
# plt.plot([puncte_de_fuga[0].x,corners[2].x],[puncte_de_fuga[0].y,corners[2].y])
# plt.plot([puncte_de_fuga[1].x,corners[0].x],[puncte_de_fuga[1].y,corners[0].y])
# plt.plot([puncte_de_fuga[1].x,corners[1].x],[puncte_de_fuga[1].y,corners[1].y])
plt.plot(figsize=(18, 18))
plt.show()