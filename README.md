BARCODE GENERATOR USING MONGODB AND PYTHON (CRUD OPERATION)

A Python-based application that generates, stores, and manages barcodes. The system uses MongoDB for database operations and allows users to create, view, update, and delete barcode records with ease.

FEATURES:
- Generates Barcodes: Creates barcodes from numerical data and save them as images.
- Database Intergration: Store barcode details (product name, code, file path) in MongoDB
- CRUD Operation:
    - Create new barcode entries.
    - Read and view saved barcode records.
    - Update existing barcode details.
    - Deelte barcode records from the database.

TECH STACK:
- Python is the core language for the project.
- MongoDB: NoSQL database for storing barcode records.
- Barcode Library for generating barcode images.
- VSCode

PROJECT STRUCTURES:
- barcode_manager.py: Handles barcode generation and saving
- db_manager.py: Manages database operations
- main.py: Entry point with a menu-driven interface
- barcodes/: Directory for saved barcode image
- .gitignore: Git ignore file (contains; venv, barcodes(images))

To run the code on the terminal, use:
python main.py
