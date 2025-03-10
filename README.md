# code 

Code - VS code helper command for organizing and starting projects extremely fast

## Install

⚠️ **Notice:** only works on Unix-like os

Clone this repo somewhere anywhere and then cd into the cloned repo
Run `./setup.sh` preferably in sudo, it'll create a code command symlink inside your local bin

⚠️ Don't delete or move the repo folder after creating the symlink, any changes will not be replicated to 
the symlink and will make the symlink unusable therefore the command unusable

**Finally,** create a 'Projects' folder inside your desktop, 
this folder will contain all your future projects

## Usage


**Creating**

To create a new project

```sh
code new PROJECT_NAME
```

This will open up a new $PROJECT_NAME folder in VSC

**Opening**

To open an existing project, file or directory
If a project can't be found your work dir will be searched for a dir with the same name

```sh
code open someProject
code open ./someFile.txt
code open ./someDir
code open someFile.txt
code open someDir
code open ~/someDir 
```

**Git implementation**

Creates a new project and clones a git repo into it

```sh
code git REPO_URL PROJECT_NAME?
```

If no $PROJECT_NAME is picked, the repo name will be choosen as the project name

**List**

Provides the full list of projects

```sh
code list PREFIX?
```

If prefix is a string, list will only contain projects starting with prefix

## Notes

This project was made relatively fast and for personal use

## License

Do anything you want with my code, credits not needed

[UNI](https://choosealicense.com/licenses/unlicense/)
