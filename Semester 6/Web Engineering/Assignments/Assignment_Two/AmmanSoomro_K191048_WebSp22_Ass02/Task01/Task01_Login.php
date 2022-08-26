<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login Process</title>
</head>
<?php
session_start();
    if($_POST["username"] == "Amman" && $_POST["password"] == "K191048"){
        $_SESSION["Login"] = "YES";
        echo "<h1> You are Logged in Correctly </h1>";
        echo "<p><a href='Task01_Document.php'>Link to protect file<a/></p>";
    }
    else{
        $_SESSION["Login"] = "NO";
        echo "<h1> You are NOT Logged in Correctly </h1>";
        echo "<p><a href='Task01_Document.php'>Link to protect file<a/></p>";
    }
?>
<body>    
</body>

