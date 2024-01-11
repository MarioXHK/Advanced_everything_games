#pragma once
class birdy {
private:
	int xpos;
	int ypos;
	int zpos;
	bool isWalking;
	bool isFlying;
	bool isSleeping;
	int birdNumber;
	int exaust;
	bool descend;
	bool tryingToSleep;
public:
	birdy();
	birdy(int num);
	void walk();
	void fly();
	void sleep();
	void draw();
};