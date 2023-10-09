# coding:utf-8
from abaqus import *
from abaqusConstants import *
from caeModules import *
import regionToolset
import math
import random
import job

session.journalOptions.setValues(replayGeometry=INDEX,recoverGeometry=INDEX)

# 输入参数
modelName = 'Model-1'   # 模型名称
baseName = 'Base'       # 基体部件名称
agName = 'Ag'           # 骨料部件名称
mergedName = 'CAECC'    # 试件总体名称
baseMaterial = 'ECC'    # 基体材料名称
agMaterial = 'Glass'    # 骨料材料名称
jobName = 'b10b-10'     # 作业名称

length = 400            # 试件长度
height = 100            # 试件高度
depth = 100             # 试件厚度
diameter = 10           # 骨料直径
dopingRate = 0.1        # 骨料掺率
agElastic = 55000       # 骨料弹性模量
agPoisson = 0.25        # 骨料泊松比
agDensity = 2.5e-9      # 骨料密度

stepTime = 0.4          # 分析步时间
elongation = 0.05       # 延伸率
seedSize = 4.0          # 网格细度
numOfCPU = 6            # 电脑 CPU 核心数，建议根据自己电脑配置尽量设高一点

# 作用面参考点
myModel = mdb.models[modelName]
myAssembly = myModel.rootAssembly
myAssembly.ReferencePoint(point=(length * 3 / 8, height, depth / 2))
myAssembly.ReferencePoint(point=(length * 5 / 8, height, depth / 2))
myAssembly.ReferencePoint(point=(length / 8, 0, depth / 2))
myAssembly.ReferencePoint(point=(length * 7 / 8, 0, depth / 2))
r1 = myAssembly.referencePoints
refPoints1=(r1[1], )
myAssembly.Set(referencePoints=refPoints1, name='rf1')
r2 = myAssembly.referencePoints
refPoints2=(r2[2], )
myAssembly.Set(referencePoints=refPoints2, name='rf2')
r3 = myAssembly.referencePoints
refPoints3=(r3[3], )
myAssembly.Set(referencePoints=refPoints3, name='rf3')
r4 = myAssembly.referencePoints
refPoints4=(r4[4], )
myAssembly.Set(referencePoints=refPoints4, name='rf4')

# 创建部件
## 基体
mysketch_1 = myModel.ConstrainedSketch(name='mysketch_1', sheetSize=800.0)
g = mysketch_1.geometry
mysketch_1.Line(point1=(0.0, 0.0), point2=(0.0, 100.0))
mysketch_1.VerticalConstraint(entity=g[2], addUndoState=False)
mysketch_1.Line(point1=(0.0, 100.0), point2=(145.0, 100.0))
mysketch_1.HorizontalConstraint(entity=g[3], addUndoState=False)
mysketch_1.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
mysketch_1.Line(point1=(145.0, 100.0), point2=(155.0, 100.0))
mysketch_1.HorizontalConstraint(entity=g[4], addUndoState=False)
mysketch_1.ParallelConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
mysketch_1.Line(point1=(155.0, 100.0), point2=(245.0, 100.0))
mysketch_1.HorizontalConstraint(entity=g[5], addUndoState=False)
mysketch_1.ParallelConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
mysketch_1.Line(point1=(245.0, 100.0), point2=(255.0, 100.0))
mysketch_1.HorizontalConstraint(entity=g[6], addUndoState=False)
mysketch_1.ParallelConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
mysketch_1.Line(point1=(255.0, 100.0), point2=(400.0, 100.0))
mysketch_1.HorizontalConstraint(entity=g[7], addUndoState=False)
mysketch_1.ParallelConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
mysketch_1.Line(point1=(400.0, 100.0), point2=(400.0, 0.0))
mysketch_1.VerticalConstraint(entity=g[8], addUndoState=False)
mysketch_1.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
mysketch_1.Line(point1=(400.0, 0.0), point2=(355.0, 0.0))
mysketch_1.HorizontalConstraint(entity=g[9], addUndoState=False)
mysketch_1.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
mysketch_1.Line(point1=(355.0, 0.0), point2=(345.0, 0.0))
mysketch_1.HorizontalConstraint(entity=g[10], addUndoState=False)
mysketch_1.ParallelConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
mysketch_1.Line(point1=(345.0, 0.0), point2=(55.0, 0.0))
mysketch_1.HorizontalConstraint(entity=g[11], addUndoState=False)
mysketch_1.ParallelConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
mysketch_1.Line(point1=(55.0, 0.0), point2=(45.0, 0.0))
mysketch_1.HorizontalConstraint(entity=g[12], addUndoState=False)
mysketch_1.ParallelConstraint(entity1=g[11], entity2=g[12], addUndoState=False)
mysketch_1.Line(point1=(45.0, 0.0), point2=(0.0, 0.0))
mysketch_1.HorizontalConstraint(entity=g[13], addUndoState=False)
mysketch_1.ParallelConstraint(entity1=g[12], entity2=g[13], addUndoState=False)
myPart = myModel.Part(name= baseName, dimensionality=THREE_D, type=DEFORMABLE_BODY)
myPart.BaseSolidExtrude(sketch=mysketch_1, depth=depth)
del mysketch_1

f = myPart.faces
v = myPart.vertices
pickedFaces = f[1:2]
myPart.PartitionFaceByShortestPath(point1=v[11], point2=v[10], faces=pickedFaces)
pickedFaces = f[2:3]
myPart.PartitionFaceByShortestPath(point1=v[6], point2=v[13], faces=pickedFaces)
pickedFaces = f[3:4]
myPart.PartitionFaceByShortestPath(point1=v[13], point2=v[8], faces=pickedFaces)
pickedFaces = f[0:1]
myPart.PartitionFaceByShortestPath(point1=v[2], point2=v[5], faces=pickedFaces)
pickedFaces = f[7:8]
myPart.PartitionFaceByShortestPath(point1=v[21], point2=v[20], faces=pickedFaces)
pickedFaces = f[8:9]
myPart.PartitionFaceByShortestPath(point1=v[18], point2=v[23], faces=pickedFaces)
pickedFaces = f[9:10]
myPart.PartitionFaceByShortestPath(point1=v[20], point2=v[23], faces=pickedFaces)
pickedFaces = f[10:11]
myPart.PartitionFaceByShortestPath(point1=v[22], point2=v[23], faces=pickedFaces)

## 骨料
mysketch_2 = myModel.ConstrainedSketch(name='mysketch_2', sheetSize=200.0)
mysketch_2.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
curve = mysketch_2.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(diameter/2.0, 0.0))
mysketch_2.autoTrimCurve(curve1=curve, point1=(-diameter/2.0, 0.0))
mysketch_2.Line(point1=(0.0, diameter/2.0), point2=(0.0, -diameter/2.0))
myPart2 = myModel.Part(name=agName, dimensionality=THREE_D, type=DEFORMABLE_BODY)
myPart2.BaseSolidRevolve(sketch=mysketch_2, angle=360.0, flipRevolveDirection=OFF)
del mysketch_2

# 材料属性
## 基体
mdb.models[modelName].Material(name=baseMaterial)
mdb.models[modelName].materials[baseMaterial].ConcreteDamagedPlasticity(table=((30.0, 0.1, 1.16, 0.667, 0.0005), ))
mdb.models[modelName].materials[baseMaterial].concreteDamagedPlasticity.ConcreteCompressionHardening(
    table=((1.35, 0.0), (50.35626102, 0.002434953), (52.82539683, 0.002843504), 
    (54.58906526, 0.003278183), (55.64726631, 0.00373899), (56.0, 0.004225926), 
    (54.50364964, 0.004781346), (53.00729927, 0.005336767), (38.04379562, 
    0.010890971), (29.06569343, 0.014223493), (15.0, 0.019444444), (15.0, 
    0.029444444)))
mdb.models[modelName].materials[baseMaterial].concreteDamagedPlasticity.ConcreteTensionStiffening(
    table=((3.3, 0.0), (5.05, 0.049812963), (4.888, 0.051818963), (4.726,
    0.053824963), (1.0, 0.099962963)))
mdb.models[modelName].materials[baseMaterial].concreteDamagedPlasticity.ConcreteCompressionDamage(
    table=((0.0, 0.0), (0.34141683, 0.002434953), (0.361561772, 0.002843504), (
    0.382363416, 0.003278183), (0.403890507, 0.00373899), (0.426224689, 
    0.004225926), (0.455150629, 0.004781346), (0.481409536, 0.005336767), (
    0.661539897, 0.010890971), (0.734745508, 0.014223493), (0.833333333, 
    0.019444444), (0.863917237, 0.029444444)))
mdb.models[modelName].materials[baseMaterial].concreteDamagedPlasticity.ConcreteTensionDamage(
    table=((0.0, 0.0), (0.938838405, 0.049812963), (0.94099592, 0.051818963),
    (0.943066472, 0.053824963), (0.980754991, 0.099962963)))
mdb.models[modelName].materials[baseMaterial].Elastic(table=((27000.0, 0.2), ))
mdb.models[modelName].materials[baseMaterial].Density(table=((2.5e-09, ), ))
mdb.models[modelName].HomogeneousSolidSection(name=baseMaterial, material=baseMaterial, thickness=None)
p = mdb.models[modelName].parts[baseName]
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(cells=cells)
p.SectionAssignment(region=region, sectionName=baseMaterial, offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='',
thicknessAssignment=FROM_SECTION)

## 骨料
mdb.models[modelName].Material(name=agMaterial)
mdb.models[modelName].materials[agMaterial].Elastic(table=((agElastic, agPoisson), ))
mdb.models[modelName].materials[agMaterial].Density(table=((agDensity, ), ))
mdb.models[modelName].HomogeneousSolidSection(name=agMaterial, material=agMaterial, thickness=None)
p = mdb.models[modelName].parts[agName]
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(cells=cells)
p.SectionAssignment(region=region, sectionName=agMaterial, offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='',
thicknessAssignment=FROM_SECTION)

# 骨料接触判定函数
def interCheck(point, center, radius1, radius2):
    sign = True
    for p in center:
        if sqrt((point[0] - p[0])**2 + (point[1] - p[1])**2 + (point[2] - p[2])**2) <= (radius1 + radius2 + 0.2):
            sign = False
            break
    return sign

# 计算骨料随机投放坐标
count = 0
center = []
radius = diameter / 2
while True:
    disX = random.uniform(radius + 0.2, length - radius - 0.2)
    disY = random.uniform(radius + 0.2, height - radius - 0.2)
    disZ = random.uniform(radius + 0.2, depth - radius - 0.2)
    if len(center) == 0:
        center.append([disX, disY, disZ])
    else:
        if interCheck([disX, disY, disZ], center, radius, radius):
            center.append([disX, disY, disZ])
            count += 1
    if count >= length * height * depth * dopingRate / 4 * 3 / math.pi / radius / radius / radius:
        break

# 装配
## 基体
myAssembly.Instance(name=baseName, part = myModel.parts[baseName], dependent=ON)

## 骨料
instances1 = []
for index in range(len(center)):
    myAssembly.Instance(name='tmpAg-{}'.format(index), part=myModel.parts[agName], dependent=ON)
    myAssembly.translate(instanceList=('tmpAg-{}'.format(index),), vector=tuple(center[index]))
    instances1.append(myAssembly.instances['tmpAg-{}'.format(index)])

session.viewports['Viewport: 1'].assemblyDisplay.geometryOptions.setValues(datumAxes=OFF)

a = mdb.models[modelName].rootAssembly
a.InstanceFromBooleanCut(name='CutBase', 
    instanceToBeCut=mdb.models[modelName].rootAssembly.instances[baseName], 
    cuttingInstances=instances1, originalInstances=DELETE)

cells1, instances2 = [], [myAssembly.instances['CutBase-1'], ]
for index in range(len(center)):
    myAssembly.Instance(name='tmpAg-{}'.format(index), part=myModel.parts[agName], dependent=ON)
    myAssembly.translate(instanceList=('tmpAg-{}'.format(index),), vector=tuple(center[index]))
    cells1.append(myAssembly.instances['tmpAg-{}'.format(index)].cells[0:8])
    instances2.append(myAssembly.instances['tmpAg-{}'.format(index)])

myAssembly.Set(cells=cells1, name=agMaterial)
myAssembly.Set(cells=myAssembly.instances['CutBase-1'].cells[0:1], name='base')

# 分析步
mdb.models[modelName].ExplicitDynamicsStep(name='Step-1', previous='Initial', 
    timePeriod=stepTime, massScaling=((SEMI_AUTOMATIC, MODEL, AT_BEGINNING, 5.0, 
    1e-05, BELOW_MIN, 0, 0, 0.0, 0.0, 0, None), ), improvedDtMethod=ON)
mdb.models[modelName].fieldOutputRequests['F-Output-1'].setValues(variables=
('S', 'E', 'U', 'RF','DAMAGEC', 'DAMAGET', 'STATUS'), numIntervals=40)
del mdb.models[modelName].historyOutputRequests['H-Output-1']
regionDef=mdb.models[modelName].rootAssembly.sets['rf1']
mdb.models[modelName].HistoryOutputRequest(name='H-Output-1', 
    createStepName='Step-1', variables=('U2', ), region=regionDef, 
    sectionPoints=DEFAULT, rebar=EXCLUDE)
regionDef=mdb.models[modelName].rootAssembly.sets['rf2']
mdb.models[modelName].HistoryOutputRequest(name='H-Output-2', 
    createStepName='Step-1', variables=('U2', ), region=regionDef, 
    sectionPoints=DEFAULT, rebar=EXCLUDE)
regionDef=mdb.models[modelName].rootAssembly.sets['rf3']
mdb.models[modelName].HistoryOutputRequest(name='H-Output-3', 
    createStepName='Step-1', variables=('RF2', ), region=regionDef, 
    sectionPoints=DEFAULT, rebar=EXCLUDE)
regionDef=mdb.models[modelName].rootAssembly.sets['rf4']
mdb.models[modelName].HistoryOutputRequest(name='H-Output-4', 
    createStepName='Step-1', variables=('RF2', ), region=regionDef, 
    sectionPoints=DEFAULT, rebar=EXCLUDE)

# 接触设置
mdb.models[modelName].ContactProperty('IntProp-1')
mdb.models[modelName].interactionProperties['IntProp-1'].TangentialBehavior(
    formulation=FRICTIONLESS)
mdb.models[modelName].interactionProperties['IntProp-1'].NormalBehavior(
    pressureOverclosure=HARD, allowSeparation=ON, 
    constraintEnforcementMethod=DEFAULT)
mdb.models[modelName].ContactExp(name='Int-1', createStepName='Initial')
mdb.models[modelName].interactions['Int-1'].includedPairs.setValuesInStep(
    stepName='Initial', useAllstar=ON)
mdb.models[modelName].interactions['Int-1'].contactPropertyAssignments.appendInStep(
    stepName='Initial', assignments=((GLOBAL, SELF, 'IntProp-1'), ))

# 相互作用
region1=regionToolset.Region(referencePoints=refPoints1)
s1 = myAssembly.instances['CutBase-1'].faces
side1Faces1 = s1[6:7]
region2=regionToolset.Region(side1Faces=side1Faces1)
mdb.models[modelName].Coupling(name='Constraint-1', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
region3=regionToolset.Region(referencePoints=refPoints2)
s2 = myAssembly.instances['CutBase-1'].faces
side1Faces2 = s2[4:5]
region4=regionToolset.Region(side1Faces=side1Faces2)
mdb.models[modelName].Coupling(name='Constraint-2', controlPoint=region3, 
    surface=region4, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
region5=regionToolset.Region(referencePoints=refPoints3)
s3 = myAssembly.instances['CutBase-1'].faces
side1Faces3 = s3[0:1]
region6=regionToolset.Region(side1Faces=side1Faces3)
mdb.models[modelName].Coupling(name='Constraint-3', controlPoint=region5, 
    surface=region6, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
region7=regionToolset.Region(referencePoints=refPoints4)
s4 = myAssembly.instances['CutBase-1'].faces
side1Faces4 = s4[2:3]
region8=regionToolset.Region(side1Faces=side1Faces4)
mdb.models[modelName].Coupling(name='Constraint-4', controlPoint=region7, 
    surface=region8, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)

# 边界条件
mdb.models[modelName].DisplacementBC(name='BC-1', createStepName='Initial', 
    region=region5, u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=UNSET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
mdb.models[modelName].DisplacementBC(name='BC-2', createStepName='Initial', 
    region=region7, u1=UNSET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=UNSET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)


# 增加荷载
mdb.models[modelName].SmoothStepAmplitude(name='Amp-1', timeSpan=STEP, data=((
    0.0, 0.0), (stepTime, 1.0)))
mdb.models[modelName].DisplacementBC(name='load-1', createStepName='Step-1', 
    region=region1, u1=UNSET, u2=-height * elongation, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET,
    amplitude='Amp-1', fixed=OFF, distributionType=UNIFORM, 
    fieldName='', localCsys=None)
mdb.models[modelName].DisplacementBC(name='load-2', createStepName='Step-1', 
    region=region3, u1=UNSET, u2=-height * elongation, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET,
    amplitude='Amp-1', fixed=OFF, distributionType=UNIFORM, 
    fieldName='', localCsys=None)

# 合并部件
myAssembly.InstanceFromBooleanMerge(name=mergedName, instances=instances2, 
    keepIntersections=ON, originalInstances=DELETE, domain=GEOMETRY)

# 插入关键字
mdb.models[modelName].keywordBlock.synchVersions(storeNodesAndElements=False)
mdb.models[modelName].keywordBlock.insert(47, """
*CONCRETE FAILURE
0,0,0,0.8639""")

# 划分网格
p = mdb.models[modelName].parts[mergedName]
p.seedPart(size=seedSize, deviationFactor=0.1, minSizeFactor=0.1)
c = p.cells
pickedRegions = c[0:count + 2]
p.setMeshControls(regions=pickedRegions, elemShape=TET, technique=FREE, 
    allowMapped=False)
elemType1 = mesh.ElemType(elemCode=UNKNOWN_HEX, elemLibrary=EXPLICIT)
elemType2 = mesh.ElemType(elemCode=UNKNOWN_WEDGE, elemLibrary=EXPLICIT)
elemType3 = mesh.ElemType(elemCode=C3D10M, elemLibrary=EXPLICIT)
cells = c[0:count + 2]
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
p.generateMesh()

# 创建作业
mdb.Job(name=jobName, model=modelName, description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, numDomains=numOfCPU, 
    activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=numOfCPU)
