import matplotlib.pyplot as plt
def visualization_menu(data):
    while True:
        print("\n== Data Visualization ==")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Go Back")
        choice = input("Enter your choice: ").strip()
        if choice == "6":
            return None
        if choice not in {"1", "2", "3", "4", "5"}:
            print("Invalid choice.")
            continue
        print("Available columns:", list(data.columns))
        try:
            if choice == "1":
                x_column = input("Enter category column name: ").strip()
                y_column = input("Enter numeric column name: ").strip()
                if x_column not in data.columns or y_column not in data.columns:
                    print("Column not found.")
                    continue
                grouped = data.groupby(x_column)[y_column].sum()
                grouped.plot(kind="bar")
                plt.title(f"{y_column} by {x_column}")
                plt.xlabel(x_column)
                plt.ylabel(y_column)
            elif choice == "2":
                x_column = input("Enter x-axis column name: ").strip()
                y_column = input("Enter y-axis column name: ").strip()
                if x_column not in data.columns or y_column not in data.columns:
                    print("Column not found.")
                    continue
                data.plot(x=x_column, y=y_column, kind="line", marker="o")
                plt.title(f"{y_column} by {x_column}")
            elif choice == "3":
                x_column = input("Enter x-axis column name: ").strip()
                y_column = input("Enter y-axis column name: ").strip()
                if x_column not in data.columns or y_column not in data.columns:
                    print("Column not found.")
                    continue
                data.plot(x=x_column, y=y_column, kind="scatter")
                plt.title(f"{y_column} vs {x_column}")
            elif choice == "4":
                column = input("Enter numeric column name: ").strip()
                if column not in data.columns:
                    print("Column not found.")
                    continue
                values = data[column].dropna()
                if values.empty:
                    print("This column has no values to plot.")
                    continue
                values.value_counts().plot(kind="pie", autopct="%1.1f%%")
                plt.ylabel("")
            elif choice == "5":
                column = input("Enter numeric column name: ").strip()
                if column not in data.columns:
                    print("Column not found.")
                    continue
                data[column].dropna().plot(kind="hist", bins=10)
                plt.xlabel(column)
            plt.tight_layout()
            plt.show()
            print("Visualization displayed successfully!")
            return plt.gcf()
        except (TypeError, ValueError) as error:
            plt.close("all")
            print("Could not create the plot. Check that the selected columns contain suitable data.")
            print("Details:", error)