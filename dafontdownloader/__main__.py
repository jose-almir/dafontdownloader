"""dafontdownloader - making it easy to download fonts.

Usage:
  dafontdownloader <name-font>...
  dafontdownloader (-h | --help)
  dafontdownloader --version
Options:
  -h --help   Show help screen
  --version   Show current version
"""
from dafontdownloader import Dafont, CompactFont
import docopt


def main():
    args = docopt.docopt(__doc__, version='dafont-dl v0.2.0')
    df_obj = Dafont()
    if args['<name-font>']:
        try:
            name = " ".join(args['<name-font>'])
            font_to_download = df_obj.search_font(name)
            font_to_download.install_font_file()
        except ValueError:
            print(f"{name} nonexistent in dafont.com")
        else:
            print("[DONE]")

if __name__ == "__main__":
    main()
