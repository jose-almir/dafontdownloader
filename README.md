# dafontdownloader

A python script to download fonts directly from [dafont](dafont.com).
## Install

### First way
To avoid using `sudo`, installation requires these steps:

1. Use `pip` to install the package with all dependencies required:

`pip install dafontdownloader --user`

2. Use `export` to persistent use of dafontdownloader script:

`echo "export PATH=${PATH}:"$HOME"/.local/bin" >> "$HOME"/.bashrc`

3. Use `source` to start using script in command line:

`source .bashrc`

### Second Way
1. Download this repository, or use `git clone https://github.com/resilientcod/dafontdownloader.git`
2. Open repository directory.
3. Use `python3 setup.py install`
4. Follow the steps 2 and 3, to persistent use of dafontdownloader script.

### Third Way (with `sudo`)
**Attention:** use at your own risk!

`sudo pip install dafontdownloader`

This allow install in bin directory, making it unnecessary to use steps 2 and 3 in the first way.
