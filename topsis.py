import sys
import pandas as pd
import numpy as np


def topsis(input_file, weights, impacts, output_file):

    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print("Error: File not found")
        sys.exit(1)

    if data.shape[1] < 3:
        print("Error: Input file must have at least 3 columns")
        sys.exit(1)

    matrix = data.iloc[:, 1:].values

    if not np.issubdtype(matrix.dtype, np.number):
        print("Error: Non-numeric values found")
        sys.exit(1)

    weights = list(map(float, weights.split(',')))
    impacts = impacts.split(',')

    n_cols = matrix.shape[1]

    if len(weights) != n_cols or len(impacts) != n_cols:
        print("Error: Number of weights, impacts and columns must be same")
        sys.exit(1)

    for i in impacts:
        if i not in ['+', '-']:
            print("Error: Impacts must be + or -")
            sys.exit(1)

    norm = np.sqrt((matrix ** 2).sum(axis=0))
    matrix = matrix / norm

    matrix = matrix * weights

    ideal_best = []
    ideal_worst = []

    for i in range(n_cols):
        if impacts[i] == '+':
            ideal_best.append(matrix[:, i].max())
            ideal_worst.append(matrix[:, i].min())
        else:
            ideal_best.append(matrix[:, i].min())
            ideal_worst.append(matrix[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((matrix - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((matrix - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)

    rank = score.argsort()[::-1] + 1

    data["Topsis Score"] = score
    data["Rank"] = rank

    data.to_csv(output_file, index=False)

    print("TOPSIS completed successfully!")
    print("Output saved in:", output_file)


if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage:")
        print("python topsis.py <InputFile> <Weights> <Impacts> <OutputFile>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    topsis(input_file, weights, impacts, output_file)
