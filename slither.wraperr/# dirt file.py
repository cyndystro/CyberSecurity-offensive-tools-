# dirt file
import pandas as pd
import matplotlib.pyplot as plt

# Read the key log file
data = pd.read_csv('key_log.txt', delimiter=' ', names=['timestamp', 'milliseconds', 'key'])

# Count the frequency of each key
key_counts = data['key'].value_counts()

# Create a bar chart
fig, ax = plt.subplots()
ax.bar(key_counts.index, key_counts.values)
ax.set_xlabel('Key')
ax.set_ylabel('Frequency')
ax.set_title('Frequency of Keystrokes')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()