def dataframe_menu(data):
    while True:
        print("\n== DataFrame Operations ==")
        print("1. Select a column")
        print("2. Filter rows")
        print("3. Sort by a column")
        print("4. Add a new column")
        print("5. Go Back")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            column = input("Enter column name: ").strip()
            if column in data.columns:
                print(data[column])
            else:
                print("Column not found.")
        elif choice == "2":
            column = input("Enter column name to filter: ").strip()
            if column not in data.columns:
                print("Column not found.")
                continue
            value = input("Show rows where this column equals: ").strip()
            result = data[data[column].astype(str) == value]
            print(result if not result.empty else "No matching rows found.")
        elif choice == "3":
            column = input("Enter column name to sort by: ").strip()
            if column not in data.columns:
                print("Column not found.")
                continue
            order = input("Ascending order? (y/n): ").strip().lower()
            print(data.sort_values(by=column, ascending=(order != "n")))
        elif choice == "4":
            name = input("Enter new column name: ").strip()
            if not name:
                print("Column name cannot be empty.")
                continue
            value = input("Enter the same value for every row: ").strip()
            data[name] = value
            print("New column added.")
            print(data.head())
        elif choice == "5":
            break
        else:
            print("Invalid choice.")