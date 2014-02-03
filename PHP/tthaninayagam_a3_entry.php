<!--
     Name: Thanushaa Thaninayagam (tthaninayagam)
     Purpose: The entry file includes the entry form and
               the entry validation. Also includes,
               the preview post of the entry
-->

<?php error_reporting(E_ERROR|E_PARSE|E_WARNING); ?>

<?php
     session_start();
     
     // Including the header, top, database access
     $title = "Create New Post";
     include('tthaninayagam_a3_header.php');
     include('tthaninayagam_a3_top.php');
     include('db.php');
?>

<?php
     
     if (isset($_SESSION['isLoggedIn'])) {
          
          // Form Validation
          if (isset($_POST['publish'])) {
               // detect color
               if ($_SESSION['color'] == 'red') {
                    $color = 1;
               } elseif ($_SESSION['color'] == 'blue') {
                    $color = 2;     
               } else { $color = 3; }
               
               $sessTitle = htmlentities($_SESSION['etitle']);
               $sessEntry = htmlentities($_SESSION['entry']);
               
               if (isset($_GET['id'])){
                    $id = $_GET['id'];
                    
                    updateEntry($dbh, $id, $sessTitle, $sessEntry, $color);
                    
               } else {
                    $id = addEntry($dbh, $sessTitle, $sessEntry, $color);
               }
               
               unset($_SESSION['blogSession']);
               $_SESSION['id'] = $id;
               
               // redirect page to view the post
               header('Location: tthaninayagam_a3_view_post.php?id='.$id);
          } elseif (isset($_POST['edit'])) {
               // redirect to form to edit
               if (isset($_GET['id'])){
                    $id = $_GET['id'];
                    header('Location: tthaninayagam_a3_entry.php?id='.$id);
               } else {
                    header('Location: tthaninayagam_a3_entry.php');
               }
          } elseif (isset($_POST['cancel'])) {
               // delete previous data
               unset($_SESSION['blogSession']);
               header('Location: tthaninayagam_a3_entry.php');
          } elseif($_POST['form']) {
               $cColor = $_POST['color'];
     
               $_SESSION['blogSession'] = 1;
               foreach($_POST as $keyName => $value) {
                  $_SESSION[$keyName] = $value;
               }
               
               // title validation
               if(strlen($_POST['etitle']) == 0) {
                    $etitleError = '*Title should be 1-50 characters. ';
               }
               if(preg_match("/^[ ]{1,}$/", $_POST['etitle'])) {
                    $etitleError .= '*Title cannot contain only spaces. ';
               }
               if (!preg_match("/^[a-zA-Z0-9 -]{1,}$/", $_POST['etitle'])) {
                    $etitleError .= '*Title can only contain spaces, hyphens, digits and the alphabet. ';
               }
               
               // entry validation
               if (strlen($_POST['entry']) == 0) {
                  $entryError .= '*Blog entry should be 1-50 characters ';
               }
               if (!preg_match("/^[-a-zA-Z0-9'<> \r\n]{1,}$/", $_POST['entry'])) {
                  $entryError .= '*Blog entry can only contain spaces, hyphens, single quotes, <>, digits and the alphabet. ';
               }
               if (preg_match("/^[ ]{1,}$/", $_POST['entry'])) {
                  $entryError .= '*Blog entry cannot contain only spaces. ';
               }
               
               // remove leading and trailing spaces for title
               preg_replace("/^ +/", '', $_POST['entry']);
               preg_replace("/ +$/", '', $_POST['entry']);
               preg_replace("/ +/", '', $_POST['entry']);
               
               // remove leading and trailing spaces for entry
               preg_replace("/^ +/", '', $_POST['entry']);
               preg_replace("/ +$/", '', $_POST['entry']);
               preg_replace("/ +/", '', $_POST['entry']);
                         
               if (!$etitleError AND !$entryError) {
                    previewform();
               } else {
                    form($dbh, $etitleError, $entryError, $cColor);
               }
               
          } else {
               // Default color for the form
               form($dbh, $etitleError, $entryError, $cColor = 'red');
          }
     } else {
          header('Location: tthaninayagam_a3_index.php');
     }
?>


<?php
     // Form Function
     function form($dbh, $etitleError, $entryError, $cColor) {
?>
     
     <div class="body"><form method="post">
          <?php
               if (isset($_GET['id'])){
                    $id = $_GET['id'];
                    
                    $post = searchEntry($dbh, $id);
                    
                    $_POST['etitle'] = $post['title'];
                    $_POST['entry'] = $post['text'];

                    // detect the color
                    if ($post['color'] == 1) {
                        $cColor = 'red';
                    } elseif ($post['color'] == 2) {
                        $cColor = 'blue';
                    } else { $cColor = 'yellow';}
               }
          
               if ($_SESSION['blogSession'] == 1) {
                    foreach($_SESSION as $keyName => $value) {
                         $_POST[$keyName] = $value;
                    }
                    $cColor = $_POST['color'];
               }

          ?>
          <br><br>
          <div>
               
               <input type="hidden" name="id" value="<?php echo (isset($_GET['id']))?$_GET['id']:'';  ?>"
               <label><p class="highlight">Title: </p>
               <input type="text" name="etitle" maxlength="50" size="60" value="<?php echo $_POST['etitle']; ?>"></label>
               <br>
               <p class = "errorMessage">
               <?php
                    // Title Error Message
                    if ($etitleError) {
                         echo $etitleError;
                    }
               ?></p>
          </div>
          
          <div>
               <label><p class="highlight">Entry: </p>
               <textarea name="entry" rows="9" cols="65" maxlength="500"><?php echo $_POST['entry']; ?></textarea></label>
               <br>
               <p class = "errorMessage">
               <?php
                    // Entry Error Message
                    if ($entryError) {
                         echo $entryError;
                    }
               ?></p>
          </div>
          
          <div>
               <p class="highlight">Font Colour: </p>
               <div><label><input type="radio" name="color" value="red" <?php echo $cColor=='red'?'checked':'' ?>>Red</label></div>
               <div><label><input type="radio" name="color" value="blue" <?php echo $cColor=='blue'?'checked':'' ?>>Blue</label></div>
               <div><label><input type="radio" name="color" value="yellow" <?php echo $cColor=='yellow'?'checked':'' ?>>Yellow</label></div>
          </div>
          
          <br><br>
          <div><input class="blueButton" type=submit name="form" value=Submit></div>
     </form></div>
     
<?php
    }
?>


<?php
     // Preview Form Function
     function previewform() { 
?>

     <div class="body"><br>
          <p class="highlight">Preview</p>
          <table>
               <tr><td>Title: </td>
                    <td style="width:550px; color:<?php echo $_POST['color']; ?>">
                         <?php echo htmlentities($_POST['etitle']); ?>
                    </td>
               </tr>
               <tr><td>Post: </td>
                    <td style="width:550px; color:<?php echo $_POST['color']; ?>">
                         <?php echo nl2br(htmlentities($_POST['entry'])); ?>
                    </td>
               </tr>
          </table>
          <br>
          <form method="post">
               <button class="blueButton" name="publish">Publish</button>
               <button class="blueButton" name="edit">Edit</button>
               <button class="blueButton" name="cancel">Cancel</button>
          </form> 
     </div>

<?php
     }
?>

<?php
     
     // Including the footer
     include('tthaninayagam_a3_footer.php');
?>