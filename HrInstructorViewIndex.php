<?php
$host = "localhost";  // Change if using a different host
$username = "root";   // Change to your MySQL username
$password = "";  // Change to your MySQL password
$database = "school_system";  // Database name

// Create connection
$conn = new mysqli($host, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die(json_encode(["error" => "Connection failed: " . $conn->connect_error]));
}


