import numpy as np
import pandas as pd
from pathlib import Path

# Step 1: Set random seed
np.random.seed(42)

# Step 2: Number of students
n = 300

# Step 3: Generate student IDs
student_id = [f"IITB{i:03d}" for i in range(1, n + 1)]

# Step 4: Generate branches
branches = [
    "Computer Science",
    "Electrical Engineering",
    "Mechanical Engineering",
    "Civil Engineering",
    "Chemical Engineering",
    "Aerospace Engineering",
    "Metallurgical Engineering",
    "Engineering Physics"
]

branch = np.random.choice(branches, n)

# Step 5: Generate CGPA and coding scores
cgpa = np.round(np.random.uniform(5.0, 10.0, n), 2)
coding_score = np.random.randint(20, 101, n)

# Step 6: Generate placement status
placement_probability = (
    0.25 + (cgpa - 5) * 0.09 + coding_score * 0.003
)

placement_probability = np.clip(
    placement_probability, 0.10, 0.98
)

placement_status = [
    "Placed" if np.random.random() < p else "Not Placed"
    for p in placement_probability
]

# Step 7: Company and sector details
companies = {
    "Google": "Technology",
    "Microsoft": "Technology",
    "Amazon": "E-commerce",
    "TCS": "IT Services",
    "Goldman Sachs": "Finance",
    "Deloitte": "Consulting",
    "Samsung": "Electronics"
}

company_list = []
sector_list = []
offers_list = []
base_salary_list = []
total_ctc_list = []

# Step 8: Generate placement details
for status in placement_status:

    if status == "Placed":
        company = np.random.choice(list(companies.keys()))
        sector = companies[company]
        offers = np.random.randint(1, 4)
        base_salary = round(np.random.uniform(8, 35), 2)
        total_ctc = round(
            base_salary * np.random.uniform(1.1, 1.5), 2
        )

    else:
        company = "Not Placed"
        sector = "Not Applicable"
        offers = 0
        base_salary = 0
        total_ctc = 0

    company_list.append(company)
    sector_list.append(sector)
    offers_list.append(offers)
    base_salary_list.append(base_salary)
    total_ctc_list.append(total_ctc)

# Step 9: Create DataFrame
df = pd.DataFrame({
    "Student_ID": student_id,
    "Institute": "IIT Bombay",
    "Branch": branch,
    "CGPA": cgpa,
    "Coding_Score": coding_score,
    "Placement_Status": placement_status,
    "Company": company_list,
    "Sector": sector_list,
    "Offers": offers_list,
    "Base_Salary_LPA": base_salary_list,
    "Total_CTC_LPA": total_ctc_list
})

# Step 10: Save CSV file
project_folder = Path(__file__).resolve().parent.parent
dataset_folder = project_folder / "Dataset"
dataset_folder.mkdir(exist_ok=True)

file_path = dataset_folder / "iit_bombay_placement_data.csv"
df.to_csv(file_path, index=False)

# Step 11: Display dataset information
print("Dataset generated successfully!")
print("Total Students:", len(df))
print("Total Columns:", len(df.columns))
print(df.head())
print("File saved at:", file_path)
