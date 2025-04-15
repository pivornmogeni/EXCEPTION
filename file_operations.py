

def read_and_modify_file():
   
    while True:
        input_filename = input(" input.txt ")
        output_filename = input("output.txt")
        
        try:
            # Read from the input file
            with open(input_filename, 'r') as input_file:
                lines = input_file.readlines()
            
            # Modify the content (add line numbers)
            modified_lines = []
            for i, line in enumerate(lines, 1):
                modified_lines.append(f"{i}. {line}")
            
            # Write to the output file
            with open(output_filename, 'w') as output_file:
                output_file.writelines(modified_lines)
            
            print(f"File successfully modified and saved as {output_filename}!")
            break
            
        except FileNotFoundError:
            print(f"Error: The file '{input_filename}' was not found. Please try again.")
        except IOError:
            print(f"Error: Could not read '{input_filename}' or write to '{output_filename}'. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")


print("=== File Modifier Program ===")
read_and_modify_file()