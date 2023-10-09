#include <iostream>
#include "reference-line.h"
#include "hat-beam.h"

using std::cin;
using std::cout;
using std::endl;

const double REBAR_RADIUS = 11;
const double PROTECTIVE_LAYER_THICKNESS = 100;
const double TOP_REBAR_LENGTH = 300;

int main()
{
    HatBeam test;
    test.m_hatBeamHeight = 2000.0;

    cout << test.m_hatBeamHeight << endl;

    char temp[] = "";

    cin >> temp;

    test.m_referenceLine[0]->m_referenceLineName = temp;

    cout << test.m_referenceLine[0]->m_referenceLineName << endl;



    system("pause");
    return 0;
}