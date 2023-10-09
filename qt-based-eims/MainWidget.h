#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QWidget>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QListWidget>
#include <QTableWidget>
#include <QGroupBox>
#include <QPushButton>
#include <QLineEdit>
#include <QFile>
#include <QTextStream>
#include "EditEmpInfoBox.h"
#include "Tool.h"
#include "Employee.h"

class MainWidget : public QWidget
{
    Q_OBJECT

public:
    //创建主窗口
    MainWidget();
    //当用户点击添加按钮时，弹出添加职工信息窗口
    void addEmpBox();

public slots:
    //更新左侧表格中的职工信息
    void flushTable();
    //更新右侧列表中的职工信息
    void flushListWidget(int row);
    void delEmpInfo();
    void findEmpInfo();
    void changeEmpInfo(int row);
    void saveEmpInfo();

private:
    //创建左侧职工信息面板
    QGroupBox * createEmpInfo();
    //创建右侧功能面板
    QGroupBox * createMenu();

private:
    QTableWidget * TableWidget;
    QListWidget * ListWidget;
    QPushButton * AddEmpBtn;
    QPushButton * DelEmpBtn;
    QPushButton * SaveBtn;
    QPushButton * ExitBtn;
    QLineEdit * FindEmpEdit;
    EditEmpInfoBox * infoBox;
};
#endif // MAINWINDOW_H
