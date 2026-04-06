import sys
import importlib


def  check_dependency(name):
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown") # get the attributs or unknown as default safly
        return True, version
    except ImportError:
        return False, None


def show_dependency_status() -> bool:
    dependencies = {
		"pandas": "Data manipulation ready",
		"numpy": "Numerical computation ready",
		"matplotlib": "Visualization ready",
		"requests": "Network access ready"
	}
    all_ok = True

    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    for lab, status in dependencies.items():
        ok, version = check_dependency(lab)
        if ok:
                print(f"[OK] {lab} ({version}) - {status}")
        else:
            print(f"[MISSING] {lab} - Not installed")
            all_ok = False

    return all_ok


def generate_matrix_data():
    import numpy as np # numpy

    x = np.arange(1000)
    y = np.random.normal(0, 1, 1000)

    return x, y


def analyze_data():
    import pandas as pd

    x, y = generate_matrix_data()

    print("\nAnalyzing Matrix data...")
    print(f"Processing {len(x)} data points...")

    df = pd.DataFrame({
        "index": x,
        "matrix_signal": y
    })

    mean_value = df["matrix_signal"].mean()
    std_value = df["matrix_signal"].std()

    print(f"Mean signal: {mean_value:.4f}")
    print(f"Std deviation: {std_value:.4f}")

    return df


def create_visualization(df):
    import matplotlib.pyplot as plt

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
    all_ok = show_dependency_status()

    if not all_ok:
        print("\nMissing required dependencies.")
        print("Install with pip:")
        print("pip install -r requirements.txt")
        print("\nOr install with Poetry:")
        print("poetry install")
        return

    df = analyze_data()
    create_visualization(df)


if __name__ == "__main__":
    main()
