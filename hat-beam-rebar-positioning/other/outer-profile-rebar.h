#pragma once

const double REBAR_RADIUS = 11;
const double PROTECTIVE_LAYER_THICKNESS = 100;
const double TOP_REBAR_LENGTH = 300;

class HatBeamData
{
public:
    HatBeamData();
    virtual ~HatBeamData();

public:
    double m_hatBeamHeight = 0;
    double m_hatBeamWidth = 0;

    void GetHatBeamHeight();
    void GetHatBeamWight();

public:
    double m_aX = 0;
    double m_aY = 0;
    double m_bX = 0;
    double m_bY = 0;
    double m_cX = 0;
    double m_cY = 0;
    double m_dX = 0;
    double m_dY = 0;
    double m_eX = 0;
    double m_eY = 0;
    double m_gX = 0;
    double m_gY = 0;
    double m_hX = 0;
    double m_hY = 0;
    double m_jX = 0;
    double m_jY = 0;

    void PrintCoordinate();
};