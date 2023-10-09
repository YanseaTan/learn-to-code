#include "MainWidget.h"
#include<QDebug>

MainWidget::MainWidget()
{
    setWindowIcon(QIcon(":/logo.ico"));
    setWindowTitle("职工信息管理系统");
    this->resize(1020,600);

    //创建水平布局
    QHBoxLayout *HBoxLayout = new QHBoxLayout(this);

    //创建两个面板框
    QGroupBox *Left_Box = createEmpInfo();
    QGroupBox *Right_Box = createMenu();

    //拉伸系数比为2：1
    HBoxLayout->addWidget(Left_Box,2);
    HBoxLayout->addWidget(Right_Box,1);
}

//创建左侧职工信息面板
QGroupBox * MainWidget::createEmpInfo()
{
    QGroupBox * box = new QGroupBox("职工信息");
    TableWidget = new QTableWidget;
    TableWidget->setSelectionBehavior(QAbstractItemView::SelectRows);
    TableWidget->setColumnCount(6);
    TableWidget->setHorizontalHeaderLabels(QStringList() <<"工号"<<"姓名"<<"性别"<<"职级"<<"电话"<<"邮箱");
    //刷新表格信息
    flushTable();
    //添加水平布局，将表格布局进去
    QHBoxLayout * AutoHBoxLayout = new QHBoxLayout;
    AutoHBoxLayout->addWidget(TableWidget);
    box->setLayout(AutoHBoxLayout);

    //点击表格中的内容时，刷新右侧显示的信息列表
    connect(TableWidget, &QTableWidget::cellClicked, this, &MainWidget::flushListWidget);
    //表格中的内容发生更改时，触发更改员工信息函数，并刷新右侧显示的信息列表
    connect(TableWidget, &QTableWidget::cellChanged, this, &MainWidget::changeEmpInfo);
    connect(TableWidget, &QTableWidget::cellChanged, this, &MainWidget::flushListWidget);
    return box;
}

//创建右侧功能面板
QGroupBox * MainWidget::createMenu()
{
    QGroupBox * box = new QGroupBox("功能面板");
    //创建总的垂直布局
    QVBoxLayout * VBoxLayout = new QVBoxLayout;
    //创建局部网格布局
    QGridLayout * Buts = new QGridLayout;

    //创建列表部件
    ListWidget = new QListWidget;
    //创建功能按钮
    AddEmpBtn = new QPushButton("添加");
    DelEmpBtn = new QPushButton("删除");
    SaveBtn = new QPushButton("保存");
    ExitBtn = new QPushButton("退出");
    //创建查找输入框
    FindEmpEdit = new QLineEdit;
    FindEmpEdit->setPlaceholderText("输入职工姓名查找...");
    FindEmpEdit->setClearButtonEnabled(true);
    FindEmpEdit->setStyleSheet("QLineEdit{padding:3,3,3,3;}");

    Buts->addWidget(AddEmpBtn,0,0);
    Buts->addWidget(DelEmpBtn,0,1);
    Buts->addWidget(SaveBtn,1,0);
    Buts->addWidget(ExitBtn,1,1);

    //添加单个部件用addWidget()，添加一个本就是布局的组合用addLayout()
    VBoxLayout->addWidget(FindEmpEdit);
    VBoxLayout->addWidget(ListWidget);
    VBoxLayout->addLayout(Buts);
    box->setLayout(VBoxLayout);

    //关联点击每一个按钮（输入框）以及会触发的槽（功能函数）
    connect(FindEmpEdit, &QLineEdit::returnPressed, this, &MainWidget::findEmpInfo);
    connect(AddEmpBtn, &QPushButton::clicked, this, &MainWidget::addEmpBox);
    connect(DelEmpBtn, &QPushButton::clicked, this, &MainWidget::delEmpInfo);
    connect(SaveBtn, &QPushButton::clicked, this, &MainWidget::saveEmpInfo);
    connect(ExitBtn, &QPushButton::clicked, this, &MainWidget::close);
    return box;
}

//添加职工
void MainWidget::addEmpBox()
{
    //添加职工需要弹出一个单独有功能的窗口，所以单独建了一个 EditEmpInfoBox 类，是一个 QDialog 对话框窗口
    infoBox = new EditEmpInfoBox;
    //如果 infoBox 发出了 closeBox 的信号（添加完成），则触发刷新左侧表格和清除右侧列表的槽
    QObject::connect(infoBox, &EditEmpInfoBox::closeBox, this, &MainWidget::flushTable);
    QObject::connect(infoBox, &EditEmpInfoBox::closeBox, ListWidget, &QListWidget::clear);
    //返回值，结束窗口
    infoBox->exec();
}

//刷新表格中的内容，当界面初始化、添加和删除职工信息后，都需要对表格内容进行更新
void MainWidget::flushTable()
{
    //更新表格内容前，要断开与 cellChanged 信号关联的所有槽，否则会导致程序闪退
    disconnect(TableWidget, &QTableWidget::cellChanged,0,0);
    QFile file(FILE_NAME);
    file.open(QIODevice::ReadOnly);
    QTextStream textStr(&file);
    QString id, name, sex, dept, tel, email;
    TableWidget->setRowCount(0);
    while(!textStr.atEnd())
    {
        TableWidget->setRowCount(TableWidget->rowCount()+1);
        //将文件中的数据读到内存
        textStr >> id >> name >> sex >> dept >> tel >> email;
        //将读到的数据依次填入到表格中
        TableWidget->setItem(TableWidget->rowCount()-1,0,new QTableWidgetItem(id));
        TableWidget->setItem(TableWidget->rowCount()-1,1,new QTableWidgetItem(name));
        TableWidget->setItem(TableWidget->rowCount()-1,2,new QTableWidgetItem(sex));
        TableWidget->setItem(TableWidget->rowCount()-1,3,new QTableWidgetItem(dept));
        TableWidget->setItem(TableWidget->rowCount()-1,4,new QTableWidgetItem(tel));
        TableWidget->setItem(TableWidget->rowCount()-1,5,new QTableWidgetItem(email));
    }
    file.close();
    //完成更新表格的任务后，重新关联与 cellChanged 相关的槽
    connect(TableWidget, &QTableWidget::cellChanged, this, &MainWidget::changeEmpInfo);
    connect(TableWidget, &QTableWidget::cellChanged, this, &MainWidget::flushListWidget);
}

//刷新右侧信息列表，需要输入一个行数
void MainWidget::flushListWidget(int row)
{
    //当列表中有信息时，直接修改
    if(ListWidget->count() > 0)
    {
        ListWidget->item(0)->setText("工 号：" + TableWidget->item(row, 0)->text());
        ListWidget->item(1)->setText("姓 名：" + TableWidget->item(row, 1)->text());
        ListWidget->item(2)->setText("性 别：" + TableWidget->item(row, 2)->text());
        ListWidget->item(3)->setText("职 级：" + TableWidget->item(row, 3)->text());
        ListWidget->item(4)->setText("电 话：" + TableWidget->item(row, 4)->text());
        ListWidget->item(5)->setText("邮 箱：" + TableWidget->item(row, 5)->text());
    }
    //当列表中没有信息时，直接添加
    else
    {
        ListWidget->addItem("工 号：" + TableWidget->item(row, 0)->text());
        ListWidget->addItem("姓 名：" + TableWidget->item(row, 1)->text());
        ListWidget->addItem("性 别：" + TableWidget->item(row, 2)->text());
        ListWidget->addItem("职 级：" + TableWidget->item(row, 3)->text());
        ListWidget->addItem("电 话：" + TableWidget->item(row, 4)->text());
        ListWidget->addItem("邮 箱：" + TableWidget->item(row, 5)->text());
    }
}

//删除职工信息
void MainWidget::delEmpInfo()
{
    //将选中的列表内容赋予给 items
    QList <QTableWidgetItem*> items = TableWidget->selectedItems();
    //如果选中了列表内容，则进行删除确认
    if(items.count() > 0)
    {
        //创建 QMessageBox 中的 question 类型，用作删除确认
        QMessageBox::StandardButton result = QMessageBox::question(this, "删除", "确定要删除工号为【" + items.at(0)->text() + "】的职工吗？");
        if(result == QMessageBox::Yes)
        {
            //将除目标学生外，其它学生的信息拷贝到一个临时文件中，然后删除原来的文件，并将临时文件的文件名改为和原文件相同的名称
            QString ID, name, sex, dept, tel, email;
            QFile file(FILE_NAME);
            file.open(QIODevice::ReadOnly);
            QTextStream readTextStr(&file);

            QFile tempFile(TEMP_FILE_NAME);
            tempFile.open(QIODevice::WriteOnly);
            QTextStream writeTextStr(&tempFile);

            while(!readTextStr.atEnd())
            {
                readTextStr >> ID >> name >> sex >> dept >> tel >> email;
                if(ID != items.at(0)->text())
                {
                    writeTextStr << ID << " " << name << " " << sex << " " << dept << " " << tel << " " << email << "\t";
                }
            }

            tempFile.close();
            file.close();
            file.remove();
            tempFile.rename(FILE_NAME);
            flushTable();
            //清除右侧列表显示内容
            ListWidget->clear();
        }
    }
    else
    {
        QMessageBox::warning(this, "提示", "请选择要删除的职工");
    }
}

//根据姓名查找职工信息
void MainWidget::findEmpInfo()
{
    //获得当前表格行数，qint32 为无符号32比特数据类型
    qint32 count = TableWidget->rowCount();
    bool findSuccess = false;
    if(count > 0)
    {
        for(qint32 i = 0; i < count; i++)
        {
            QString name = TableWidget->item(i, 1)->text();
            if(name == FindEmpEdit->text())
            {
                findSuccess = true;
                //如果名字对上了，则左侧表格中选中对应行并刷新右侧信息列表，跳出循环
                TableWidget->selectRow(i);
                flushListWidget(i);
                break;
            }
        }
        if(findSuccess == false)
        {
            QMessageBox::information(this, "查找失败", "当前表格中没有【" + FindEmpEdit->text() + "】职工");
        }
    }
}

//将职工信息变动保存到文件中
void MainWidget::changeEmpInfo(int row)
{
    QString ID, name, sex, dept, tel, email;
    QString empName = TableWidget->item(row, 1)->text();
    QFile file(FILE_NAME);
    file.open(QIODevice::ReadOnly);
    QTextStream readTextStr(&file);

    QFile tempFile(TEMP_FILE_NAME);
    tempFile.open(QIODevice::WriteOnly);
    QTextStream writeTextStr(&tempFile);

    while(!readTextStr.atEnd())
    {
        readTextStr >> ID >> name >> sex >> dept >> tel >> email;
        //如果当前行不是要修改的那行，就从原文件读到的数据进行写入
        if(name != empName)
        {
            writeTextStr << ID << " " << name << " " << sex << " " << dept << " " << tel << " " << email << "\t";
        }
        //如果当前行是要修改的那行，就从表格中那行的数据进行写入
        else
        {
            for(int i = 0; i < TableWidget->columnCount(); i++)
            {
                writeTextStr << TableWidget->item(row, i)->text() << " ";
            }
        }
    }

    tempFile.close();
    file.close();
    file.remove();
    tempFile.rename(FILE_NAME);
}

//保存职工信息
void MainWidget::saveEmpInfo()
{
    QFile file(FILE_NAME);
    file.open(QIODevice::WriteOnly);
    QTextStream textStr(&file);

    for(int i = 0; i < TableWidget->rowCount(); i++)
    {
        for(int j = 0; j < TableWidget->columnCount(); j++)
        {
            textStr << TableWidget->item(i, j)->text() << " ";
        }
        textStr << "\n";
    }
    file.close();
    QMessageBox::information(this, "保存", "保存成功！");
}
