from setuptools import find_packages, setup

def get_requirements(file_path):
    '''
    This function returns the list of requirements
    '''
    with open(file_path) as file:
        requirements = file.read().splitlines()
        if '-e .' in requirements:
            requirements.remove('-e .')
    
setup(
    name = 'fat_percent_estimator',
    version = '0.0.1',
    author = 'Mandeep',
    author_email= 'mndppsingh20@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)