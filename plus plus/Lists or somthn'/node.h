#include<iostream>
#pragma once

class Node {
public:
    int data; //the actual information we're trying to store
    Node* next; //the address of the next node in the list

    Node(int info) //constructor
    {
        data = info; //put the info we're storing into the node
        next = NULL; //leave the link to the next node blank for now
    }
};
