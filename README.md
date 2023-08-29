# How to package toolbox_02450
Additional boilerplate for packaging the toolbox used in course 02450 at DTU 


## Installation

Create conda environment:

```bash
conda create -n 02450 python=3.11
```

Activate conda environment:

```bash
conda activate 02450
```

Navigate to the repository root, then copy the toolbox_02450 to this folder. Your folder structure should look like this:

```bash
toolbox_02450_package/
├── toolbox_02450/
│   ├── __init__.py
│   └── ...
├── LICENSE
├── README.md
└── setup.py
```

Now build the package:

```bash
python setup.py sdist
```

Install package to environment:

```bash 
pip install ./dist/<REPLACE-WITH-ACTUAL-PACKAGE-NAME>.tar.gz
```

Example:

```bash 
pip install ./dist/toolbox_02450-0.1.tar.gz 
```

## Usage

Check that everything is working:

```python
import toolbox_02450
print(toolbox_02450.__version__)
```

Congratulations, now you can continue with the exercises in the course!


