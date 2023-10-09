#include <iostream>
#include "data-structure-test.h"

using namespace std;

HatBeamData::HatBeamData()
{
    ShowMenu();
}

HatBeamData::~HatBeamData()
{

}

void HatBeamData::ShowMenu()
{
    cout << "************** Test System **************" << endl
        << "1. Input Hat Beam Structure Data" << endl
        << "2. Create Reference Line Data" << endl
        << "3. Create Top Rebar Control Point Data" << endl
        << "4. Create Bottom Rebar Control Point Data" << endl
        << "5. Show All Original Data" << endl
        << "6. Show All Rebar Exact Coordinate Data" << endl
        << "7. Exit" << endl
        << "*****************************************" << endl;
}

void HatBeamData::GetHatBeamData()
{
    cout << endl;
    cout << "Height: ";
    double tempHeight = 0.0;
    cin >> tempHeight;
    m_hatBeamHeight = tempHeight;

    cout << "Width: ";
    double tempWight = 0.0;
    cin >> tempWight;
    m_hatBeamWidth = tempWight;

    cout << "Arc Rebar Radius: ";
    double tempRadius = 0.0;
    cin >> tempRadius;
    m_arcRebarRadius = tempRadius;

    cout << "Input Structure Info Successfully" << endl;
}

void HatBeamData::GetReferenceLineData()
{
    cout << endl;
    cout << "Name: ";
    string tempName = "";
    cin >> tempName;
    m_referenceLineName.push_back(tempName);

    cout << "Position: ";
    double tempPosition = 0.0;
    cin >> tempPosition;
    m_referenceLinePosition.push_back(tempPosition);

    cout << "Create Reference Line Successfully" << endl;
}

void HatBeamData::GetTopRebarControlPointData()
{
    cout << endl;
    cout << "Choose a Reference Line: " << endl;
    for (int i = 0; i < m_referenceLineName.size(); i++)
    {
        cout << i + 1 << ". " << m_referenceLineName[i] << endl;
    }
    int tempNum = 0;
    cin >> tempNum;
    m_topRebarControlPointReferenceLine.push_back(tempNum);

    cout << "Position: ";
    double tempPosition = 0.0;
    cin >> tempPosition;
    m_topRebarControlPointPosition.push_back(tempPosition);

    cout << "Start Layer: ";
    int tempStart = 0;
    cin >> tempStart;
    m_topRebarControlPointStart.push_back(tempStart);

    cout << "Stop Layer: ";
    int tempStop = 0;
    cin >> tempStop;
    m_topRebarControlPointStop.push_back(tempStop);
}

void HatBeamData::GetBotRebarControlPointData()
{
    cout << endl;
    cout << "Choose a Reference Line: " << endl;
    for (int i = 0; i < m_referenceLineName.size(); i++)
    {
        cout << i + 1 << ". " << m_referenceLineName[i] << endl;
    }
    int tempNum = 0;
    cin >> tempNum;
    m_botRebarControlPointReferenceLine.push_back(tempNum - 1);

    cout << "Position: ";
    double tempPosition = 0.0;
    cin >> tempPosition;
    m_botRebarControlPointPosition.push_back(tempPosition);

    cout << "Start Layer: ";
    int tempStart = 0;
    cin >> tempStart;
    m_botRebarControlPointStart.push_back(tempStart);

    cout << "Stop Layer: ";
    int tempStop = 0;
    cin >> tempStop;
    m_botRebarControlPointStop.push_back(tempStop);
}

void HatBeamData::PrintOriginalData()
{
    cout << endl
        << "******** Structure Data ********" << endl
        << "Height" << "\t\t\t" << m_hatBeamHeight << endl
        << "Width" << "\t\t\t" << m_hatBeamWidth << endl
        << "Arc Rebar Radius" << "\t" << m_arcRebarRadius << endl
        << "********************************" << endl << endl;

    cout << "******** Reference Line ********" << endl
        << "Name" << "\t\t\t" << "Position" << endl;
    for (int i = 0; i < m_referenceLineName.size(); i++)
    {
        cout << m_referenceLineName[i] << "\t\t\t" << 
            m_referenceLinePosition[i] << endl;
    }
    cout << "********************************" << endl << endl;

    cout << "****************** Top Rebar Control Point Data ******************"
        << endl << "ID" << "\t" << "Reference Line" << "\t    " << "Position" 
        << "\t" << "Start Layer" << "\t" << "Stop Layer" << endl;
    for (int j = 0; j < m_topRebarControlPointPosition.size(); j++)
    {
        cout << j + 1 << "\t" << m_referenceLineName[j] << "\t\t    " << 
            m_topRebarControlPointPosition[j] << "\t" << 
            m_topRebarControlPointStart[j] << "\t\t" << 
            m_topRebarControlPointStop[j] << endl;
    }
    cout << "******************************************************************"
        << endl << endl;

    cout << "**************** Bottom Rebar Control Point Data *****************"
        << endl << "ID" << "\t" << "Reference Line" << "\t    " << "Position" 
        << "\t" << "Start Layer" << "\t" << "Stop Layer" << endl;
    for (int k = 0; k < m_botRebarControlPointPosition.size(); k++)
    {
        cout << k + 1 << "\t" << m_referenceLineName[k] << "\t\t    " << 
            m_botRebarControlPointPosition[k] << "\t" << 
            m_botRebarControlPointStart[k] << "\t\t" << 
            m_botRebarControlPointStop[k] << endl;
    }
    cout << "******************************************************************"
        << endl << endl;
}

void HatBeamData::GetOuterProfileRebarCoordinate()
{
    m_aX = PROTECTIVE_LAYER_THICKNESS + 3 * REBAR_RADIUS;
    m_aY = PROTECTIVE_LAYER_THICKNESS + REBAR_RADIUS + TOP_REBAR_LENGTH;
    m_bX = m_aX;
    m_bY = m_aY - TOP_REBAR_LENGTH;
    m_cX = m_hatBeamWidth - m_aX;
    m_cY = m_bY;
    m_dX = m_cX;
    m_dY = m_aY;
    m_eX = m_aX - 2 * REBAR_RADIUS;
    m_eY = m_bY;
    m_gX = m_eX;
    m_gY = m_hatBeamHeight - m_bY;
    m_hX = m_hatBeamWidth - m_eX;
    m_hY = m_gY;
    m_jX = m_hX;
    m_jY = m_eY;
}

void HatBeamData::GetInnerRebarCoordinate()
{
    m_truncateRebarOnTopX.clear();
    m_truncateRebarOnTopY.clear();
    m_truncateRebarOnBotX.clear();
    m_truncateRebarOnBotY.clear();

    m_arcRebarX.clear();
    m_arcRebarY.clear();
    m_arcRebarTangentX.clear();
    m_arcRebarTangentY.clear();
    m_arcRebarCenterX.clear();
    m_arcRebarCenterY.clear();

    m_diagonalRebarX.clear();
    m_diagonalRebarY.clear();
    m_diagonalRebarAnotherX.clear();
    m_diagonalRebarAnotherY.clear();

    // Get Truncate Rebar Coordinate
    for (int i = 0; i < m_topRebarControlPointStart.size(); i++)
    {
        if (m_topRebarControlPointStart[i] < 0 && m_topRebarControlPointStop[i] == 0)
        {
            double tempX = 0.0;
            int tempNum = m_topRebarControlPointReferenceLine[i];
            tempX = m_referenceLinePosition[tempNum - 1] + m_topRebarControlPointPosition[i];
            m_truncateRebarOnTopX.push_back(tempX);

            double tempY = 0.0;
            tempY = m_bY - m_topRebarControlPointStart[i] * REBAR_RADIUS * 2;
            m_truncateRebarOnTopY.push_back(tempY);
        }
    }

    for (int i = 0; i < m_botRebarControlPointStart.size(); i++)
    {
        if (m_botRebarControlPointStart[i] < 0 && m_botRebarControlPointStop[i] == 0)
        {
            double tempX = 0.0;
            int tempNum = m_botRebarControlPointReferenceLine[i];
            tempX = m_referenceLinePosition[tempNum - 1] + m_botRebarControlPointPosition[i];
            m_truncateRebarOnBotX.push_back(tempX);

            double tempY = 0.0;
            tempY = m_gY + m_botRebarControlPointStart[i] * REBAR_RADIUS * 2;
            m_truncateRebarOnBotY.push_back(tempY);
        }
    }

    // Get Arc Rebar Coordinate
    for (int i = 0; i < m_botRebarControlPointStart.size(); i++)
    {
        if (m_botRebarControlPointStart[i] == 0 && m_botRebarControlPointStop[i] == -1)
        {
            double tempX = 0.0;
            int tempNum = m_botRebarControlPointReferenceLine[i];
            tempX = m_referenceLinePosition[tempNum - 1] + m_botRebarControlPointPosition[i];
            m_arcRebarX.push_back(tempX);

            double tempY = 0.0;
            
        }
    }
}

void HatBeamData::PrintRebarCoordinateData()
{
    cout << "***** Outer Profile Rebar Coordinate *****" << endl
        << "A" << "\t" << "(" << m_aX << ", " << m_aY << ")" << "\t" 
        << "B" << "\t" << "(" << m_bX << ", " << m_bY << ")" << endl 
        << "C" << "\t" << "(" << m_cX << ", " << m_cY << ")" << "\t" 
        << "D" << "\t" << "(" << m_dX << ", " << m_dY << ")" << endl 
        << "E" << "\t" << "(" << m_eX << ", " << m_eY << ")" << "\t" 
        << "G" << "\t" << "(" << m_gX << ", " << m_gY << ")" << endl 
        << "H" << "\t" << "(" << m_hX << ", " << m_hY << ")" << "\t" 
        << "J" << "\t" << "(" << m_jX << ", " << m_jY << ")" << endl 
        << "*******************************************" 
        << endl << endl;

    cout << "*** Truncate Rebar Coordinate ***" << endl;
    for (int i = 0; i < m_truncateRebarOnTopX.size(); i++)
    {
        cout << i + 1 << "\t\t    " << "(" << m_truncateRebarOnTopX[i] << ", " 
            << m_truncateRebarOnTopY[i] << ")" << endl;
    }
    cout << "*********************************" << endl << endl;
}

int main()
{
    HatBeamData test;

    while (true)
    {
        int num = 0;
        cin >> num;
        switch (num)
        {
            case 1 :
                test.GetHatBeamData();
                system("pause");
                break;
            case 2 :
                test.GetReferenceLineData();
                system("pause");
                break;
            case 3 :
                test.GetTopRebarControlPointData();
                system("pause");
                break;
            case 4 :
                test.GetBotRebarControlPointData();
                system("pause");
                break;
            case 5 :
                test.PrintOriginalData();
                system("pause");
                break;
            case 6 :
                test.GetOuterProfileRebarCoordinate();
                test.GetInnerRebarCoordinate();
                test.PrintRebarCoordinateData();
                system("pause");
                break;
            case 7 :
                return 0;
            default :
                cout << "Please Input Right Number" << endl;
        }

        system("cls");
        test.ShowMenu();
    }


    system("pause");
    return 0;
}