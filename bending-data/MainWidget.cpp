#include "MainWidget.h"

MainWidget::MainWidget()
{
    setWindowIcon(QIcon(":/logo.ico"));
    setWindowTitle("BendingData-1.1");
    this->resize(280, 180);

    QGroupBox * Menu = menu();
    Text3 = new QLabel;
    Text3->setText("");
    Text3->setAlignment(Qt::AlignCenter);
    SelectFileBtn = new QPushButton("选择文件");

    QVBoxLayout *v = new QVBoxLayout(this);
    v->addWidget(Menu);
    v->addWidget(Text3);
    v->addWidget(SelectFileBtn);
    this->setLayout(v);

    connect(SelectFileBtn, &QPushButton::clicked, this, &MainWidget::selectFile);
}

QGroupBox * MainWidget::menu()
{
    QGroupBox * box = new QGroupBox("试验参数");

    Text1 = new QLabel;
    Text2 = new QLabel;
    MM1 = new QLabel;
    MM2 = new QLabel;
    Text1->setText("四点弯曲的跨度：");
    Text2->setText("截面高度：");
    MM1->setText("mm");
    MM2->setText("mm");

    Line1 = new QLineEdit;
    Line2 = new QLineEdit;

    // 在输入框内输入好默认的试验参数
    Line1->setText("150");
    Line2->setText("40");

    QGridLayout * grid = new QGridLayout;
    grid->addWidget(Text1, 0, 0);
    grid->addWidget(Line1, 0, 1);
    grid->addWidget(MM1, 0, 2);
    grid->addWidget(Text2, 1, 0);
    grid->addWidget(Line2, 1, 1);
    grid->addWidget(MM2, 1, 2);
    box->setLayout(grid);

    // 当用户按下回车键，或者鼠标点击输入框外的其它位置时对试验参数进行更新
    connect(Line1, &QLineEdit::editingFinished, this, &MainWidget::updateParam);
    connect(Line2, &QLineEdit::editingFinished, this, &MainWidget::updateParam);

    return box;
}

void MainWidget::updateParam()
{
    // 将用户输入好的文本转换为 int 赋值给变量
    span = Line1->text().toInt();
    section = Line2->text().toInt();
}

void MainWidget::selectFile()
{
    // 弹出文件对话框进行文件选择
    QFileDialog * f = new QFileDialog(this);
    f->setWindowTitle("选择数据文件*.txt");
    f->setNameFilter("*.txt");
    f->setViewMode(QFileDialog::Detail);

    // 当用户选择文件后，将路径保存到 filePath 中
    if(f->exec() == QDialog::Accepted)
    {
        filePath = f->selectedFiles()[0];
        getXlsx();
    }
}

void MainWidget::getXlsx()
{
    Text3->setText("处理中，请稍后 🐢🐢🐢");
    Text3->repaint();
    QString data, force, def1, def2, def3, disp, disp1, disp2, disp3, disp4, stress, strain, time;
    QFile file(filePath);
    file.open(QIODevice::ReadOnly);
    QTextStream readFile(&file);

    QFile temp1("temp.txt");
    temp1.open(QIODevice::WriteOnly);
    QTextStream writeTemp(&temp1);

    // 去除原文件除数据外的冗余内容，将数据暂存在 temp.txt 中
    int rowCount = 0;
    while (!readFile.atEnd() && rowOfData == -1)
    {
        ++rowCount;
        readFile >> data;

        if (rowCount > 105)
        {
            readFile >> force >> def1 >> def2 >> def3 >> disp >> disp1 >> disp2 >> disp3 >> disp4 >> stress >> strain >> time;
            while (force != "=========================分析信息==========================")
            {
                writeTemp << disp1 << " " << disp2 << " " << disp3 << " " << disp4 << " " << force << "\n";
                readFile >> force >> def1 >> def2 >> def3 >> disp >> disp1 >> disp2 >> disp3 >> disp4 >> stress >> strain >> time;
            }
            rowOfData = def2.toInt();
        }
    }

    file.close();
    temp1.close();

    QFile temp2("temp.txt");
    temp2.open(QIODevice::ReadOnly);
    QTextStream readTemp(&temp2);

    QXlsx::Document xlsx1("frame.xlsx");

    // 将 temp.txt 文件中的数据导入到 xlsx 文件中
    for (int i = 2; i < rowOfData + 2; ++i)
    {
        for (int j = 1; j < 6; ++j)
        {
            readTemp >> data;
            double num = data.toDouble();
            xlsx1.write(i, j, num);
        }
    }
    // 写入试验参数
    xlsx1.write(1, 12, span);
    xlsx1.write(2, 12, section);

    temp2.remove();

    // 这一步会让 filePath 的长度也减少4，因此要放在后面进行操作，否则会影响前面 filePath 的读取
    QString outputPath;
    int index = filePath.length()-4;
    outputPath = filePath.replace(index, 4, ".xlsx");
    xlsx1.saveAs(outputPath);

    QXlsx::Document xlsx2("formula.xlsx");
    QXlsx::Document xlsx3(outputPath);

    // 将部分公式复制到需要输出的文件中
    for (int i = 2; i < rowOfData + 2; ++i)
    {
        for (int j = 6; j < 11; ++j)
        {
            QString s = xlsx2.read(i, j).toString();
            xlsx3.write(i, j, s);
        }
    }

    for (int i = 5; i < 20; ++i)
    {
        QString s = xlsx2.read(i, 12).toString();
        xlsx3.write(i, 12, s);
    }
    xlsx3.write(10, 12, "=INDEX(F:F,L9)");

    // 创建散点图
    QXlsx::Chart *scatterChart = xlsx3.insertChart(20, 10, QSize(500, 300));
    scatterChart->setChartType(QXlsx::Chart::CT_Scatter);
    scatterChart->setChartStyle(2);
    scatterChart->addSeries(QXlsx::CellRange("F2:G50000"));

    xlsx3.save();

    Text3->setText("处理完成 👍");
    QMessageBox::information(this, "处理完毕", "数据处理完毕");

    rowOfData = -1;
}
