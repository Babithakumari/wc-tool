## Introduction
This is a python implementation of the wc tool

## Additional Notes
### Steps to make python script executable
1. Make the script executable the following way:
`chmod +x script-name.py`

2. Write a shebang on top of the script  pointing to the python interpreter(e.g. `#!/usr/bin/env python3`)

3. Add the folder containing the script to the path
`export PATH=$PATH:<path-to-your-script>`

4. To be able to execute the script without the `.py` extension, create a symbolic link the script in a directory already included in the path
`ln -s some_file.py some_file`