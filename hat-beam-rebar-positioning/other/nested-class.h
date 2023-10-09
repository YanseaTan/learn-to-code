#pragma once

int lineNum = 0;

class HatBeamData
{
public:
    HatBeamData();
    virtual ~HatBeamData();

public:
    double m_hatBeamHeight = 0.0;
    double m_hatBeamWidth = 0.0;

    void GetHatBeamHeight();
    void GetHatBeamWight();

public:
    class ReferenceLine
    {
    public:
        ReferenceLine();
        virtual ~ReferenceLine();

    public:
        double m_linePosition = 0.0;

        void GetLinePosition();
    };

public:
    void PrintInfo();
};