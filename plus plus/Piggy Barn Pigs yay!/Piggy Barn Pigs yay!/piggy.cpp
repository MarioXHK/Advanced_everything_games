#include"piggy.h"
#include<iostream>
using namespace std;
//class function definitions AND standalone function definitions go here
piggy::piggy() {
	xpos = rand() % 600 + 100;
	ypos = rand() % 600 + 100;
	isAsleep = false;
	isWalking = false;
	number = 0;
}

piggy::piggy(int num) {
	xpos = rand() % 600 + 100;
	ypos = rand() % 600 + 100;
	isAsleep = false;
	isWalking = false;
	number = num;
}
void piggy::walk() {
	if (isAsleep) {
		int slep = rand() % 10 + 1;
		if (slep < 7)
			cout << "Dreaming about walking!\n";
		else {
			cout << "Woke up!\n";
			isAsleep = false;
		}
		return;
	}
	//randomly move in one of 8 directions when isWalking is true
	if (isWalking == true) {
		xpos += rand() % 10 - 5;
		ypos += rand() % 10 - 5;
		int off = rand() % 100 + 1;

		if (off < 30) { //30% chance walking will turn off each turn
			isWalking = false;
		}
	}
	//10% chance any turn that isWalking will turn ON
	int num = rand() % 100 + 1;
	if (num < 10) {
		isWalking = true;
		cout << "walking!" << endl;
		system("pause");

	}
}
void piggy::sleep() {
	isAsleep = true;
}


void piggy::draw() {
	//eventually this will hold drawing functions to make it graphical
	cout << "Hello I am pig # " << number << endl;
	cout << "My position is " << xpos << " , " << ypos << endl;
	cout << "I am ";
	if (isAsleep) cout << " asleep." << endl;
	else cout << " not asleep." << endl;
}