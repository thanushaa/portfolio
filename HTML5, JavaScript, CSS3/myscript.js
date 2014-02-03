 /*************************************************************/
 /* Name : Thanusha Thaninayagam                              */
 /*                                                           */
 /*************************************************************/


 /*************************************************************/
 /* FormValidation Function Description :                     */
 /*                                                           */
 /* validates all functions, changes the first letter of      */
 /* client surname to a captial, enables the price field,     */
 /* and change value of field13 to 'Y'                        */
 /*************************************************************/
 
    function FormValidation() {
		
		// check if each function has an error, return false
		if (!field01Validation()){
			return false;}
		if (!field02Validation()){
			return false;}
		if (!field03Validation()){
			return false;}
		if (!field02AndField03()){
			return false;}
		if (!field04Validation()){
			return false;}
		if (!field05Validation()){
			return false;}
		if (!field09Validation()){
			return false;}
		if (!field10Validation()){
			return false;}
			
		// no Errors then..
		var input01Value = document.pizza.field01.value;
		document.pizza.field01.value = input01Value.substr(0,1).toUpperCase() + input01Value.substr(1,input01Value.length-1).toLowerCase();
			
		document.pizza.field13.value = 'Y';
		
		document.pizza.field07.disabled = false;
		
		return true;
		} 
	
	
	function field01Validation() {

        var alphString = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
		var countAlpha = 0;
		var countApostrophe = 0;
		var countHyphen = 0;

        var inputValue = document.pizza.field01.value;

		// check if its empty
        if (inputValue.length < 1)
        {
		   alert("Client Surname : Please re-enter a name (at least 1 alphabetic character).");
		   document.pizza.field01.focus();
		   return false;
        }
        else
	    {
			for (var i = 0; i < inputValue.length; i++)
			{
				var passAlpha = false;
				// check if the character is a letter
				if (alphString.indexOf(inputValue.substr(i,1))!= -1)
				{
					countAlpha++
				}
				// check if the character is a hypen
				else if (inputValue.substr(i,1) == "-")
				{
					countHyphen++;
				}
				// check if the character is a apostrophe
				else if (inputValue.substr(i,1) == "'")
				{
					countApostrohpe++;
				}
					
			}  // for
        } // else

		// check for errors
		if (countAlpha < 1)
		{
			alert("Client Surname : Please re-enter a name with at least one Alphabet letter.");
			document.pizza.field01.focus();
			return false;
		}	
		else if (countHyphen > 1)
        {
		    alert("Client Surname : Only one Hyphen allowed.");
		    document.pizza.field01.focus();
		    return false;
		}
		else if (countApostrophe > 1)
		{
			alert("Client Surname : Only one Apostrophe allowed.");
		    document.pizza.field01.focus();
		    return false;
		}
          
		return true; 
    }  // function for field01

	
    function field02Validation() {

	    var inputValue = document.pizza.field02.value;
		var capitalStr = "TG";
		
		// check if the input is less than 12 characters
		if (inputValue.length < 12)
		{
			alert("Client Number : Must have a length of 12.");
		    document.pizza.field02.focus();
		    return false;
		}
		// check if the first letter is either a T or G
		else if (capitalStr.indexOf(inputValue[0]) == -1)
		{
			alert("Client Number : Letter should be a captial T or G.");
		    document.pizza.field02.focus();
		    return false;
		}
		// check if theres a hyphen in postion 7
		else if (inputValue.substr(6,1) != '-')
		{
			alert("Client Number : There must be Hyphen in the 7th postion.");
		    document.pizza.field02.focus();
		    return false;
		}
		// check if positions 2-6 are numeric
		else if (parseInt(inputValue.substr(1,5)) != inputValue.substr(1,5))
		{
			alert("Client Number : Positions 2-6 must be Numeric.");
		    document.pizza.field02.focus();
		    return false;
		}
		// check if positions 8-12 are numeric
		else if (parseInt(inputValue.substr(7,5)) != inputValue.substr(7,5))
		{
			alert("Client Number : Positions 8-12 must be Numeric.");
		    document.pizza.field02.focus();
		    return false;
		}
		
		return true;
    }  // function for field02
	
	
    function field03Validation() {

	    var inputValue = document.pizza.field03.value;

		// check if its less than 12 characters
		if (inputValue.length < 12)
		{
			alert("Telephone : Must be a length of 12(nnn-nnn-nnnn).");
		    document.pizza.field03.focus();
		    return false;
		}
		// check if area code is numeric
		else if (parseInt(inputValue.substr(0,3)) != inputValue.substr(0,3))
		{
			alert("Telephone : Positions 1-3 must be Numeric.");
		    document.pizza.field03.focus();
		    return false;
		}
		// check if the area code is not all zero's
		else if (inputValue.substr(0,3) == '000')
		{
			alert("Telephone : Positions 1-3 cannot be 000.");
		    document.pizza.field03.focus();
		    return false;
		}
		// check if there is a hyphen after area code
		else if (inputValue.substr(3,1) != '-')
		{
			alert("Telephone : There must be Hyphen in the 4th postion.");
		    document.pizza.field03.focus();
		    return false;
		}
		// check if positions 5-7 are numeric
		else if (parseInt(inputValue.substr(4,3)) != inputValue.substr(4,3))
		{
			alert("Telephone : Positions 5-7 must be Numeric.");
		    document.pizza.field03.focus();
		    return false;
		}
		// check if there is a hyphen in position 7
		else if (inputValue.substr(7,1) != '-')
		{
			alert("Telephone : There must be Hyphen in the 8th postion.");
		    document.pizza.field03.focus();
		    return false;
		}
		// check if positions 9-12 are numeric
		else if (parseInt(inputValue.substr(8,4)) != inputValue.substr(8,4))
		{
			alert("Telephone : Positions 9-12 must be Numeric.");
		    document.pizza.field03.focus();
		    return false;
		}
		// check if the phone number is not all zero's
		else if (inputValue.substr(4,8) == '000-0000')
		{
			alert("Telephone : Positions 5-12 cannot be 000-0000.");
		    document.pizza.field03.focus();
		    return false;
		}
		
		return true;
    }  // function for field03


	function field02AndField03(){
		
		var input02Value = document.pizza.field02.value;
		var input03Value = document.pizza.field03.value;
		
		// check if 'T' and '416' match
		if (input02Value.substr(0,1) == 'T')
		{
			if (input03Value.substr(0,3) != '416')
			{
				alert("Client Number & Telephone : Does not match.");
				document.pizza.field03.focus();
				return false;
			}
			return true;
		}
		// check if 'G' and '905' match
		else if (input02Value.substr(0,1) == 'G')
		{
			if (input03Value.substr(0,3) != '905')
			{
				alert("Client Number & Telephone : Does not match.");
				document.pizza.field03.focus();
				return false;
			}
			return true;
		}
			
		return true;
	} // function for field02 and field03 relationship
	
	
    function field04Validation() {

	    var inputValue = document.pizza.field04.value;
		var monthStr = "jan feb mar apr may jun jul aug sep oct nov dec";
		var monthValue = inputValue.substr(0,3).toLowerCase();
		var yearValue = inputValue.substr(3,4);
		
		// check if it less than 7 characters
		if (inputValue.length < 7)
		{
			alert("Date of Birth : Must be a length of 7(mmmyyyy).");
		    document.pizza.field04.focus();
		    return false;
		}
		// check if the month exists
		else if (monthStr.indexOf(monthValue) == -1)
		{
			alert("Date of Birth : Month must be a three letter abbreviation for month(mmm)");
		    document.pizza.field04.focus();
		    return false;
		}
		// check if year is numeric
		else if (parseInt(inputValue.substr(3,4)) != inputValue.substr(3,4))
		{
			alert("Date of Birth : Year should be numeric.");
		    document.pizza.field04.focus();
		    return false;
		}
		// check if younger than 19
		else if ((2012 - yearValue) < 19)
		{
			alert("You should be older than 19 years of age.");
		    document.pizza.field04.focus();
		    return false;
		}
		return true;
    }  // function for field04
	

    function field05Validation() {
		
		// check if pizza size has been selected
		if (document.pizza.field05.selectedIndex == -1)
		{
			alert("Pizza Size : A selection is required.\n");
			document.pizza.field05.focus();
			return false;
		} // if
		
		// No Error, calculate the prize of pizza
		calculatePrice();
		return true;
	}  // function for field05V

	
	function calculatePrice(){	
		
		var selected = document.pizza.field05.selectedIndex;
		var pizzaPrices = new Array('11.55','15.25','22.00','25.00');
		var selectedValue = document.pizza.field05.options[selected].value;

		// calculate the price if a certain size is selected
		if (selectedValue = 'small')
		{
			var total = pizzaPrices[0]*1.13;
			total = total.toFixed(2);
			document.pizza.field07.value = total;
		}
		else if (selectedValue = 'medium')
		{
			var total = pizzaPrices[1]*1.13;
			total = total.toFixed(2);
			document.pizza.field07.value = total;
		}
		else if (selectedValue = 'large')
		{
			var total = pizzaPrices[2]*1.13;
			total = total.toFixed(2);
			document.pizza.field07.value = total;
		}
		else if (selectedValue = 'xLarge')
		{
			var total = pizzaPrices[3]*1.13;
			total = total.toFixed(2);
			document.pizza.field07.value = total;
		}
           return true;
    }  // function for calculatePrice

	
    function field09Validation() {

		var specialtyArea = 0;
		var max = document.pizza.field09.length;

		// check if anything has been checked
		for (var i = 0; i < max; i++) {
			if (document.pizza.field09[i].checked == true) {
				specialtyArea++;
			}
		}
		
		if (specialtyArea == 0) {
			alert("Sauce : A selection is required.\n");
			return false;
		}
		
		return true;
	}  // function for field09
	

    function field10Validation() {

		var specialtyArea = 0;

		// check if anything has been checked
		for (var i = 0; i < document.pizza.field10.length; i++) 
		{
			if (document.pizza.field10[i].checked == true) 
			{
				specialtyArea++;
			}
		}
		
		// check if the nothing has been checked
		if (specialtyArea == 0)
		{
			alert("Toppings : A selection is required.\n");
			return false;
		}
		// check if more than 1 has been checked
		else if (specialtyArea > 1)
		{	
			alert("Toppings : Only one topping can be checked.\n");
			return false;
		}
		return true;
	}  // function for field10
	
	