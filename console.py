#!/usr/bin/python3
import cmd
import os

class CommandInterpreter(cmd.Cmd):
    """
    CommandInterpreter class implements a simple command-line interpreter
    with basic commands for navigating the file system.

    Attributes:
        prompt (str): Prompt for the interpreter, displays current directory.
    """

    def __init__(self):
        """
        Initializes the CommandInterpreter class.
        """
        super().__init__()
        self.update_prompt()

    def update_prompt(self):
        """
        Updates the prompt with the current working directory.
        """
        self.prompt = f"{os.getcwd()}$ "

    def do_quit(self, arg):
        """
        Command to quit the interpreter.

        Returns:
            bool: True to exit the interpreter.
        """
        return True
    
    # Alias for quit
    do_exit = do_quit

    def help_quit(self, args):
        """
        Provides help information for the quit command.
        """
        print("Quit command to exit the program.")

    def do_EOF(self, args):
        """
        Handles the end of file (EOF) condition.

        Returns:
            bool: True to exit the interpreter.
        """
        print()
        return True

    def do_pwd(self, arg):
        """
        Command to print current working directory.
        """
        print(os.getcwd())

    def do_ls(self, arg):
        """
        Command to list files in the current directory.
        """
        files = os.listdir('.')
        for file in files:
            print(file)

    def do_cd(self, arg):
        """
        Command to change current working directory.

        Args:
            arg (str): The directory to change to.
        """
        try:
            os.chdir(arg)
            self.update_prompt()  # Update prompt after changing directory
        except FileNotFoundError:
            print("Directory not found:", arg)
        except PermissionError:
            print("Permission denied for directory:", arg)

    def do_clear(self, arg):
        """
        Command to clear the screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    CommandInterpreter().cmdloop()
