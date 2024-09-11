import subprocess

def main():
    while True:
        user_input = input("Enter command (upload or search): ").lower()

        if user_input == "upload" or user_input == "search":
            if user_input == "upload":
                subprocess.run(["python", "upload_files.py"])
            elif user_input == "search":
                subprocess.run(["python", "vector_search_files.py"])

            break
        else:
            print("Invalid input. Please enter upload or search.")

if __name__ == "__main__":
    main()