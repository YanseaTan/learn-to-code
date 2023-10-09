#include "MainWidget.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    MainWidget mWidget;
    mWidget.show();

    a.exec();
    return 0;
}
