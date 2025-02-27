


async function loadData() {
    try {
        const response = await fetch("HrInstructorDataFetch.php"); // Fetch data from PHP API
        const data = await response.json();

        // Store data globally
        window.facultyOptions = data.faculties;
        window.professorOptions = data.professors;
        window.semesterOptions = data.semesters;
        window.schoolYearOptions = data.schoolYears;

        console.log("Data Loaded:", data); // Debugging
    } catch (error) {
        console.error("Error loading data:", error);
    }

}


// Call loadData() when the page loads
    document.addEventListener("DOMContentLoaded", function () {
        loadData();
    });


function showCombobox(inputId, optionsArray) {
    const inputElement = document.getElementById(inputId);
    const combobox = document.getElementById(inputId + "Combobox");
    const inputValue = inputElement.value.toLowerCase();

    combobox.innerHTML = "";

    if (inputValue) {
        let filteredOptions = [];

        if (Array.isArray(optionsArray)) {
            filteredOptions = optionsArray.filter(option => option.toLowerCase().includes(inputValue));
        } else if (typeof optionsArray === "object") {
            // Handle object case for professors
            Object.keys(optionsArray).forEach(faculty => {
                optionsArray[faculty].forEach(professor => {
                    if (professor.toLowerCase().includes(inputValue)) {
                        filteredOptions.push(professor);
                    }
                });
            });
        }

        if (filteredOptions.length > 0) {
            filteredOptions.forEach(option => {
                const div = document.createElement("div");
                div.textContent = option;
                div.onclick = function () {
                    inputElement.value = option;
                    combobox.style.display = "none";
                };
                combobox.appendChild(div);
            });

            combobox.style.display = "block";
            combobox.style.position = "absolute";
            combobox.style.width = inputElement.offsetWidth + "px";
        } else {
            combobox.style.display = "none";
        }
    } else {
        combobox.style.display = "none";
    }
}

// Hide combobox when clicking outside
document.addEventListener("click", function (event) {
    ["FacultyInput", "ProfessorInput", "SemesterInput", "SchoolYearInput"].forEach(inputId => {
        const combobox = document.getElementById(inputId + "Combobox");
        if (!event.target.closest(`#${inputId}, #${inputId}Combobox`)) {
            combobox.style.display = "none";
        }
    });
});



async function fetch_instructor_pie_chart_data() {
    try{
        const  response = await fetch("http://localhost:8000/api/instructor-pie-chart/")
        const result = await response.json();

        const labels = result.data.map(item => item.category);
        const scores = result.data.map(item => item.score);

        const data = {
            labels: labels,
            datasets: [{
                data: scores,
                backgroundColor: [
                    "#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0",
                    "#9966FF", "#FF9F40", "#FF6384", "#36A2EB",
                    "#FFCE56", "#4BC0C0", "#9966FF"
                ],
                hoverOffset: 20
            }]
        };

        const ctx = document.getElementById("instructor_pie_chart").getContext("2d");
        const instructor_pie_chart = new Chart(ctx, {
            type: "pie",
            data: data,
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { position: "bottom" } },
                onclick: function (event, elements) {
                    if (elements.length > 0) {
                        const index = elements[0].index;
                        const category = labels[index]; // Get clicked category
                        const description = descriptions[index]; // Get category description
                        openModal(category, description); // Show modal
                    }
                }
            }
        })
    } catch (error) {
        console.error("Error fetching pie chart data:", error);
    }
}

async function fetch_student_pie_chart_data() {
    try {
        const response = await fetch("http://localhost:8000/api/student-pie-chart/"); // Call Django API
        const result = await response.json();

        // Extract labels and data
        const labels = result.data.map(item => item.category);  // Extract category names
        const scores = result.data.map(item => item.score);      // Extract corresponding scores
        const descriptions = result.data.map(item => item.description); // Extract descriptions

        // Define chart data
        const data = {
            labels: labels,
            datasets: [{
                data: scores,



                backgroundColor: [
                    "#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0",
                    "#9966FF", "#FF9F40", "#FF6384", "#36A2EB",
                    "#FFCE56", "#4BC0C0", "#9966FF"
                ],
                hoverOffset: 40 // Effect when hovering
            }]
        };

        // Render Chart
        const ctx = document.getElementById("student_pie_chart").getContext("2d");
        const student_pie_chart = new Chart(ctx, {
            type: "pie",
            data: data,
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { position: "bottom" } },
                onClick: function (event, elements) {
                    if (elements.length > 0) {
                        const index = elements[0].index;
                        const category = labels[index]; // Get clicked category
                        const description = descriptions[index]; // Get category description
                        openModal(category, description); // Show modal
                    }
                }
            }
        });

    } catch (error) {
        console.error("Error fetching pie chart data:", error);
    }
}

function openModal(category, description) {
    document.getElementById("modalTitle").innerText = `Category: ${category}`;
    document.getElementById("modalText").innerText = description;
    document.getElementById("modalOverlay").style.display = "block";
    document.getElementById("infoModal").style.display = "block";
}

function closeModal() {
    document.getElementById("modalOverlay").style.display = "none";
    document.getElementById("infoModal").style.display = "none";
}

// Close button event
document.getElementById("closeBtn").addEventListener("click", closeModal);

// Run function when page loads
fetch_student_pie_chart_data()
fetch_instructor_pie_chart_data()




