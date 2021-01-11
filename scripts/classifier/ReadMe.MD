# Automatic classifier for commits which improve nonfunctional properties.

The reproduce file contains all code for using the classifier along with documentation for other classification techniques.

The autominer.py file contains a scripts to randomly select repositories and mine them for NFP improving commits. The first time the file is run it will train the classifier, and then pickle it for use in future runs to save time.