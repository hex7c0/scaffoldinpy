#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@file scaffoldinpy main
@module scaffoldinpy
@package scaffoldinpy
@subpackage main
@version 0.0.2
@author hex7c0 <hex7c0@gmail.com>
@copyright hex7c0 2014
@license GPLv3
'''

NAME = 'scaffoldinpy'
VERSION = '0.0.2'

try:
    # check version
    from sys import version_info
    if(version_info[0] < 3):
        print('must use Python 3 or greater')
        quit()
    del version_info
    # import
    from re import subn
    from json import load
    from os import walk, remove, replace
    from time import time, gmtime, strftime
    from os.path import exists, isfile, isabs, abspath
    from argparse import ArgumentParser, ArgumentTypeError
    from subprocess import check_output, CalledProcessError
except ImportError as error:
    print('in %s cannot load required libraries: %s!' \
        % (__name__, error))
    quit(1)

def scaffolding(args):
    '''
    project scaffolding

    @param list args - parsed input
    @return: bool
    '''

    def empty(*boh):
        '''
        empty function

        @param list boh - I don't want to know :)
        @return: str
        '''

        return boh[2] + boh[0]

    def clone(git, path):
        '''
        git cloning

        @param list git - git options
        @param list path - dir path
        @return: bool
        '''

        print('git')
        out = False
        try:
            out = check_output(['git', 'clone'] + git + path)
            if(out):
                print(out)
            out = True
        except CalledProcessError:
            out = False
        return out

    def regex(patterns, original):
        '''
        string regex

        @param dict patterns - json
        @param str original - read
        @return: tuple
        '''

        counter = 0
        for ele in patterns:
            tmp = subn(ele, patterns[ele], original)
            original = tmp[0]
            counter += tmp[1]
        return original, counter

    def rename_f(what, where, root):
        '''
        rename dir

        @param dict what - json
        @param list where - dirs
        @param str root - root path
        '''

        for old in where:
            if(old in what):
                replace(root + old, root + what[old])
        return

    def rename(what, where, root):
        '''
        rename file

        @param str what - old file name
        @param dict where - json
        @param str root - root path
        @return: str
        '''

        if(what in where):
            replace(root + what, root + where[what])
            what = where[what]
        return root + what

    try:
        if(not clone(args.git, args.dir)):
            return False

        if(not args.json[0]):
            return True

        print('parsing')
        with open(args.json[0]) as file:
            try:
                json = load(file)
                try:
                    if(not json['dirs']):
                        json['dirs'] = ''
                        rename_f = empty
                except KeyError:
                    json['dirs'] = ''
                    rename_f = empty
                try:
                    if(not json['files']):
                        json['files'] = ''
                        rename = empty
                except KeyError:
                    json['files'] = ''
                    rename = empty
            except ValueError:
                print('json misconfigured')
                return False
        for root, dirs, files in walk(args.dir[0]):
            root += '/'
            rename_f(json['dirs'], dirs, root)
            for _file in files:
                _file = rename(_file, json['files'], root)
                with open(_file, 'r') as read:
                    try:
                        orig = read.read()
                    except UnicodeDecodeError:
                        continue
                mod = regex(json['patterns'], orig)
                if(mod[1]):
                    with open(_file, 'w') as write:
                        write.write(mod[0])
        return True

    except KeyboardInterrupt:
        return False

if __name__ == '__main__':

    def check(root, out=True):
        '''
        type for argparse

        @param str root - path of file
        @return str|bool
        '''

        roo = root if isabs(root) else abspath(root)
        if(not exists(roo)):
            if(out):
                raise ArgumentTypeError('"%s" not found' % root)
            roo = False
        if(not isfile(roo)):
            if(out):
                raise ArgumentTypeError('"%s" not a file' % root)
            roo = False
        return roo

    def crono(start, pprint=True):
        '''
        given the initial unix time
        return time spent

        @param time start - stating time
        @param bool pprint - if print to output
        @return: str
        '''

        if(pprint):
            end = time() - start
            microsecond = int((end - int(end)) * 1000)
            if (end < 60):  # sec
                return '%s sec and %s ms' % (strftime('%S', \
                                                 gmtime(end)), microsecond)
            if (end < 3600):  # min
                return '%s min and %s ms' % (strftime('%M,%S', \
                                                 gmtime(end)), microsecond)
            # hr
            return '%s hr and %s ms' % (strftime('%H.%M,%S', \
                                                 gmtime(end)), microsecond)
        else:
            return int(strftime('%S', gmtime(start)))

    PARSER = ArgumentParser(description='Run %s' % NAME, prog=NAME)

    PARSER.add_argument('-v', '--version', action='version', \
                        version='%s version %s' % (NAME, VERSION))
    PARSER.add_argument('-s', '--suicide', action='store_false', \
                         help='disable self destruction after work')
    PARSER.add_argument('-j', '--json', metavar='path', nargs=1, type=check, \
                         help='path of cfg json file', default=[False])
    PARSER.add_argument('-d', '--dir', metavar='path', nargs=1, type=str, \
                         help='name of a new directory to clone into', \
                         default=['scaffoldipy'])
    PARSER.add_argument('git', type=str, nargs='+', help='git url and options')

    ARGV = PARSER.parse_args()

    START = time()
    if(scaffolding(ARGV)):
        print('scaffolding generated in %s' % crono(START))
        if(ARGV.suicide):
            remove(ARGV.json[0])
            remove('scaffoldipy.py')
        quit(0)
    else:
        print('something wrong')
    quit(1)
