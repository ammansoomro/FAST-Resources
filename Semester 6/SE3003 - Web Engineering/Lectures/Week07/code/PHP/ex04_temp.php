<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
<?php
if(isset($_POST['submit']))
{
	$f= $_POST['far'];
	$c= ($f - 32) * (5/9);
	echo " Temprature in Celcius =".$c;
}		
?>
</body>
</html>