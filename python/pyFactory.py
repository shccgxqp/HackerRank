import os
import shutil 

my_path = os.path.abspath(os.getcwd())+ '/python/'

# mkdir : Question.py
mkdirs={
    '01. Introduction' : [

    ],
    '02. Basic Data Types' : [

    ],
    '03. Strings' : [

    ],
    '04. Sets' : [
    '001. Introduct to Sets', '002. String Split and Join', "003. What's Your Name", '004.  Mutations', '005.  find-a-string',
    '006.  String Validators', '007.  Text Alignment', '008.  Text Wrap', '009.  Designer Door', '010.  String Formatting',
    '011.  Alphabet Rangoli', '012.  Capitalize!', '013.  The Minion Game', '014.  Merge the Tools'
    ],
    '05. Math' : [
    '001. Polar Coordinates', '002. Find Angle MBC','003. Triangle Quest 2','004. Mod Divmod','005. Power - Mod Power',
    '006. Integers Come In All Sizes','007. Triangle Quest'
    ], 
    '06. Itertools' : [

    ],
    '07. Collections' : [

    ],
    '08. Date and Time' : [

    ],
    '09. Errors and Exceptions' : [

    ],
    '10. Classes' : [

    ], 
    '11. Built-Ins' : [

    ],
    '12. Python Functionals' : [

    ],
    '13. Regex and Parsing' : [

    ],
    '14. XML' : [

    ],
    '15. Closures and Decorators' : [

    ], 
    '16. Numpy' : [

    ],
    '17. Debugging':[

    ]
}



def createPy (mkdirName, Listspy):
    for pyname in Listspy:
        if os.path.isfile(my_path + mkdirName +'/'+ pyname+'.py') :
            print('   "'+ pyname + '"  OK.')
        else:
            shutil.copyfile(my_path + 'model.py ', my_path + mkdirName + '/' +  pyname+'.py')
            print('    Create  "'+ pyname +' .py"   Success.')




if __name__ == '__main__':

    if os.path.exists(my_path) == 0:
        os.mkdir(my_path)

    for mkdir in mkdirs.keys():
        if ( os.path.exists(my_path+ mkdir)) :
            print(mkdir +' : OK.')
            createPy(mkdir,mkdirs[mkdir])

        else :
            os.mkdir(my_path + mkdir)
            print('    Create  "'+ mkdir +' "   Success.')