/*

	Name: Thanusha
	Program: Rock Paper Scissors Lizard Spock

*/

#include <stdio.h>
#include <stdlib.h> 
#include <string.h>

void displayGestures();
void compGesture(int);	
void determineWinner(int, int, int, int, int);
void displayStats(int, int, int, int);


void displayGestures() {

	// display the possible gestures
	printf("1) Rock\n");
	printf("2) Paper\n");
	printf("3) Scissors\n");
	printf("4) Lizard\n");
	printf("5) Spock\n");

}

void compGesture(int gestureNum) {

	//char gesture[8] = "\0";

/*
	switch (gestureNum) {
		case 1: 
			strcpy(gesture, "Rock");
			break;
		case 2:
			strcpy(gesture, "Paper");
			break;
		case 3:
			strcpy(gesture, "Scissors");
			break;
		case 4:
			strcpy(gesture, "Lizard");
			break;
		case 5:
			strcpy(gesture, "Spock");
			break;
	}
*/

	if (gestureNum == 1) {
		printf("Computer player chose: Rock \n");
		// strcpy(gesture, "Rock");
	} else if (gestureNum == 2) {
		printf("Computer player chose: Paper \n");
		// strcpy(gesture, "Paper");
	} else if (gestureNum == 3) {
		printf("Computer player chose: Scissors \n");
		// strcpy(gesture, "Scissors");
	} else if (gestureNum == 4) {
		printf("Computer player chose: Lizard \n");
		// strcpy(gesture, "Lizard");
	} else if (gestureNum == 5) {
		printf("Computer player chose: Spock \n");
		// strcpy(gesture, "Spock");
	}

	//printf("Computer player chose: %s \n", gesture);

}

void determineWinner(int playerOne, int comp, int numOfPlayerWon, int numOfCompWon, int numOfTies) {

	char compWon[] = "Computer player won!\n";
	char playerWon[] = "Player 1 won!\n";
	char tie[] = "Tie Game!\n";

/*
	switch(playerOne) {
		case 1: // rock
			switch(comp) {
				case 1:
					printf("%c", tie);
					numOfTies++;
					break;
				case 2:
					printf("%c", compWon);
					numOfCompWon++;
					break;
				case 3:
					printf("%c", playerWon);
					numOfPlayerWon++;
					break;
				case 4:
					printf("%c", playerWon);
					numOfPlayerWon++;
					break;
				case 5:
					printf("%c", compWon);
					numOfCompWon++;
					break;
			}
			break;

		case 2: // paper
			switch(comp) {
				case 1:
					printf("%c", compWon);
					numOfCompWon++;
					break;
				case 2:
					printf("%c", tie);
					numOfTies++;
					break;
				case 3:
					printf("%c", compWon);
					numOfCompWon++;
					break;
				case 4:
					printf("%c", compWon);
					numOfCompWon++;
					break;
				case 5:
					printf("%c", playerWon);
					numOfPlayerWon++;
					break;
			}
			break;

		case 3: // scissors
			switch(comp) {
				case 1: // rock
					printf("%c", compWon);
					numOfCompWon++;
					break;
				case 2: // paper
					printf("%c", playerWon);
					numOfPlayerWon++;
					break;
				case 3: // scissors
					printf("%c", tie);
					numOfTies++;
					break;
				case 4: // lizard
					printf("%c", playerWon);
					numOfPlayerWon++;
					break;
				case 5: // spock
					printf("%c", compWon);
					numOfCompWon++;
					break;
			}
			break;
		
		case 4: // lizard
			switch(comp) {
				case 1: // rock
					printf("%c", compWon);
					numOfCompWon++;
					break;
				case 2: // paper
					printf("%c", playerWon);
					numOfPlayerWon++;
					break;
				case 3: // scissors
					printf("%c", compWon);
					numOfCompWon++;
					break;
				case 4: // lizard
					printf("%c", tie);
					numOfTies++;
					break;
				case 5: // spock
					printf("%c", playerWon);
					numOfPlayerWon++;
					break;
			}
			break;
		
		case 5: // spock
			switch(comp) {
				case 1: // rock
					printf("%c", playerWon);
					numOfPlayerWon++;
					break;
				case 2: // paper
					printf("%c", compWon);
					numOfCompWon++;
					break;
				case 3: // scissors
					printf("%c", tie);
					numOfTies++;
					break;
				case 4: // lizard
					printf("%c", compWon);
					numOfCompWon++;
					break;
				case 5: // spock
					printf("%c", tie);
					numOfTies++;
					break;
			}
			break;
	}
*/

	// possibilties 
	if (playerOne == 1 && comp == 1) { // rock and rock
		printf("%s", tie);
		numOfTies++;

	} else if (playerOne == 1 && comp == 2) { // rock and paper
		printf("%s", compWon);
		numOfCompWon++;

	} else if (playerOne == 1 && comp == 3) { // rock and scissors
		printf("%s", playerWon);
		numOfPlayerWon++;

	} else if (playerOne == 1 && comp == 4) { // rock and lizard
		printf("%s", playerWon);
		numOfPlayerWon++;

	} else if (playerOne == 1 && comp == 5) { // rock and spock
		printf("%s", compWon);
		numOfCompWon++;

	} else if (playerOne == 2 && comp == 1) {
		printf("%s", compWon);
		numOfCompWon++;

	} else if (playerOne == 2 && comp == 2) {
		printf("%s", tie);
		numOfTies++;

	} else if (playerOne == 2 && comp == 3) {
		printf("%s", compWon);
		numOfCompWon++;

	} else if (playerOne == 2 && comp == 4) {
		printf("%s", compWon);
		numOfCompWon++;

	} else if (playerOne == 2 && comp == 5) {
		printf("%s", playerWon);
		numOfPlayerWon++;

	} else if (playerOne == 3 && comp == 1) {
		printf("%s", compWon);
		numOfCompWon++;

	} else if (playerOne == 3 && comp == 2) {	
		printf("%s", playerWon);
		numOfPlayerWon++;

	} else if (playerOne == 3 && comp == 3) {
		printf("%s", tie);
		numOfTies++;

	} else if (playerOne == 3 && comp == 4) {
		printf("%s", playerWon);
		numOfPlayerWon++;

	} else if (playerOne == 3 && comp == 5) {
		printf("%s", compWon);
		numOfCompWon++;

	} else if (playerOne == 4 && comp == 1) {
		printf("%s", compWon);
		numOfCompWon++;

	} else if (playerOne == 4 && comp == 2) {	
		printf("%s", playerWon);
		numOfPlayerWon++;

	} else if (playerOne == 4 && comp == 3) {
		printf("%s", compWon);
		numOfCompWon++;

	} else if (playerOne == 4 && comp == 4) {
		printf("%s", tie);
		numOfTies++;

	} else if (playerOne == 4 && comp == 5) {
		printf("%s", playerWon);
		numOfPlayerWon++;

	} else if (playerOne == 5 && comp == 1) {
		printf("%s", playerWon);
		numOfPlayerWon++;

	} else if (playerOne == 5 && comp == 2) {	
		printf("%s", compWon);
		numOfCompWon++;

	} else if (playerOne == 5 && comp == 3) {
		printf("%s", playerWon);
		numOfPlayerWon++;

	} else if (playerOne == 5 && comp == 4) {
		printf("%s", compWon);
		numOfCompWon++;

	} else if (playerOne == 5 && comp == 5) {
		printf("%s", tie);
		numOfTies++;

	}
}	


void displayStats(int numOfPlay, int numOfPlayerWon, int numOfCompWon, int numOfTies) {

	printf("\n\n================================\n");
	printf("Statistics\n");
	printf("================================\n");
	printf("Number of games played: %d", numOfPlay);
	printf("Number of games won by Player 1: %d", numOfPlayerWon);
	printf("Number of games won by the computer: %d", numOfCompWon);	
	printf("Number of games Tied: %d", numOfTies);
	printf("Player 1 win Percentage: %2.2lf", numOfPlayerWon/numOfPlay);
	printf("Computer win Percentage: %2.2lf", numOfCompWon/numOfPlay);

}


main() {

	int play = 1;
	int playerOne;
	int comp;
	int numOfPlay = 0;
	int numOfPlayerWon = 0;
	int numOfCompWon = 0;
	int numOfTies = 0;

	printf("Rock Paper Scissors Lizard Spock\n");
	printf("================================\n");

	do {
		// display gestures
		displayGestures();

		printf("Player 1, enter your move (1 - 5): ");
		do {
			scanf("%d", &playerOne);
			while(getchar()!='\n');
		} while (playerOne != (1 || 2 || 3 || 4 || 5));

		// generate random gesture for the computer
		comp = rand() % 5 + 1;
		//printf("%d\n", comp);
		compGesture(comp);

		// determine winner
		determineWinner(playerOne, comp, numOfPlayerWon, numOfCompWon, numOfTies);

		printf("Do you wish to go again? (1 for Yes, 2 for No): ");
		//scanf("%d", &play);
		do {
			scanf("%d", &play);
			while(getchar()!='\n');
		} while (play != (1 || 2));
		
		numOfPlay++;


	} while (play == 1);

	displayStats(numOfPlay, numOfPlayerWon, numOfCompWon, numOfTies);

}