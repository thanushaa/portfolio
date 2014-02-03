<?php 
           /*
           Name: Thanushaa Thaninayagam (tthaninayagam)
           Purpose: The header file includes the beginning tags of html: head,
                                    title and CSS.
           */
?>

<!DOCTYPE html>
<html lang='en'>
<head>
     <meta charset="utf-8" />
     <title><?php echo isset($title)?$title:'INT322 Entry'; ?></title>
           
      <style type="text/css">
          body { margin: 0px;
               background: #000000;
               font-family: "Lucida Sans Unicode", "Lucida Grande", sans-serif;
               font-size: 13px;
               letter-spacing: 0.5px;
               color: #FFFFFF;
          }
          div.body { padding: 5px;
               margin: 0px 50px 0px 50px;
               line-height: 14px;
          }              
          div.bar { background-color: #4A7992;
               margin: 0px;
               padding: 15px;
               font-size: 14px;
          }
          label.align{
               width: 100px;
               float: left;
          }
               
          p.errorMessage{ color: red;
               font-size: 11px;
          }
          p.highlight{ background: #4A7992;
               font-size: 13px;
               font-weight: 450;
               padding: 5px;
               text-transform: uppercase;
          }

          table, tr, td{
               border-collapse:collapse;
               border: 1px solid grey;
          }
          td {
               width: 100px;
               padding:2px;
          }
          table.viewPost, tr.viewPost, td.viewPost{
               vertical-align: top;
               border: 1px solid black;
               width: 550px;
               height: auto;
          }
          
          a.navbar:link, a.navbar:visited {
               color: #FFFFFF;
               margin: 0px;
               padding: 15px;
               font-size: 14px;
               font-weight: 700;
               background-color: #4A7992;
               text-decoration: none;
               text-transform: uppercase;
          }
          a.active:link, a.active:visited, a.active:hover, a.navbar:hover {
               color: #FFFFFF;
               margin: 0px;
               padding: 19px 15px;
               font-size:14px;
               font-weight: 700;
               background-color: #000000;
               text-decoration: none; 
               text-transform: uppercase;
          }
          
          .blueButton {
               border: #4A7992 1px solid;
               background-color: #4A7992;
               color: #FFFFFF;
               font-family: "Lucida Sans Unicode", "Lucida Grande", sans-serif;
               font-size: 12px;
               font-weight: 450;
               letter-spacing: 1px;
               padding:2px 8px;
               text-decoration: none;
               text-transform: uppercase;
          }
          
          .blueBar {
               border: #4A7992 1px solid;
               background-color: #4A7992;
               color: #FFFFFF;
               font-family: "Lucida Sans Unicode", "Lucida Grande", sans-serif;
               font-size: 14px;
               font-weight: 700;
               letter-spacing: 1px;

               text-decoration: none;
               text-transform: uppercase;
          }
      </style>    
</head>
<body>