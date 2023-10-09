#pragma once
#include<iostream>
#include<string>
#include"Worker.h"
using namespace std;

//class inheritance
class Employee :public Worker {
public:

	//constructor
	Employee(int id, string name, int deptId);

	virtual void showInfo();
	virtual string getDeptName();
};