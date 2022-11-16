import os
import shutil 

my_path = os.path.abspath(os.getcwd())+ '/python/'

# mkdir : Question.py
mkdirs={
    '01. Introduction' : [
    '001. Say Hello, World! With Python', '002. Python If-Else', '003. Arithmetic Operators', '004. Python Division', '005. Loops',
    '006. Write a function', '007. Print Function'
    ],
    '02. Basic Data Types' : [
    '001. List Comprehensions', '002. Find the Runner-Up Score!', '003. Nested Lists', '004. Finding the percentage', '005. Lists',
    '006. Tuples'
    ],
    '03. Strings' : [
    '001. sWAP cASE', '002. String Split and Join', "003. What's Your Name", '004. Mutations', '005. find-a-string',
    '006. String Validators', '007. Text Alignment', '008. Text Wrap', '009. Designer Door', '010. String Formatting',
    '011. Alphabet Rangoli', '012. Capitalize!', '013. The Minion Game', '014. Merge the Tools'   
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
    '001. itertoolsproduct()', '002. itertoolscombinations()', '003. itertoolspermutations()', '004. itertoolscombinations_with_replacement()', '005. Compress the String!',
    '006. Iterables and Iterators', '007. Maximize It!'
    ],
    '07. Collections' : [
    '001. collectionsCounter()', '002. DefaultDict Tutorial', '003. Collections namedtuple()', '004. Collections OrderedDict()', '005. Word Order',
    '006. Collections deque()', '007. Company Logo', '008. Piling Up!'
    ],
    '08. Date and Time' : [
    '001. Calendar Module', '002. Time Delta'
    ],
    '09. Errors and Exceptions' : [
    '001. Exceptions', '002. Incorrect Regex'
    ],
    '10. Classes' : [
    '001. Dealing with Complex Numbers', '002. Find the Torsional Angle'
    ], 
    '11. Built-Ins' : [
    '001. Zipped!', '002. Input()' , '003. Python Evaluation', '004. Athlete Sort' , '005. Any or All',
    '006. ginortS'
    ],
    '12. Python Functionals' : [
    '001. Map and Lambda Function', '002. Validating Email Addresses With a Filter', '003. Reduce Function'
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