#ifndef EDITEMPINFOBOX_H
#define EDITEMPINFOBOX_H

#include <QWidget>
#include <QLineEdit>
#include <QFormLayout>
#include <QPushButton>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QFile>
#include <QTextStream>
#include <QMessageBox>
#include "Tool.h"
#include "Employee.h"

//创建的 EditEmpInfoBox 类是一个 QDialog 对话框类型的窗口
class EditEmpInfoBox : public QDialog
{
    Q_OBJECT
public:
    EditEmpInfoBox();
signals:
    void closeBox();
public slots:
    void saveEmpInfo();
public:
    //发出 closeBox 信号
    void emitCloseBox();
private:
    QLineEdit * ID;
    QLineEdit * name;
    QLineEdit * sex;
    QLineEdit * dept;
    QLineEdit * tel;
    QLineEdit * email;
    QPushButton * submit;
    QPushButton * cancel;
};

#endif // EDITEMPINFOBOX_H
