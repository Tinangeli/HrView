const facultyOptions = [
    "CITE - Information Technology",
    "CAAS - Contemporary Arts And Sciences",
    "CSC - College of Sciences and Criminology",
    "CAHS - College of Allied Health and Sciences "
];

const professorOptions = ["Martin", "Cua", "Chester"];

const semesterOptions = ["1st Semester", "2nd Semester"];

const schoolYearOptions = ["2024 - 2025", "2023 - 2024", "2022 - 2023"];

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