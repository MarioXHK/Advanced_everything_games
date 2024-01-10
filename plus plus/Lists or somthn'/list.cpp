#include"node.h"
#include"list.h"
#include<iostream>
using namespace std;
#pragma once

//--------------------- print list function ---------------------------------------------------
void Linkedlist::printList()
{
    //comments! put these where they belong.
    
    // set up an iterator (something to keep track of where we are on the list)
    Node* temp = head;
    
    // check for empty list
    if (head == NULL) {
        cout << "List empty" << endl;
        return;
    }

    // walk through the list
    while (temp != NULL) {
        cout << temp->data << " ";
        temp = temp->next;
    }
}

//---------------------- insert node function --------------------------------------------------
void Linkedlist::insertNode(int data)
{
    //comments! put these where they belong.
    
    

    //create the new node
    Node* newNode = new Node(data);

    //insert at the end of the list
    if (head == NULL) {
        head = newNode;
        return;
    }
    //assign the iterator to the start of the list
    Node* temp = head;

    //walk through the list until the end
    while (temp->next != NULL) {
        temp = temp->next;
    }
    //update the iterator
    temp->next = newNode;
}

//------------------------------------------------------------------------

//----------------- delete node function -------------------------------------------------------
void Linkedlist::deleteNode(int nodeOffset)
{
    //add comments to each line or section that does something important!

    Node* temp1 = head;
    Node* temp2 = NULL;

    //List Length Holder Initializing
    int ListLen = 0;

    // Checks if list is empty, if it is, then the function ends
    if (head == NULL) {
        cout << "List empty." << endl;
        return;
    }

    //Goes through the list
    while (temp1 != NULL) {
        temp1 = temp1->next;
        ListLen++;
    }

    //Checks if list is out of range
    if (ListLen < nodeOffset) {
        cout << "Index out of range"
            << endl;
        return;
    }

    //Gets the last thing in the list
    temp1 = head;

    //Checks if offset is equal to 1, if so it deletes temp1 and ends the function
    if (nodeOffset == 1) {
        head = head->next;
        delete temp1;
        return;
    }

    while (nodeOffset-- > 1) {

        temp2 = temp1;
        temp1 = temp1->next;
    }

    temp2-> next = temp1->next;
    delete temp1;
}

//--------------------- print list function ---------------------------------------------------
void Linkedlist::listLength()
{
    //List Length Holder Initializing
    int ListLen = 0;

    // set up an iterator (something to keep track of where we are on the list)
    Node* temp = head;

    // check for empty list
    if (head == NULL) {
        cout << "List empty" << endl;
        return;
    }

    // walk through the list
    while (temp != NULL) {
        ListLen++;
        temp = temp->next;
    }

    cout << ListLen << endl;
}