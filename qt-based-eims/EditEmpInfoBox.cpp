#include "EditEmpInfoBox.h"

EditEmpInfoBox::EditEmpInfoBox()
{
    setWindowTitle("添加职工信息");
    //创建垂直布局
    QVBoxLayout * VBox = new QVBoxLayout;
    //创建表单布局
    QFormLayout * FormLayout = new QFormLayout;
    ID = new QLineEdit;
    name = new QLineEdit;
    sex = new QLineEdit;
    dept = new QLineEdit;
    tel = new QLineEdit;
    email = new QLineEdit;
    FormLayout->addRow("工 号：",ID);
    FormLayout->addRow("姓 名：",name);
    FormLayout->addRow("性 别：",sex);
    FormLayout->addRow("职 级：",dept);
    FormLayout->addRow("电 话：",tel);
    FormLayout->addRow("邮 箱：",email);
    //标签有足够的空间适应，如果最小大小比可用空间大，输入框会被换到下一行
    FormLayout->setRowWrapPolicy(QFormLayout::WrapLongRows);

    //创建水平布局
    QHBoxLayout * HBox = new QHBoxLayout;
    submit = new QPushButton("提交");
    cancel = new QPushButton("取消");
    HBox->addWidget(submit);
    HBox->addWidget(cancel);

    VBox->addLayout(FormLayout,4);
    VBox->addLayout(HBox,1);
    this->setLayout(VBox);

    //提交信息触发 saveEmpInfo 这个自定义的槽
    QObject::connect(submit, &QPushButton::clicked, this, &EditEmpInfoBox::saveEmpInfo);
    QObject::connect(cancel, &QPushButton::clicked, this, &EditEmpInfoBox::close);
}

void EditEmpInfoBox::saveEmpInfo()
{
    //判断所有数据是否都已经填写
    if(this->ID->text() != "" && this->name->text() != "" && this->sex->text() != "" && this->dept->text() != "" && this->tel->text() != "" && this->email->text() != "")
    {
        Employee emp;
        emp.setID(this->ID->text());
        emp.setName(this->name->text());
        emp.setSex(this->sex->text());
        emp.setDept(this->dept->text());
        emp.setTel(this->tel->text());
        emp.setEmail(this->email->text());

        QFile file(FILE_NAME);
        //以（只写|追加）的方式打开文件
        file.open(QIODevice::WriteOnly|QIODevice::Append);
        QTextStream textStr(&file);
        textStr << emp.getID() << " " << emp.getName() << " " << emp.getSex() << " " << emp.getDept() << " " << emp.getTel() << " " << emp.getEmail() << "\t";
        file.close();
        this->close();
        //添加完成后发出关闭添加页面的信号
        emitCloseBox();
    }
    else
    {
        QMessageBox::warning(this, "提示", "请将信息填写完整", QMessageBox::Ok);
    }
}

void EditEmpInfoBox::emitCloseBox()
{
    emit closeBox();
}
