/* 

	Assignment Number: 3
	Student Name: Thanusha Thaninayagam

	Student Oath: This assignment represents my 
	own work in accordance with Seneca Academic Policy

	Signature: Thanusha Thaninayagam
	
	Purpose: Design and code a class called 'SetiWriter',
	to write data to a file.
	
*/

#include "seti.h"

class SetiWriter{
	private:
		FILE * setiFile;
		char fileName[21];
		char accessMode[3];
		
	public:
		SetiWriter( );
		SetiWriter(char [ ], char [ ]);
		~SetiWriter( );
		
		long write(const Seti &, bool, int);
};