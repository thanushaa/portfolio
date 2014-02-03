/* Student Assignment Submission Form
==================================
I declare that the attached assignment is wholly my own work in accordance with
Seneca Academic Policy. No part of this assignment has been copied manually or
electronically from any other source (including web sites) or distributed to other students.
My name is : Thanusha Thaninayagam */


#include <stdio.h>


/* Function for User Input of Employee No, and calculates the Gross Pay of Salary Paid or Hourly Rate and Hours Worked */
double weeklypay_input(int *employee_no, char *paid_ans, double *salary_paid, double *hourly_rate, double *hrs_worked);

/* Function for calculating the Long Term Benefits (LTB) */
int    longterm_benefit(double gross_pay);

/* Function for calculating the Employment Insurance (EI) */
double employment_insurance(double gross_pay);

/* Function for calculating the Canada Pension Plan (CPP) */
double canada_pension_plan(double gross_pay);

/* Function for calculating the Federal and Provincial Taxes (FT & PT) */
double federaland_provincialtax(char paid_ans, double gross_pay);

/* Function for displaying the Pay Stub of the Weekly Pay */
void weeklypay_output(int employee_no, int weekly_date, char paid_ans, double salary_paid, double hourly_rate, double hrs_worked, double gross_pay, double ltb, double ei, double cpp, double taxes);

/* Function for calculating another employee's Weekly Pay */
char   another_employee(char *weeklyinput_ans);


main() {

	int    employee_no, weekly_date;
	double salary_paid = 0, hourly_rate = 0, hrs_worked = 0, gross_pay = 0, ltb = 0, ei = 0, cpp = 0, taxes = 0;
	char   weeklyinput_ans, paid_ans;


	printf("Welcome to Thanusha Thaninayagam's Payroll Systems\n\n");

	/* Decision for User Input of the Weekly Pay */
	printf("Would you like to input the Weekly Pay? (Y/N): ");
	scanf("%c", &weeklyinput_ans);


	/* The While-Loop continues to calculate an Employee's Weekly Pay while user inputs YES ('Y' or 'y') */
	do {

		/* User Input of the Weekly Ending Date */
		printf("What is the weekly ending date? (YYYYMMDD): ");
		while(getchar()!='\n');
		scanf("%d", &weekly_date);

		/* The User Input of Employee No and the Calculation for Gross Pay of the Salary Paid or Hourly Rate and Hours Worked*/
		gross_pay = weeklypay_input(&employee_no, &paid_ans, &salary_paid, &hourly_rate, &hrs_worked);

		/* Calculation of the Long Term Benefits (LTB) */
		ltb = longterm_benefit(gross_pay);

		/* Calculation of the Employment Insurance (EI) */
		ei = employment_insurance(gross_pay);

		/* Calculation of the Canada Pension Plan (CPP) */
		cpp = canada_pension_plan(gross_pay);

		/* Calculation of the Federal and Provincial Taxes (FT & PT) */
		taxes = federaland_provincialtax(paid_ans, gross_pay);

		/* Displays the Pay Stub of the Weekly Pay */
		weeklypay_output(employee_no, weekly_date, paid_ans, salary_paid, hourly_rate, hrs_worked, gross_pay, ltb, ei, cpp, taxes);

		/* Decision for Inputting Another Employee's Weekly Pay */
		another_employee(&weeklyinput_ans);

	} while (weeklyinput_ans == 'Y' || weeklyinput_ans == 'y');

}


double weeklypay_input(int *employee_no, char *paid_ans, double *salary_paid, double *hourly_rate, double *hrs_worked) {

	double gross_pay = 0;


	/* User Input of Employee's Number*/
	printf("What is the employee's number? : ");
	scanf("%d", employee_no);


	/* The While-Loop continues until given an input of either Salary ('S' or 's') or Hourly Paid ('H' or 'h') */
	do {

		/* User Input of Employee being paid: Salary or Hourly Rate */
		printf("Is the employee paid salary or hourly rate? (S for Salary or H for Hourly Rate): ");
		while(getchar()!='\n');
		scanf("%c", paid_ans);

	} while (*paid_ans != 's' && *paid_ans != 'S' && *paid_ans != 'h' && *paid_ans != 'H');


	/* If the user inputted Salary Paid ('S' or 's') then calculate the Gross Pay from the Salary Paid */
	if (*paid_ans == 's' || *paid_ans == 'S') {

		/* User Input of the Salary Paid */
		printf("What is the salary paid? : ");
		while(getchar()!='\n');
		scanf("%lf", salary_paid);

		/* Calculation of the Gross Pay */
		gross_pay = *salary_paid / 52;

	}

	/* Else if the user inputted Hourly Rate ('H' or 'h') then calculate the Gross Pay from the Hourly Rate and Hours Worked */
	else {

		/* User Input of Hourly Rate */
		printf("What is the hourly rate? : ");
		while(getchar()!='\n');
		scanf("%lf", hourly_rate);

		/* User Input of Hours Worked */
		printf("What is the hours worked? : ");
		while(getchar()!='\n');
		scanf("%lf", hrs_worked);

		/* Calculate the Gross Pay for either Salary or Hourly Rate and Hours Worked */
		if (*hrs_worked > 44) { gross_pay = ((*hrs_worked - 44) * (1.5 * *hourly_rate)) + (*hourly_rate * 44); }
		else { gross_pay = (*hrs_worked * *hourly_rate); }

	}

	return gross_pay;

}


int longterm_benefit(double gross_pay) {

	int count = 0;


	/* Calculating how many full 100's in the Gross Pay */
	count = (gross_pay / 100);

	/* If there more than 50 full 100's in the Gross Pay than set count to exactly 50 */
	if (count >= 50) { count = 50; }

	/* Return Calculation of Long Term Benefit (LTB) */
	return ("%.0d", count * 2);

}


double employment_insurance(double gross_pay) {

	double ei = 0;


	/* Calculation of Employment Insurance (EI), 1.4% of the Gross Pay and the maximum of EI is 11.80 */
	ei = gross_pay * 0.014;

	/* If EI exceeds than set it to the maximum */
	if (ei >= 11.80) { ei = 11.80; }

	return ei;

}


double canada_pension_plan(double gross_pay) {

	double cpp = 0;


	/* Calculate 1.6% of the first 700 earned */
	if (gross_pay <= 700) { cpp = gross_pay * 0.016; }
	else { cpp = 700 * 0.016; }

	return cpp;

}


double federaland_provincialtax(char paid_ans, double gross_pay) {

	double annual_pay = 0, federal_tax = 0;
	int    count = 1;


	/* Calculate the Annual Pay if the Employee's Pay is Hourly else */
	if (paid_ans == 'h' || paid_ans == 'H') { annual_pay = gross_pay * 52; }
	/* Calculate the Annual Pay if the Employee's Pay is Salary */
	else { annual_pay = gross_pay * 52; }


	/* The While-Loop continues if the Annual Pay is greater than or equal to 20,000 and the counter less than 3 */
	do {

		/* Calculation of 16% on the first 20,000 earned Annually */
		if (count == 1) {

			annual_pay -= 20000;
			federal_tax += 0.16 * 20000;

		}

		/* Calculation of 23% on the next 20,000 earned Annually*/
		else if (count == 2) {

			annual_pay -= 20000;
			federal_tax += 0.23 * 20000;

		}

		count++;

	} while (annual_pay >= 20000 && count < 3);

	/* Calculation of 23% if the Annual Pay is greater than 0 and less than 20,000 */
	if (annual_pay > 0 && annual_pay < 20000) { federal_tax += 0.23 * annual_pay; }

	/* Calculation of 29% the remainder earned Annually if Annual Pay is still greater than 20,000 */
	if (annual_pay >= 20000) { federal_tax += 0.29 * annual_pay; }

	/* Calculating the Provincial Tax */
	federal_tax += federal_tax * 0.47;

	return federal_tax / 52 ;

}


void weeklypay_output(int employee_no, int weekly_date, char paid_ans, double salary_paid, double hourly_rate, double hrs_worked, double gross_pay, double ltb, double ei, double cpp, double taxes) {

	double total_deduct = 0, net_pay = 0;

	/* The Weekly Pay Stub of an Employee */
	printf("\n\n\n\n\n\n_________________________________________________________________________");

	printf("\n\n\nThanusha Thaninayagam's Payroll Systems\n");
	printf("102 Orfus Road, Downsview ON\n\n");

	printf("Employee Number: %d         For Week Ending: %d\n\n", employee_no, weekly_date);

	/* Print appropriate line of Employee being paid: Salary or Hourly Rate & Hours Worked */
	if (paid_ans == 's' || paid_ans == 'S') { printf("Salary Paid: %.2lf\n\n", salary_paid); }
	else { printf("Hourly Rate:     %.2lf       Hours Worked:   %.2lf\n\n", hourly_rate, hrs_worked); }

	printf("GROSS PAY:                                %8.2lf\n\n", gross_pay);

	printf("DEDUCTIONS:\n");
	printf("Long Term Benefits:                       %8.2lf\n", ltb);
	printf("Employment Insurance:                     %8.2lf\n", ei);
	printf("Canada Pension Plan:                      %8.2lf\n", cpp);
	printf("Federal Tax:                              %8.2lf\n\n", taxes);

	/* Calculation of the Total Deductions */
	total_deduct = ltb + ei + cpp + taxes;
	printf("TOTAL DEDUCTIONS:                         %8.2lf\n\n", total_deduct);

	/* Calculation of the Net Pay*/
	net_pay = gross_pay - total_deduct;
	printf("NET PAY:                                  %8.2lf\n\n", net_pay);

	printf("_________________________________________________________________________\n\n\n");


}


char another_employee(char *weeklyinput_ans) {

	/* User Input for decision of another Employee's Weekly Pay */
	printf("Would you like to input another employee's Weekly Pay? (Y/N): ");
	while(getchar()!='\n');
	scanf("%c", weeklyinput_ans);

	return *weeklyinput_ans;

}
