# TINY_Language_Scanner_Parser

Build & Run Steps:
(1) Install "Anaconda Individual Edition" from 
        https://www.anaconda.com/products/individual
(2) Open Anaconda Prompt
(3) Check the Conda version in the Anaconda Prompt using command
        conda --version
(4) Check the Python version in the Anaconda Prompt using command
        python --version
(5) Create a python virtual environment in the Anaconda Prompt using command
        conda create -n <yourenvname> python=x.x anaconda
            NOTE:
                Replace <yourenvname> with the name of your environment
                Replace x.x with the version of python from step (4)
(6) Activate the python virtual environment in the Anaconda Prompt using command
        activate <yourenvname>
            NOTE:
              Replace <yourenvname> with the name of your environment
(7) Install the graphviz Library in the Anaconda Prompt using command
         conda install graphviz
(8) Install the python-graphviz Library in the Anaconda Prompt using command
         conda install python-graphviz
(9) Install the pydot Library in the Anaconda Prompt using command
         conda install pydot
(10) Open Pycharm
(11) Create New Project and use the virtual environment you created using the Anaconda Prompt as follows:
         >> Expand Python Interpreter
         >> Choose Previously configured interpreter
         >> Browse for Paths
         >> Choose a path that resembles this path:
                  C:\Users\hp\anaconda3\envs\<yourenvname>\python.exe
(12) Create the three .py files & copy their content from here
         (1) main.py
         (2) Scanner.py
         (3) Parser.py
(13) Run main.py

Input:
{ Sample program in TINY language – computes factorial }
     read x;   {input an integer }
     if  0 < x   then     {  don’t compute if x <= 0 }
        fact  := 1;
        repeat 
           fact  := fact *  x;
            x  := x  -  1
        until  x  =  0;
        write  fact   {  output  factorial of x }
     end
Output:
Scanner Output:

![ScannerOutput](https://user-images.githubusercontent.com/73910634/146786523-5025f40e-1d17-4d0b-a6a8-55cc9ad85b4c.PNG)

Parser Output:
![Parse_Tree gv](https://user-images.githubusercontent.com/73910634/146785255-c2abf8c8-72b8-4762-97ee-6145ef5bc82e.png)


