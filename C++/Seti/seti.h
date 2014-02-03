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


class Seti{
	public:
		char *signal;
		char* allocateMem(int);
		int frequency, 
			a, b;
		
		Seti( ); // default constructor
		Seti(const Seti &); // copy constructor
		Seti(const char [ ], int, int, int);
		Seti(const char [ ], int, int, int, int);
		~Seti( ); // destructor
		
		int getFrequency ( ) const;
		void getRanges (int *, int *) const;
		void setRanges (int, int);
		void getMessage(char *) const;
		bool replaceChar(int, char);
		bool copyPrimes(char *) const;
		bool copyFibonacci(char *) const;
		int initCap( );	
		
		Seti operator++( ); // operator ++
		bool operator!( ) const; // operator !
		Seti operator+(const Seti &); // operator +
		void operator=(const Seti &); // operator =
		
		friend Seti join(Seti, Seti); // friend for non-member
		class SetiWriter;
};