file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")
merged_file = input("Enter name for merged file: ")

try:
    with open(file1, "r") as f1, open(file2, "r") as f2, open(merged_file, "w") as out:
        out.write(f1.read())
        out.write("\n")          # optional separator
        out.write(f2.read())
    print(f"Files merged successfully into '{merged_file}'")
except FileNotFoundError:
    print("One or both input files not found!")
