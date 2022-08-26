<html>
 	<head>
 		<title>Address Book</title>
 	</head>
 	<body>
 <?php
 error_reporting(E_ERROR | E_PARSE);
 // Connects to your Database 
$link = mysqli_connect("localhost", "root", "") or die(mysql_error()); 
 mysqli_select_db($link, "K190300") or die(mysql_error()); 


$mode = $_GET['mode']; //Hidden variable send via form to indicate operations: edited, remove , add etc. 
$name = $_GET['name']; // DB col 
$phone = $_GET['phone']; // DB col 
$email = $_GET['email']; // DB col 
$id = $_GET['id']; // DB col
$self = $_SERVER['PHP_SELF']; //PHP_SELF is the name of the currently executing script.
//echo "self = ". $self."<BR>";
//


if ( $mode=="add") 
 {
 Print '<h2>Add Contact</h2>
 <p> 
 <form action=';
 echo $self; 
 Print '
 method=GET> 
 <table>
 <tr><td>Name:</td><td><input type="text" name="name" /></td></tr> 
 <tr><td>Phone:</td><td><input type="text" name="phone" /></td></tr> 
 <tr><td>Email:</td><td><input type="text" name="email" /></td></tr> 
 <tr><td colspan="2" align="center"><input type="submit" /></td></tr> 
 <input type=hidden name=mode value=added>
 </table> 
 </form> <p>';
 } 
 
 if ( $mode=="added") 
 {
 mysqli_query ($link,"INSERT INTO address (name, phone, email) VALUES ('$name', '$phone', '$email')");
 }

 if ( $mode=="edit") 
 { 
 Print '<h2>Edit Contact</h2> 
 <p> 
 <form action=';
 echo $self; 
 Print '
 method=GET> 
 <table> 
 <tr><td>Name:</td><td><input type="text" value="'; 
 Print $name; 
 print '" name="name" /></td></tr> 
 <tr><td>Phone:</td><td><input type="text" value="'; 
 Print $phone; 
 print '" name="phone" /></td></tr> 
 <tr><td>Email:</td><td><input type="text" value="'; 
 Print $email; 
 print '" name="email" /></td></tr> 
 <tr><td colspan="2" align="center"><input type="submit" /></td></tr> 
 <input type=hidden name=mode value=edited> 
 <input type=hidden name=id value='; 
 Print $id; 
 print '> 
 </table> 
 </form> <p>'; 
 } 
 
 if ( $mode=="edited") 
 { 
 mysqli_query ($link, "UPDATE address SET name = '$name', phone = '$phone', email = '$email' WHERE id = $id"); 
 Print "Data Updated!<p>"; 
 } 

if ( $mode=="remove") 
 {
 mysqli_query ($link,"DELETE FROM address where id=$id");
 Print "Entry has been removed <p>";
 }
 

 $data = mysqli_query($link, "SELECT * FROM address ORDER BY name ASC") 
 or die(mysql_error()); 
 Print "<h2>Address Book</h2><p>"; 
 Print "<table border cellpadding=3>"; 
 Print "<tr><th width=100>Name</th><th width=100>Phone</th><th width=200>Email</th><th width=100 colspan=2>Admin</th></tr>"; Print "<td colspan=5 align=right><a href=" .$_SERVER['PHP_SELF']. "?mode=add>Add Contact</a></td>"; 
 while($info = mysqli_fetch_array( $data )) 
 { 
 Print "<tr><td>".$info['name'] . "</td> "; 
 Print "<td>".$info['phone'] . "</td> "; 
 Print "<td> <a href=mailto:".$info['email'] . ">" .$info['email'] . "</a></td>"; 
 Print "<td><a href=" .$_SERVER['PHP_SELF']. "?id=" . $info['id'] ."&name=" . $info['name'] . "&phone=" . $info['phone'] ."&email=" . $info['email'] . "&mode=edit>Edit</a></td>"; Print "<td><a href=" .$_SERVER['PHP_SELF']. "?id=" . $info['id'] ."&mode=remove>Remove</a></td></tr>"; 
 } 
 Print "</table>"; 
 ?> 

<p>


 	</body> 
 </html> 
