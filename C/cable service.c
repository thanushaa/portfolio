#include<stdio.h>

main() {
	double total = 0, discount, tax, internet_pkg, telephone_pkg, television_pkg, payperview_pkg;
	int    count = 0, service1_ans, service2_ans, service3_ans, ppv4_ans;
	char   ans1, ans2, ans3, ppv_ans;
	
	/* Student Assignment Submission Form 
	================================== 
	I declare that the attached assignment is wholly my own work in accordance with 
	Seneca Academic Policy. No part of this assignment has been copied manually or 
	electronically from any other source (including web sites) or distributed to other students.
	My name is : Thanusha Thaninayagam */

	
	printf("\n\n\nWelcome to XYZ Cable Providers\n\n");

	/* Service 1 - Internet */

	printf("Would you like to subcribe to Internet? (Y or N): ");
	scanf("%c", &ans1);

	/* If the input is 'Y' then add to count, ask for another user input.. */
	/* .. and assuming the input is valid, check for package chosen */

	if (ans1 == 'Y') {

		count = count + 1;

		printf("Choose package 1, 2 or 3: ");
		scanf("%d", &service1_ans);
		
		/* Assuming the input is valid, get the price for chosen package */

		if (service1_ans == 1) { internet_pkg = 15.99; }
		else if (service1_ans == 2) { internet_pkg = 21.99; }
		else { internet_pkg = 25.99; }
		
		/* Add the package amount to the total amount */
		
		total = total + internet_pkg;
		
	}


	/* Service 2 - Telephone */

	printf("\nWould you like to subscribe to Home Telephone? (Y or N): ");
	while(getchar()!='\n');
	scanf("%c", &ans2);

	/* If the input is 'Y' then add to count, ask for another user input.. */
	/* .. and assuming the input is valid, check for package chosen */

	if (ans2 == 'Y') {

		count = count + 1;

		printf("Choose package 1, 2 or 3: ");
		scanf("%d", &service2_ans);
		
		/* Assuming the input is valid, get the price for chosen package */
		
		if (service2_ans == 1) { telephone_pkg = 14.99; }
		else if (service2_ans == 2) { telephone_pkg = 24.99; }
		else { telephone_pkg = 35.99; }
		
		/* Add the package amount to the total amount */
		
		total = total + telephone_pkg;
		
	}


	/* Service 3 - Television */

	printf("\nWould you like to subscribe to Television? (Y or N): ");
	while(getchar()!='\n');
	scanf("%c", &ans3);
	
	/* If the input is 'Y' then add to count, ask for another user input.. */
	/* .. and assuming the input is valid, check for package chosen */

	if (ans3 == 'Y') {

		count = count + 1;

		printf("Choose package 1 or 2: ");
		scanf("%d", &service3_ans);
		
		/* Assuming the input is valid, get the price for chosen package */
		
		if (service3_ans == 1) { television_pkg = 14.99; }
		else { television_pkg = 24.99; }

		/* Add the package amount to the total amount */
		total = total + television_pkg;
		
		/* Extra Usage for Television - Pay Per View */

		printf("\nWould you like to subscribe to Pay Per View? (Y or N): ");
		while(getchar()!='\n');
		scanf("%c", &ppv_ans);

		if (ppv_ans == 'Y') {

			printf("Choose package 1 or 2: ");
			scanf("%d", &ppv4_ans);
			
			/* Assuming the input is valid, get the price for chosen package */
			
			if (ppv4_ans == 1) { payperview_pkg = 3.99; }
			else { payperview_pkg = 5.99; }
			
			/* Add the package amount to the total amount */
			
			total = total + payperview_pkg;
			
		}
		
	}

	
	/* Bill Details */

	printf("\n\nXYZ Cable Providers");
	printf("\nService\t\t\tPackage\t\t\tCost");
	
	/* If the Services were chosen, list the package and price */
	
	if (ans1 == 'Y') { printf("\nInternet\t\t%d\t\t\t$%2.2lf", service1_ans, internet_pkg); }
	if (ans2 == 'Y') { printf("\nTelephone\t\t%d\t\t\t$%2.2lf", service2_ans, telephone_pkg); }
	if (ans3 == 'Y') { printf("\nTelevision\t\t%d\t\t\t$%2.2lf", service3_ans, television_pkg); }
	if (ppv_ans == 'Y') { printf("\nExtra (Pay Per View)\t%d\t\t\t$%8.2lf", ppv4_ans, payperview_pkg); }

	printf("\n\nSubtotal\t\t\t\t\t$%8.2lf", total);
	
	/* If more than 1 Services are chosen, apply discount.. */
	/* .. else, do not apply the discount */
	
	if (count > 1) {
		discount = total * 0.05;
		total = total - discount;
		printf("\nBundle Discount\t\t%5\t\t\t$%8.2lf", discount); }
	else { printf("\nBundle Discount\t\t%0\t\t\t$ 0.00"); }

	printf("\nTotal Before Tax\t\t\t\t$%2.2lf", total);
	
	/* Apply the tax */
	
	tax = total * 0.13;
	printf("\nHST\t\t\t%13\t\t\t$%3.2lf", tax);
	total = total + tax;
	
	/* Total amount */

	printf("\n\nAmount Due\t\t\t\t\t$%2.2lf\n\n\n\n", total);
}
