#pragma once
class piggy {
private: //private variables can only be seen/used by members of the class
	int xpos;
	int ypos;
	bool isWalking;
	bool isAsleep;
	int number;
public: //can be seen and used by everything in your program
	piggy(); //default constructor: initalizes all the variables in your pig
	piggy(int num); //parameterized constructor
	void walk();
	void sleep();
	void draw();
};