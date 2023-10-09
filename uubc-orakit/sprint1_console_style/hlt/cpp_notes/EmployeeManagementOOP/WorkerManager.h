#pragma once
#include<iostream>
#include<fstream>
#include"Worker.h"
#include"Employee.h"
#include"Manager.h"
#include"Boss.h"

#define FILENAME "empFile.txt"

using namespace std;

class WorkerManager {
public:

    WorkerManager(); //constructor

    int m_EmpNum;

    Worker** m_EmpArray;

    bool m_FileIsEmpty;

    int getEmpNum();

    void initEmp();
    
    void showMenu();

    void exitSystem();

    void addEmp();

    void save();

    ~WorkerManager(); //destructor
};