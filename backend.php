<?php
$conn = mysqli_connect("localhost", "your_username", "your_password", "crud_example");

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

if (isset($_POST['create'])) {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $sql = "INSERT INTO users (name, email) VALUES ('$name', '$email')";
    mysqli_query($conn, $sql);
} elseif (isset($_POST['read'])) {
    $result = mysqli_query($conn, "SELECT * FROM users");
    while ($row = mysqli_fetch_assoc($result)) {
        echo "ID: " . $row['id'] . " - Name: " . $row['name'] . " - Email: " . $row['email'] . "<br>";
    }
} elseif (isset($_POST['update'])) {
    // Assuming you have a specific user ID to update, modify the query accordingly.
    $id_to_update = 1;
    $new_name = "New Name";
    $new_email = "new@email.com";
    $sql = "UPDATE users SET name='$new_name', email='$new_email' WHERE id=$id_to_update";
    mysqli_query($conn, $sql);
} elseif (isset($_POST['delete'])) {
    // Assuming you have a specific user ID to delete, modify the query accordingly.
    $id_to_delete = 1;
    $sql = "DELETE FROM users WHERE id=$id_to_delete";
    mysqli_query($conn, $sql);
}

mysqli_close($conn);
?>
