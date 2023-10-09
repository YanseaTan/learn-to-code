#pragma once
#include<iostream>
#include<string>
using namespace std;

//Worker abstract class, without any implementation(without Worker.cpp)
class Worker {
public:

	//class behavior
	//pure virtual function
	virtual void showInfo() = 0;
	virtual string getDeptName() = 0;

	//class properties
	int m_Id;
	string m_Name;
	int m_DeptId;
};