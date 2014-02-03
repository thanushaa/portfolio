/* 
	Assignment Number: 1
	Student Name: Thanusha Thaninayagam

	Student Oath: This assignment represents my 
	own work in accordance with Seneca Academic Policy

	Signature: Thanusha Thaninayagam
	
*/

#include <stdio.h>
#include <string.h>
#include <ctype.h>

long analyze(const char [ ], char [ ], int, int, int);

/*	
	analyze Function: Search for a frequency signal, decode message if signal
	is found and return a the length of signal. If not found, return -1 and set
	the signal to 'NON-SEQUITOR'.
*/

long analyze(const char rawData[ ], char signal[ ], int frequency, int a, int b){

	int i= 0, j = 0, k = 0, ch, signalPosition = 0, nextLine;
	long len = strlen(rawData);
	
	/* Search for the frequency signal */
	while(rawData[i] != '\0') {
	
		nextLine = i + 61;
		if(isdigit(rawData[i]) && rawData[i] - '0' >= frequency && nextLine < len - 1){
			if (rawData[i] == rawData[nextLine] && rawData[i] == rawData[nextLine + 61]){
				/* Frequency signal has been found */
				signalPosition = nextLine + 61 + 1; 
			}
		}
		i++;
		
	} 
	
	/* Check if Signal is found */
	if(signalPosition != 0){
	
		/* Signal must be found so decode the message*/
		for(j = signalPosition; j < len; j++){
			ch = rawData[j];
			
			/* Check for spaces */		
			if(rawData[j] == ' ' && rawData[j + 1] != ' '){ 
				signal[k] = ch;
				k++;
			}
			/* Check for '>>' characters */
			else if(rawData[j] == '>' && rawData[j+1] == '>'){
				ch = rawData[j + 2];
				signal[k]= ch + frequency;
				j = j + 2;
				k++;
			}
			/* Check for '<<' characters */	
			else if(rawData[j] == '<' && rawData[j + 1] == '<'){
				ch = rawData[j + 2];
				signal[k]= ch - frequency;
				j = j + 2;
				k++;
			}
			/* Check for NUL, NAK, and ETX for NON-SEQUITOR */
			else if(j + 2 < len - 1 && rawData[j] == 'N' && rawData[j + 1] == 'U' && rawData[j + 2] == 'L'){
				strcpy(signal, "NON-SEQUITOR");
				return -1;
			}
			else if(j + 2 < len - 1 && rawData[j] == 'N' && rawData[j + 1] == 'A' && rawData[j + 2] == 'K'){
				strcpy(signal, "NON-SEQUITOR");
				return -1;
			}
			else if(j + 2 < len - 1 && rawData[j] == 'E' && rawData[j + 1] == 'T' && rawData[j + 2] == 'X'){
				strcpy(signal, "NON-SEQUITOR");
				return -1;
			}
			/* Check if rawData[j] ranges between ASCII values a and b */
			else if(ch >= a && ch <= b && ch != 32){
				signal[k] = ch;
				k++;
			}
			signal[k + 1] = '\0';
		}
	}
	/* No Signal */
	else{
		strcpy(signal, "NON-SEQUITOR");
		return -1;
	}

	/* Return the length of the message */
	return strlen(signal);
}