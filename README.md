# This is a Python repository with Continuous Integration using Github Actions 

[![Python CI](https://github.com/DivyaSharma0795/Basic_Python_Repository/actions/workflows/main.yml/badge.svg)](https://github.com/DivyaSharma0795/Basic_Python_Repository/actions/workflows/main.yml)
[![Black Formatter](https://github.com/nogibjj/DukeIDS706_ds655_IndividualProject01/actions/workflows/BlackFormatter.yml/badge.svg)](https://github.com/nogibjj/DukeIDS706_ds655_IndividualProject01/actions/workflows/BlackFormatter.yml)
[![Install](https://github.com/nogibjj/DukeIDS706_ds655_IndividualProject01/actions/workflows/Install.yml/badge.svg)](https://github.com/nogibjj/DukeIDS706_ds655_IndividualProject01/actions/workflows/Install.yml)
[![Lint](https://github.com/nogibjj/DukeIDS706_ds655_IndividualProject01/actions/workflows/RuffLint.yml/badge.svg)](https://github.com/nogibjj/DukeIDS706_ds655_IndividualProject01/actions/workflows/RuffLint.yml)

Please follow this [link]() to see a video demonstrating this repository and the files in it.

Files in this repository include:

## 1. Readme
  The `README.md` file is a markdown file that contains basic information about the repository, what files it contains, and how to consume them


## 2. Requirements
  The `requirements.txt` file has a list of packages to be installed for any required project. Currently, my requirements file contains some basic python packages.


## 3. Codes
  This folder contains all the code files used in this repository - the files named "Test_" will be used for testing and the remaining will define certain functions
  -  The `Pandas_Notebook.ipynb` contains codes in a jupyter iPython Notebook
  -  The `lib.py` file contains common codes for python and Jupyter files
  -  The `test_graph.ipynb` file is a jupyter notebook to generate the chart using jupyter
  -  The `test_lib.py` contains test codes for the lib.py file


## 4. Resources
  -  This folder contains any other files relevant to this project. Currently, I have added -


## 5. Outputs
This folder contains the output files relevant to this project. Currently, these include -
  -  `PlotImage.png` - This file contains a png of the graph generated
  -  `Summary.md` - This is a markdown file with summary statistics


## 6. CI/CD Automation Files


  ### 6(a). Makefile
  The `Makefile` contains instructions for installing packages (specified in `requirements.txt`), formatting the code (using black formatting), testing the code (running all the sample python code files starting with the term *'Check...'* ), and linting the code using pylint


  ### 6(b). Github Actions
  Github Actions uses 4 different YML files to call the functions defined in the Makefile based on triggers such as push or pull. Currently, every time a change is pushed onto the repository, it runs the install packages, formatting the code, linting the code, and then testing the code functions
    -  `main.yml`
    -  `Install.yml`
    -  `RuffLint.yml`
    -  `BlackFormatter.yml`


  ### 6(c). Devcontainer
  The `.devcontainer` folder mainly contains two files - 
    * `Dockerfile` defines the environment variables - essentially it ensures that all collaborators using the repository are working on the same environment to avoid conflicts and version mismatch issues
    * `devcontainer.json` is a json file that specifies the environment variables including the installed extensions in the virtual environment
