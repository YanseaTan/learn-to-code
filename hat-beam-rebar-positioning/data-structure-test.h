#pragma once
#include <vector>
#include <string>

using namespace std;

const double REBAR_RADIUS = 11;
const double PROTECTIVE_LAYER_THICKNESS = 100;
const double TOP_REBAR_LENGTH = 300;

class HatBeamData
{
public:
    HatBeamData();
    virtual ~HatBeamData();

public:
    void ShowMenu();

public:
    // Hat Beam Structure Data
    double m_hatBeamHeight = 0.0;
    double m_hatBeamWidth = 0.0;
    double m_arcRebarRadius = 0.0;

    void GetHatBeamData();

public:
    // Reference Line Data
    vector<string> m_referenceLineName;
    vector<double> m_referenceLinePosition;

    void GetReferenceLineData();

public:
    // Top Rebar Control Point Data
    vector<int> m_topRebarControlPointReferenceLine;
    vector<double> m_topRebarControlPointPosition;
    vector<int> m_topRebarControlPointStart;
    vector<int> m_topRebarControlPointStop;

    void GetTopRebarControlPointData();

public:
    // Bottom Rebar Control Point Data
    vector<int> m_botRebarControlPointReferenceLine;
    vector<double> m_botRebarControlPointPosition;
    vector<int> m_botRebarControlPointStart;
    vector<int> m_botRebarControlPointStop;

    void GetBotRebarControlPointData();

public:
    // Outer Profile Rebar Coordinate
    double m_aX = 0.0;
    double m_aY = 0.0;
    double m_bX = 0.0;
    double m_bY = 0.0;
    double m_cX = 0.0;
    double m_cY = 0.0;
    double m_dX = 0.0;
    double m_dY = 0.0;
    double m_eX = 0.0;
    double m_eY = 0.0;
    double m_gX = 0.0;
    double m_gY = 0.0;
    double m_hX = 0.0;
    double m_hY = 0.0;
    double m_jX = 0.0;
    double m_jY = 0.0;

    void GetOuterProfileRebarCoordinate();

public:
    // Truncate Rebar Coordinate
    vector<double> m_truncateRebarOnTopX;
    vector<double> m_truncateRebarOnTopY;
    vector<double> m_truncateRebarOnBotX;
    vector<double> m_truncateRebarOnBotY;

    // Arc Rebar Coordinate
    vector<double> m_arcRebarX;
    vector<double> m_arcRebarY;
    vector<double> m_arcRebarTangentX;
    vector<double> m_arcRebarTangentY;
    vector<double> m_arcRebarCenterX;
    vector<double> m_arcRebarCenterY;

    // Diagonal Rebar Coordinate
    vector<double> m_diagonalRebarX;
    vector<double> m_diagonalRebarY;
    vector<double> m_diagonalRebarAnotherX;
    vector<double> m_diagonalRebarAnotherY;

    void GetInnerRebarCoordinate();

public:
    void PrintOriginalData();
    void PrintRebarCoordinateData();
};