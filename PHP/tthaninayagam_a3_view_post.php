<?php 
     /*
     Name: Thanushaa Thaninayagam (tthaninayagam)
     Purpose: An id is passed to the view post file in order to
				view the post of the file
     */
?>

<?php
     // including header, top, database access
     include('tthaninayagam_a3_header.php');
     include('tthaninayagam_a3_top.php');
	include('db.php');

     $id = $_GET['id'];

	viewEntry($dbh, $id);
?>

<?php
     function viewPost($title, $text, $color, $entryError) {
?>

     <div class="body"><br><br>
          <p class="highlight">View Post</p>
     <?php
          // post entry if found
          if($entryError == '') {
               $_POST['color'] = $color;
     ?>        
          <br>
          <table class="viewPost">
               <tr class="viewPost">
                    <td class="viewPost" style="font-weight:700; font-size:16px; color:<?php echo $color; ?>">
                         <?php echo $title; ?>
                    </td>
               </tr>
               <tr>
                     <td class="viewPost" style="color:grey">
                         <?php echo date('l \t\h\e jS, Y'); ?>
                    </td>
               </tr>
               <tr>
                    <td class="viewPost" style="color:grey"> </td>
               </tr>
               <tr>
                    <td class="viewPost" style="color:grey"> </td>
               </tr>
               <tr class="viewPost">
                    <td class="viewPost" style="color:<?php echo $color; ?>">
                         <?php echo nl2br($text); ?>
                    </td>
               </tr>
          </table>    
        
     <?php    
          } else {  
     ?>
    
          <p class="errorMessage"><?php echo $entryError; ?></p>
    
     <?php
          }
     ?>
          <br><br>   
          <a class="blueButton" href="tthaninayagam_a3_index.php"> < Index</a>
     </div>
<?php
     }
?>

<?php

     // including the footer
     include('tthaninayagam_a3_footer.php');
?>