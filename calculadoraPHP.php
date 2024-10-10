<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora PHP</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        input[type="text"] {
            width: 200px;
            height: 30px;
            margin-bottom: 10px;
            font-size: 20px;
            text-align: right;
        }
        button {
            width: 50px;
            height: 50px;
            font-size: 20px;
            margin: 5px;
        }
    </style>
</head>
<body>
    <h1>Calculadora em PHP</h1>
    <form method="post" action="">
        <input type="text" name="expression" value="<?= isset($_POST['expression']) ? $_POST['expression'] : '' ?>" readonly><br>
        
        <button type="submit" name="expression" value="<?= (isset($_POST['expression']) ? $_POST['expression'] : '') . '1' ?>">1</button>
        <button type="submit" name="expression" value="<?= (isset($_POST['expression']) ? $_POST['expression'] : '') . '2' ?>">2</button>
        <button type="submit" name="expression" value="<?= (isset($_POST['expression']) ? $_POST['expression'] : '') . '3' ?>">3</button>
        <button type="submit" name="expression" value="<?= (isset($_POST['expression']) ? $_POST['expression'] : '') . '+' ?>">+</button><br>
        
        <button type="submit" name="expression" value="<?= (isset($_POST['expression']) ? $_POST['expression'] : '') . '4' ?>">4</button>
        <button type="submit" name="expression" value="<?= (isset($_POST['expression']) ? $_POST['expression'] : '') . '5' ?>">5</button>
        <button type="submit" name="expression" value="<?= (isset($_POST['expression']) ? $_POST['expression'] : '') . '6' ?>">6</button>
        <button type="submit" name="expression" value="<?= (isset($_POST['expression']) ? $_POST['expression'] : '') . '-' ?>">-</button><br>
        
        <button type="submit" name="expression" value="<?= (isset($_POST['expression']) ? $_POST['expression'] : '') . '7' ?>">7</button>
        <button type="submit" name="expression" value="<?= (isset($_POST['expression']) ? $_POST['expression'] : '') . '8' ?>">8</button>
        <button type="submit" name="expression" value="<?= (isset($_POST['expression']) ? $_POST['expression'] : '') . '9' ?>">9</button>
        <button type="submit" name="expression" value="<?= (isset($_POST['expression']) ? $_POST['expression'] : '') . '*' ?>">*</button><br>
        
        <button type="submit" name="expression" value="<?= (isset($_POST['expression']) ? $_POST['expression'] : '') . '0' ?>">0</button>
        <button type="submit" name="expression" value="<?= (isset($_POST['expression']) ? '' : '') ?>">C</button>
        <button type="submit" name="equals" value="=">=</button>
        <button type="submit" name="expression" value="<?= (isset($_POST['expression']) ? $_POST['expression'] : '') . '/' ?>">/</button>
    </form>

    <?php
    if (isset($_POST['equals']) && isset($_POST['expression'])) {
        try {
            $result = eval("return " . $_POST['expression'] . ";");
            echo "<h2>Resultado: " . $result . "</h2>";
        } catch (Exception $e) {
            echo "<h2>Erro na expressão!</h2>";
        }
    }
    ?>
</body>
</html>

