from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() #reads each line 1 by 1
        [req.replace("\n","")for req in requirements] #defnd a lst comp to replace \n by blank while reading lines

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) #to not consider -e while reading
    return requirements



setup(

name = 'mlproject1',
version = '0.0.1',
author = 'Vinesh',
author_email = 'vineshpatil1054@gmail.com',
packages = find_packages(),
#install_requires = ['pandas', 'numpy', 'seaborn'] #for large no. of reqs i create path
install_requires = get_requirements('requirements.txt')
)