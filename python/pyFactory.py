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
    '001. Introduct to Sets', '002. No Idea!', "003. Symmetric Difference", '004. Set add()', '005. Set discard(), remove() & pop()',
    '006. Set union() Operation', '007. Set intersection() Operation', '008. Set difference() Operation', '009. Set symmetric_difference() Operation', '010. Set Mutations',
    "011. The Captain's Room", '012. Check Subset', '013. Check Strict Superset'
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
    '001. Detect Floating Point Number', '002. Re.split()', '003. Group(), Groups() & Groupdict()', '004. Re.findall() & Re.finditer()', '005. Re.start() & Re.end()',
    '006. Regex Substitution', '007. Validating Roman Numerals', '008. Validating phone numbers', '009. Validating and Parsing Email Addresses', '010. Hex Color Code',
    '011. HTML Parser - Part 1', '012. HTML Parser - Part 2', '013. Detect HTML Tags, Attributes and Attribute Values', '014. Validating UID', '015. Validating Credit Card Numbers',
    '016. Validating Postal Codes', '017. Matrix Script'
    ],
    '14. XML' : [
    '001. XML 1 - Find the Score', '002. XML2 - Find the Maximum Depth'
    ],
    '15. Closures and Decorators' : [
    '001. Standardize Mobile Number Using Decorators', '002. Decorators 2 - Name Directory'
    ], 
    '16. Numpy' : [
    '001. Mean, Var, and Std', '002. Dot and Cross', '003. Inner and Outer', '004. Polynomials', '005. Linear Algebra',
    '006. Shape and Reshape', '007. Arrays', '008. Transpose and Flatten', '009. Concatenate', '010. Zeros and Ones',
    '011. Eye and Identity', '012. Array Mathematics', '013. Floor, Ceil and Rint', '014. Sum and Prod', '015. Min and Max'
    ],
    '17. Debugging':[
    '001. Words Score', '002. Default Arguments'
    ]
}

def createPy (mkdirName, Listspy):
    for pyname in Listspy:
        if os.path.isfile(my_path + mkdirName +'/'+ pyname+'.py') :
            print('   "'+ pyname + '" OK.')
        else:
            shutil.copyfile(my_path + 'model.py ', my_path + mkdirName + '/' +  pyname+'.py')
            print('    Create "'+ pyname +' .py" Success.')

def editPy (mkdirName,index , question):
    return 


if __name__ == '__main__':

    if os.path.exists(my_path) == 0:
        os.mkdir(my_path)

    for mkdir in mkdirs.keys():
        if ( os.path.exists(my_path+ mkdir)) :
            print(mkdir +' OK.')
            createPy(mkdir,mkdirs[mkdir])

        else :
            os.mkdir(my_path + mkdir)
            print('    Create "'+ mkdir +' " Success.')