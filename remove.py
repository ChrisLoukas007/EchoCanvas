import pandas as pd

# Filepath to the CSV file
file_path = "/Users/chrisloukasntais/VsCode/EchoCanvas/human_easy.csv"

# Load the CSV file
df = pd.read_csv(file_path)

# Get unique values in the "subject" column
unique_subjects = df["subject"].unique()

# Print the number of unique values and the values themselves
print(f"Number of unique values in 'subject': {len(unique_subjects)}")
print("Unique values in 'subject':")
print(unique_subjects)


# Save the updated CSV file
df.to_csv(file_path, index=False)

print("It happened successfully.")