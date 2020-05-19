from qgis.core import *

layer = iface.activeLayer()

ext = layer.extent()

minLon = ext.xMinimum() #xmin
maxLon = ext.xMaximum() #xmax
minLat = ext.yMinimum()  #ymin
maxLat = ext.yMaximum() #ymax

transform = QgsCoordinateTransform(QgsCoordinateReferenceSystem(3857),QgsCoordinateReferenceSystem(4326),QgsProject.instance())
#transform = QgsCoordinateTransform(QgsCoordinateReferenceSystem(4326),QgsCoordinateReferenceSystem(3857),QgsProject.instance())
t2, t1 = transform.transform(float(minLon), float(minLat))
t4, t3 = transform.transform(float(maxLon), float(maxLat))

vlayer = iface.activeLayer()
options = QgsMapSettings()
options.setLayers([vlayer])
options.setBackgroundColor(QColor(255, 255, 255))
r = (vlayer.extent().height()/vlayer.extent().width())
print(r)
if r > 1:
    w = (800/r)
    h= 800
else:
    w = 800
    h =  (800*r)
    
options.setOutputSize(QSize(w, h))
CSVout = "%s,%d,%d,%d,%d,%d,%d,%f,%f,%f,%f" %(layer.name()+".bmp",h,w,minLon,maxLon,maxLat,minLat,t1,t2,t3,t4)
MAPcsv = open("./MAPImages/MAPS.csv","a+")
MAPcsv.write("\n"+CSVout)
MAPcsv.close()
    
options.setExtent(vlayer.extent())

render = QgsMapRendererParallelJob(options)

def finished():
    img = render.renderedImage()
    img.save("./MAPImages/"+layer.name()+".bmp","bmp")
    #img.save(image_location, "png")
    print("saved")

render.finished.connect(finished)

render.start()