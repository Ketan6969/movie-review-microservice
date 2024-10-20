<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
</head>
<body>
    <form action="login.php" method="post" class="login-form">
        <input type="text" name="email" id="email" placeholder="Email" required>
        <input type="text" name="password" id="password" placeholder="Password" required>
        <input type="submit" value="Log in" name="submit">
    </form>
</body>
</html>

<?php
    if($_SERVER['REQUEST_METHOD'] == "POST") {
        $email = $_POST['email'];
        $password = $_POST['password'];

    }

?>

