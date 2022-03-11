# StaticAnalyzerTool
QA StaticAnalyzerTool project 1  
description : 
tool written in python that reads c++ source code and try to detect Logical Errors such as <br>
* Unreachable code
* Magic number
* Do the attributes
* more than three parameters

Team members : 
* Mohamad Nasser
* Yaseen Asaliya
* Motaz Hashhoush

# Working principle: 
* <b>Data reading and Tokens</b> <sup>Mohamad Nasser</sup> <br>
      read the c++ source code from .txt file and then use tokizing logic
      <br> to give each line a token to his state 
      for example : 
      <code>
        int x = 5; //will get Declaration token 
      </code>
* <b>Unreachable code</b> <sup>Mohamad Nasser</sup> <br>
      the code detect the line that contains <code> return  </code> statment
      <br> and then see all possibiltes to this return such as <br>
      alone return without if <br>
       inside if <br>
      
      also the code can detect the unreachable lines cused by similar nested if stetments 

* <b>Magic number/string</b> <sup>Yaseen Asaliya</sup>
     <br>the code detect all line that contain number or string such as : 
     <code> 
        if(x == -1)       
        return "str"
      </code> 
      ,and it will <br>
     be check the magic value if it not initial value for a variable <br>
     for example or any case that apply the magic number it will be stored <br>
     in result list to print it later.

* <b>Do the attributes</b> <sup>Motaz Hashhoush</sup> <br>
The order of the data type is checked in each prototype function and the order should be like this : <code> integer, string, character </code>. <br>
It also checks the values that are sent when this function is called so that they must be on the same data type parameters as in the function.  <br>
Example. we have this prototype function <code> bool Check( int status, string name, char startChar) </code> <br>
and we have the call of this function <code> Check(1.5, 'D', "Data");</code> the call violates the data type standards in the function .


* <b> more than three parameters </b> <sup>Motaz Hashhoush</sup> <br>
Each function must contain no more than three parameters, <br> 
that's why we check the number of parameters by the number of commas "," <br>
if the number of commas is equal to two, then this means that we have three parameters, <br>
and if the number of commas is greater than two, this indicates that we have more than three parameters and it is not permissible .


</br>

see distribution of tasks <a href="https://mud-risk-c1e.notion.site/QA-Group-Assignment-06463ee5c72949329cd49fb9b35ee095"> Tasks </a> <br>
see how to run our project <a href="https://drive.google.com/file/d/1pUA7daW0g4ycnZjtk4R5xDUQFl10LIEx/view?usp=sharing"> Run </a>
