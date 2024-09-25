import numpy as np

def calculate(list_of_numbers):
    """
    Calculates various statistical measures of a 3x3 matrix.
    """

    # Check number of elements
    if len(list_of_numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    print("\n\n\n---------- calculating various statistical measures of a 3x3 matrix...")

    # Convert list into 3x3 numpy array
    numpy_array_3x3 = np.array(list_of_numbers).reshape(3, 3)
    print("\n---------- numpy_array_3x3:")
    print(numpy_array_3x3)

    # Calc mean along both axes and flattened matrix
    mean_along_columns = np.mean(numpy_array_3x3, axis=0).tolist()
    mean_along_rows = np.mean(numpy_array_3x3, axis=1).tolist() 
    mean_of_all_elements = np.mean(numpy_array_3x3).tolist()
    print(f"\n---------- mean_along_columns: {mean_along_columns}")
    print(f"\n---------- mean_along_rows: {mean_along_rows}")
    print(f"\n---------- mean_of_all_elements: {mean_of_all_elements}")

    # Calc variance along both axes and flattened matrix
    variance_along_columns = np.var(numpy_array_3x3, axis=0).tolist()
    variance_along_rows = np.var(numpy_array_3x3, axis=1).tolist()
    variance_of_all_elements = np.var(numpy_array_3x3).tolist()
    print(f"\n---------- variance_along_columns: {variance_along_columns}")
    print(f"\n---------- variance_along_rows: {variance_along_rows}")
    print(f"\n---------- variance_of_all_elements: {variance_of_all_elements}")

    # Calc standard deviation along both axes and flattened matrix
    std_dev_along_columns = np.std(numpy_array_3x3, axis=0).tolist()
    std_dev_along_rows = np.std(numpy_array_3x3, axis=1).tolist()
    std_dev_of_all_elements = np.std(numpy_array_3x3).tolist()
    print(f"\n---------- std_dev_along_columns: {std_dev_along_columns}")
    print(f"\n---------- std_dev_along_rows: {std_dev_along_rows}")
    print(f"\n---------- std_dev_of_all_elements: {std_dev_of_all_elements}")

    # Find max along both axes and flattened matrix
    max_along_columns = np.max(numpy_array_3x3, axis=0).tolist()
    max_along_rows = np.max(numpy_array_3x3, axis=1).tolist()
    max_of_all_elements = np.max(numpy_array_3x3).tolist()
    print(f"\n---------- max_along_columns: {max_along_columns}")
    print(f"\n---------- max_along_rows: {max_along_rows}")
    print(f"\n---------- max_of_all_elements: {max_of_all_elements}")

    # Find min along both axes and flattened matrix
    min_along_columns = np.min(numpy_array_3x3, axis=0).tolist()
    min_along_rows = np.min(numpy_array_3x3, axis=1).tolist()
    min_of_all_elements = np.min(numpy_array_3x3).tolist()
    print(f"\n---------- min_along_columns: {min_along_columns}")
    print(f"\n---------- min_along_rows: {min_along_rows}")
    print(f"\n---------- min_of_all_elements: {min_of_all_elements}")

    # Calc sum along both axes and flattened matrix
    sum_along_columns = np.sum(numpy_array_3x3, axis=0).tolist()
    sum_along_rows = np.sum(numpy_array_3x3, axis=1).tolist()
    sum_of_all_elements = np.sum(numpy_array_3x3).tolist()
    print(f"\n---------- sum_along_columns: {sum_along_columns}")
    print(f"\n---------- sum_along_rows: {sum_along_rows}")
    print(f"\n---------- sum_of_all_elements: {sum_of_all_elements}")

    # Create dictionary
    calculations = {
        'mean': [mean_along_columns, mean_along_rows, mean_of_all_elements],
        'variance': [variance_along_columns, variance_along_rows, variance_of_all_elements],
        'standard deviation': [std_dev_along_columns, std_dev_along_rows, std_dev_of_all_elements],
        'max': [max_along_columns, max_along_rows, max_of_all_elements],
        'min': [min_along_columns, min_along_rows, min_of_all_elements],
        'sum': [sum_along_columns, sum_along_rows, sum_of_all_elements]
    }
    print("\n---------- calculations:")
    print(calculations)

    return calculations