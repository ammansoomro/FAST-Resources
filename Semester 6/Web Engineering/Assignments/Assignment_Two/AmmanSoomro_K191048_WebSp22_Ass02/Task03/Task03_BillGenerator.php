<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link rel="stylesheet" href="Task03.css">
      <title>Task 03</title>
   </head>
   <?php   
         $Bill = (double) $_POST['Bill_Value'];
         $Temp_Bill = (double) $_POST['Bill_Value'];
         $Units = $Bill;
         $Total_Bill = 0;
        
         if ($Temp_Bill <= 50) {
             $Total_Bill = $Temp_Bill * 3.50; 
         }
         
         else if ($Temp_Bill <= 150) {
             $Temp_Bill = $Temp_Bill - 50;
             $Total_Bill = $Total_Bill + (50 * 3.5) +  ($Temp_Bill * 4);
         }
         
         else if ($Temp_Bill <= 250)
         {
             $Temp_Bill = $Temp_Bill - 150;
             $Total_Bill = $Total_Bill + ($Temp_Bill * 5.20) + (50 * 3.5) + (100 * 4);
         }
         else
         {
             $Temp_Bill = $Temp_Bill - 250;
             $Total_Bill = $Total_Bill + ($Temp_Bill * 6.50) + (100 * 5.20) + (50 * 3.5) + (100 * 4);
         }
         ?>
   <body>

      <div class="container">
         <div class="form">
         <h2>PHP Electricity Bill</h2>
            <form action="" method="post">
                <p>
                    <input type="text" name="Bill_Value" id="Bill_Value" placeholder="Enter Your Unitss" value="<?php echo $Bill ?>">
                </p>
                <label>    
                    <?php echo "No of Units and Bill: $Units = $Total_Bill" ?>
                </label>
                <p>
                    <button type="submit" name="Submit"> Calculate</button>
                </p>
            </form>
         </div>
      </div>
   </body>
</html>