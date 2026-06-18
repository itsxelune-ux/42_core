import importlib.metadata


def check_dependency(package_name, description):
    try:
        module = importlib.import_module(package_name)
        version = module.__version__

        print(f"[OK] {package_name} ({version}) - {description}")

        return module

    except ImportError:
        print(f"[MISSING] {package_name}")
        return None


def analyze_data(pd, np):
    print("\nAnalyzing Matrix data...")

    data = np.random.randint(0, 100, 1000)

    df = pd.DataFrame({
        "matrix_signal": data
    })

    print(f"Processing {len(df)} data points...")
    print(f"Average signal: {df['matrix_signal'].mean():.2f}")
    print(f"Maximum signal: {df['matrix_signal'].max()}")
    print(f"Minimum signal: {df['matrix_signal'].min()}")
    return df


def generate_visualization(df):
    import matplotlib.pyplot as plt

    print("\nGenerating visualization...")

    plt.hist(df["matrix_signal"])            # histogram
    plt.title("Matrix Signal Distribution")  # adds title
    plt.xlabel("Signal Strength")            # labels the X-axis
    plt.ylabel("Frequency")                  # labels the Y-axis
    plt.savefig("matrix_analysis.png")       # saves it as an image
    plt.close()                              # closes the plot window in memory

    print("Results saved to: matrix_analysis.png")


def compare_managers():
    print("\nDependency Management Comparison\n")

    print("pip:")
    print("- uses requirements.txt")
    print("- installs packages directly")
    print("- simple, manual dependency handling\n")

    print("Poetry:")
    print("- uses pyproject.toml")
    print("- resolves dependencies automatically")
    print("- creates virtual environments")
    print("- locks exact versions")


def print_install_help():
    print("\nMissing dependencies detected.\n")

    print("Install with pip:")
    print("pip install -r requirements.txt\n")

    print("Install with Poetry:")
    print("poetry install")


def main():
    print("LOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")

    pd = check_dependency(
        "pandas",
        "Data manipulation ready"
    )

    np = check_dependency(
        "numpy",
        "Numerical computation ready"
    )

    mpl = check_dependency(
        "matplotlib",
        "Visualization ready"
    )

    if pd is None or np is None or mpl is None:
        print_install_help()
        return

    compare_managers()

    df = analyze_data(pd, np)
    generate_visualization(df)

    print("\nAnalysis complete!")


if __name__ == "__main__":
    main()
