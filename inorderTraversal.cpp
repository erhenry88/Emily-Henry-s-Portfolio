// inorderTraversal.cpp : This file contains the 'main' function. Program execution begins and ends there.
//Emily Henry
//CS 3220
//Module 3 Assignment 3 Problem 7 inorderTraversal
//April 4,2021

#include <iostream>
#include "BinarySearchTree.h"'
#include <string>

using namespace std;

int index = 0;
void inorderTraversal(BinarySearchTree<string> x[], int root);
int main()
{
  
	BinarySearchTree<string> array[9];
	array[0].item = "Jose";
	array[0].leftChild = 1;
	array[0].rightChild = 4;
	array[1].item = "Deepak";
	array[1].leftChild = 2;
	array[1].rightChild = 3;
	array[2].item = "Anton";
	array[2].leftChild = -1;
	array[2].rightChild = -1;
	array[3].item = "Elisa";
	array[3].leftChild = -1;
	array[3].rightChild = -1;
	array[4].item = "Mia";
	array[4].leftChild = -1;
	array[4].rightChild = 5;
	array[5].item = "Qiang";
	array[5].leftChild = -1;
	array[5].rightChild = 6;
	array[6].item = "Zoe";
	array[6].leftChild = -1;
	array[6].rightChild = -1;
	int root = 0;
	inorderTraversal(array, root);
	

}



void inorderTraversal(BinarySearchTree<std::string> x[], int root) {
	if (root == -1) {
		return;
	}

	inorderTraversal(x, x[root].leftChild);
	cout << x[index].item << " ";
	x[index++].item = x[root].item;
	

	inorderTraversal(x,x[root].rightChild);
}


