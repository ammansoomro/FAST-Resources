<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculator</title>
    <link rel="stylesheet" href="Task04.css">
</head>
<?php
    $val1 = (double)$_POST["val1"];
    $val2 = (double)$_POST["val2"];
    $Operator = $_POST["Operator"];
    $Answer = 0;
        switch ($Operator) {
        case "+":
        $Answer = $val1 + $val2;
        break;
        case "-":
         $Answer = $val1 - $val2;
        break;
        case "*":
        $Answer = $val1 * $val2;
        break;
        case "/":
        $Answer = $val1 / $val2;
    }
?>
<body>
    <div class="container">
        <div class="form">
            <form action="" method="post">
                <h2>Calculator</h2>
                <p>
                <input type="text" value="<?php $val1?>" name="val1" id="val1" placeholder="Enter a Number"><br>
                <input type="text" value="<?php $val2?>" name="val2" id="val2" placeholder="Enter a Number">
                </p>
                <p>
                <select name="Operator" id="Operator">
                    <option value="0">Select an Operator</option>
                    <option value="+">+</option>
                    <option value="-">-</option>
                    <option value="*">*</option>
                    <option value="/">/</option>
                </select>
                </p>
                <p>
                <label> <?php echo $Answer?> </label>
                </p>
                <p>
                <button type="submit"> Calculate</button>            
                </p>
            </form>
        </div>
    </div>
</body>
</html>