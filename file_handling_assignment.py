def file_handling():
    try:
        # File Creation
        with open('my_file.txt', 'w') as file:
            file.write("Hello, world!\n")
            file.write("This is a file handling example.\n")
            file.write("Number 1234\n")
        
        print("File created and initial content written successfully.")

        # File Reading and Display
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("\nFile content after initial write:\n")
            print(content)

        # File Appending
        with open('my_file.txt', 'a') as file:
            file.write("Appending another line.\n")
            file.write("Adding yet another line.\n")
            file.write("Final line appended.\n")

        print("\nAdditional lines appended successfully.")

        # File Reading and Display after appending
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("\nFile content after appending:\n")
            print(content)

    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nFile handling operations completed.")

if __name__ == "__main__":
    file_handling()
