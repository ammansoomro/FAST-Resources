<?php
session_start();
if($_SESSION["Login"] != "YES"){
    header("Location: Task01_Form.php");
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
    <link rel="stylesheet" href="Task01.css" />
</head>
<body>
    <div class="Document">
        <center>
        <h1>This Document is Protected</h1>
        <h3>
            You can only see it if you are logged in.
        </h3>
        </center>
    </div>
</body>
</html>