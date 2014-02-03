<?php
     /*
     Name: Thanushaa Thaninayagam (tthaninayagam)
     Purpose: Access to the database
     */

     // connecting to the database
     require "database.config.php";
     $dbh = new PDO("mysql:host=" . $database_config_host . ";dbname=" . $database_config_database,
                    $database_config_username,
                    $database_config_password);
     
     
     function searchUser($dbh, $user) {
          
          // search for username in the database
          $loginQuery = $dbh->prepare("select * from user where username like ?");
          $loginQuery->execute(array($user));
          $account = $loginQuery->fetch(PDO::FETCH_ASSOC); 
          
          return $account;
     }
     
     
     function searchEntry($dbh, $id) {

          // search id in the database
          $entryQuery = $dbh->prepare("select * from BlogPost where id = ?");
          $entryQuery->execute(array($id));
          $foundEntry = $entryQuery->fetch(PDO::FETCH_ASSOC);
          
          return $foundEntry;
          
     }
     
     
     function viewEntry($dbh, $id) {
          
          // search id in the database in order to view the post
          $entryQuery = $dbh->prepare("select title, text, color from BlogPost where id = ?");
          $entryQuery->execute(array($id));
          $found = $entryQuery->rowCount();
          
          if ($found == 1) {
               $entry = $entryQuery->fetch();
             
               // detect the color
               if ($entry['color'] == 1) {
                    $color = 'red';
               } elseif ($entry['color'] == 2) {
                    $color = 'blue';
               } else {$color = 'yellow';}
     
               $text = $entry['text'];
               $title = $entry['title'];
     
               // view the entry
               viewPost($title, $text, $color, $entryError = '');     
          } else {
               $entryError = 'Sorry, could not find that post';
               viewPost($title = '', $text = '', $color = '', $entryError);
          }
          
     }
     
     
     function updateEntry($dbh, $id, $sessTitle, $sessEntry, $color) {

          // update blogpost in the database
          $updateQuery = $dbh->prepare("update BlogPost
                                        set title = ?, text = ?, color = ?
                                        where id = ?");
          $updateQuery->execute(array($sessTitle, $sessEntry, $color, $id));

     }
     
     
     function addEntry($dbh, $sessTitle, $sessEntry, $color) {
          
          // insert entry in the database
          $insertQuery = $dbh->prepare("insert into BlogPost (`title`,`text`,`color`)
                                        values(?, ?, ?)");
          $insertQuery->execute(array($sessTitle, $sessEntry, $color));
          $id = $dbh->lastInsertId();
          
          return $id;

     }    

     
     function tenEntries($dbh) {
          
          // selecting the 10 recent entries
          $entryQuery = $dbh->prepare("select * from BlogPost order by id desc limit 10");
          $entryQuery->execute();
          
          try {
               foreach ($entryQuery->fetchAll(PDO::FETCH_ASSOC) as $row) {
                    $id = $row['id'];

                    // detect the color
                    if ($row['color'] == 1) {
                        $color = 'red';
                    } elseif ($row['color'] == 2) {
                        $color = 'blue';
                    } else { $color = 'yellow';}
?>

                    <li style="color:<?php echo $color; ?>">
                         <p style="margin:1px;font-weight: 700;"><?php echo $row["title"] ?>: </p>
                         <ul style="list-style: none;"><li>
                         
                         <?php
                              // display only 100 words of each entry
                              if (strlen($row['text']) > 101) {
                                   echo substr(nl2br($row['text']), 0, 103);
                              } else { echo nl2br($row['text']);}
                         ?>
                         
                         </li></ul><br>
                         
                    <?php
                         if (isset($_SESSION['isLoggedIn'])){
                    ?>
                     
                         <a class="blueButton" href="<?php echo "tthaninayagam_a3_entry.php?id=".$id ?>"> < Edit Post</a><br><br>
                     
                    <?php		
                         }
                    ?>
                     
                    <a class="blueButton" href="<?php echo "tthaninayagam_a3_view_post.php?id=".$id ?>"> < View Full Post</a>
                    <br><br><br>	
                    </li><br>
                    
     <?php
               } // end of foreach 
          } // end of try
          catch (PDOException $e) {
     ?>
     
               <li><?php print_r($e)?></li>

<?php
          } // end of catch
     
     }
?>