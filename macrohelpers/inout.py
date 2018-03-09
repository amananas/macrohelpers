"""
This module provides helpers and macros for input/output and debug interfaces.
"""

import sys


class BashColors:
    """ Bash color equivalents. """
    LIGHTPURPLE = '\033[95m'
    LIGHTBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNINGYELLOW = '\033[93m'
    FAILRED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERL = '\033[4m'

class Output:
    """ Output and debug related macros. """

    def __init__(self,
                 debugFileName=None):
        """ Constructor... """
        self._debugFile = None
        if debugFileName:
            self._debugFile = open(debugFileName, 'w')
            if not self._debugFile:
                self.printerr('Error encountered while trying to open debug file ' + debugFileName)
                sys.exit(1)
        self._ok = BashColors.OKGREEN
        self._warn = BashColors.WARNINGYELLOW
        self._err = BashColors.FAILRED
        self._crit = BashColors.FAILRED + BashColors.BOLD + BashColors.UNDERL

    def cleanup(self):
        """ Destructor... """
        if self._debugFile:
            self._debugFile.close()

    def print(self, message, ending='\n'):
        """ Print in debug file and on stdout without formatting. """
        if self._debugFile:
            self._debugFile.write(message + ending)
        sys.stdout.write(message + ending)

    def printok(self, message, ending='\n'):
        """ Print in debug file and on stdout with ok formatting. """
        if self._debugFile:
            self._debugFile.write(message + ending)
        sys.stdout.write(self._ok + message + ending + BashColors.ENDC)

    def printwarn(self, message, ending='\n'):
        """ Print in debug file and on stdout with warning formatting. """
        if self._debugFile:
            self._debugFile.write(message + ending)
        sys.stdout.write(self._warn + message + ending + BashColors.ENDC)

    def printerr(self, message, ending='\n'):
        """ Print in debug file and on stdout with error formatting. """
        if self._debugFile:
            self._debugFile.write(message + ending)
        sys.stdout.write(self._err + message + ending + BashColors.ENDC)

    def printcrit(self, message, ending='\n'):
        """ Print in debug file and on stdout with critical error formatting. """
        if self._debugFile:
            self._debugFile.write(message + ending)
        sys.stdout.write(self._crit + message + ending + BashColors.ENDC)

    def debug(self, message, ending='\n'):
        """ Print in debug file only. """
        if self._debugFile:
            self._debugFile.write(message + ending)

    def setOkColor(self, color):
        """ Sets the ok color. """
        self._ok = color

    def setWarnColor(self, color):
        """ Sets the warning color. """
        self._warn = color

    def setErrColor(self, color):
        """ Sets the error color. """
        self._err = color

    def setCritColor(self, color):
        """ Sets the critical error color. """
        self._crit = color

def offerChoice(message='', default=None, forceAnswer=False, color=''):
    """
    Offers a choice to the user, result is True or False,
    or may be None if no answer is provided.
    """
    offer = color + message
    if default is True:
        offer = offer + ' (Y/n): '
    elif default is False:
        offer = offer + ' (y/N): '
    else:
        offer = offer + ' (y/n): '

    while True:
        sys.stdout.write(offer + BashColors.ENDC)
        answer = input().rstrip()
        if answer == 'y' or answer == 'Y':
            return True
        if answer == 'n' or answer == 'N':
            return False
        if default != None:
            return default
        if not forceAnswer:
            return None
