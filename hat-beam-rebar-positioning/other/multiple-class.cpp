#include <iostream>
#include "multiple-class.h"

using std::cout;
using std::endl;

HatBeamData::HatBeamData()
{

}

HatBeamData::~HatBeamData()
{

}

ReferenceLineData::ReferenceLineData(char *name, double position)
{
    m_referenceLineName = name;
    m_referenceLinePosition = position;
}

ReferenceLineData::~ReferenceLineData()
{

}

int main()
{
    HatBeamData test;
    char temp[] = "kd";
    test.rl[0]->m_referenceLineName = temp;
    test.rl[0]->m_referenceLinePosition = 5000;
    test.rl[1]->m_referenceLinePosition = 10000;
    ReferenceLineData r2("kz", 15000);

    cout << test.rl << endl;
    cout << test.rl[0]->m_referenceLineName << endl;
    cout << test.rl[0]->m_referenceLinePosition << endl;
    cout << test.rl[1]->m_referenceLinePosition << endl;
    cout << r2.m_referenceLineName << endl;
    cout << r2.m_referenceLinePosition << endl;

    system("pause");
    return 0;
}