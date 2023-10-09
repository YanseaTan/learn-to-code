#include"WorkerManager.h"

//"::" scope
WorkerManager::WorkerManager() {
    ifstream ifs;
    //open the file for reading
    ifs.open(FILENAME, ios::in);

    //check if the file exists
    if (!ifs.is_open()) {
        cout << "There is no empFile.txt." << endl;
        //initialize properties
        this->m_EmpNum = 0;
        this->m_EmpArray = NULL;
        this->m_FileIsEmpty = true;
        ifs.close();
        return; //exit the constructor, do not run the remaining "if()"
    }

    //check if the file is empty
    char ch;
    ifs >> ch; //"ifs >>": input from file to memory
    if (ifs.eof()) {
        cout << "The empFile.txt is empty." << endl;
        this->m_EmpNum = 0;
        this->m_EmpArray = NULL;
        this->m_FileIsEmpty = true;
        ifs.close();
        return;
    }

    this->m_EmpNum = this->getEmpNum();
    
    //open up memory space
    this->m_EmpArray = new Worker * [this->m_EmpNum];
    //import data from a file into an in-memory array
    this->initEmp();

}

int WorkerManager::getEmpNum() {
    ifstream ifs;
    ifs.open(FILENAME, ios::in);

    int id;
    string name;
    int deptId;
    int num = 0;
    while (ifs >> id && ifs >> name && ifs >> deptId) {
        num++;
    }

    ifs.close();
    return num;
}

void WorkerManager::initEmp() {
    ifstream ifs;
    ifs.open(FILENAME, ios::in);

    int id;
    string name;
    int deptId;
    int i = 0;
    while (ifs >> id && ifs >> name && ifs >> deptId) {
        Worker* worker = NULL;

        switch (deptId) {
        case 1:
            worker = new Employee(id, name, deptId);
            break;
        case 2:
            worker = new Manager(id, name, deptId);
            break;
        case 3:
            worker = new Boss(id, name, deptId);
            break;
        default:
            break;
        }
        
        this->m_EmpArray[i] = worker;
        i++;
    }
    ifs.close();
}

void WorkerManager::showMenu() {
    cout << "Welcome to the EmployeeManagement system!" << endl;
    cout << "1. Add employee information" << endl;
    cout << "2. Show employee information" << endl;
    cout << "3. Delete ex-employee" << endl;
    cout << "4. Modify employee information" << endl;
    cout << "5. Find employee information" << endl;
    cout << "6. Sort by number" << endl;
    cout << "7. Clear document" << endl;
    cout << "0. Exit" << endl;
}

void WorkerManager::exitSystem() {
    cout << "bye~" << endl;
    system("pause");
    exit(0); //exit the program
}

void WorkerManager::addEmp() {
    int addNum = 0;
    cout << "Please enter the number of employees to add: " << endl;
    cin >> addNum;

    if (addNum > 0) {
        int newSize = this->m_EmpNum + addNum;
        Worker** newSpace = new Worker * [newSize];

        if (this->m_EmpArray != NULL) {
            for (int i = 0; i < this->m_EmpNum; i++) {
                newSpace[i] = this->m_EmpArray[i];
            }
        }

        for (int i = 0; i < addNum; i++) {
            int id;
            string name;
            int deptId;

            cout << "Please enter the " << i + 1 << "-th employee ID: " << endl;
            cin >> id;
            cout << "Please enter the " << i + 1 << "-th employee Name: " << endl;
            cin >> name;
            cout << "Please enter the " << i + 1 << "-th employee Rank: " << endl;
            cout << "1. Employee" << endl;
            cout << "2. Manager" << endl;
            cout << "3. Boss" << endl;
            cin >> deptId;

            Worker* worker = NULL;
            switch (deptId) {
            case 1:
                worker = new Employee(id, name, 1);
                break; //need 'break;' here
            case 2:
                worker = new Manager(id, name, 2);
                break;
            case 3:
                worker = new Boss(id, name, 3);
                break;
            default:
                break;
            }

            newSpace[this->m_EmpNum + i] = worker;
        }
        delete[] this->m_EmpArray;
        this->m_EmpArray = newSpace;
        this->m_EmpNum = newSize;
        this->m_FileIsEmpty = false;

        cout << "Successfully added " << addNum << " new employees!" << endl;
        this->save();
    }
    else {
        cout << "Incorrect input, please try again." << endl;
    }

    system("pause");
    system("cls");
}

void WorkerManager::save() {
    ofstream ofs;
    //open the file for writing
    ofs.open(FILENAME, ios::out);

    for (int i = 0; i < this->m_EmpNum; i++) {
        ofs << this->m_EmpArray[i]->m_Id << " ";
        ofs << this->m_EmpArray[i]->m_Name << " ";
        ofs << this->m_EmpArray[i]->m_DeptId << endl;
    }

    ofs.close();
}

WorkerManager::~WorkerManager() {
    if (this->m_EmpArray != NULL) {
        delete[] this->m_EmpArray;
        this->m_EmpArray = NULL;
    }
}