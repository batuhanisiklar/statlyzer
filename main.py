import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate arithmetic mean
def arithmeticMean(data):
    total = 0
    for number in data:
        total = total + number
    return total / len(data)

# Function to calculate median
def median(data):
    sorted_data = sorted(data)
    length = len(sorted_data)
    if length % 2 == 0:
        return (sorted_data[length // 2 - 1] + sorted_data[length // 2]) / 2
    else:
        return sorted_data[length // 2]

# Function to calculate mode
def mode(data):
    count_dict = {}
    for number in data:
        if number not in count_dict:
            count_dict[number] = 0
        count_dict[number] += 1

    most_frequent = []
    max_count = 0
    for number, count in count_dict.items():
        if count > max_count:
            max_count = count
            most_frequent = [number]
        elif count == max_count:
            most_frequent.append(number)

    return most_frequent

# Function to calculate range
def dataRange(data):
    return max(data) - min(data)

# Function to calculate mean absolute deviation
def meanAbsoluteDeviation(data):
    mean = arithmeticMean(data)
    total_abs_deviation = 0
    for number in data:
        total_abs_deviation = total_abs_deviation + abs(mean - number)
    return total_abs_deviation / len(data)

# Function to calculate variance
def variance(data):
    mean = arithmeticMean(data)
    total_squared_diff = 0
    for number in data:
        squared_diff = (number - mean) ** 2
        total_squared_diff = total_squared_diff + squared_diff
    return total_squared_diff / (len(data) - 1)

# Function to calculate standard deviation
def standardDeviation(data):
    return variance(data) ** 0.5

# Function to calculate coefficient of variation
def coefficientOfVariation(data):
    return standardDeviation(data) / arithmeticMean(data)

# Function to calculate interquartile range
def interquartileRange(data):
    sorted_data = sorted(data)
    Q1 = sorted_data[len(sorted_data) // 4]
    Q3 = sorted_data[(len(sorted_data) * 3) // 4]
    return Q3 - Q1

# Function to detect and remove outliers
def detect_outliers(data, column):
    sorted_column = sorted(data[column])
    Q1_index = int(0.25 * len(sorted_column))
    Q3_index = int(0.75 * len(sorted_column))
    Q1 = sorted_column[Q1_index]
    Q3 = sorted_column[Q3_index]
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outlier_rows = []
    for index, number in enumerate(data[column]):
        if number < lower_bound or number > upper_bound:
            outlier_rows.append(index)
    print("Outliers:")
    print(data.iloc[outlier_rows])
    cleaned_data = data.drop(data.index[outlier_rows])
    return cleaned_data

# Function to create boxplot for the data
def createBoxplot(data):
    for column in data.columns:
        plt.figure()
        plt.boxplot(data[column])
        plt.title(f'Boxplot - {column}')
        plt.xticks([1], [column])
    plt.show()

# Function to write statistics to a file
def writeStatistics(data, file):
    for column in data.columns:
        file.write(f"Statistics for column {column}:\n")
        file.write(f"Arithmetic Mean: {arithmeticMean(data[column])}\n")
        file.write(f"Median: {median(data[column])}\n")
        file.write(f"Mode: {mode(data[column])}\n")
        file.write(f"Range: {dataRange(data[column])}\n")
        file.write(f"Mean Absolute Deviation: {meanAbsoluteDeviation(data[column])}\n")
        file.write(f"Variance: {variance(data[column])}\n")
        file.write(f"Standard Deviation: {standardDeviation(data[column])}\n")
        file.write(f"Coefficient of Variation: {coefficientOfVariation(data[column])}\n")
        file.write(f"Interquartile Range: {interquartileRange(data[column])}\n\n")

# Read the dataset
df = pd.read_csv('veri_seti.csv')

# Open the file to write results
file = open('sonuc.txt', 'w')

# Create boxplot
createBoxplot(df)

# Detect and remove outliers for each column
for column in df.columns:
    df = detect_outliers(df, column)

# Write statistics of the cleaned data to the file
writeStatistics(df, file)

# Close the file
file.close()