#pragma once
#include<iostream>
#include<string>
#include"Worker.h"
using namespace std;

class Boss :public Worker {
public:

	Boss(int id, string name, int deptId);

	virtual void showInfo();
	virtual string getDeptName();
};