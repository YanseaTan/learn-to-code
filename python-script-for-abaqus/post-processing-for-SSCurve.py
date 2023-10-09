x = session.xyPlots['XYPlot-1']
session.viewports['Viewport: 1'].setValues(displayedObject=x)
odb = session.odbs['C:/temp/{}.odb'.format(jobName)]
session.XYDataFromHistory(name='RF2', odb=odb, 
    outputVariableName='Reaction force: RF2 PI: rootAssembly Node 2 in NSET RF2', 
    steps=('Step-1', ), __linkedVpName__='Viewport: 1')
session.XYDataFromHistory(name='U2', odb=odb, 
    outputVariableName='Spatial displacement: U2 PI: rootAssembly Node 1 in NSET RF1', 
    steps=('Step-1', ), __linkedVpName__='Viewport: 1')
xy1 = session.xyDataObjects['U2']
xy2 = session.xyDataObjects['RF2']
xy3 = combine(xy1 / length * typeOfTest, -xy2 / width / depth * typeOfTest)
xy3.setValues(sourceDescription='combine ( "U2"/length, -"RF2"/width/depth )')
tmpName = xy3.name
session.xyDataObjects.changeKey(tmpName, 'stress-strain-curve')
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['stress-strain-curve']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
