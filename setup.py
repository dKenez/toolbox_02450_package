from setuptools import setup, find_packages

setup(
    name='toolbox_02450',
    version='0.1',
    description='A toolbox for course 02450 at DTU',
    author='DTU Course 02450',
    author_email='',
    url='http://www2.imm.dtu.dk/courses/02450/',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
        'numpy',
        'matplotlib',
        'scikit-learn',
        'scipy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
