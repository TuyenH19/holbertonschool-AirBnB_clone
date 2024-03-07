#!/usr/bin/python3
"""Module Console"""
import cmd
import sys
import models
import shlex
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Create class HBNB"""
    prompt = "(hbnb) "  # set the command prompt

    classes = {'BaseModel': BaseModel}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line + ENTER is entered"""
        pass

    def do_create(self, arg):
        """Usage: create <class>
        Creates a new class instance of BaseModel, saves it to the JSON file
        and prints its id
        """
        if arg:
            if arg in self.classes:
                # instance = models.base_model.BaseModel()
                get_class = getattr(sys.modules[__name__], arg)
                instance = get_class()
                print(instance.id)
                instance.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return

    def do_show(self, arg):
        """string representation based on the class name and id
        """
        tokens = shlex.split(arg)
        if len(tokens) == 0:
            print("** class name missing **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        elif tokens[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            dic = models.storage.all()
            # Key has format <className>.id
            keyU = tokens[0] + '.' + str(tokens[1])
            if keyU in dic:
                print(dic[keyU])
            else:
                print("** no instance found **")
        return

    def do_destroy(self, argument):
        """Deletes an instance based on the class name and id"""
        tokensD = shlex.split(argument)
        if len(tokensD) == 0:
            print("** class name missing **")
            return
        elif len(tokensD) == 1:
            print("** instance id missing **")
            return
        elif tokensD[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            dic = models.storage.all()
            # Key has format <className>.id
            key = tokensD[0] + '.' + tokensD[1]
            if key in dic:
                del dic[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, argument):
        """all string representation of all instances"""
        tokensA = shlex.split(argument)
        listI = []
        dic = models.storage.all()
        # show all if no class is passed
        if len(tokensA) == 0:
            for key in dic:
                representation_Class = str(dic[key])
                listI.append(representation_Class)
            # if listI:
            print(listI)
            return

        if tokensA[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            # Representation for a specific class
            representation_Class = ""
            for key in dic:
                className = key.split('.')
                if className[0] == tokensA[0]:
                    # This form doesn't work
                    # listI.append(dic[key])
                    representation_Class = str(dic[key])
                    listI.append(representation_Class)
            # if listI:
            print(listI)

    def do_update(self, argument):
        """Updates an instance based on the class name and id """
        tokensU = shlex.split(argument)
        if len(tokensU) == 0:
            print("** class name missing **")
            return
        elif len(tokensU) == 1:
            print("** instance id missing **")
            return
        elif len(tokensU) == 2:
            print("** attribute name missing **")
            return
        elif len(tokensU) == 3:
            print("** value missing **")
            return
        elif tokensU[0] not in self.classes:
            print("** class doesn't exist **")
            return
        keyI = tokensU[0] + "." + tokensU[1]
        dicI = models.storage.all()
        try:
            instanceU = dicI[keyI]
        except KeyError:
            print("** no instance found **")
            return
        try:
            typeA = type(getattr(instanceU, tokensU[2]))
            tokensU[3] = typeA(tokensU[3])
        except AttributeError:
            pass
        setattr(instanceU, tokensU[2], tokensU[3])
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
