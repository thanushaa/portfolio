/* 

	Assignment Number: 3
	Student Name: Thanusha Thaninayagam

	Student Oath: This assignment represents my 
	own work in accordance with Seneca Academic Policy

	Signature: Thanusha Thaninayagam
	
	Purpose: Design and code a class called 'Seti',
	to properly encapsulate information specific to
	the analysis of a radio signal.
	
*/

#include <cstdio>
#include <cstring>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include "seti.h"
#include <iostream>
using namespace std;

Seti join(Seti one, Seti two);
long analyze(const char [ ], char [ ], int, int, int);


char* Seti::allocateMem(int num) {
	
	char *temp;
	
	try { 
		temp = new char[num];
	}
	catch(std::bad_alloc) {
		cout << "error allocating... " << num << " bytes of memory..." << endl;
		temp = NULL;
	}
	return temp;
}

	
/* 
	Seti(): Create Seti object without any parameters. Set
	default values.
*/	
	
Seti::Seti( ){
	
	char rawData[5];
	
	signal = allocateMem(61);
	
	// default values for Seti
	strcpy(rawData, "");
	frequency = 0;
	a = 32;
	b = 126;
	
	// get signal
	analyze(rawData, signal, frequency, a, b);
}


/* 
	Seti(const char [ ], int, int, int): Create Seti object 
	with parameters. Validate the signal, frequency, and ranges.
*/

Seti::Seti(const char rawData[ ], int newFreq, int newA, int newB){
	
	signal = allocateMem(61);
	
	// validating the frequency
	if(newFreq >= 0 && newFreq <= 9)
		frequency = newFreq;
	else
		frequency = 0;
	
	// validating the range a and b
	if(newA >= 0 && newA <= 255)
		a = newA;
	else
		a = 0;
	
	if(newB >= 0 && newB <= 255)
		b = newB;
	else
		b = 0;
	
	// get signal
	analyze(rawData, signal, frequency, a, b);
	
	int lengthStr = strlen(signal);
	
	// if the signal is longer than 60 characters,
	// exclude the remainder of the string.
	if(lengthStr > 61)
		signal[61] = '\0';
	else
		signal[lengthStr] = '\0';
} 


/*	
	Seti(const char [ ], int, int, int, int): Create a Seti 
	object with passing the length to allocate memory.
*/

Seti::Seti(const char rawData[ ], int newFreq, int newA, int newB, int length){
	
	signal = allocateMem(length + 1);
	
	// validating the frequency
	if(newFreq >= 0 && newFreq <= 9)
		frequency = newFreq;
	else
		frequency = 0;
	
	// validating the range a and b
	if(newA >= 0 && newA <= 255)
		a = newA;
	else
		a = 0;
	
	if(newB >= 0 && newB <= 255)
		b = newB;
	else
		b = 0;
	
	// get signal
	analyze(rawData, signal, frequency, a, b);
	
	int lengthStr = strlen(signal);
	
	// if the signal is longer than the length ,
	// exclude the remainder of the string.
	if(lengthStr > length)
		signal[length + 1] = '\0';
	else
		signal[lengthStr] = '\0';

}


/* 
	getFrequency: Return the objects frequency. 
*/

int Seti::getFrequency( ) const{

	return frequency;
}


/*
	getRanges: Update the pointers to the range values stored in class.
*/

 void Seti::getRanges (int *pa, int *pb) const{

	// set a and b ranges to pa and pb 
	*pa = a;
	*pb = b;
}


/*
	setRanges: Set the ranges a and b being stored in class to the
	values newA an newB. The new ranges should be between 0 and 255.
	
*/

void Seti::setRanges (int newA, int newB){
	
	// new ranges should be between 0 and 225
	if(newA >= 0 && newA <= 255)
		a = newA; 
	if(newB >= 0 && newB <= 255)
		b = newB;

}


/*
	getMessage: Copy Seti's message into pointer pSignal.
*/

void Seti::getMessage(char *pSignal) const{
	
	// copy signal into pSignal
	strcpy(pSignal, signal);
}


/*
	replaceChar: Replace the character 'letter' in signal at the position
	given 'pos'.
*/

bool Seti::replaceChar(int pos, char letter){
	
	int lengthStr = strlen(signal) - 1;
	
	// if pos value is within the array and signal
	// is NOT a NON-SEQUITOR string return true
	if(pos >= 0 && pos <= lengthStr && strcmp(signal, "NON-SEQUITOR") != 0){
		signal[pos] = letter;
		return true;
	}
	else
		return false;
}


/*
	copyPrimes: Return true if all characters whose position within 
	Seti's signal array that are prime numbers are copied into 
	pointer ppSignal. Return false if signal is 'NON-SEQUITOR'.
*/

bool Seti::copyPrimes(char *ppSignal) const{

	int i = 2, j, k = 0, count = 0,
		length = strlen(signal);
		
	// signal should NOT be 'NON-SEQUITOR for this method to work
	if(strcmp(signal, "NON-SEQUITOR") == 0){
		strcpy(ppSignal, "\0");
		return false;
	}
	
	// copy all the prime positioned characters into pSignal	
	while(i < length){
	
		// checking if i is a prime number
		for(j = 1; j <= i; j++){
			if(i % j == 0)
				count += j;
		}
		// if prime than add character to ppSignal
		if(count == i + 1){
			ppSignal[k] = signal[i];
			ppSignal[k + 1] = '\0';
			k++;
		}
		count = 0;
		i++;
	}
	ppSignal[k + 1] = '\0';
	return true;
}

/*
	copyFibonacci: Return true if all characters whose position within 
	Seti's signal array that are Fibonacci numbers are copied into 
	pointer fpSignal. Return false if signal is 'NON-SEQUITOR'.
*/

bool Seti::copyFibonacci(char *fpSignal) const{
	
	int i = 2, j,
		lengthStr = strlen(signal) -1, 
		fibonacci[lengthStr];
	
	// signal should NOT be 'NON-SEQUITOR for this method to work
	if(strcmp(signal, "NON-SEQUITOR") == 0)
		return false;
	
	// determine the Fibonacci sequence
	fibonacci[0] = 0;
	fibonacci[1] = 1;
	while((fibonacci[i - 1] + fibonacci[i - 2]) < lengthStr){
		fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
		i++;
	}
	
	// copy all the fibonacci positioned characters into fpSignal
	for(j = 0; j < i; j++){
		fpSignal[j] = signal[fibonacci[j]];
		fpSignal[j + 1] = '\0';
	}

	return true;
}


/*
	initCap: Return the number of characters converted. 
*/

int Seti::initCap( ){

	int i = 0, charConverted = 0,
		lengthStr = strlen(signal);
	
	if(strcmp(signal, "NON-SEQUITOR") == 0){
		charConverted = 0;
	}
	else{
		while(i < lengthStr){
			if(isalpha(signal[i])){
			
				// if the first character is lowercase, change it to upper
				if(i == 0 && islower(signal[i])){
					signal[i] = toupper(signal[i]);
					charConverted++;
				}
				// if the last character is a space and the character is 
				// lowercase, change it to uppercase
				else if(i > 0 && isspace(signal[i-1]) && islower(signal[i])){
					signal[i] = toupper(signal[i]);
					charConverted++;
				}
				// if the last character is not a space and the character is
				// uppercase, change it lowercase
				else if(i > 0 && !isspace(signal[i-1]) && isupper(signal[i])){
					signal[i] = tolower(signal[i]);
					charConverted++;
				}
			}
			i++;
		}
	}
	return charConverted;
}


/*  operator ++: Increase the value of frequency by 1 */

Seti Seti::operator++( ){

	// increase frequency by 1 if frequency
	// is under 9
	if (frequency < 9) 
		frequency++; 
		
	return *this;
}


/*	operator !: Return true if signal is NOT valid */

bool Seti::operator!( ) const{

	// return false if signal is valid
	if (strcmp(signal, "NON-SEQUITOR") != 0)
		return false;
	else return true;
	
}


/*	operator = */

void Seti::operator=(const Seti &from){

	int size = strlen(from.signal);

	if(signal)
		delete [ ] signal;
	
	frequency = from.frequency;
	a = from.a;
	b = from.b;
	
	// allocate memory
	signal = allocateMem(size + 1);
	if(signal) 
		strcpy(signal, from.signal);
}


/* operator +: Join two Seti objects together */

Seti Seti::operator+(const Seti &from){
	
	return join(*this, from);
}


/*	copy constructor	*/

Seti::Seti(const Seti &from){

	int size = strlen(from.signal);
	
	if(signal)
		delete [ ] signal;
	
	frequency = from.frequency;
	a = from.a;
	b = from.b;
	
	// allocate memory
	signal = allocateMem(size + 1);
	if(signal) 
		strcpy(signal, from.signal);
}


/*	Destructor for Seti */

Seti::~Seti( ){
	
	// free up memory that has been dynamically allocated
	if(signal) 
		delete [ ] signal;
}


/*
	join: Return a Seti object that joins two Seti objects together.
*/

Seti join(Seti one, Seti two){
	
	char newSignal[61];
	
	int totalOne = strlen(one.signal), totalTwo = strlen(two.signal),
		i, j = 0, frequency, a, b;
	
	// If both objects are valid then join two objects
	if (strcmp(one.signal, "NON-SEQUITOR") != 0 && strcmp(two.signal, "NON-SEQUITOR") != 0){
		
		if(totalOne == 61){
			strcpy(newSignal, one.signal);
			frequency = one.frequency;
			a = one.a;
			b = one.b;
		}
		else if(totalOne + totalTwo < 61 || totalOne + totalTwo > 61 ){
			
			// signals add up to less than 60 characters
			if(totalOne + totalTwo < 61){
				strcpy(newSignal, one.signal);
				strcat(newSignal, two.signal);
			}
			// signals add up to more than 60 characters
			else if(totalOne + totalTwo > 61){
				strcpy(newSignal, one.signal);
				i = totalOne;
				while(i != 60){
					newSignal[i] = two.signal[j];
					newSignal[i + 1] = '\0';
					i++;
					j++;
				}
			}	
			
			// get the lower frequency 
			if(one.frequency > two.frequency)
				frequency = two.frequency;
			else
				frequency = one.frequency;
			
			// get the lower 'a' range
			if(one.a > two.a)
				a = two.a;
			else
				a = one.a;
			
			// get the lower 'b' range
			if(one.b > two.b)
				b = one.b;
			else
				b = two.b;	
		}
	}
	// one of the signals must be NOT valid
	else{
		return Seti();
	}
	
	Seti c;
	strcpy(c.signal, newSignal);
	c.frequency = frequency;
	c.setRanges(a, b);
	return c;
}