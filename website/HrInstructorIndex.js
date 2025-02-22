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
        const filteredOptions = optionsArray.filter(option => option.toLowerCase().includes(inputValue));

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


async function loadPlot() {
    try {
        const response = await fetch("http://127.0.0.1:8000/api/plot/");
        const data = await response.json();

        if (data.image) {
            // Set the Base64 image as the src of an <img> tag
            document.getElementById("plotImage").src = "data:image/png;base64," + data.image;
        } else {
            console.error("No image received from API.");
        }
    } catch (error) {
        console.error("Error loading plot:", error);
    }
}

async function loadPieChart() {
    try {
        const response = await fetch("http://localhost:8000/api/pie/"); // Adjust URL if needed
        const data = await response.json();

        if (data.image) {
            document.getElementById("pieChart").src = "data:image/png;base64," + data.image;
        } else {
            console.error("Error loading pie chart:", data.error);
        }
    } catch (error) {
        console.error("Request failed:", error);
    }
}

// Call function when the page loads
document.addEventListener("DOMContentLoaded", loadPieChart);



