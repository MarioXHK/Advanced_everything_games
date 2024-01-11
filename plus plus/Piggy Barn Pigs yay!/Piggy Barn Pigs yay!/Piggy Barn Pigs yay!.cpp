// Pigs!!
//piggy simulator!
//a quick introduction/review of C++ classes!

#include<iostream>
using namespace std;
//standalone function declarations/prototypes would go here too!
#include"piggy.h"
#include"birdy.h"

int main() {
	piggy p1(1); //instantiate a pig object
	birdy p2(2); //instantiate a bird bject
	while (true) { //game loop!
		p2.walk();
		p2.fly();
		p2.draw();
	}
}

