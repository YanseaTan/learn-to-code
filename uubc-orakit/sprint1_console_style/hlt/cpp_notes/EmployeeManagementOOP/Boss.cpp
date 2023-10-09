#include"Boss.h"

Boss::Boss(int id, string name, int deptId) {
	this->m_Id = id;
	this->m_Name = name;
	this->m_DeptId = deptId;
}

void Boss::showInfo() {
	cout << "ID: " << this->m_Id;
	cout << "\tName: " << this->m_Name;
	cout << "\tRank: " << this->getDeptName();
	cout << "\tDuty: Manage all company affairs" << endl;
}

string Boss::getDeptName() {
	return string("Boss");
}