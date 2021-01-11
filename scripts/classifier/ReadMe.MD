# Automatic classifier for commits which improve nonfunctional properties.

The reproduce file contains all code for using the classifier along with documentation for other classification techniques.

The autominer.py file contains a scripts to randomly select repositories and mine them for NFP improving commits.

A pretrained version is provided in the pickle file which is used by the automine file.

In order to retriain the classifier the commit messages must be added to the files found in the data directory data, they can be found by searching github or downloading the repo they are from and using the git log command.