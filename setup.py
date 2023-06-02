from setuptools import setup, find_packages


setup(
    name='TrelloWrapper',
    version='1.0.0',
    author='Your Name',
    author_email='your_email@example.com',
    description='A short description of your package',
    long_description='A longer description of your package',
    url='https://github.com/your_username/your_package',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='your, package, keywords',
    install_requires=[
        "requests"
    ],
    entry_points={
        'console_scripts': [
            'your_script_name=your_package_name.module_name:main',
        ],
    },
)

