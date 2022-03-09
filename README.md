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
     <br>the code detect all line that contain number or string ,and it will <br>
     be check the magic value if it not initial value for a variable <br>
     for example or any case that apply the magic number it will be stored <br>
     in result list to print it later.

* <b>Do the attributes</b> <sup>Motaz Hashhoush</sup>


* <b> more than three parameters </b> <sup>Motaz Hashhoush</sup>


</br>

see distribution of tasks <a href="https://mud-risk-c1e.notion.site/QA-Group-Assignment-06463ee5c72949329cd49fb9b35ee095"> tasks </a>
