/* 

	Assignment Number: 3
	Student Name: Thanusha Thaninayagam

	Student Oath: This assignment represents my 
	own work in accordance with Seneca Academic Policy

	Signature: Thanusha Thaninayagam
	
	Purpose: Design and code a class called 'SetiWriter',
	to write data to a file.
	
*/

#include <cstdio>
#include <cstring>
#include <ctype.h>
#include <stdio.h>
#include "setiwriter.h"

#include <iostream>
using namespace std;


/*
	SetiWriter( ): Default SetiWriter. When values are 
	not supplied to the object.
*/

SetiWriter::SetiWriter( ){

	// default values
	strcpy(fileName, "seti.dat");
	strcpy(accessMode, "w");
}


/*
	SetiWriter: When the values for the filename and 
	accessmode are supplied. Validate the values passed.
*/

SetiWriter::SetiWriter(char name [ ], char mode [ ]){
	
	// filename should be less than 21 characters
	if(strlen(name) < 21)
		strcpy(fileName, name);
	else
		strcpy(fileName, "seti.dat");
		
	// mode should be r, w,rb, wb, or a
	if((strcmp(mode, "r") || strcmp(mode, "w") || strcmp(mode, "rb") || strcmp(mode, "wb") ||strcmp(mode, "a")) == 0)
		strcpy(accessMode, mode);
	else
		strcpy(accessMode, "w");
}


/*
	~SetiWriter: Destructor. When destroyed, 
	close any files that are open.
*/

SetiWriter::~SetiWriter( ){
	
	// close the file
	fclose(setiFile);
}


/*
	write: Writes the data stored in the Seti object to 
	the file if the signal is valid.
*/

long SetiWriter::write(const Seti &r, bool wFlag, int type){
	
	int signalLen = strlen(r.signal);
	char copySignal[signalLen];
	long numBytes = 0;
	
	setiFile = fopen(fileName, accessMode);
	strcpy(copySignal, r.signal);
	
	if(strcmp(copySignal, "NON-SEQUITOR") == 0)
		return numBytes;
	
	// if wFlag is false, write entire signal into file
	if(wFlag == false && setiFile != NULL)
		fputs(copySignal, setiFile);
	// if wFlag is false, write only fibonacci or prime
	// positioned characters of the signal into file
	else if(wFlag == true && setiFile != NULL){
		
		//  copy fibonacci positioned characters
		if(type == 1)
			r.copyFibonacci(copySignal);
		//  copy prime positioned characters
		else if(type == 3)
			r.copyPrimes(copySignal);
			
		fputs(copySignal, setiFile);
	}
	
	// calculate the total number of bytes written
	// into the file
	numBytes = numBytes + strlen(copySignal);
	return numBytes;
}