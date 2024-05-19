#!/usr/bin/python3
import cmd
import os

class ConsoleCommands(cmd.Cmd):
    # Customizing the prompt
    prompt = "airbnbclone($) "

    # Exiting the command interpreter
    def do_quit(self, arg):
        """Exit the command interpreter"""
        return True

    # Alias for quit command
    do_exit = do_quit

    # Command to list all available commands
    def do_help(self, arg):
        """List available commands"""
        super().do_help(arg)

    # Command to greet the user
    def do_hello(self, arg):
        """Greet the user"""
        if arg:
            print("Hello, {}!".format(arg))
        else:
            print("Hello!")

    # Command to calculate the square of a number
    def do_square(self, arg):
        """Calculate the square of a number"""
        try:
            num = float(arg)
            print("Square of {} is {}".format(num, num ** 2))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Command to add two numbers
    def do_add(self, arg):
        """Add two numbers"""
        try:
            nums = list(map(float, arg.split()))
            if len(nums) != 2:
                raise ValueError
            result = sum(nums)
            print("Sum of {} and {} is {}".format(nums[0], nums[1], result))
        except ValueError:
            print("Invalid input. Please enter two valid numbers separated by space.")

    # Command to display current prompt
    def do_prompt(self, arg):
        """Display current prompt"""
        print("Current prompt: {}".format(self.prompt))

    # Command to change prompt
    def do_changeprompt(self, arg):
        """Change prompt"""
        if arg:
            self.prompt = arg.strip() + " "
            print("Prompt changed to '{}'".format(self.prompt))
        else:
            print("Please provide a new prompt.")

    # Command to display current directory
    def do_pwd(self, arg):
        """Print the current working directory"""
        import os
        print(os.getcwd())

    # Command to list files in the directory
    def do_ls(self, arg):
        """List files in the current directory"""
        files = os.listdir('.')
        for file in files:
            print(file)

    # Command to change directory
    def do_cd(self, arg):
        """Change current directory"""
        try:
            os.chdir(arg)
            print("Directory changed to '{}'".format(os.getcwd()))
        except FileNotFoundError:
            print("Directory '{}' not found".format(arg))

    # Command to create a new directory
    def do_mkdir(self, arg):
        """Create a new directory"""
        try:
            os.mkdir(arg)
            print("Directory '{}' created".format(arg))
        except FileExistsError:
            print("Directory '{}' already exists".format(arg))

    # Command to remove a directory
    def do_rmdir(self, arg):
        """Remove a directory"""
        try:
            os.rmdir(arg)
            print("Directory '{}' removed".format(arg))
        except FileNotFoundError:
            print("Directory '{}' not found".format(arg))
        except OSError as e:
            print(e)

    # Command to print file content
    def do_cat(self, arg):
        """Print the contents of a file"""
        try:
            with open(arg, 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("File '{}' not found".format(arg))

    # Command to create a new file
    def do_touch(self, arg):
        """Create a new file"""
        try:
            with open(arg, 'a'):
                pass
            print("File '{}' created".format(arg))
        except FileExistsError:
            print("File '{}' already exists".format(arg))

    # Command to remove a file
    def do_rm(self, arg):
        """Remove a file"""
        try:
            os.remove(arg)
            print("File '{}' removed".format(arg))
        except FileNotFoundError:
            print("File '{}' not found".format(arg))

    # Command to display environment variables
    def do_env(self, arg):
        """Display environment variables"""
        for key, value in os.environ.items():
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    ConsoleCommands().cmdloop()
