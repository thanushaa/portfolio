<?php 
     /*
     Name: Thanushaa Thaninayagam (tthaninayagam)
     Purpose: The top file includes the name and logo that
                appears on every PHP page.
     */
     
     session_start();
?>

     <div class="body">
          <h1>Programming with PHP</h1>
     </div>
     
     <div class="bar">
          <a class="
                    <?php
                         if($_SERVER["PHP_SELF"] == "/~int322_132a17/assign3/tthaninayagam_a3_index.php") {
                              echo "active";
                         } else { echo "navbar";}
                    ?>" 
               href="/~int322_132a17/assign3/tthaninayagam_a3_index.php">Index</a>

     <?php 	   
          if (!isset($_SESSION['isLoggedIn'])){
     ?>	  
	  	   
               <a class="<?php
                              if($_SERVER["PHP_SELF"] == "/~int322_132a17/assign3/tthaninayagam_a3_login.php") {
                                   echo "active";
                              } else { echo "navbar";}
                         ?>" 
		    href="/~int322_132a17/assign3/tthaninayagam_a3_login.php">Login</a>
	
     <?php
		} else {
     ?>
	
			<a class="<?php
                              if($_SERVER["PHP_SELF"] == "/~int322_132a17/assign3/tthaninayagam_a3_logout.php") {
                                   echo "active";
                              } else { echo "navbar";}
                         ?>" 
				href="/~int322_132a17/assign3/tthaninayagam_a3_logout.php">Logout</a>
	
     <?php
	}
     ?>
	
		<a class="
                    <?php
                         if($_SERVER["PHP_SELF"] == "/~int322_132a17/assign3/tthaninayagam_a3_entry.php") {
                              echo "active";
					} else { echo "navbar";}
                    ?>" 
			href="/~int322_132a17/assign3/tthaninayagam_a3_entry.php">Create New Post</a>

     </div>