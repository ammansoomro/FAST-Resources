<?php $conn = mysqli_connect('localhost','id18683804_k191048','e)tvli/t9/FPJrMl','id18683804_assignment02');
if($_SERVER['REQUEST_METHOD'] == 'POST')
{
    $get_Query = $_REQUEST['Query'];
        $conn->query($get_Query);
    echo "$get_Query Executed. Check Your Database to Confirm if it was Successful";
    echo '<br><a href="http://localhost:8232/WE/Task02_LocalDatabase.html"> Go Back</a>';
}
?>
