// Henry,Emily_M8_Assignment8.cpp : This file contains the 'main' function. Program execution begins and ends there.
//Emily Henry
//CS 3220
//May 7, 2021
//Assignment 8 Exercise 10 p 695

#include <iostream>
#include "BTree.h"
#include <iostream>

using namespace std;

int main()
{
	BTree btreeObj(3);
	btreeObj.insert(10);
	btreeObj.insert(15);
	btreeObj.insert(5);
	btreeObj.insert(1);
	btreeObj.insert(20);
	btreeObj.insert(33);
	btreeObj.insert(7);
	btreeObj.insert(27);

	btreeObj.Traverse();
	btreeObj.rangeQuerySearchTree(1, 30);
 
}


