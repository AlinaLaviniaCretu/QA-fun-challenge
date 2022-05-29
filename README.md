# QA automation challenge

This mini-project contains the following files:

- **my_program.py** 
  
  Contains the python methods used for:
  
     - Opening and parsing the input file
     - Extracting the data from the XML: the GCP ids, GCP coordinates, GCP ids that can be found in images
     - Computing the area covered by the GCP points
     - Creating a file (if it does not exist) and writing the number of GCP points, the area covered by them and for each of the GCPs in how many images it can be seen.


- **example.p4d**
  
  - Contains the input data structured in an XML format


- **output.txt**
  
  - Is the file produced after running the program and contains the requested information: number of GCP points, the area covered by them and for each of the GCPs in how many images it can be seen.
## Prerequisites
- Python version equal or greater than 3.8


## Installation

1. Create a python virtual environment.
2. Change the work dir to the root directory of the venv.
3. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install _shapely_ package.

```bash
pip install shapely
```


## Usage
1. Change the work dir to the root directory of the virtual environment.
2. Use the following command to run the program:

```bash
python my_program.py example.p4d output.txt
```

## Assumptions
- Input data is structured in an XML format