#ifndef MAINWIDGET_H
#define MAINWIDGET_H

#include <QWidget>
#include <QLabel>
#include <QMovie>
#include <QGroupBox>
#include <QVBoxLayout>
#include <QPushButton>
#include <QLineEdit>
#include <QMessageBox>
#include <QFileDialog>
#include <QFile>
#include <QTextStream>
#include "xlsxdocument.h"
#include "xlsxcellrange.h"
#include "xlsxchart.h"

class MainWidget : public QWidget
{
    Q_OBJECT

public:
    MainWidget();
    void selectFile();
    void getXlsx();

public slots:
    void updateParam();

private:
    QGroupBox * menu();

private:
    QLabel * Text1;
    QLabel * Text2;
    QLabel * Text3;
    QLabel * MM1;
    QLabel * MM2;
    QLineEdit * Line1;
    QLineEdit * Line2;
    QPushButton * SelectFileBtn;

    int span = 150;
    int section = 40;
    int rowOfData = -1;
    QString filePath;
};
#endif // MAINWIDGET_H
