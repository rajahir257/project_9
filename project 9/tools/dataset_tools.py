import pandas as pd
def load_dataset():
    print("\n== Load Dataset ==")
    path = input("Enter the path of the dataset (CSV file): ").strip()
    try:
        data = pd.read_csv(path)
        print("Dataset loaded successfully!")
        print(f"Rows: {data.shape[0]}, Columns: {data.shape[1]}")
        return data
    except FileNotFoundError:
        print("File not found. Check the file path and try again.")
    except Exception as error:
        print("Could not load the dataset:", error)
    return None
def explore_data(data):
    while True:
        print("\n== Explore Data ==")
        print("1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display data types")
        print("5. Display basic info")
        print("6. Go Back")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            print(data.head())
        elif choice == "2":
            print(data.tail())
        elif choice == "3":
            print(list(data.columns))
        elif choice == "4":
            print(data.dtypes)
        elif choice == "5":
            data.info()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")