import json
import random

# Load your existing training data
with open("train_data.json", "r", encoding="utf-8") as f:
    training_data = json.load(f)

# Set the random seed for reproducibility
random.seed(42)

# Split the data into training and dev sets (80% train, 20% dev)
train_size = int(0.8 * len(training_data))  # 80% for training
dev_size = len(training_data) - train_size  # 20% for development

# Shuffle the data randomly
random.shuffle(training_data)

# Split the data
train_data = training_data[:train_size]
dev_data = training_data[train_size:]

# Save the dev set to a new JSON file
with open("dev_data.json", "w", encoding="utf-8") as f:
    json.dump(dev_data, f, ensure_ascii=False, indent=4)

# Optionally, save the train data if needed (for confirmation or later use)
with open("train_data_split.json", "w", encoding="utf-8") as f:
    json.dump(train_data, f, ensure_ascii=False, indent=4)

print(f"Data split: {len(train_data)} training examples and {len(dev_data)} development examples.")
