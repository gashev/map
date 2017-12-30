#!/usr/bin/python

import json
import os
import os.path
import sys

configFile = os.environ['HOME'] + '/.map'

commands = {
    'add' : 'add item to list',
    'delete': 'delete item from list',
    'destroy': 'destroy list',
    'export': 'export to bash code',
    'show': 'show details from list'
}

def add(args):
    name = args[2]
    data = readConfig()
    if name not in data:
        data[name] = []
    values = args[3:]
    for value in values:
        if value not in data[name]:
            data[name].append(value)
    print(' '.join(data[name]))
    writeConfig(data)

def delete(args):
    name = args[2]
    data = readConfig()
    if name not in data:
        return

    values = args[3:]
    for value in values:
        if value in data[name]:
            data[name].remove(value)

    print(' '.join(data[name]))
    writeConfig(data)

def destroy(args):
    name = args[2]
    data = readConfig()
    if name in data:
        data.pop(name)
        writeConfig(data)

def export(args):
    data = readConfig()
    for key in data:
        print("export %s=\"%s\"" % (key, ' '.join(data[key])))

def help(args):
    print("\nUsage: map <command> <list> [<item>] ...")
    print("\nPaths mapping tool.")
    print("\nCommands:")

    commandNames = sorted(commands.keys())
    for command in commandNames:
        print('  %-12s%s' % (command, commands[command]))

def show(args):
    name = args[2]
    data = readConfig()
    print(' '.join(data[name]))

def readConfig():
    try:
        data = {}
        if os.path.exists(configFile):
            data = json.load(open(configFile))

        return data
    except Exception as e:
        sys.stderr.write("Error read %s. %s\n" % (configFile, e))
        sys.exit(1)

def writeConfig(data):
    try:
        with open(configFile, 'wt') as outfile:
            json.dump(
                data,
                outfile,
                sort_keys=True,
                indent=4,
                separators=(',', ': ')
            )
    except Exception as e:
        sys.stderr.write("Error write %s. %s\n" % (configFile, e))
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        sys.stderr.write("ERROR: command not found.\n")
        return help(sys.argv)

    command = sys.argv[1]

    if command not in commands.keys():
        sys.stderr.write("ERROR: %s command not found.\n" % (command))
        return help(sys.argv)

    if command == 'add':
        return add(sys.argv)

    if command == 'delete':
        return delete(sys.argv)

    if command == 'destroy':
        return destroy(sys.argv)

    if command == 'show':
        return show(sys.argv)

    if command == 'export':
        return export(sys.argv)

    if command == 'help':
        return help(sys.argv)

    sys.stderr.write("ERROR: %s command was not implemented.\n" % (command))

if __name__== "__main__":
    main()
