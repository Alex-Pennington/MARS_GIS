	
from qgis.core import *
names = [layer for layer in QgsProject.instance().mapLayers().values()]

for layerName in names:
    layer = layerName
    ext = layer.extent()

    t2 = ext.xMinimum() #xmin
    t4 = ext.xMaximum() #xmax
    t1 = ext.yMinimum()  #ymin
    t3 = ext.yMaximum() #ymax
    coords = "%f,%f,%f,%f" %(t2, t4, t1, t3)
    transform = QgsCoordinateTransform(QgsCoordinateReferenceSystem(4326),QgsCoordinateReferenceSystem(3857),QgsProject.instance())
    minLon, minLat = transform.transform(float(t2), float(t1))
    maxLon, maxLat = transform.transform(float(t4), float(t3))
    mincoordsT = "%f,%f" %(minLon,minLat)
    maxcoordsT = "%f,%f" %(maxLon,maxLat)
    CSVout = "%s,%f,%f,%f,%f,%f,%f,%f,%f" %(layer.name()+".bmp",minLon,maxLon,maxLat,minLat,t1,t2,t3,t4)
    print(CSVout)
    options = QgsMapSettings()
    options.setLayers([layer])
    options.setBackgroundColor(QColor(255, 255, 255))
    options.setOutputSize(QSize(800, 600))
    options.setExtent(layer.extent())
    render = QgsMapRendererSequentialJob(options)
    render.start()
    img = render.renderedImage()
    img.save("D:/GRASS_GIS_DB/MAPImages/"+layer.name()+".png","png")
    print("saved")
    render = QgsMapRendererParallelJob(options)
    


