"""dafont-dl - making it easy to download fonts.

Usage:
  dafont-dl <name-font>...
  dafont-dl (-h | --help)
  dafont-dl --version
Options:
  -h --help   Show help screen
  --version   Show current version
"""

from dafontlib import Dafont, CompactFont
import docopt
import crayons

def main():
    args = docopt.docopt(__doc__, version='dafont-dl v0.0.1')
    df_obj = Dafont()
    if args['<name-font>']:
        try:
            name = " ".join(args['<name-font>'])
            font_to_download = df_obj.search_font(name)
            font_to_download.install_font_file()
        except ValueError:
            print(crayons.red(f"{name} nonexistent in dafont.com", bold=True))
        else:
            print(crayons.green("[DONE]", bold=True))

if __name__ == "__main__":
    main()
