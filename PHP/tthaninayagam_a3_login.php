<?php
     /*
     Name: Thanushaa Thaninayagam (tthaninayagam)
     Purpose: Allows user to login.

     */


     // including header and top
     include('tthaninayagam_a3_header.php');
     include('tthaninayagam_a3_top.php');
     include('db.php');
     
     if($_SERVER['REQUEST_METHOD'] == 'POST'){
          $user = $_POST['username'];
          
          $account = searchUser($dbh, $user);
          
          require_once "PasswordHash.php";
          $password = create_hash($account['password']);
          if (strlen($_POST['username']) == 0 || strlen($_POST['password']) == 0) {
               $userError = "Username or Password Empty";
               loginForm($userError);
          } elseif(($_POST['username'] == $account['username']) && validate_password($_POST['password'], $password)){
               $_SESSION['isLoggedIn'] = 1;
               header('Location: tthaninayagam_a3_index.php');
          } else {
               $userError = "Username or Password Invalid";
               loginForm($userError); 
          }
          
     } elseif($_SERVER['REQUEST_METHOD'] == 'GET') {
          $userError = 0;
          loginForm($userError);
     }
?>

<?php
     // Login Form
     function loginForm($userError) {

          if(!isset($_SESSION['isLoggedIn'])) {
?>
          
               <div class="body">
               <form method="post">
                    <p>You're NOT logged in! Would you like to login?<br><br>
                    Temp Username: int322<br>
                    Temp Password: abcd<br><br>
                    
                    <div>
                         <label><p class="highlight">Username: </p>
                         <input type="text" name="username"><br>
                    </div>
                    
                    
                    <div>
                         <label><p class="highlight">Password: </p>
                         <input type="password" name="password"><br>
                         
                         <p class = "errorMessage">
                         <?php
                              // User Error Message
                              if ($userError) { echo $userError; }
                         ?></p>                         
                    </div>
                    <br><br>
                    <div><input class="blueButton" type="submit" name="login" value="login"></div>
               </form>
               </div>
          
<?php
          } else {
               header('Location: tthaninayagam_a3_logout.php');
          }
     }
?>