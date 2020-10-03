# Importing matplotlib
import matplotlib.pyplot as plt

# Data import
raw_data = open('Lab 1 Pasco Data (thermal expansion).csv')

# constants
rad = 2.65/2
tube_len = 411

# Lists of data
data = []

cu_temp = []
bs_temp = []
al_temp = []

cu_len = []
bs_len = []
al_len = []

# splitting the raw data
for element in raw_data:
  data.append(element.split(','))

# copper data
for i in range(83, 803, 20):
  cu_temp.append(float(data[i][1]))
  cu_len.append(round(float(data[i][2])*rad+tube_len, 3))

# brass data
for i in range(163, 1283, 20):
  bs_temp.append(float(data[i][5]))
  bs_len.append(round(float(data[i][6])*rad+tube_len, 3))

# aluminum data
for i in range(103, 983, 20):
  al_temp.append(float(data[i][9]))
  al_len.append(round(float(data[i][10])*rad+tube_len, 3))

# ==GRAPHS==


# copper graph

cu_graph = plt.figure()

cu_graph.add_subplot(1,1,1)
plt.plot(cu_temp, cu_len, 'k.')
plt.title("Length vs temperature of copper tube")
plt.xlabel("Temperature (\u00B0C)")
plt.ylabel("Length of tube (mm)")
plt.xlim(23, 93)
plt.ylim(410.95, 411.75)


# brass graph

bs_graph = plt.figure()

bs_graph.add_subplot(1,1,1)
plt.plot(bs_temp, bs_len, 'k.')
plt.title("Length vs temperature of brass tube")
plt.xlabel("Temperature (\u00B0C)")
plt.ylabel("Length of tube (mm)")
plt.xlim(23, 93)
plt.ylim(410.95, 411.75)


# aluminum graph

al_graph = plt.figure()

al_graph.add_subplot(1,1,1)
plt.plot(al_temp, al_len, 'k.')
plt.title("Length vs temperature of aluminum tube")
plt.xlabel("Temperature (\u00B0C)")
plt.ylabel("Length of tube (mm)")
plt.xlim(23, 93)
plt.ylim(410.95, 411.75)


# save graphs as image files
cu_graph.savefig("copper.png")
bs_graph.savefig("brass.png")
al_graph.savefig("aluminum.png")