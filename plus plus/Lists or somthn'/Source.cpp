#include <iostream> 
#include"list.h"
using namespace std;


int main()
{
    Linkedlist list;

    list.insertNode(1);
    list.insertNode(2);
    list.insertNode(3);
    list.insertNode(4);

    cout << "Elements of the list are: ";

    list.printList();
    cout << "The list length: ";
    list.listLength();
    cout << endl;

    list.deleteNode(2);

    cout << "Elements of the list are: ";
    list.printList();
    cout << "The list length: ";
    list.listLength();
    cout << endl;
    return 0;
}