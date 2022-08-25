<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
<?php

$array1 = explode(" ",$_POST["str01"]); 
echo "<PRE>";
print_r ($array1);
echo "</PRE>";
echo "<BR>";
foreach($array1 as $element) {
	echo $element."<br/>";
}
?>
</body>
</html>