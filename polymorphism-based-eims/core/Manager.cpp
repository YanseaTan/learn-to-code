#include"Manager.h"

Manager::Manager(int id, string name, int deptId) {
	this->m_Id = id;
	this->m_Name = name;
	this->m_DeptId = deptId;
}

void Manager::showInfo() {
	cout << "ID: " << this->m_Id;
	cout << "\tName: " << this->m_Name;
	cout << "\tRank: " << this->getDeptName();
	cout << "\tDuty: Complete the tasks assigned by the boss and issue the tasks to the employees" << endl;
}

string Manager::getDeptName() {
	return string("Manager");
}