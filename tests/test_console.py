#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
import os

from console import CommandInterpreter

class TestCommandInterpreter(unittest.TestCase):
    """
    TestCommandInterpreter class contains unit tests for the CommandInterpreter class.
    """

    def setUp(self):
        """
        Set up method to prepare for each test case.
        """
        self.cmd_interpreter = CommandInterpreter()

    def test_quit(self):
        """
        Test the quit command.
        """
        self.assertTrue(self.cmd_interpreter.do_quit(None))

    def test_pwd(self):
        """
        Test the pwd command.
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd_interpreter.do_pwd(None)
            self.assertEqual(fake_out.getvalue().strip(), os.getcwd())

    def test_ls(self):
        """
        Test the ls command.
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd_interpreter.do_ls(None)

    def test_cd(self):
        """
        Test the cd command.
        """
        initial_dir = os.getcwd()
        test_dir = "/tmp"
        self.cmd_interpreter.do_cd(test_dir)
        self.assertEqual(os.getcwd(), test_dir)
        self.assertTrue(self.cmd_interpreter.prompt.startswith(test_dir))

        with patch('builtins.print') as mock_print:
            self.cmd_interpreter.do_cd("/nonexistent")
            mock_print.assert_called_with("Directory not found:", "/nonexistent")

    def test_clear(self):
        """
        Test the clear command.
        """
        pass

if __name__ == '__main__':
    unittest.main()
