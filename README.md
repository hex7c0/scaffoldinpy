# scaffoldipy

[![Build Status](https://travis-ci.org/hex7c0/scaffoldinpy.svg?branch=master)](https://travis-ci.org/hex7c0/scaffoldinpy)

Build your project, cloning a skeleton from git repository and replace it with patterns.
You can write your own RegExp inside json file

## API

Run through bash

```bash
python3 scaffold.py git@github.com:hex7c0/scaffoldinpy.git
```

### scaffoldipy(options)

#### options

 - `git` - **String** Git url and options *(default "required")*
 - `-d`, `--dir` - **String** Name of a new directory to clone into *(default "False")*
 - `-j`, `--json` - **String** Path of cfg json file *(default "False")*
 - `-s`, `--suicide` - **Boolean** Remove json and script files after work *(default "True")*
 - `-h`, `--help` - Show this help message and exit
 - `-v`, `--version` - Show program's version number and exit

## Examples

Take a look at my [examples](examples)

### [License GPLv3](LICENSE)
