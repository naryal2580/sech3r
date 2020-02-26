# SéCh3r v4.2
A Security HTTP-Header Checker.    # Demoisturize it!



#### What's this?

> This is a tool, used in order to determine the presence of Security HTTP-Headers along with version disclosure checks.



## Installation

In order to get this tool running, follow the instruction below:

#### Installation via pip

```
% python3 -m pip install sech3r  # Super User permission, accordingly.
```

#### Installation via GitHub

```
% git clone https://github.com/naryal2580/sech3r.git
% cd sech3r
% python3 -n pip install -r -U requirements.txt  # Super User permission, accordingly.
% python3 setup.py install
```

##### Note: Usage without installation is also possible, just run the `sech3r.py`



## Usgae

```
$ sech3r -h
     /  __       ____
 ()  _ / () |)    __/ ,_
 /\ |/|     |/\     \/  |
/(_)|_/\___/|  |/\__/   |/

Usage:
    sech3r [--verbose] [--searchForVuln] [--noRedirects] [--noColor]
    sech3r <urls>... [--verbose] [--searchForVuln] [--noRedirects] [--noColor]
    sech3r -h | --help
    sech3r -V | --version

Options:
    -h --help           Display help, basically this screen.
    -V --version        Display version number.
    <urls>               Optional URL(s) input from the Command-Line.
    -v --verbose        Show verbose output.
    -s --searchForVuln  Open Default WebBrowser, Googling for Vulnerabilities.
    -r --noRedirects    Do not follow HTTP-redirects.
    -c --noColor        No Colours to be used for the Output.

Examples:
    sech3r demo.testfire.net
    sech3r demo.testfire.net -vs
    sech3r demo.testfire.net -vr
    sech3r demo.testfire.net -c
    sech3r -vsrc
```

**NOTE**: I am still working on no-redirection feature.

## TODOs

- Added No redirect support
- Input of URLs from a textfile
- Output to a file
- Additional Header Assesments for better output
- Better APIs for chaining of this tool, via pip
- Other misc. optimizations

----

</> with ❤️ & ✌️ --naryal2580