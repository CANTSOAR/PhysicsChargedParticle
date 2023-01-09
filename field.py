import matplotlib.pyplot as plt
import numpy as np

def create_field(charges, xvals, yvals, zvals, size = 5, scale = 10):

  xbounds = [mean(xvals) - size / 2, mean(xvals) + size / 2]
  ybounds = [mean(yvals) - size / 2, mean(yvals) + size / 2]
  zbounds = [mean(zvals) - size / 2, mean(zvals) + size / 2]

  xrange = xbounds[1] - xbounds[0]
  yrange = ybounds[1] - ybounds[0]
  zrange = zbounds[1] - zbounds[0]

  xpos = []
  ypos = []
  zpos = []
  
  i = []
  j = []
  k = []

  konstant = 1
  
  for x in range(scale):
    for y in range(scale):
      for z in range(scale):
        xval = xbounds[0] + xrange * x/(scale - 1)
        yval = ybounds[0] + yrange * y/(scale - 1)
        zval = zbounds[0] + zrange * z/(scale - 1)
        
        xpos.append(xval)
        ypos.append(yval)
        zpos.append(zval)
        
        icharge = 0
        jcharge = 0
        kcharge = 0
        
        for charge in range(len(charges)):
          r = ((xval - xvals[charge]) ** 2 + (yval - yvals[charge]) ** 2 + (zval - zvals[charge]) ** 2) ** (1/2) + .0000000001
          
          icharge += konstant * charges[charge] / r ** 3 * (xval - xvals[charge])
          jcharge += konstant * charges[charge] / r ** 3 * (yval - yvals[charge])
          kcharge += konstant * charges[charge] / r ** 3 * (zval - zvals[charge])

        if abs(icharge) > 1.1 * size/scale or abs(jcharge) > 1.5 * size/scale or abs(kcharge) > 1.5 * size/scale:
          icharge = 0
          jcharge = 0
          kcharge = 0
        
        i.append(icharge)
        j.append(jcharge)
        k.append(kcharge)

  fig = plt.figure()
  plot = fig.add_subplot(111, projection="3d")
  plot.quiver(*[xpos, ypos, zpos],
              *[i, j, k],
              length=1,
              arrow_length_ratio=.1,
              color=magcolors(i, j, k, code = [1, 0, 0]))
  plot.scatter(xvals, yvals, zvals, color = magcolors(charges, [1], [1], code = [1, 1, 0]), linewidths = 3)
  plt.show()

def mean(arr):
  return np.mean(np.array(arr)).tolist()

def magcolors(i, j, k, code = [1, 1, 1]):
  i = np.array(i)
  j = np.array(j)
  k = np.array(k)

  lengths = (i ** 2 + j ** 2 + k ** 2) ** (1/2)
  
  colors = [[code[0] * (1 - length / max(lengths)) ** 4, 1 - code[1] * (1 - length / max(lengths)) ** 4, 1 - code[2] * (1 - length / max(lengths)) ** 4] for length in lengths]
  return colors


while True:
  chargenum = int(input("how many charges: "))
  charges = []
  xpos = []
  ypos = []
  zpos = []

  for charge in range(chargenum):
    charges.append(int(input("charge " + str(charge + 1) + " charge amount: ")))
    xpos.append(int(input("charge " + str(charge + 1) + " x axis position: ")))
    ypos.append(int(input("charge " + str(charge + 1) + " y axis position: ")))
    zpos.append(int(input("charge " + str(charge + 1) + " z axis position: ")))

  size = int(input("how large of a view area? (x by x cube): "))
  scale = int(input("how many arrows in the viewing area? (more will kill comp x_x): "))

  create_field(charges, xpos, ypos, zpos, size, scale)