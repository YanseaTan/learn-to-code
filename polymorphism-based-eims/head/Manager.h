#pragma once
#include<iostream>
#include<string>
#include"Worker.h"
using namespace std;

class Manager :public Worker {
public:

	Manager(int id, string name, int deptId);

	virtual void showInfo();
	virtual string getDeptName();
};