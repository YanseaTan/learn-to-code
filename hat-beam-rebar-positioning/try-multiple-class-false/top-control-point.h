#pragma once

class TopControlPoint
{
public:
    TopControlPoint();
    virtual ~TopControlPoint();

public:
    int m_topControlPointReferenceLine = 0;
    double m_topControlPointPosition = 0.0;
    int m_topControlPointStart = 0;
    int m_topControlPointStop = 0;
};