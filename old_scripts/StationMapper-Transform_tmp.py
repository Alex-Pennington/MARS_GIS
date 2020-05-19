	
from qgis.core import *

layer = iface.activeLayer()

ext = layer.extent()

t2 = ext.xMinimum() #xmin
t4 = ext.xMaximum() #xmax
t1 = ext.yMinimum()  #ymin
t3 = ext.yMaximum() #ymax
coords = "%f,%f,%f,%f" %(t2, t4, t1, t3)

#print(coords)

#transform = QgsCoordinateTransform(QgsCoordinateReferenceSystem(4326),QgsCoordinateReferenceSystem(3857))
transform = QgsCoordinateTransform(QgsCoordinateReferenceSystem(4326),QgsCoordinateReferenceSystem(3857),QgsProject.instance())
minLon, minLat = transform.transform(float(t2), float(t1))
maxLon, maxLat = transform.transform(float(t4), float(t3))
mincoordsT = "%f,%f" %(minLon,minLat)
maxcoordsT = "%f,%f" %(maxLon,maxLat)
#print(mincoordsT)
#print(maxcoordsT)

CSVout = "%s,%s,%s,%d,%d,%d,%d,%f,%f,%f,%f" %(layer.name()+".bmp","800","600",minLon,maxLon,maxLat,minLat,t1,t2,t3,t4)
MAPcsv = open("D:/GRASS_GIS_DB/MAPImages/MAPS.csv","a+")
MAPcsv.write("\n"+CSVout)
MAPcsv.close()
print(CSVout)


#image_location = "D:/GRASS_GIS_DB/render.png"

vlayer = iface.activeLayer()
options = QgsMapSettings()
options.setLayers([vlayer])
options.setBackgroundColor(QColor(255, 255, 255))
options.setOutputSize(QSize(800, 600))
options.setExtent(vlayer.extent())

render = QgsMapRendererParallelJob(options)

def finished():
    img = render.renderedImage()
    img.save("D:/GRASS_GIS_DB/MAPImages/"+layer.name()+".bmp","bmp")
    #img.save(image_location, "png")
    print("saved")

render.finished.connect(finished)

render.start()