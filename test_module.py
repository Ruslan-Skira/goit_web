import argparse
parser = argparse.ArgumentParser(description='Test this awesome module')

parser.add_argument('--name', help='add please your name')
arguments = parser.parse_args()
name = arguments.name

print(f'Hello awesome developers {name}')
