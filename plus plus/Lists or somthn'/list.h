#include"node.h"
#pragma once


class Linkedlist {
    Node* head; //the address (pointer) of the first node in the list

public:
    Linkedlist() { head = NULL; }

    void insertNode(int); //adds node to end of list
    void printList();
    void deleteNode(int); //deletes node at given position
    void listLength();
    void reverseList(int);
};
