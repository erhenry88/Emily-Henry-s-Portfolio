//Emily Henry
//CS 3220
//May 7, 2021
//Assignment 8 Exercise 10 p 695

#include "BTree.h"
#include <cstddef>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
BTree::BTree(int t1) {
	root = NULL;
	t = t1;
}

void BTree::Traverse() {
	if (root != NULL) {
		root->Traverse();
	}
}

BTreeNode* BTreeNode::searchTree(int key) {
	int i = 0;
	while (i < currentNumberOfKeys && key > keys[i]) {
		i++;
	}
	if (keys[i] == key) {
		return this;
	}
	if (leaf == true) {
		return NULL;
	}
	return child[i]->searchTree(key);
}
void BTreeNode::rangeQuerySearchTree(int startKey, int endKey) {
	//cout << endl;
	int i;
	//cout << "currentNumberofKeys " << currentNumberOfKeys << endl;
	for (i = 0;i < currentNumberOfKeys;i++) {
		if (leaf == false) {
			child[i]->rangeQuerySearchTree(startKey,endKey);
		}
		//cout << "keys[i] " << keys[i]<<endl;
		if (keys[i] > startKey && keys[i] < endKey) {
			cout << " " << keys[i];
		}
	}
	if (leaf == false) {		//print the last child
		child[i]->rangeQuerySearchTree(startKey,endKey);
	}

}
void BTree::rangeQuerySearchTree(int startSearchKey, int endSearchKey) {
	if (root == NULL) {
		return ;
	}
	else {
		cout << endl;
		root->rangeQuerySearchTree(startSearchKey,endSearchKey);

	}
}

BTreeNode* BTree::searchTree(int searchKey) {
	if (root == NULL) {
		return NULL;
	}
	else {
		BTreeNode* btree = root->searchTree(searchKey);
		
		return btree;
	}
}

BTreeNode::BTreeNode(int p1, bool leaf1) {
	minKey = p1;
	leaf = leaf1;
	keys = new int[2 * minKey - 1];
	child = new BTreeNode * [2 * minKey];
	currentNumberOfKeys = 0;
}

void BTreeNode::Traverse() {

	int i;
	//cout << "currentNumberofKeys " << currentNumberOfKeys << endl;
	for (i = 0;i < currentNumberOfKeys;i++) {
		if (leaf == false) {
			child[i]->Traverse();
		}
		cout << " " << keys[i];
	}
	if (leaf == false) {		//print the last child
		child[i]->Traverse();
	}
}
void BTreeNode::insert(int k) {
	int i = currentNumberOfKeys - 1;
	if (leaf == true) {
		while (i >= 0 && keys[i] > k) {
			keys[i + 1] = keys[i];
			//cout <<"keys[i+1] "<< keys[i + 1];
			i--;
		}
		keys[i + 1] = k;
		currentNumberOfKeys = currentNumberOfKeys + 1;
	}
	else {
		while (i >= 0 && keys[i] > k) {
			i--;
		}
		//check if the child we found is full
		if (child[i + 1]->currentNumberOfKeys == (2 * minKey - 1)) {
			splitChild(i + 1, child[i + 1]);
			if (keys[i + 1] < k) {
				i++;
			}
			//child[i + 1]->insert(k);
		}
		else
			child[i + 1]->insert(k);
	}

}
/*
void BTreeNode::insert(int k) {
	int i = currentNumberOfKeys - 1;
	if (leaf == true) {
		while (i>=0  && keys[i] > k) {
			keys[i + 1] = keys[i];
			//cout <<"keys[i+1] "<< keys[i + 1];
			i--;
		}
		keys[i + 1] = k;
		currentNumberOfKeys = currentNumberOfKeys + 1;
	}
	else {
		while (i >= 0 && keys[i] > k) {			
			i--;				
		}									
												//check if the child we found is full
		if (child[i + 1]->currentNumberOfKeys == (2 * minKey - 1)) {
			splitChild(i + 1, child[i + 1]);
			if (keys[i + 1] < k) {
				i++;
			}
			child[i + 1]->insert(k);
		}
	}
}
*/
void BTreeNode::splitChild(int i, BTreeNode* y) {		//we split because child y is full and this is utility function to split y
	BTreeNode* z = new BTreeNode(y->minKey, y->leaf);
	z->currentNumberOfKeys = minKey - 1;
	//copy the keys											
	for (int j = 0;j < minKey - 1;j++) {
		z->keys[j] = y->keys[j + minKey];
		
	}
	if (y->leaf == false) {			// if y is not a leaf 
		for (int j = 0; j < minKey;j++) {
			z->child[j] = y->child[j + minKey];		//set 3 of z's child to y's child  
		}
	}
	y->currentNumberOfKeys = minKey - 1;		//sets y's current number of keys to 2 because node is split
	
	for (int j = currentNumberOfKeys;j >= i + 1;j--) {	// move children over
		child[j + 1] = child[j];
	}
	child[i + 1] = z;					//link this to the node

	for (int j = currentNumberOfKeys - 1;j >= i;j--) {
		keys[j + 1] = keys[j];
	}											// move up
	keys[i] = y->keys[minKey - 1];				// copying middle key of y to this node
	currentNumberOfKeys = currentNumberOfKeys + 1;
}    

void BTree:: insert(int k) {
	if (root == NULL) {
		root = new BTreeNode(t, true);
		//cout << "BTreeNodeLeaf " << root->leaf<<endl;
		//cout << "t " << t<<endl ;
		
		root->keys[0] = k;
		//cout << "key[0] " << root->keys[0]<<endl;
		root->currentNumberOfKeys = 1;
		//cout << "currentNumnerOfKeys " << root->currentNumberOfKeys<<endl;
	}
	else {
		if (root->currentNumberOfKeys == (2 * t - 1)) {
			BTreeNode* s = new BTreeNode(t, false);
			s->child[0] = root;
			s->splitChild(0, root);
			int i = 0;
			if (s->keys[0] < k) {
				i++;
			}
			s->child[i]->insert(k);
			root = s;
			
		}
		else {
			root->insert(k);
		}

	}
}
/*BTreeNode* BTreeNode::rangeQuery(int startKey, int endKey) {
	
	for (int i = 0;i < currentNumberOfKeys;i++) {
		if (keys[i] > startKey && keys[i] < endKey) {
			cout << keys[i];
		}
		else {
			break;
		}
	}

	
}
*/
int* BTreeNode::getKeys() {
	return keys;
}

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
