# 1.Download rockyou file
# 2.Create variable `results = []`
# 3.On each line of the file you check if the "user" word exists in the line
# 4.User decides (based on the input) if he wants to add it to the results
# 5.After the file reading is finished app returns the results and the
# amount of added lines

from pathlib import Path

THIS_FILE = Path(__file__).absolute()
ROOT_DIR = THIS_FILE.parent

# Example 5: Search for the word "user" in each line of the "rockyou.txt" file
file = open(ROOT_DIR / "rockyou.txt")
results = []

while True:
    try:
        line = file.readline()

        if not line:
            break

        # Check if the word 'user' exists in the line
        if "user" in line:
            print(f"Found 'user' in: {line.strip()}")
            decision = input(
                "Do you want to add this to results? (yes/no): "
            ).lower()
            # If user decides to add it, append it to results list
            if decision == "yes":
                results.append(line.strip())

    except Exception:
        break

file.close()

# After finishing reading the file, print results and the number of added lines
print("\nResults:")
for line in results:
    print(line)

print(f"\nTotal added lines: {len(results)}")
# max is Total added lines: 1519
