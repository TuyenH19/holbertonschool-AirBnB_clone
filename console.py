#!/usr/bin/python3
"""Module Console"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Create class HBNB"""
    prompt = "(hbnb) "  # set the command prompt

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line + ENTER is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
