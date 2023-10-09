#ifndef EMPLOYEE_H
#define EMPLOYEE_H

#include <QString>

class Employee
{
public:
    QString getID() const;
    void setID(const QString &value);

    QString getName() const;
    void setName(const QString &value);

    QString getSex() const;
    void setSex(const QString &value);

    QString getDept() const;
    void setDept(const QString &value);

    QString getTel() const;
    void setTel(const QString &value);

    QString getEmail() const;
    void setEmail(const QString &value);

private:
    QString ID;
    QString name;
    QString sex;
    QString dept;
    QString tel;
    QString email;
};

#endif // EMPLOYEE_H
