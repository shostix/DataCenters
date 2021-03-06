#include "misc/xmlconverter.h"

#include <iostream>
using std::cerr;
using std::endl;

#include <QtCore/QString>
#include <QtCore/QFile>
#include <QtCore/QIODevice>
#include <QtCore/QTextStream>

#include "routing/testrouter.h"
#include "routing/dijkstrarouter.h"
#include "routing/ksprouter.h"

int main(int argc, char ** argv)
{
    if ( argc != 2 )
    {
        cerr << "Usage: " << *argv << " <inputFile>" << endl;
        return -1;
    }

    QString inputName = QString(argv[1]);
    QString input;
    {
        QFile inputFile(inputName);
        inputFile.open(QIODevice::ReadOnly | QIODevice::Text);
        QTextStream inputStream(&inputFile);
        input = inputStream.readAll();
        inputFile.close();
    }

    XMLConverter * converter = new XMLConverter(input);

    Network * network = converter->getNetwork();
    Link * tunnel = converter->getTunnel();

    DijkstraRouter dRouter(tunnel, network);

    if ( dRouter.route() )
       dRouter.print();
    else
        cerr << "Dijkstra route failed" << endl;

    KSPRouter kRouter(tunnel, network);

    if ( kRouter.route() )
       kRouter.print();
    else 
        cerr << "KShortestPathes route failed" << endl;

    delete converter;
    return 0;
}

