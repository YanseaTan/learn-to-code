#include "Employee.h"

QString Employee::getID() const
{
    return ID;
}
void Employee::setID(const QString &value)
{
    ID = value;
}

QString Employee::getName() const
{
    return name;
}
void Employee::setName(const QString &value)
{
    name = value;
}

QString Employee::getSex() const
{
    return sex;
}
void Employee::setSex(const QString &value)
{
    sex = value;
}

QString Employee::getDept() const
{
    return dept;
}
void Employee::setDept(const QString &value)
{
    dept = value;
}

QString Employee::getTel() const
{
    return tel;
}
void Employee::setTel(const QString &value)
{
    tel = value;
}

QString Employee::getEmail() const
{
    return email;
}
void Employee::setEmail(const QString &value)
{
    email = value;
}
