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
jobName = '9grid-b-t'   # 作业名称

length = 100            # 试件长度
width = 100             # 试件宽度
diameter = 20           # 骨料直径
agElastic = 55000       # 骨料弹性模量
agPoisson = 0.25        # 骨料泊松比
agDensity = 2.5e-9      # 骨料密度

stepTime = 0.4          # 分析步时间
typeOfTest = 1          # 试验种类，拉伸为 1，压缩为 -1
elongation = 0.025      # 延伸率，拉伸建议为 0.1，压缩建议为 0.02
seedSize = 0.5          # 网格细度
numOfCPU = 6            # 电脑 CPU 核心数，建议根据自己电脑配置尽量设高一点

# 作用面参考点
myModel = mdb.models[modelName]
myAssembly = myModel.rootAssembly
myAssembly.ReferencePoint(point=(width / 2, length, 0))
myAssembly.ReferencePoint(point=(width / 2, 0, 0))
r1 = myAssembly.referencePoints
refPoints1=(r1[1], )
myAssembly.Set(referencePoints=refPoints1, name='rf1')
r2 = myAssembly.referencePoints
refPoints2=(r2[2], )
myAssembly.Set(referencePoints=refPoints2, name='rf2')

# 创建部件
## 基体
myModel = mdb.models[modelName]
mySketch = mdb.models[modelName].ConstrainedSketch(name='sketch_1', sheetSize=100.0) #create sketch
mySketch.rectangle(point1=(0,0), point2=(100, 100))
myPart = myModel.Part(name=baseName, dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
myPart.BaseShell(sketch=mySketch)
del myModel.sketches['sketch_1']

## 骨料
mySketch = myModel.ConstrainedSketch(name='sketch_2', sheetSize=100)

center10 = [(16, 16), (50, 16), (84, 16), (16, 50), (50, 50), (84, 50), (16, 84), (50, 84), (84, 84)]

for p in center10:
    x,y = p[0], p[1]
    mySketch.CircleByCenterPerimeter(center=(x, y), point1=(x+diameter/2, y))

myPart = myModel.Part(name=agName, dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
myPart.BaseShell(sketch=mySketch)
del myModel.sketches['sketch_2']

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
f = p.faces
faces = f[0:1]
region = regionToolset.Region(faces=faces)
p.SectionAssignment(region=region, sectionName=baseMaterial, offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)

## 骨料
mdb.models[modelName].Material(name=agMaterial)
mdb.models[modelName].materials[agMaterial].Elastic(table=((agElastic, agPoisson), ))
mdb.models[modelName].materials[agMaterial].Density(table=((agDensity, ), ))
mdb.models[modelName].HomogeneousSolidSection(name=agMaterial, material=agMaterial, thickness=None)
p = mdb.models[modelName].parts[agName]
f = p.faces
faces = f[0:9]
region = regionToolset.Region(faces=faces)
p = mdb.models[modelName].parts[agName]
p.SectionAssignment(region=region, sectionName=agMaterial, offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)

# 装配
## 基体
myAssembly = myModel.rootAssembly
myAssembly.Instance(name=baseName, part = myModel.parts[baseName], dependent=ON)

## 骨料
myAssembly.Instance(name=agName, part = myModel.parts[agName], dependent=ON)

myAssembly.InstanceFromBooleanCut(name='Part-CutBase', 
    instanceToBeCut=myAssembly.instances[baseName], 
    cuttingInstances=(myAssembly.instances[agName], ), 
    originalInstances=DELETE)

myAssembly.Instance(name=agName, part = myModel.parts[agName], dependent=ON)

# 分析步
mdb.models[modelName].ExplicitDynamicsStep(name='Step-1', previous='Initial', 
    timePeriod=stepTime, massScaling=((SEMI_AUTOMATIC, MODEL, AT_BEGINNING, 5.0, 
    1e-05, BELOW_MIN, 0, 0, 0.0, 0.0, 0, None), ), improvedDtMethod=ON)
mdb.models[modelName].fieldOutputRequests['F-Output-1'].setValues(variables=
('S', 'E', 'U', 'RF','DAMAGEC', 'DAMAGET', 'STATUS'), numIntervals=40)
del mdb.models[modelName].historyOutputRequests['H-Output-1']
regionDef=mdb.models[modelName].rootAssembly.sets['rf1']
mdb.models[modelName].HistoryOutputRequest(name='H-Output-1', 
    createStepName='Step-1', variables=('RF2', ), region=regionDef, 
    sectionPoints=DEFAULT, rebar=EXCLUDE)
regionDef=mdb.models[modelName].rootAssembly.sets['rf2']
mdb.models[modelName].HistoryOutputRequest(name='H-Output-2', 
    createStepName='Step-1', variables=('U2', ), region=regionDef, 
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

# 边界条件
region1=regionToolset.Region(referencePoints=refPoints1)
s1 = myAssembly.instances['Part-CutBase-1'].edges
side1Edges1 = s1[9:10]
region2=regionToolset.Region(side1Edges=side1Edges1)
mdb.models[modelName].Coupling(name='Constraint-1', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    localCsys=None, u1=OFF, u2=ON, ur3=OFF)
region3=regionToolset.Region(referencePoints=refPoints2)
s2 = myAssembly.instances['Part-CutBase-1'].edges
side1Edges2 = s2[11:12]
region4=regionToolset.Region(side1Edges=side1Edges2)
mdb.models[modelName].Coupling(name='Constraint-2', controlPoint=region3, 
    surface=region4, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    localCsys=None, u1=OFF, u2=ON, ur3=OFF)
mdb.models[modelName].EncastreBC(name='BC-1', createStepName='Initial', 
    region=region1, localCsys=None)

# 增加荷载
mdb.models[modelName].SmoothStepAmplitude(name='Amp-1', timeSpan=STEP, data=((
    0.0, 0.0), (stepTime, 1.0)))
mdb.models[modelName].DisplacementBC(name='load', createStepName='Step-1', 
    region=region3, u1=0.0, u2=typeOfTest * elongation * length, ur3=0.0, amplitude='Amp-1', fixed=OFF, 
    distributionType=UNIFORM, fieldName='', localCsys=None)

# 合并部件
myAssembly.InstanceFromBooleanMerge(name=mergedName, instances=(
    myAssembly.instances['Part-CutBase-1'], myAssembly.instances[agName], ), 
    keepIntersections=ON, originalInstances=DELETE, domain=GEOMETRY)

# 插入关键字
mdb.models[modelName].keywordBlock.synchVersions(storeNodesAndElements=False)
mdb.models[modelName].keywordBlock.insert(33, """
*CONCRETE FAILURE
0,0,0,0.8639""")

# 划分网格
p = mdb.models[modelName].parts[mergedName]
p.seedPart(size=seedSize, deviationFactor=0.1, minSizeFactor=0.1)
f = p.faces
pickedRegions = f[0:10]
p.setMeshControls(regions=pickedRegions, elemShape=TRI, allowMapped=False)
elemType1 = mesh.ElemType(elemCode=CPS4R, elemLibrary=EXPLICIT)
elemType2 = mesh.ElemType(elemCode=CPS3, elemLibrary=EXPLICIT, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)
faces = f[0:10]
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
p.generateMesh()

# 创建作业
mdb.Job(name=jobName, model=modelName, description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, numDomains=numOfCPU, 
    activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=numOfCPU)