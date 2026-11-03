from tools.dataset_tools import load_dataset, explore_data
from tools.dataframe_operations import dataframe_menu
from tools.missing_data import missing_data_menu
from tools.statistics_tools import show_statistics
from tools.visualization import visualization_menu

# def show_menu():
#     print("\n========== Data Analysis & Visualization Program ==========")
#     print("Please select an option:")
#     print("1. Load Dataset")
#     print("2. Explore Data")
#     print("3. Perform DataFrame Operations")
#     print("4. Handle Missing Data")
#     print("5. Generate Descriptive Statistics")
#     print("6. Data Visualization")
#     print("7. Save Visualization")
#     print("8. Exit")
#     print("=" * 58)
    
def main():
    data = None
    last_plot = None
    while True:
        
        print("\n========== Data Analysis & Visualization Program ==========")
        print("Please select an option:")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("=" * 58)
        
        choice = input("enter your choice: ")
        
        if choice == "1":
            data = load_dataset()
        elif choice == "2":
            if data is None:
                print("Please load a dataset first.")
            else:
                explore_data(data)
        elif choice == "3":
            if data is None:
                print("Please load a dataset first.")
            else:
                dataframe_menu(data)
        elif choice == "4":
            if data is None:
                print("Please load a dataset first.")
            else:
                data = missing_data_menu(data)
        elif choice == "5":
            if data is None:
                print("Please load a dataset first.")
            else:
                show_statistics(data)
        elif choice == "6":
            if data is None:
                print("Please load a dataset first.")
            else:
                last_plot = visualization_menu(data)
        elif choice == "7":
            if last_plot is None:
                print("Please create a visualization first.")
            else:
                filename = input("Enter file name (e.g., chart.png): ").strip()
                if not filename:
                    filename = "chart.png"
                if not filename.lower().endswith(".png"):
                    filename += ".png"
                last_plot.savefig(filename)
                print(f"Visualization saved as {filename} successfully!")
        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")
if __name__ == "__main__":
    main()