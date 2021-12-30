"""
Invoker
"""
from collections import deque
from icommand import ICommand


class Invoker():
    """Command invoker class"""

    def __init__(self):
        self._stack = deque(maxlen=3)
        self._unexecute_stack = deque(maxlen=3)

    def add_command(self, *command: ICommand):
        """Adding command(s) to stack"""
        self._stack.extend(command)

    def execute_command(self):
        """Executing commands from main stack and adding the command to undo stack"""
        if not self._stack:
            return
        command: ICommand = self._stack.pop()
        command.execute()
        self._unexecute_stack.append(command)

    def unexecute_command(self):
        """Executing commands from undo stack and adding the command to main stack"""
        if not self._unexecute_stack:
            return
        command: ICommand = self._unexecute_stack.pop()
        command.unexecute()
        self._stack.append(command)

    def __str__(self):
        return 'stack: ' + str(self._stack) + '\n undo: ' + str(self._unexecute_stack)
