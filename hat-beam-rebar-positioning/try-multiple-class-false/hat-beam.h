#pragma once
#include "reference-line.h"
#include "top-control-point.h"

class HatBeam
{
public:
    HatBeam();
    virtual ~HatBeam();

public:
    double m_hatBeamHeight = 0.0;
    double m_hatBeamWidth = 0.0;
    double m_arcRebarRadius = 0.0;

public:
    ReferenceLine *m_referenceLine[10];

public:
    TopControlPoint *m_topControlPoint[100];
};