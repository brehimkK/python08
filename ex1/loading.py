import sys
import importlib


REQUIRED_PACKAGES = ["pandas", "numpy", "matplotlib"]


def check_dependencies():
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:\n")

    missing = []
    installed = {}

    for pkg in REQUIRED_PACKAGES:
        try:
            module = importlib.import_module(pkg)
            try:
                from importlib.metadata import version
                ver = version(pkg)
            except Exception:
                ver = "unknown"

            print(f"[OK] {pkg} ({ver}) - Ready")
            installed[pkg] = module

        except ImportError:
            print(f"[MISSING] {pkg} - Not installed")
            missing.append(pkg)
    try:
        module = importlib.import_module("requests")
        from importlib.metadata import version
        print(f"[OK] requests ({version('requests')}) - Optional")
    except Exception:
        pass

    if missing:
        print("\nSome dependencies are missing.\n")
        print("Install with pip:")
        print("  pip install -r requirements.txt\n")
        print("Install with Poetry:")
        print("  poetry install\n")
        sys.exit(1)

    return installed


def generate_data(np):
    size = 1000

    x = np.arange(size)
    y = np.random.normal(0, 1, size)

    return x, y


def analyze_data(pd, x, y):
    df = pd.DataFrame({
        "index": x,
        "matrix_signal": y
    })

    return df


def visualize(plt, df):
    print("Generating visualization...\n")

    plt.figure()
    plt.plot(df["index"], df["matrix_signal"])
    plt.title("Matrix Data Analysis")
    plt.xlabel("Index")
    plt.ylabel("Signal")

    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main():
    modules = check_dependencies()

    pd = modules["pandas"]
    np = modules["numpy"]
    plt = importlib.import_module("matplotlib.pyplot")

    print("\nAnalyzing Matrix data...")
    x, y = generate_data(np)

    print(f"Processing {len(x)} data points...\n")

    df = analyze_data(pd, x, y)
    visualize(plt, df)


if __name__ == "__main__":
    main()
