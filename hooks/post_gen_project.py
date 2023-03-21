import os
import shutil

##############################################################################
# Utilities
##############################################################################


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


##############################################################################
# Cookiecutter clean-up
##############################################################################

# Directive flags
no_license = "{{cookiecutter.open_source_license}}" == "None"

# Remove license (if specified)
if no_license:
    remove("LICENSE")
