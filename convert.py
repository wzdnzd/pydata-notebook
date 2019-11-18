import os
import argparse

PATH = os.path.abspath(os.path.dirname(__file__))


def convert(extends):
    output = os.path.join(PATH, extends)

    if os.path.exists(output):
        os.remove(output)

    os.makedirs(output)

    for root, _, files in os.walk(PATH, topdown=True):
        for f in files:
            if f.endswith('.ipynb'):
                command = 'jupyter nbconvert --to {} --output-dir {} {}'.format(
                    extends, '"' + output + '"', '"' + os.path.join(root, f) + '"')

                outlines = os.popen(command, 'r')
                print(outlines.read())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='convert ".ipynb" file to ".html" or ".pdf"')
    parser.add_argument('-f', '--format', type=str, required=True,
                        choices=['html', 'pdf'], default='html', help='format')
    convert(parser.parse_args())
