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
agMaterial = 'T'        # 骨料材料名称
jobName = 'T0508-03s-c' # 作业名称

length = 100            # 试件长度
width = 100             # 试件宽度
depth = 100             # 试件厚度
diameter_1 = 8          # 骨料直径1
dopingRate_1 = 0.068    # 骨料掺率1
diameter_2 = 6.5        # 骨料直径2
dopingRate_2 = 0.066    # 骨料掺率2
diameter_3 = 5          # 骨料直径3
dopingRate_3 = 0.066    # 骨料掺率3
agElastic = 20000       # 骨料弹性模量
agPoisson = 0.2         # 骨料泊松比
agDensity = 1.73e-9     # 骨料密度

stepTime = 0.3          # 分析步时间
typeOfTest = -1         # 试验种类，拉伸为 1，压缩为 -1
elongation = 0.02       # 延伸率，拉伸建议为 0.1，压缩建议为 0.02
seedSize = 2.0          # 网格细度
numOfCPU = 12           # 电脑 CPU 核心数，建议根据自己电脑配置尽量设高一点

# 作用面参考点
myModel = mdb.models[modelName]
myAssembly = myModel.rootAssembly
myAssembly.ReferencePoint(point=(width / 2, length, depth / 2))
myAssembly.ReferencePoint(point=(width / 2, 0, depth / 2))
r1 = myAssembly.referencePoints
refPoints1=(r1[1], )
myAssembly.Set(referencePoints=refPoints1, name='rf1')
r2 = myAssembly.referencePoints
refPoints2=(r2[2], )
myAssembly.Set(referencePoints=refPoints2, name='rf2')

# 创建部件
## 基体
mysketch_1 = myModel.ConstrainedSketch(name='mysketch_1', sheetSize=200.0)
mysketch_1.rectangle(point1=(0.0, 0.0), point2=(width, length))
myPart = myModel.Part(name=baseName, dimensionality=THREE_D, type=DEFORMABLE_BODY)
myPart.BaseSolidExtrude(sketch=mysketch_1, depth=depth)
del mysketch_1

## 骨料
for diameter in [diameter_1, diameter_2, diameter_3]:
    partName = agName + "-{}".format(int(diameter))
    mysketch_2 = myModel.ConstrainedSketch(name='mysketch_2', sheetSize=200.0)
    mysketch_2.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
    curve = mysketch_2.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(diameter/2.0, 0.0))
    mysketch_2.autoTrimCurve(curve1=curve, point1=(-diameter/2.0, 0.0))
    mysketch_2.Line(point1=(0.0, diameter / 2.0), point2=(0.0, -diameter / 2.0))
    myPart2 = myModel.Part(name=partName, dimensionality=THREE_D, type=DEFORMABLE_BODY)
    myPart2.BaseSolidRevolve(sketch=mysketch_2, angle=360.0, flipRevolveDirection=OFF)
    del mysketch_2

# 材料属性
## 基体
mdb.models[modelName].Material(name=baseMaterial)
mdb.models[modelName].materials[baseMaterial].ConcreteDamagedPlasticity(table=((30.0, 0.1, 1.16, 0.667, 0.0005), ))
mdb.models[modelName].materials[baseMaterial].concreteDamagedPlasticity.ConcreteCompressionHardening(
    table=((1.25, 0.0), (58.44923154, 0.001962031), (61.31519274, 0.002347392), 
    (63.36230789, 0.002765508), (64.59057697, 0.003216377), (65.0, 0.0037), (
    63.17518248, 0.004272993), (61.35036496, 0.004845985), (43.10218978, 
    0.010575912), (32.15328467, 0.014013869), (15.0, 0.0194), (15.0, 0.0294)))
mdb.models[modelName].materials[baseMaterial].concreteDamagedPlasticity.ConcreteTensionStiffening(
    table=((3.0, 0.0), (9.6, 0.099616), (9.428, 0.10162288), (9.256, 
    0.10362976), (1.0, 0.19996)))
mdb.models[modelName].materials[baseMaterial].concreteDamagedPlasticity.ConcreteCompressionDamage(
    table=((0.0, 0.0), (0.262630498, 0.001962031), (0.285185381, 0.002347392), 
    (0.308475527, 0.002765508), (0.332577903, 0.003216377), (0.357583926, 
    0.0037), (0.390394619, 0.004272993), (0.420201429, 0.004845985), (
    0.625607528, 0.010575912), (0.710067465, 0.014013869), (0.826794919, 
    0.0194), (0.858578644, 0.0294)))
mdb.models[modelName].materials[baseMaterial].concreteDamagedPlasticity.ConcreteTensionDamage(
    table=((0.0, 0.0), (0.938032266, 0.099616), (0.939194943, 0.10162288), (
    0.940334264, 0.10362976), (0.985857864, 0.19996)))
mdb.models[modelName].materials[baseMaterial].Elastic(table=((25000.0, 0.2), ))
mdb.models[modelName].materials[baseMaterial].Density(table=((1.93e-09, ), ))
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
for diameter in [diameter_1, diameter_2, diameter_3]:
    partName = agName + "-{}".format(int(diameter))
    p = mdb.models[modelName].parts[partName]
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = regionToolset.Region(cells=cells)
    p.SectionAssignment(region=region, sectionName=agMaterial, offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)

# 骨料接触判定函数
def interCheck(point, center, radius1, radius2):
    sign = True
    for p in center:
        if sqrt((point[0] - p[0])**2 + (point[1] - p[1])**2 + (point[2] - p[2])**2) <= (radius1 + radius2 + 1):
            sign = False
            break
    return sign

# 计算骨料随机投放坐标
count_1 = 1
center_1 = []
radius_1 = diameter_1 / 2
while True:
    disX = random.uniform(radius_1 + 1, width - radius_1 - 1)
    disY = random.uniform(radius_1 + 1, length - radius_1 - 1)
    disZ = random.uniform(radius_1 + 1, depth - radius_1 - 1)
    if len(center_1) == 0:
        center_1.append([disX, disY, disZ])
    else:
        if interCheck([disX, disY, disZ], center_1, radius_1, radius_1):
            center_1.append([disX, disY, disZ])
            count_1 += 1
    if count_1 >= length * width * depth * dopingRate_1 / 4 * 3 / math.pi / radius_1 / radius_1 / radius_1:
        break

count_2 = 1
center_2 = []
radius_2 = diameter_2 / 2
while True:
    disX = random.uniform(radius_2 + 1, width - radius_2 - 1)
    disY = random.uniform(radius_2 + 1, length - radius_2 - 1)
    disZ = random.uniform(radius_2 + 1, depth - radius_2 - 1)
    if len(center_2) == 0:
        center_2.append([disX, disY, disZ])
    else:
        if interCheck([disX, disY, disZ], center_2, radius_2, radius_2):
            if interCheck([disX, disY, disZ], center_1, radius_2, radius_1):
                center_2.append([disX, disY, disZ])
                count_2 += 1
    if count_2 >= length * width * depth * dopingRate_2 / 4 * 3 / math.pi / radius_2 / radius_2 / radius_2:
        break

count_3 = 1
center_3 = []
radius_3 = diameter_3 / 2
while True:
    disX = random.uniform(radius_3 + 1, width - radius_3 - 1)
    disY = random.uniform(radius_3 + 1, length - radius_3 - 1)
    disZ = random.uniform(radius_3 + 1, depth - radius_3 - 1)
    if len(center_3) == 0:
        center_3.append([disX, disY, disZ])
    else:
        if interCheck([disX, disY, disZ], center_3, radius_3, radius_3):
            if interCheck([disX, disY, disZ], center_2, radius_3, radius_2):
                if interCheck([disX, disY, disZ], center_1, radius_3, radius_1):
                    center_3.append([disX, disY, disZ])
                    count_3 += 1
    if count_3 >= length * width * depth * dopingRate_3 / 4 * 3 / math.pi / radius_3 / radius_3 / radius_3:
        break

# 装配
## 基体
myAssembly.Instance(name=baseName, part = myModel.parts[baseName], dependent=ON)

## 骨料
instances1 = []
partName = agName + "-{}".format(int(diameter_1))
for index in range(len(center_1)):
    myAssembly.Instance(name='tmpAg-1-{}'.format(index), part=myModel.parts[partName], dependent=ON)
    myAssembly.translate(instanceList=('tmpAg-1-{}'.format(index),), vector=tuple(center_1[index]))
    instances1.append(myAssembly.instances['tmpAg-1-{}'.format(index)])

partName = agName + "-{}".format(int(diameter_2))
for index in range(len(center_2)):
    myAssembly.Instance(name='tmpAg-2-{}'.format(index), part=myModel.parts[partName], dependent=ON)
    myAssembly.translate(instanceList=('tmpAg-2-{}'.format(index),), vector=tuple(center_2[index]))
    instances1.append(myAssembly.instances['tmpAg-2-{}'.format(index)])

partName = agName + "-{}".format(int(diameter_3))
for index in range(len(center_3)):
    myAssembly.Instance(name='tmpAg-3-{}'.format(index), part=myModel.parts[partName], dependent=ON)
    myAssembly.translate(instanceList=('tmpAg-3-{}'.format(index),), vector=tuple(center_3[index]))
    instances1.append(myAssembly.instances['tmpAg-3-{}'.format(index)])

session.viewports['Viewport: 1'].assemblyDisplay.geometryOptions.setValues(datumAxes=OFF)

a = mdb.models[modelName].rootAssembly
a.InstanceFromBooleanCut(name='CutBase', 
    instanceToBeCut=mdb.models[modelName].rootAssembly.instances[baseName], 
    cuttingInstances=instances1, originalInstances=DELETE)

cells1, instances2 = [], [myAssembly.instances['CutBase-1'], ]
partName = agName + "-{}".format(int(diameter_1))
for index in range(len(center_1)):
    myAssembly.Instance(name='tmpAg-1-{}'.format(index), part=myModel.parts[partName], dependent=ON)
    myAssembly.translate(instanceList=('tmpAg-1-{}'.format(index),), vector=tuple(center_1[index]))
    cells1.append(myAssembly.instances['tmpAg-1-{}'.format(index)].cells[0:8])
    instances2.append(myAssembly.instances['tmpAg-1-{}'.format(index)])

partName = agName + "-{}".format(int(diameter_2))
for index in range(len(center_2)):
    myAssembly.Instance(name='tmpAg-2-{}'.format(index), part=myModel.parts[partName], dependent=ON)
    myAssembly.translate(instanceList=('tmpAg-2-{}'.format(index),), vector=tuple(center_2[index]))
    cells1.append(myAssembly.instances['tmpAg-2-{}'.format(index)].cells[0:8])
    instances2.append(myAssembly.instances['tmpAg-2-{}'.format(index)])

partName = agName + "-{}".format(int(diameter_3))
for index in range(len(center_3)):
    myAssembly.Instance(name='tmpAg-3-{}'.format(index), part=myModel.parts[partName], dependent=ON)
    myAssembly.translate(instanceList=('tmpAg-3-{}'.format(index),), vector=tuple(center_3[index]))
    cells1.append(myAssembly.instances['tmpAg-3-{}'.format(index)].cells[0:8])
    instances2.append(myAssembly.instances['tmpAg-3-{}'.format(index)])

myAssembly.Set(cells=cells1, name=agMaterial)
myAssembly.Set(cells=myAssembly.instances['CutBase-1'].cells[0:1], name='base')

# 分析步
mdb.models[modelName].ExplicitDynamicsStep(name='Step-1', previous='Initial', 
    timePeriod=stepTime, massScaling=((SEMI_AUTOMATIC, MODEL, AT_BEGINNING, 5.0, 
    1e-05, BELOW_MIN, 0, 0, 0.0, 0.0, 0, None), ), improvedDtMethod=ON)
mdb.models[modelName].fieldOutputRequests['F-Output-1'].setValues(variables=
('S', 'E', 'U','RF','DAMAGEC', 'DAMAGET', 'STATUS'), numIntervals=40)
del mdb.models[modelName].historyOutputRequests['H-Output-1']
regionDef=mdb.models[modelName].rootAssembly.sets['rf2']
mdb.models[modelName].HistoryOutputRequest(name='H-Output-1', 
    createStepName='Step-1', variables=('RF2', ), region=regionDef, 
    sectionPoints=DEFAULT, rebar=EXCLUDE)
regionDef=mdb.models[modelName].rootAssembly.sets['rf1']
mdb.models[modelName].HistoryOutputRequest(name='H-Output-2', 
    createStepName='Step-1', variables=('U2', ), region=regionDef, 
    sectionPoints=DEFAULT, rebar=EXCLUDE)

# 相互作用
mdb.models['Model-1'].ContactProperty('IntProp-1')
mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
    formulation=FRICTIONLESS)
mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(
    pressureOverclosure=HARD, allowSeparation=ON, 
    constraintEnforcementMethod=DEFAULT)
mdb.models['Model-1'].ContactExp(name='Int-1', createStepName='Initial')
mdb.models['Model-1'].interactions['Int-1'].includedPairs.setValuesInStep(
    stepName='Initial', useAllstar=ON)
mdb.models['Model-1'].interactions['Int-1'].contactPropertyAssignments.appendInStep(
    stepName='Initial', assignments=((GLOBAL, SELF, 'IntProp-1'), ))

# 边界条件
region1=regionToolset.Region(referencePoints=refPoints1)
s1 = myAssembly.instances['CutBase-1'].faces
side1Faces1 = s1[1:2]
region2=regionToolset.Region(side1Faces=side1Faces1)
mdb.models[modelName].Coupling(name='Constraint-1', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=OFF, ur2=OFF, ur3=OFF)
region3=regionToolset.Region(referencePoints=refPoints2)
s2 = myAssembly.instances['CutBase-1'].faces
side1Faces2 = s2[3:4]
region4=regionToolset.Region(side1Faces=side1Faces2)
mdb.models[modelName].Coupling(name='Constraint-2', controlPoint=region3, 
    surface=region4, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=OFF, ur2=OFF, ur3=OFF)
mdb.models[modelName].EncastreBC(name='BC-1', createStepName='Initial', 
    region=region3, localCsys=None)


# 增加荷载
mdb.models[modelName].SmoothStepAmplitude(name='Amp-1', timeSpan=STEP, data=((
    0.0, 0.0), (stepTime, 1.0)))
mdb.models[modelName].DisplacementBC(name='load', createStepName='Step-1', 
    region=region1, u1=0.0, u2=typeOfTest * elongation * length, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0, 
    amplitude='Amp-1', fixed=OFF, distributionType=UNIFORM, fieldName='', 
    localCsys=None)

# 合并部件
myAssembly.InstanceFromBooleanMerge(name=mergedName, instances=instances2, 
    keepIntersections=ON, originalInstances=DELETE, domain=GEOMETRY)

# 插入关键字
mdb.models[modelName].keywordBlock.synchVersions(storeNodesAndElements=False)
mdb.models[modelName].keywordBlock.insert(32, """
*CONCRETE FAILURE
0.19996,0.0294,0,0""")

# 划分网格
p = mdb.models[modelName].parts[mergedName]
p.seedPart(size=seedSize, deviationFactor=0.1, minSizeFactor=0.1)
c = p.cells
pickedRegions = c[0:10000]
p.setMeshControls(regions=pickedRegions, elemShape=TET, technique=FREE, 
    allowMapped=False)
elemType1 = mesh.ElemType(elemCode=UNKNOWN_HEX, elemLibrary=EXPLICIT)
elemType2 = mesh.ElemType(elemCode=UNKNOWN_WEDGE, elemLibrary=EXPLICIT)
elemType3 = mesh.ElemType(elemCode=C3D10M, elemLibrary=EXPLICIT)
cells = c[0:10000]
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
