<?php include("mylib.php"); ?>
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
<?php 

	$kamran = new person("Kamran Malik");
	$fatima = new person("Fatima Rehan");
	$kamran->set_pin_no(1234);
 
	echo "Kamran's full name: " . $kamran->get_name()."<BR>";
	echo "Kamran's pin no : " . $kamran->get_pin_no()."<BR>";
	echo "Fatima's full name: " . $fatima->get_name()."<BR>"; 


	/* $pin_no is private, hence this line will generate an error.*/  
	//echo "Fetch private attribute: ".$kamran->pin_no; 

	// Using Inheritance. 
		$kamran = new person("Kamran Malik");
		echo "Kamran's full name: " . $kamran->get_name()."<BR>";
 
		$alina = new employee("Alina");
		echo "Overriding parents functions get_name() : ".$alina->get_name()."<BR>";

		$ali = new employee("Ali");
		echo "Overriding parents functions get_name() : " .$ali->get_name()."<BR>";

		$alina->set_pin_no(4321);
		echo "Alina's pin no : " . $alina->get_pin_no()."<BR>";


?>
</body>
</html>