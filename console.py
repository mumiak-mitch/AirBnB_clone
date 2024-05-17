#!/usr/bin/python3
import cmd

print(dir(cmd.Cmd))

class ConsoleCommands(cmd.Cmd):
    #customizing the prompt
    prompt = "airbnbclone($) "

    #exiting the command interpreter
    def do_quit(self, arg):
        """This exists the command interpreter"""
        return True
    
    #aliasing
    do_exit = do_quit

ConsoleCommands().cmdloop()