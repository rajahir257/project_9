def show_statistics(data):
    print("\n== Descriptive Statistics ==")
    print(data.describe(include="all"))
    print("\nMissing values in each column:")
    print(data.isnull().sum())