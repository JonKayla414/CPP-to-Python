/*
* 
*
*@Author: Numerous Authours
* Jon-Kayla Pointer
* 
* School: Southern New Hampsire University
*
* This program is designed to use Python and C ++.
* This program reads a file called "inputfile.txt" and analyzes the data to make a list of the frequency number of items purchased for a grocercy item.
* After analyzing the data it writes the data into a file named "frequency.dat"
* Prompts user to make a menu selection until use chooses to exit the program.
* 
* 
* 
*/


#include <Python.h>
#include <iostream>
#include <Windows.h>
#include <cmath>
#include <string>
#include <stdio.h>

using namespace std;

/*
Description:
	To call this function, simply pass the function name in Python that you wish to call.
Example:
	callProcedure("printsomething");
Output:
	Python will print on the screen: Hello from python!
Return:
	None
*/
void CallProcedure(string pName)
{

	char* procname = new char[pName.length() + 1];
	std::strcpy(procname, pName.c_str());

	Py_Initialize();
	 //PyObject* my_module = PyImport_ImportModule("pythonCode");
	//PyObject* sys = PyImport_ImportModule("sys");
	//PyObject* path = PyObject_GetAttrString(sys, "path");
	//PyList_Append(path, PyUnicode_FromString("."));
	PyObject* my_mod = PyImport_ImportModule("pythonCode");

	PyErr_Print();
	PyObject* my_function = PyObject_GetAttrString(my_mod, procname);
	PyObject* my_result = PyObject_CallObject(my_function, NULL);
	Py_Finalize();

	delete[] procname;
}

/*
Description:
	To call this function, pass the name of the Python functino you wish to call and the string parameter you want to send
Example:
	int x = callIntFunc("PrintMe","Test");
Output:
	Python will print on the screen:
		You sent me: Test
Return:
	100 is returned to the C++
*/
int callIntFunc(string proc, string param)
{
	char* procname = new char[proc.length() + 1];
	std::strcpy(procname, proc.c_str());

	char* paramval = new char[param.length() + 1];
	std::strcpy(paramval, param.c_str());


	PyObject* pName, * pModule, * pDict, * pFunc, * pValue = nullptr, * presult = nullptr;
	// Initialize the Python Interpreter
	Py_Initialize();
	PyObject* sys = PyImport_ImportModule("sys");
	PyObject* path = PyObject_GetAttrString(sys, "path");
	PyList_Append(path, PyUnicode_FromString("."));
	// Build the name object
	pName = PyUnicode_FromString((char*)"pythonCode");
	// Load the module object
	pModule = PyImport_Import(pName);
	// pDict is a borrowed reference 
	pDict = PyModule_GetDict(pModule);
	// pFunc is also a borrowed reference 

	pFunc = PyDict_GetItemString(pDict, procname);
	if (PyCallable_Check(pFunc))
	{
		pValue = Py_BuildValue("(z)", paramval);
		PyErr_Print();
		presult = PyObject_CallObject(pFunc, pValue);
		PyErr_Print();
	}
	else
	{
		PyErr_Print();
	}
	//printf("Result is %d\n", _PyLong_AsInt(presult));
	Py_DECREF(pValue);
	// Clean up
	Py_DECREF(pModule);
	Py_DECREF(pName);
	// Finish the Python Interpreter
	Py_Finalize();

	// clean 
	delete[] procname;
	delete[] paramval;


	return _PyLong_AsInt(presult);
}

/*
Description:
	To call this function, pass the name of the Python functino you wish to call and the string parameter you want to send
Example:
	int x = callIntFunc("doublevalue",5);
Return:
	25 is returned to the C++
*/
int callIntFunc(string proc, int param)
{
	char* procname = new char[proc.length() + 1];
	std::strcpy(procname, proc.c_str());

	PyObject* pName, * pModule, * pDict, * pFunc, * pValue = nullptr, * presult = nullptr;
	// Initialize the Python Interpreter
	Py_Initialize();
	PyObject* sys = PyImport_ImportModule("sys");
	PyObject* path = PyObject_GetAttrString(sys, "path");
	PyList_Append(path, PyUnicode_FromString("."));
	// Build the name object
	pName = PyUnicode_FromString((char*)"pythonCode");
	// Load the module object
	pModule = PyImport_Import(pName);
	// pDict is a borrowed reference 
	pDict = PyModule_GetDict(pModule);
	// pFunc is also a borrowed reference 
	pFunc = PyDict_GetItemString(pDict, procname);
	if (PyCallable_Check(pFunc))
	{
		pValue = Py_BuildValue("(i)", param);
		PyErr_Print();
		presult = PyObject_CallObject(pFunc, pValue);
		PyErr_Print();
	}
	else
	{
		PyErr_Print();
	}
	//printf("Result is %d\n", _PyLong_AsInt(presult));
	Py_DECREF(pValue);
	// Clean up
	Py_DECREF(pModule);
	Py_DECREF(pName);
	// Finish the Python Interpreter
	Py_Finalize();

	// clean 
	delete[] procname;

	return _PyLong_AsInt(presult);
}



/** 
*
* Displays the Menu Selection
*
* Returns no value.
*/
void displayMenu() {
	cout << "Main Menu: \n";
	string line1 = "1: List all items purchased and the frequency number.";
	string line2 = "2: Display the frequency of a specific item";
	string line3 = "3: Make histogram";
	string line4 = "4: Read Histogram";
	string line5 = "5: Exit";
	string line6 = "Enter your selection as a number 1, 2, 3, 4, or 5.";

	printf("%10s\n%10s\n%s\n%s\n%s\n%s ", line1.c_str(), line2.c_str(), line3.c_str(), line4.c_str(), line5.c_str(), line6.c_str());

}


/**
*
 Checks if the user inputed a number or a string.
*
* @param String value that the user entered
* @return -999 if the value is not number otherwise returns the corresponding number
*/int checkValue(string userI) {
	string input = userI;
	int amount_input;


	try {
		amount_input = stoi(input);


	}
	catch (exception& err)
	{
		amount_input = -999;

	}

	return amount_input;
}

/** 
* 
* Prompts user to make an appropriate menu selection. Calls the function CallIntFuc( param) For prorgram to call the corresponding fuction that the user selected.
* Calls the funcction checkVal(param) to ensure that a user enters a valid entry.
* 
* @param No parameters
* @return No return values
*/
void driver(){
	
	// initilize variables
	string user;
	string userItem;
	int choice;
	int attempt=0;
	int valid = 0;

	int validString = 0;
	int breaker = 0;

	


	//Welcome the user
	cout << "Welcome to the Grocery-Tracking Program!\n"; 
	displayMenu();
	cout << ("Entering wrong input 3 times will quit program.\n");
	cin >> user;
	valid = checkValue(user);
	attempt++;
	cout << valid;
	while (attempt < 4 && valid == -999 && valid > 5) {
		if (valid == 1 || valid == 2 || valid == 3 || valid == 4 || valid == 5) {
			break;
		}
		else {
			cout << "In Valid Input!\n";
			cout << "Attempt number: " << attempt;
			displayMenu();
			cout << ("\nEntering wrong input 3 times will quit program.\n");
			cin >> user;
			valid = checkValue(user);
			attempt++;
		}
	}
	if (attempt < 4 && valid != -999) {
		if (valid == 1 || valid == 2 || valid == 3 || valid == 4 || valid == 5) {
			
			
			while (breaker < 1 && attempt < 4) {
				
				//Choice 1
				if (valid == 1) {
					attempt = 0;
					CallProcedure("printAllList");
					cout << "Main Menu: \n";
					displayMenu();
					cout << ("Entering a wrong input 3 times in a row will quit program.\n");
					cout << "Attempt: " << attempt << endl;
					cin >> user;
					valid = checkValue(user);

				}
				//Choice 2 
				else if (valid == 2) 
				{

					attempt = 0;

					cout << "Please enter a grocery name item." << endl << "Note: Any invalid inputs will take you to main menu.\n";
					cin >> userItem;
					validString = checkValue(userItem);
					if (validString == -999) {
						callIntFunc("printSpecItem", userItem);

						cout << "Main Menu: \n";
						displayMenu();
						cout << ("Entering a wrong input 3 times in a row will quit program.\n");
						cout << "Attempt: " << attempt << endl;
						cin >> user;
						valid = checkValue(user);
					}
					else {
						cout << "Invalid input! Taking you to Main Menu!\n";
						cout << "Main Menu: \n";
						displayMenu();
						cout << ("Entering a wrong input 3 times in a row will quit program.\n");
						cout << "Attempt: " << attempt << endl;
						cin >> user;
						valid = checkValue(user);
					}
				} 
				//Choice 3
				else if (valid == 3) {
					attempt = 0;

					CallProcedure("makeHistogram");
					cout << "Main Menu: \n";
					displayMenu();
					cout << ("Entering a wrong input 3 times in a row will quit program.\n");
					cout << "Attempt: " << attempt << endl;
					cin >> user;
					valid = checkValue(user);

					
				}
				//Choice 4
				else if (valid == 4) {
					attempt = 0;

					CallProcedure("readFreq");
					cout << "Main Menu: \n";
					displayMenu();
					cout << ("Entering a wrong input 3 times in a row will quit program.\n");
					cout << "Attempt: " << attempt << endl;
					cin >> user;
					valid = checkValue(user);

				}
				//Choice 5. User quitts so end loop
				else if (valid == 5) {
					
					cout << "Good-Bye!\n";
					breaker = 99;
					break;
				}
				//Wrong Input
				else {
					attempt++;
					cout << "Invalid Input!\n";
					if (attempt == 3) {
						cout << "Maximum number of attempts reached!\n";
						cout << "Exiting program\n";
						cout << "Good-Bye\n";
						breaker = 99;
						break;
					}
					else {
						displayMenu();
						cout << ("Entering a wrong input 3 times in a row will quit program.\n" );
						cout << "Attempt: " << attempt << endl;
						cin >> user;
						valid = checkValue(user);
					}
				}
			}
		}else {
			cout << "Good-Bye!\n";
		}
	
	
	}
	else {
		cout << "Good-Bye";
	}

}



// Main function
void main()
{
	CallProcedure("printsomething");
	//CallProcedure("printAllList");
	//CallProcedure("makeHistogram");
	//CallProcedure("readFreq");
	//callIntFunc("printSpecItem", "spinach");
	//MultiplicationTableProgram();
	//cout << callIntFunc("PrintMe", "House") << endl;
	//cout << callIntFunc("SquareValue", 2);
	driver();
}