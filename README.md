# Comprehensive Medication Management Dashboard

## 📋 Project Overview

This project aims to develop an integrated healthcare system for comprehensive medication management. The system analyzes multiple healthcare datasets to enhance patient safety and treatment effectiveness.

### 🎯 Objectives

- Design an integrated system for managing:
    - Patient demographics
    - Medical conditions
    - Prescribed medications
    - Known allergies

### 🔍 Key Goals

1. Identify potential adverse drug reactions (ADRs)
2. Validate medication appropriateness for medical conditions
3. Provide actionable insights to healthcare providers

### 📊 Dataset Structure

| Dataset | Description | Key Fields |
|---------|-------------|------------|
| `patients.csv` | Demographic information | ID, birthdate, gender, address |
| `medications.csv` | Prescription records | Medication codes, descriptions, dates |
| `conditions.csv` | Medical diagnoses | Condition codes, descriptions, dates |
| `allergies.csv` | Allergy records | Allergen codes, descriptions, dates |


### 📈 Interactive Dashboard

Access our comprehensive medication management dashboard on Tableau Public:
[View Dashboard](https://public.tableau.com/views/ComprehensiveMedicationManagementDashboard/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

The dashboard provides:
- Real-time medication analytics
- Patient demographic insights
- Drug interaction monitoring
- Treatment effectiveness metrics


## 🚀 Features

- MongoDB CRUD operations
- CSV file import functionality
- API data integration
- Comprehensive error handling
- Bulk and single document operations
- Collection management

## 🛠️ Technologies

- Python
- MongoDB
- pandas
- pymongo
- requests

## 💻 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Comprehensive-Medication-Management-Dashboard.git
cd Comprehensive-Medication-Management-Dashboard
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure MongoDB connection:
   - Ensure MongoDB is installed and running
   - Update the connection URI as needed

## 📚 Usage

### MongoDB CRUD Operations

```python
from mongodb_crud import MongoCRUD

# Initialize connection
crud = MongoCRUD(uri="your_mongodb_uri", db_name="your_database")

# Insert a document
crud.insert_document("collection_name", {"key": "value"})

# Read documents
documents = crud.read_documents("collection_name", query={"key": "value"})

# Update documents
crud.update_document("collection_name", 
                    query={"key": "value"}, 
                    new_values={"key": "new_value"})

# Delete documents
crud.delete_document("collection_name", query={"key": "value"})
```

### Importing CSV Data

```python
from extract import import_csv_to_mongodb

import_csv_to_mongodb(
    uri="your_mongodb_uri",
    db_name="your_database",
    collection_name="your_collection",
    csv_file_path="path/to/your/file.csv"
)
```

### API Integration

```python
from extract import fetch_api_to_mongodb

fetch_api_to_mongodb(
    uri="your_mongodb_uri",
    db_name="your_database",
    collection_name="your_collection",
    api_url="https://api.example.com/data",
    params={"key": "value"}
)
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2024 Mrunal Manohar Patil

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED.

## 👤 Author

Mrunal Manohar Patil  
✉️ mrunalmmpatil@gmail.com


