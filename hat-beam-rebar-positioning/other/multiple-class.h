#pragma once
#include <vector>
#include <string>

using std::string;
using std::vector;

const double REBAR_RADIUS = 11;
const double PROTECTIVE_LAYER_THICKNESS = 100;
const double TOP_REBAR_LENGTH = 300;

class ReferenceLineData;

class HatBeamData
{
public:
    HatBeamData();
    virtual ~HatBeamData();

public:
    // Hat Beam Structure Data
    double m_hatBeamHeight = 0.0;
    double m_hatBeamWidth = 0.0;
    double m_arcRebarRadius = 0.0;

public:
    ReferenceLineData *rl[];
};

class ReferenceLineData
{
public:
    ReferenceLineData(char *name, double position);
    virtual ~ReferenceLineData();

public:
    char *m_referenceLineName;
    double m_referenceLinePosition = 0.0;
};