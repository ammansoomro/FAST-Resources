function updateOutput() {
    var num1 = document.getElementsByName("num1")[0].value;
    var num2 = document.getElementsByName("num2")[0].value;
    var operator = document.getElementsByName("operator")[0].value;
    var result = document.getElementsByName("result")[0];
    switch (operator) {
        case "add":
            result.value = parseInt(num1) + parseInt(num2);
            break;
        case "sub":
            result.value = parseInt(num1) - parseInt(num2);
            break;
        case "mul":
            result.value = parseInt(num1) * parseInt(num2);
            break;
        case "div":
            result.value = (parseInt(num1) / parseInt(num2)).toFixed(1);
            break;
    }
}