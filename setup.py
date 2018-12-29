from setuptools import setup 
import sys

if sys.version_info[0] < 3:
    print("\nReconSpider is currently under testing for Python 2, Please run using: python3 setup.py install")



else:

    fout = open("core/config.py", "w")
    fout.write("shodan_api = " + '"' + 'C23OXE0bVMrul2YeqcL7zxb6jZ4pj2by'+ '"' + "\n")
    fout.close()
    
    setup(
        name='ReconSpider',

        version='1.0.5',
        description='Most Advanced OSINT Framework',
        url='https://github.com/bhavsec/reconspider/',
        
        author = 'BhavKaran (@bhavsec)',
        author_email='contact@bhavkaran.com',
        license='GPL-3.0',

        install_requires = ['shodan','requests', 'prompt_toolkit'],
        console =['reconspider.py'],
    )
