# EA979

To compile the program, you'll need to install the following

Steps to compile and execute:

$ brew install python3
$ python3 --version

if is version 3.7

$ $ brew unlink python
$ brew install --ignore-dependencies https://raw.githubusercontent.com/Homebrew/homebrew-core/f2a764ef944b1080be64bd88dca9a1d80130c558/Formula/python.rb
$ brew switch python 3.6.5_1
$brew link --overwrite --dry-run python
$ sudo easy_install pip
$ sudo pip install --upgrade pip
$ pip install pptk

$ pip install numpy
$ pip install matplotlib
$ pip install PyAudio
$ pip install scipy
$ pip install plyfile
