import pandas as pd
def missing_data_menu(data):
    while True:
        print("\n== Handle Missing Data ==")
        print("1. Display rows with missing values")
        print("2. Fill missing numeric values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")
        print("5. Go Back")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            missing_rows = data[data.isnull().any(axis=1)]
            if missing_rows.empty:
                print("No missing values found in the dataset!")
            else:
                print(missing_rows)
        elif choice == "2":
            numeric_columns = data.select_dtypes(include="number").columns
            if len(numeric_columns) == 0:
                print("No numeric columns available.")
            else:
                for column in numeric_columns:
                    data[column] = data[column].fillna(data[column].mean())
                print("Missing numeric values filled with the column mean.")
        elif choice == "3":
            before = len(data)
            data.dropna(inplace=True)
            print(f"Removed {before - len(data)} row(s) with missing values.")
        elif choice == "4":
            value = input("Enter replacement value (e.g., Unknown or 0): ")
            data.fillna(value, inplace=True)
            print("Missing values replaced.")
        elif choice == "5":
            return data
        else:
            print("Invalid choice.")