from setuptools import setup, find_packages

setup(
    name='mkdocs-blueprintue',
    version='0.1.2',
    description='MkDocs plugin for rendering Unreal Engine Blueprint nodes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='mkdocs plugin blueprint unreal engine',
    url='https://github.com/kisspread/uebp',
    author='kisspread',
    author_email='kisspread@users.noreply.github.com',
    license='MIT',
    python_requires='>=3.6',
    install_requires=[
        'mkdocs>=1.0.4',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.plugins': [
            'blueprintue = mkdocs_blueprintue:BlueprintUEPlugin',
        ]
    }
)
