from setuptools import setup

setup(
    name='inkbird',
    version='0.1.0',    
    description='Inkbird sensor reading package',
    url='https://github.com/sittingfrog/inkbird',
    author='sittingfrog',
    license='MIT',
    packages=['inkbird'],
    install_requires=['bluepy',
                      'wheel',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',    
        'Programming Language :: Python :: 3',
    ],
)