# Template folder
This repo contains a template directory structure, which is made based on the instructions found in the [Hitchhicker's Guide](https://docs.python-guide.org/writing/structure/). In His article, he refers to [another guide by Kenneth Reitz](https://www.kennethreitz.org/essays/repository-structure-and-python) found online.

```shell
README.rst
LICENSE
setup.py
requirements.txt
sample/__init__.py
sample/core.py
sample/helpers.py
docs/conf.py
docs/index.rst
tests/test_basic.py
tests/test_advanced.py
```
## Note
`
Although Hitchhicker suggests  `.rst`  as a format for formatted documents I use  `.md` because, I'm more familiar with it, and it is sufficient for my needs.`
## Recommendations
1. The actual module
    1. If your module consists of more than one file, place them in a directory and name the directory as the `module` name
    ```
      ./sample/__init__.py
      ./sample/core.py
      ./sample/helpers.py
    ```
    1. if the module is just a single file, you could alternatevely keep it as a file directly under the root folder.
2. LICENCE

    Keep your copyright claims and the details of the license (permissions) you share the files with others. To know more about the licenses visit site [www.choosealicesence.com](https://choosealicense.com). 

    If you fail to include a license in your repo, other users may not be able to benefit from your contribution, and may not be able to join you in further expanding your work.

    I personally choose `MIT` as the default license for my work unless I have a specific reason to choose another license.
