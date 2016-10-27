QT_VERSION = $$[QT_VERSION]
QT_VERSION = $$split(QT_VERSION, ".")
QT_VER_MAJ = $$member(QT_VERSION, 0)
QT_VER_MIN = $$member(QT_VERSION, 1)

lessThan(QT_VER_MAJ, 4) {
	error(DetectShutdown is only tested under Qt 4.x!)
}

QT += widgets
QMAKE_CXXFLAGS += -std=c++14
TARGET = DetectShutdown
CODECFORSRC = UTF-8

!isEmpty(DEBUG) {
    DEFINES += DEBUG
    QMAKE_CXXFLAGS += -g
}

SOURCES = main.cpp
