import tkinter as tk

class SimpleInterpreterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Command Interpreter")

        # Set the background color to black
        self.root.configure(bg="black")
        
        self.text_entry = tk.Entry(root, width=40, bg="black", fg="white")  # Set entry colors
        self.execute_button = tk.Button(root, text="Execute", command=self.execute_command, bg="black", fg="white")  # Set button colors
        self.output_text = tk.Text(root, height=10, width=40, bg="black", fg="white")  # Set text area colors

        self.text_entry.pack(pady=10)
        self.execute_button.pack()
        self.output_text.pack(padx=10, pady=5)


        
    def execute_command(self):
        command = self.text_entry.get()
        self.text_entry.delete(0, tk.END)  # Clear the input field

        # Execute the command and update the output
        output = self.interpret_command(command)
        self.output_text.insert(tk.END, output + "\n")
    
    def interpret_command(self, command):
        # Change text color to green if the command is "print"
        if command.startswith("print"):
            self.text_entry.config(fg="green")  # Set text color to green
            message = command[6:].strip()
            return message  # Return the message to be printed
        elif command.startswith("warn"):
            self.text_entry.config(fg="orange")  # Set text color to orange for warnings
            message = command[5:].strip()
            return f"Warning: {message}"
        elif command.startswith("error"):
            self.text_entry.config(fg="red")  # Set text color to red for errors
            message = command[7:].strip()  # Adjust the index to exclude the ' character
            return f"Error: {message}"
        else:
            self.text_entry.config(fg="black")  # Reset text color to black
            return "Invalid command"

        parts = command.split(" ")
        if len(parts) >= 4 and parts[1] == "define" and parts[2] == "variable":
            variable_name = parts[0]
            variable_value = " ".join(parts[4:])
            self.variables[variable_name] = variable_value
            return f"Variable {variable_name} defined with value: {variable_value}"
        elif parts[0] in self.variables:
            return str(self.variables[parts[0]])
        elif parts[0] == "run":
            os.system(" ".join(parts[1:]))  # Execute the system command after "run"
            return "System command executed"
        else:
            return "Invalid command"
# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleInterpreterGUI(root)
    root.mainloop()



