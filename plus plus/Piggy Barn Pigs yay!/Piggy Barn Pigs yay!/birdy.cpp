#include"birdy.h"
#include<iostream>
using namespace std;

birdy::birdy() {
	xpos = rand() % 600 + 100;
	ypos = rand() % 600 + 100;
	zpos = 0;
	isSleeping = false;
	isWalking = false;
	isFlying = false;
	birdNumber = 0;
	exaust = 0;
	descend = false;
	tryingToSleep = false;
}

birdy::birdy(int num) {
	xpos = rand() % 600 + 100;
	ypos = rand() % 600 + 100;
	zpos = 0;
	isSleeping = false;
	isWalking = false;
	isFlying = false;
	birdNumber = num;
	exaust = 0;
	descend = false;
	tryingToSleep = false;
}

void birdy::walk() {
	if (descend)
		return;
	
	if (isWalking) {
		xpos += rand() % 10 - 5;
		ypos += rand() % 10 - 5;
		int off = rand() % 100 + 1;

		if (off < 60) {
			isWalking == false;
		}
	}
	bool pause = false;
	int num = rand() % 100 + 1;
	if (num < 20) {
		isWalking = true;
		cout << "walking!\n";
		pause = true;
	}

	if (num < 10) {
		isFlying = true;
		cout << "Beginning to fly!\n";
		pause = false;
	}

	if (pause)
		system("pause");
	
}

void birdy::fly() {
	if (isFlying) {
		xpos += rand() % 10 - 5;
		ypos += rand() % 10 - 5;
		if (descend) {
			zpos += 5 + (rand() % 5);
			if (zpos <= 0) {
				zpos = 0;
				isFlying == false;
				descend = false;
				cout << "Landed on the ground.\n";
				if (tryingToSleep) {
					tryingToSleep = false;
					sleep();
				}
				else 
					system("pause");
				return;
			}
		}
		else 
			zpos += rand() % 20 - 10;
		
		int off = rand() % 100 + 1;
		if (off < (5+exaust) && !descend) {
			exaust = 0;
			cout << "Exausted of flying.\n";
			descend = true;
		}
		else if (!descend)
			exaust += 5;
	}
}

void birdy::sleep() {
	if (isFlying) {
		exaust = 0;
		tryingToSleep = true;
		cout << "Tired of flying.\n";
		descend = true;
	}
	else {
		isSleeping = true;
		system("pause");
	}
}


void birdy::draw() {
	//eventually this will hold drawing functions to make it graphical
	cout << "Hello I am bird # " << birdNumber << endl;
	cout << "My position is " << xpos << " , " << ypos << " and I'm " << zpos << " feet in the air!\n";
	cout << "I am ";
	if (isSleeping) cout << " asleep." << endl;
	else cout << " not asleep." << endl;
}