#pragma once

class ReferenceLine
{
public:
    ReferenceLine();
    virtual ~ReferenceLine();

public:
    char *m_referenceLineName;
    double m_referenceLinePosition = 0.0;
};