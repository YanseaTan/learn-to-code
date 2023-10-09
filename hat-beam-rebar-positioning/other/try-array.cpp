#include <iostream>
#include "try-array.h"

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
    cout << "****** Test System ******" << endl;
    cout << "1. Input Structure Info" << endl;
    cout << "2. Create Reference Line" << endl;
    cout << "3. Show All Info" << endl;
    cout << "4. Exit" << endl;
}

void HatBeamData::GetHatBeamInfo()
{
    cout << endl;
    cout << "Height: " << endl;
    double tempHeight = 0;
    cin >> tempHeight;
    m_hatBeamHeight = tempHeight;

    cout << "Width: " << endl;
    double tempWight = 0;
    cin >> tempWight;
    m_hatBeamWidth = tempWight;

    cout << "Input Structure Info Successfully" << endl;
}

void HatBeamData::GetReferenceLineInfo()
{
    cout << endl;
    cout << "Name: " << endl;
    string tempName = " ";
    cin >> tempName;
    m_referenceLineName.push_back(tempName);

    cout << "Position: " << endl;
    double tempPosition = 0.0;
    cin >> tempPosition;
    m_referenceLinePosition.push_back(tempPosition);

    cout << "Create Reference Line Successfully" << endl;
}

void HatBeamData::PrintInfo()
{
    cout << endl;
    cout << "**** Structure Data ****" << endl;
    cout << "Height" << "\t\t" << m_hatBeamHeight << endl;
    cout << "Width" << "\t\t" << m_hatBeamWidth << endl;
    cout << "************************" << endl << endl;

    cout << "**** Reference Line ****" << endl;
    cout << "Name" << "\t\t" << "Position" << endl;
    for (int i = 0; i < m_referenceLineName.size(); i++)
    {
        cout << m_referenceLineName[i] << "\t\t" << m_referenceLinePosition[i] << endl;
    }
    cout << "************************" << endl;
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
                test.GetHatBeamInfo();
                system("pause");
                break;
            case 2 :
                test.GetReferenceLineInfo();
                system("pause");
                break;
            case 3 :
                test.PrintInfo();
                system("pause");
                break;
            case 4 :
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