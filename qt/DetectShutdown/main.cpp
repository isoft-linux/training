#include <QApplication>
#include <QMainWindow>
#include <QSessionManager>
#include <QFile>
#include <QStandardPaths>
#include <QDateTime>
#include <QDebug>

int main(int argc, char* argv[]) 
{
    QApplication app(argc, argv);
    QObject::connect(&app, &QApplication::commitDataRequest, [](QSessionManager &manager) {
        qDebug() << "DEBUG:" << __FILE__ << __PRETTY_FUNCTION__ << "It might logout or shutdown";
        QFile file(QStandardPaths::writableLocation(QStandardPaths::HomeLocation) + "/.DetectShutdown.txt");
        if (file.open(QIODevice::Append | QIODevice::Text)) {
            QTextStream out(&file);
            out << QDateTime::currentDateTime().toString() << " " << manager.sessionId() 
                << " " << manager.sessionKey() << "\n";
            file.close();
        }
    });
    QMainWindow window;
    window.show();
    return app.exec();
}
