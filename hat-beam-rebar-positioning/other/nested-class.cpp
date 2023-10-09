#include <iostream>
#include "nested-class.h"

using namespace std;

HatBeamData::HatBeamData()
{

}

HatBeamData::~HatBeamData()
{

}

void HatBeamData::GetHatBeamHeight()
{
    cout << "height: " << endl;
    double tempHeight = 0;
    cin >> tempHeight;
    m_hatBeamHeight = tempHeight;
}

void HatBeamData::GetHatBeamWight()
{
    cout << "width: " << endl;
    double tempWight = 0;
    cin >> tempWight;
    m_hatBeamWidth = tempWight;
}

HatBeamData::ReferenceLine::ReferenceLine()
{
    lineNum++;
}

HatBeamData::ReferenceLine::~ReferenceLine()
{

}

void HatBeamData::ReferenceLine::GetLinePosition()
{
    cout << "reference line position: " << endl;
    double tempPosition = 0.0;
    cin >> tempPosition;
    m_linePosition = tempPosition;
}

void HatBeamData::PrintInfo()
{
    cout << "height: " << m_hatBeamHeight << endl;
    cout << "width: " << m_hatBeamWidth << endl;
}

int main()
{
    system("pause");
    return 0;
}
