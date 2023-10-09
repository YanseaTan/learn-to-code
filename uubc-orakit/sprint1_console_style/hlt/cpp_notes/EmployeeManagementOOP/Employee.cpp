#include"Employee.h"

Employee::Employee(int id, string name, int deptId) {
	this->m_Id = id;
	this->m_Name = name;
	this->m_DeptId = deptId;
}

void Employee::showInfo() {
	cout << "ID: " << this->m_Id;
	cout << "\tName: " << this->m_Name;
	cout << "\tRank: " << this->getDeptName();
	cout << "\tDuty: Complete the tasks assigned by the manager" << endl;
}

string Employee::getDeptName() {
	return string("Employee");
}