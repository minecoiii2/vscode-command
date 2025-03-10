#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os
import sys # type: ignore

# project folder
PROJECT_FOLDER = os.path.expanduser("~/Desktop/Projects")

# path exit, if path does/doesnt exist exit
def existsExit(path: str, msg: str):
    name = path.split('/')[-1]#.split('.')[0]
    print("'" + name + "' " + msg)
    exit()

# if project dir does not exists then exit
if not os.path.isdir(PROJECT_FOLDER): existsExit(PROJECT_FOLDER, 'folder needs to exist in Desktop to continue')

# help output
def help():
    print("usage:")
    print("\topen\tfile|dir|ProjectName:string\n\t-> opens file/dir or an existing project file\n")
    print("\tnew\tProjectName:string\n\t-> creates a new project file\n")
    print("\tlist\n\t-> lists all projects\n")
    print("\tgit\tGithubRepoUrl:string\tProjectName?:string?\n\t-> creates and new project and clones a git repo in it\n")

# retrieve args
fargs = sys.argv[1:]

if len(fargs) == 0:
    print("Argument 1 'Command' missing")
    help()
    exit()

# get current work dir
pwd = os.getcwd()

# retrieve args and cmd
cmd = fargs[0]
args = fargs[1:]

# open path in vsc
def openInVSC(path: str):
    os.system(f"open {path} -a 'Visual Studio Code'")

# main

if cmd == 'open':
    if len(args) < 1:
        print('Missing argument')
        help()
        exit()

    first = args[0]
    ff = first[0]

    isPath = ff == '.' or ff == '~' or ff == '/'

    if not isPath:
        path = PROJECT_FOLDER + '/' + first
        isPath = not os.path.isdir(path)

    if isPath:
        path = pwd + '/' + first.removeprefix('./')
        if not os.path.exists(path):
            existsExit(path, 'project/file does not exist')

    openInVSC(path)

elif cmd == 'new':
    if len(args) < 1:
        print('Missing argument')
        help()
        exit()

    name = args[0].replace("'", '').replace('"', '')
    path = PROJECT_FOLDER + '/' + name

    if os.path.isdir(path):
        existsExit(path, 'project already exists')

    os.mkdir(path)
    openInVSC(path)
elif cmd == 'git':
    if len(args) < 1:
        print('Missing argument')
        help()
        exit()

    repourl = args[0]

    try:
        name = args[1]
    except IndexError:
        name = repourl.split('/')[-1].split('.')[0]

    path = PROJECT_FOLDER + '/' + name
    
    if os.path.isdir(path):
        existsExit(path, 'project already exists')

    os.mkdir(path)
    os.system('git clone ' + repourl + ' ' + path)
    openInVSC(path)
elif cmd == 'list':
    try:
        prefix = args[0].lower()
    except IndexError:
        prefix = None

    c = 0
    for f in os.listdir(PROJECT_FOLDER):
        if prefix != None:
            if f.lower().find(prefix.lower()) != 0:
                continue
        c += 1
        print(c.__str__() + '\t' + f)
else:
    # wrong command
    print("'" + cmd + "' command does not exist")
    help()