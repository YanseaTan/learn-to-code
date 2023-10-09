#pragma once
#include <vector>
#include <string>

using namespace std;

class HatBeamData
{
public:
    HatBeamData();
    virtual ~HatBeamData();

public:
    void ShowMenu();

public:
    double m_hatBeamHeight = 0.0;
    double m_hatBeamWidth = 0.0;

    void GetHatBeamInfo();

public:
    vector<string> m_referenceLineName;
    vector<double> m_referenceLinePosition;

    void GetReferenceLineInfo();

public:
    void PrintInfo();
};