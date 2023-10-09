#include<iostream>
#include"WorkerManager.h"
#include"Worker.h"
#include"Employee.h"
#include"Manager.h"
#include"Boss.h"
using namespace std;

int main() {
    WorkerManager wm;

    int choice = 0;

    while (true) {
        wm.showMenu();
        cout << "Please enter your choice :" << endl;
        cin >> choice;

        switch (choice)
        {
        case 1:
            wm.addEmp();
            break;

        case 2:
            wm.showEmp();
            break;

        case 3:
            wm.delEmp();
            break;

        case 4:
            wm.modEmp();
            break;

        case 5:
            wm.findEmp();
            break;

        case 6:
            wm.sortEmp();
            break;

        case 7:
            wm.cleanFile();
            break;

        case 0:
            wm.exitSystem();
            break;

        default:
            system("cls");
            break;
        }
    }

    system("pause");
    return 0;
}