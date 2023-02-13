# function to snake case a string
def snake_case(string):
    # converting to lower case
    string = string.lower()
    # replacing spaces with underscores
    string = string.replace(" ", "_")
    return string