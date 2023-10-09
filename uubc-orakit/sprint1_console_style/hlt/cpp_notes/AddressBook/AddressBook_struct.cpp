#include<iostream>
#include<string>
#define MAX 1000 //do not end with ";"
using namespace std;

struct Person
{
    string m_Name;
    int m_Sex;
    int m_Age;
    string m_Phone;
    string m_Addr;
}; //end with ";"

struct AddressBook
{
    struct Person personArray[MAX];
    int m_Size;
};

void showMenu()
{
    cout<<"Welcome to the AddressBook system!"<<endl;
    cout<<"1. Add new person"<<endl;
    cout<<"2. Show all person"<<endl;
    cout<<"3. Delete someone"<<endl;
    cout<<"4. Search someone"<<endl;
    cout<<"5. Modify someone"<<endl;
    cout<<"6. Clear data"<<endl;
    cout<<"0. Exit"<<endl;
}

void addPerson(AddressBook * abs)
{
    if(abs->m_Size == MAX)
    {
        cout<<"AddressBook is full!"<<endl;
        return;
    }
    else
    {
        string name;
        cout<<"Please enter the name: "<<endl;
        cin>>name;
        abs->personArray[abs->m_Size].m_Name = name;

        int sex;
        cout<<"Please enter the sex number: "<<endl;
        cout<<"1 --- man"<<endl;
        cout<<"2 --- woman"<<endl;
        while(true)
        {
            cin>>sex; //cin out of while() may make program never stop 
            if(sex == 1 || sex == 2)
            {
                abs->personArray[abs->m_Size].m_Sex = sex;
                break; //break from while()
            }
            cout<<"Please enter right number: "<<endl;
        }
        
        int age;
        cout<<"Please enter the age: "<<endl;
        cin>>age;
        abs->personArray[abs->m_Size].m_Age = age;

        string phone;
        cout<<"Please enter the phone number: "<<endl;
        cin>>phone;
        abs->personArray[abs->m_Size].m_Phone = phone;

        string addr;
        cout<<"Please enter the address: "<<endl;
        cin>>addr;
        abs->personArray[abs->m_Size].m_Addr = addr;

        abs->m_Size++;

        cout<<"Added successfully!"<<endl;

        system("pause");
        system("cls");

    }
}

void showPerson(AddressBook * abs)
{
    if(abs->m_Size == 0)
    {
        cout<<"Ops...the AddressBook is empty :)"<<endl;
    }
    else
    {
        for(int i = 0;i < abs->m_Size;i++) //use ";" inside for()
        {
            cout<<"Name: "<<abs->personArray[i].m_Name<<"\t";
            cout<<"Sex: "<<(abs->personArray[i].m_Sex == 1 ? "man" : "woman")<<"\t";
            cout<<"Age: "<<abs->personArray[i].m_Age<<"\t";
            cout<<"Phone: "<<abs->personArray[i].m_Phone<<"\t";
            cout<<"Address: "<<abs->personArray[i].m_Addr<<endl;
        }
    }

    system("pause");
    system("cls");
}

int isExist(AddressBook * abs, string name)
{
    for(int i = 0;i < abs->m_Size;i++)
    {
        if(abs->personArray[i].m_Name == name)
        {
            return i;
        }
    }
    return -1;
}

void deletePerson(AddressBook * abs)
{
    cout<<"Please enter the name who you want to delete: "<<endl;
    string name;
    cin>>name;

    int ret = isExist(abs,name);
    if(ret != -1)
    {
        for(int i = 0;i < abs->m_Size;i++)
        {
            abs->personArray[i] = abs->personArray[i+1];
        }
        abs->m_Size--;
        cout<<"Delete successfully!"<<endl;
    }
    else
    {
        cout<<"There is no one named "<<name<<"~"<<endl;
    }

    system("pause");
	system("cls");
}

void searchPerson(AddressBook * abs)
{
    cout<<"Please enter the name who you want to delete: "<<endl;
    string name;
    cin>>name;

    int ret = isExist(abs,name);
    if(ret != -1)
    {
        cout<<"Name: "<<abs->personArray[ret].m_Name<<"\t";
        cout<<"Sex: "<<(abs->personArray[ret].m_Sex == 1 ? "man" : "woman")<<"\t";
        cout<<"Age: "<<abs->personArray[ret].m_Age<<"\t";
        cout<<"Phone: "<<abs->personArray[ret].m_Phone<<"\t";
        cout<<"Address: "<<abs->personArray[ret].m_Addr<<endl;
    }
    else
    {
        cout<<"There is no one named "<<name<<"~"<<endl;
    }

    system("pause");
	system("cls");
}

void modifyPerson(AddressBook * abs)
{
    cout<<"Please enter the name who you want to modify: "<<endl;
    string name;
    cin>>name;

    int ret = isExist(abs,name);
    if(ret != -1)
    {
        cout<<"Please enter the name: "<<endl;
        cin>>name;
        abs->personArray[ret].m_Name = name;

        int sex;
        cout<<"Please enter the sex number: "<<endl;
        cout<<"1 --- man"<<endl;
        cout<<"2 --- woman"<<endl;
        while(true)
        {
            cin>>sex;
            if(sex == 1 || sex == 2)
            {
                abs->personArray[ret].m_Sex = sex;
                break;
            }
            cout<<"Please enter right number: "<<endl;
        }

        int age;
        cout<<"Please enter the age: "<<endl;
        cin>>age;
        abs->personArray[ret].m_Age = age;

        string phone;
        cout<<"Please enter the phone number: "<<endl;
        cin>>phone;
        abs->personArray[ret].m_Phone = phone;

        string addr;
        cout<<"Please enter the address: "<<endl;
        cin>>addr;
        abs->personArray[ret].m_Addr = addr;

        cout<<"Modified successfully!"<<endl;
    }
    else
    {
        cout<<"There is no one named "<<name<<"~"<<endl;
    }

    system("pause");
	system("cls");
}

void cleanPerson(AddressBook * abs)
{
    abs->m_Size = 0;
    cout<<"Cleared successfully!"<<endl;

    system("pause");
	system("cls");
}

int main()
{
    AddressBook abs;
    abs.m_Size = 0;

    while (true)
    {
        showMenu();
        int select;
        cin>>select;
        switch (select)
        {
            case 1:
            addPerson(&abs); //end with ";" when use function
                break;

            case 2:
            showPerson(&abs);
                break;

            case 3:
            deletePerson(&abs);
                break;

            case 4:
            searchPerson(&abs);
                break;

            case 5:
            modifyPerson(&abs);
                break;

            case 6:
            cleanPerson(&abs);
                break;

            case 0:
            cout<<"bye~"<<endl;
            system("pause");
            return 0; //shut dowm main()
                break;
        
            default:
                break;
        }
    }
}