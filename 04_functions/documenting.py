# ----------------------------------------------------
#   DOCUMENTING THE FUNCTIIONS AND BUILT-IN FUNCTIONS
# ----------------------------------------------------

def chai_flavour():
    """
    This function returns the chai flavour
    we can also provide info about the arguments it accepts .
    this should always be the first line.
    """
    return "Ginger chai"

print("DOC:",chai_flavour.__doc__)

print("HELP:",help(chai_flavour))

print("NAME:",chai_flavour.__name__)

# output:
# DOC: 
#     This function returns the chai flavour
    
# Help on function chai_flavour in module __main__:

# chai_flavour()
#     This function returns the chai flavour

# HELP: None
# NAME: chai_flavour