import os
import pathlib as plb
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

# Remove !.env from .gitignore
with plb.Path(".gitignore").open("r") as f:
    content = f.read()
    
content = (
    content
    .replace("!.env", "")
    .replace("### Replace in post hook", "")
    .strip()
)

with plb.Path(".gitignore").open("w") as f:
    f.write(content)
