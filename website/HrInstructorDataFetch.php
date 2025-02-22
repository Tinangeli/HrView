<?php
header('Content-Type: application/json');

include 'HrInstructorViewIndex.php'; // Ensure this file exists and contains $conn

if (!$conn) {
    die(json_encode(["error" => "Database connection failed."]));
}

// Query to fetch faculties
$faculties = [];
$result = $conn->query("SELECT * FROM faculties");
if (!$result) {
    die(json_encode(["error" => "Query failed: " . $conn->error]));
}
while ($row = $result->fetch_assoc()) {
    $faculties[$row["id"]] = $row["name"];
}

// Query to fetch professors
$professors = [];
$result = $conn->query("SELECT * FROM professors");
if (!$result) {
    die(json_encode(["error" => "Query failed: " . $conn->error]));
}
while ($row = $result->fetch_assoc()) {
    $professors[$faculties[$row["faculty_id"]]][] = $row["name"];
}

// Query to fetch semesters
$semesters = [];
$result = $conn->query("SELECT * FROM semesters");
if (!$result) {
    die(json_encode(["error" => "Query failed: " . $conn->error]));
}
while ($row = $result->fetch_assoc()) {
    $semesters[] = $row["name"];
}

// Query to fetch school years
$schoolYears = [];
$result = $conn->query("SELECT * FROM school_years");
if (!$result) {
    die(json_encode(["error" => "Query failed: " . $conn->error]));
}
while ($row = $result->fetch_assoc()) {
    $schoolYears[] = $row["year"];
}

// Output JSON
echo json_encode([
    "faculties" => array_values($faculties),
    "professors" => $professors,
    "semesters" => $semesters,
    "schoolYears" => $schoolYears
]);

$conn->close();
?>
