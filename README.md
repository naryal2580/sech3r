# SéCh3r v4.7
A Security HTTP-Header Checker.    # Demoisturize it!



#### What's this?

> This is a tool, used in order to determine the presence of Security HTTP-Headers along with version disclosure checks.



## Installation

In order to get this tool running, follow the instruction below:

#### Installation via pip

```
$ python3 -m pip install sech3r  # Super User permission, accordingly.
```

#### Installation via GitHub

```
$ git clone https://github.com/naryal2580/sech3r.git
$ cd sech3r
$ python3 setup.py install  # Super User permission, accordingly.
```

#### Use without installation
```
$ git clone https://github.com/naryal2580/sech3r.git
$ cd sech3r
$ python3 -m pip install -U -r requirements.txt  # Super User permission, accordingly.
$ python3 sech3r.py
```



## Usage

```
$ sech3r -h
     /  __       ____
 ()  _ / () |)    __/ ,_
 /\ |/|     |/\     \/  |
/(_)|_/\___/|  |/\__/   |/

Usage:
    sech3r [--verbose] [--searchForVuln] [--noRedirects] [--insecure] [--noColor] [--quiet]
    sech3r <urls>... [--verbose] [--searchForVuln] [--noRedirects] [--insecure] [--noColor] [--quiet]
    sech3r -h | --help
    sech3r -V | --version

Options:
    -h --help           Display help, basically this screen.
    -V --version        Display version number.
    <urls>              Optional URL(s) input from the Command-Line.
    -v --verbose        Show verbose output.
    -s --searchForVuln  Open Default WebBrowser, Googling for Vulnerabilities.
    -r --noRedirects    Do not follow HTTP-redirects.
    -k --insecure       Bypass TLS/SSL verification.
    -c --noColor        No Colours to be used for the Output.
    -q --quiet          Silent Mode, nothing else not even colors.

Examples:
    sech3r demo.testfire.net
    sech3r demo.testfire.net -vs
    sech3r demo.testfire.net -vr
    sech3r demo.testfire.net -c
    sech3r demo.testfire.net -q
    sech3r -vsirc
```


## TODOs

- Input of URLs from a textfile
- Output to a file
- Additional Header Assesments for better output

----

</> with <3 --naryal2580