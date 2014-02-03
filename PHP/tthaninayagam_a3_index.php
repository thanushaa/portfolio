<?php 
     /*
     Name: Thanushaa Thaninayagam (tthaninayagam)
     Purpose: The index page displays the last 10 entries
				and be able to view the entries.
     */
?>

<?php
     // including header, top, database access
     include('tthaninayagam_a3_header.php');
     include('tthaninayagam_a3_top.php');
	include('db.php');     
?>

     <div class="body">
     <br><br>
     <p class="highlight">Last 10 Entries</p>
     <ul style="list-style-type:none;">

	<?php
		// the last ten entries of the blog
		tenEntries($dbh);
	?>	
        
     </ul>
     </div> 

<?php
    // including the footer
    include('tthaninayagam_a3_footer.php');
?>