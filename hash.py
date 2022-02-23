import hashlib, os, sys

def sha(string):
    encoded=string.encode()
    result = hashlib.sha256(encoded)
    result = result.hexdigest()
    return result

def file(fileName):
    f = open(fileName, 'r')
    return f.read()

def fileCoded(fileName):
    return sha(file(fileName))


def comp(fileA, fileB):
    print(fileCoded(fileA))
    print(fileCoded(fileB))
    print(fileCoded(fileA) == fileCoded(fileB))
    return fileCoded(fileA) == fileCoded(fileB)

args = sys.argv[1:]

comp(args[0], args[1])