# scaffoldipy

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

Take a look at my [examples](https://github.com/hex7c0/scaffoldipy/tree/master/examples)

### [License GPLv3](http://opensource.org/licenses/GPL-3.0)
