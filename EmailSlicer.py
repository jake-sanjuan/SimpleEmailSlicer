"""
This program is meant to slice an email and return the username and domain name.
This functionality is contained in class EmailSlicer.

classes
-------
EmailSlicer; slices email

Functions
--------
main(); creates object and loops until user tells program to stop
"""

class EmailSlicer:
    """
    Class EmailSlicer

    Slices emails and returns username and domain name

    Attributes
    --------
    self.email; user input email address

    Methods
    -------
    __init__; Initializes self.email instance variable, calls method splitEmail()
    splitEmail; Splits email by '@' char, prints username and domain name
    """

    def __init__(self):
        self.email = input("Please enter an email address to separate. ")
        self.splitEmail()

    def splitEmail(self):
        """
        Method splitEmail

        This method splits the user input string self.email into two elements in
        a list.  Uses list slicing to get userName and domainName, prints these
        values to the user

        Exceptions
        ---------
        Catches IndexError exception. This will happen anytime text without or
        with more than one '@' is entered.

        :return:
        No return statement
        """
        try:
            splitEmailList = self.email.split('@')
            userName = splitEmailList[0]
            domainName = splitEmailList[1]
            print("User name: ", userName + "\n" + "Domain name: ", domainName)
        except IndexError:
            print("Please enter a valid email to be split!")


def main():
    """
    Creates EmailSlicer object, loops until user enters 'n' to stop loop
    :return:
    No return statement
    """
    while True:
        EmailSlicer()
        goAgain = input("Do you have another email to split? (y / n) ")
        if goAgain == 'n':
            exit(0)


if __name__ == '__main__':
    main()


