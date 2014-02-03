<?php
     /*
     Name: Thanushaa Thaninayagam (tthaninayagam)
     Purpose: Allows user to logout.
     */


	// including header and top
     include('tthaninayagam_a3_header.php');
     include('tthaninayagam_a3_top.php');

	if ($_SERVER["REQUEST_METHOD"] == "POST"){
		// destory the session and redirect to login page
		session_destroy();
		header('Location: tthaninayagam_a3_login.php');        
	} elseif ($_SERVER["REQUEST_METHOD"] == "GET") {
		if (!isset($_SESSION['isLoggedIn'])){
			header('Location: tthaninayagam_a3_index.php');  
		} else {
?>

			<div class="body">
				<br><br>
				<p>You're currently logged in. Would you like to logout?</p>
				<br>
				<form method="POST">
					<input class="blueButton" type="submit" name="logout" value="logout">
				</form>
			
			</div>

<?php			
		}
	} // end of elseif
?>