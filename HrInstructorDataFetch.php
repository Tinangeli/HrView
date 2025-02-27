<?php
header('Content-Type: application/json');
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT); // Enable error reporting

include 'HrInstructorViewIndex.php'; // Ensure this contains $conn

if (!$conn) {
    die(json_encode(["error" => "Database connection failed."]));
}

try {
    // Fetch courses (faculties)
    $faculties = [];
    $result = $conn->query("SELECT id, course_name FROM courses");
    while ($row = $result->fetch_assoc()) {
        $faculties[$row["id"]] = $row["course_name"];
    }

    // Fetch professors based on roles
    $professors = [];
    $result = $conn->query("SELECT users.id, users.name FROM users 
                            JOIN model_has_roles ON users.id = model_has_roles.model_id 
                            JOIN roles ON model_has_roles.role_id = roles.id 
                            WHERE roles.role_name = 'Professor'");
    while ($row = $result->fetch_assoc()) {
        $professors[] = $row["name"];
    }

    // Fetch semesters
    $semesters = [];
    $result = $conn->query("SELECT DISTINCT semester FROM schedules");
    while ($row = $result->fetch_assoc()) {
        $semesters[] = $row["semester"];
    }

    // Fetch school years
    $schoolYears = [];
    $result = $conn->query("SELECT DISTINCT year FROM schedules");
    while ($row = $result->fetch_assoc()) {
        $schoolYears[] = $row["year"];
    }

    // Fetch evaluation scores (students & instructors)
    $evaluation_scores = [];
    $result = $conn->query("SELECT evaluation.id, evaluation_name, score, evaluation_marks.timestamp FROM evaluation 
                            JOIN evaluation_marks ON evaluation.id = evaluation_marks.evaluation_id");
    while ($row = $result->fetch_assoc()) {
        $evaluation_scores[] = $row;
    }

    // Output JSON response
    echo json_encode([
        "faculties" => array_values($faculties),
        "professors" => $professors,
        "semesters" => array_unique($semesters),
        "schoolYears" => array_unique($schoolYears),
        "evaluation_scores" => $evaluation_scores
    ]);
} catch (Exception $e) {
    echo json_encode(["error" => $e->getMessage()]);
}

// Close connection
$conn->close();
?>