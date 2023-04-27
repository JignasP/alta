# alta
# Copyright © 2023, Jignas Paturu

import os
import subprocess

a='''
               +@@@@@@@@?    +@@@@@+      ,#@@@@@@@@@@@@; ,%@@@@@@@@
               %@@@  @@@?    ?@@@?:,      +@@@S%@@@?S@@@; :@@@#:#@@@
              ,@@@@  @@@?    S@@@;        %@@@+%@@@+S@@@; *@@@? #@@@
              +@@@%  @@@?   ,#@@@:       ,@@@@:#@@@:S@@@;,S@@@; #@@@
              +???;  @@@?   :@@@#,       +@@@%:@@@#,S@@@;,*??*,,#@@@
                     @@@?   ;@@@S        %@@@+;@@@S,#@@@;      ,#@@@
                     @@@?   *@@@?       :@@@@,*@@@? #@@@;      ,#@@@
                     @@@?   ?@@@+       :???+ ?@@@+ *???:      ;@@@@
                    @@@@?   S@@@;            ,S@@@;           +#@@@@
                  @@@@@@?  ,#@@@:            ,#@@@:         ,?@;#@@@
                 @? *@@@?  :@@@#,   ,:::,    :@@@#,        ,S@: #@@@
               ?@?  *@@@?  +@@@%    S@@@;    +@@@%        ;#@; ,#@@@
             :S@S,  *@@@?  *@@@*    S@@@;    *@@@?       +@@+  ,#@@@
            ;#@#:   *@@@?  %@@@+    S@@@;    %@@@+     ,?@@?   ,#@@@
           +@@@+    *@@@? ,S@@@:    S@@@;   ,S@@@:    ,S@@#,   ,#@@@
          +@@@S,    *@@@? ,@@@#,    S@@@;   ,@@@#,   ,S@@@+    ,#@@@
         ,#@@@;     ?@@@? ;@@@S,    S@@@;   ;@@@S,   +@@@S,    ,#@@@
         ;@@@S      ?@@@? +@@@%     S@@@;   +@@@%    %@@@+     ,#@@@
         ?@@@S???+  ?@@@? ?@@@*  ;??#@@@;   ?@@@*   ,@@@@????: ,#@@@
        ,#@@@@@@@@: ?@@@? S@@@; ;@@@@@@@;   S@@@;   +@@@@@@@@S ,#@@@
        +@@@@@@@@@% ?@@@?,#@@@,,#@@@@@@@;  ,#@@@:   %@@@@@@@@@;,#@@@
        %@@@@@@@@@@;?@@@?,@@@#:S@@@@@@@@;  :@@@#,  :@@@@@@@@@@S:@@@@
        @@@@@@@@@@@@@@@@+:@@@@@@@@@@@@@@:  ;@@@%   +@@@@@@@@@@@@@@@@'''

print('\033[0;32m ',a ,'\033[0;0m' )
print("")
print('\033[0;31m Copyright © 2023, Jignas Paturu\033[0;0m'.center(100) )
print('\033[0;31m github.com/JignasP\033[0;0m'.center(100) )


def win():

    result = subprocess.run(["powershell", "Get-ExecutionPolicy"], capture_output=True, text=True)
    result = (str(result))[83:-15]

    if(result=='Restricted' or result=='Undefined'):
        link="https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.3"
        print('\033[0;37;41m Error:Execution Policy:',result,'\033[0;0m')
        print('\033[0;37;43m Docs:',link,' \033[0;0m')

    else:
        subprocess.Popen(["powershell.exe","./test.ps1"]) 
    
def unix():
    subprocess.Popen(['sh', './test.sh']) 

if (os.name == 'nt'):
    win() 


if(os.name == 'posix'):
    unix()
