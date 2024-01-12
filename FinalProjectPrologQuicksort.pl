"Emily Henry
CS 3910 Final Project Prolog Quicksort Implementation
December 12, 2021"

:- initialization(main).
main :- write('Hello World!').

list_order([X,Y|Tail]) :- X=<Y,list_order([Y|Tail]).list_order([x]) 
sortThisList[2,5,10,9,6,8,7,3,1,4]


getMin(thisList):-		"get the minimum of the first element and the first element of the Tail of given list"

not(list_order(thisList))->		"if list is not sorted do the following:"
drop(1,thisList,Tmin)
list_min(Tmin,[Head|thisList],Min)	"sets min to the minimum of the two (first element Tmin and tail first element)"

Min = [Head|thisList]->		"if Min is the head of the tail"
drop(1,thisList,Min)		"drop the first element of the tail and make it Min"
Min = Tmin->				"if Min is T (the first element)"

append(Min,thisList,[Head|thisList])	 "append it to the front of the list"



getMax(thisList[]):-
not(list_order(thisList))->	

drop(1,thisList,Tmax)				"get the first element and label it Tmax"
list_max(Tmax,[Head|thisList],Max)	"check which is larger Tmax or head of tail"

Max = [Head|thisList]->			"if the head of tail is larger"
drop(1,thisList,Max)			"take the head from the tail and append it to the end"

Max = Tmax ->					"if the first element Tmax is larger append it to the end"

append(Max,thisList,thisList)		"append to the end of the list"




"Quicksort Function"
quicksort([]):-			
list_order(sortThisList)->		"if list is sorted print the list to the console"
[sortThisList][write]

not(list_order(thisList))->		"if list is not sorted perform the recursive call and the getMin and"
take(1,sortThisList,pivot)		"getMax functions"
append(
	quicksort(getMin(sortThisList)),pivot,quicksort(getMax(sortThisList))).

quicksort(sortThisList)

	
