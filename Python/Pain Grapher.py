import pandas as pd
import matplotlib.pyplot as plt

# Read data from Excel file
excel_file_path = "/Users/ayesha/Desktop/November Pain Index.xlsx"
df = pd.read_excel(excel_file_path, parse_dates=['date'])

# Extract pain type from the 'detail' column
df['pain_type'] = df['detail'].str.extract(r'(\b\w+\b)')

# Create a dictionary to map pain types to colors
colors = {'Shoulder': 'blue', 'Leg': 'green', 'Back': 'red', 'Generalised': 'purple'}

# Create a new column 'color' based on the 'pain_type'
df['color'] = df['pain_type'].map(colors)

# Create a pivot table for plotting
pivot_table = df.pivot_table(index=['date', 'time of day'], columns='pain_type', values='rating', aggfunc='mean')

# Plot the data in separate subplots for each pain type
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10), sharex=True)

for ax, (pain_type, color) in zip(axes.flatten(), colors.items()):
    ax.bar(
        pivot_table.index.get_level_values('date'),
        pivot_table[pain_type],
        label=f'{pain_type} Pain',
        color=color,
        alpha=0.7,  # Adjust transparency
    )
    ax.set_title(f'{pain_type} Pain')
    ax.set_ylabel('Pain Severity')
    ax.legend()
    ax.grid(True)

# Customize the overall plot
plt.suptitle('Pain Severity Over Time', y=1.02)
plt.xlabel('Date')

# Adjust layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()