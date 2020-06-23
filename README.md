# SéCh3r v4.8
A Security HTTP-Header Checker.    # Demoisturize it!



#### What's this?

> This is a tool, used in order to determine the presence of Security HTTP-Headers along with version disclosure checks.



## Features

- Checks if security headers are present
- Checks if Version Disclosure headers are present
- Have got a fancy output
- Will Google you for CVEs (from the disclosed version number via HTTP Headers)
- Have got silent mode, in case you wanna see only URL and headers
- Verbose mode, if you want to inspect whole HTTP Header response
- No redirect mode, in case don't wanna redirect
- Insecure mode, if you wanna ignore TLS/SSL warnings
- No color mode, in case escapes sequences are creating issues
- Can also take file input, for several URLs to be tested for HTTP Headers
- Can also save the output, in the form of JSON File



## Install

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
$ python3 ./sech3r.py
```



## Usage

> Just provide the command line arguments accordingly, and Demoisturize it! :p


```
$ sech3r -h
     /  __       ____
 ()  _ / () |)    __/ ,_
 /\ |/|     |/\     \/  |
/(_)|_/\___/|  |/\__/   |/

Usage:
    sech3r [--verbose] [--searchForVuln] [--noRedirects] [--insecure] [--noColor] [--quiet] [--output <filename>]
    sech3r <urls>... [--verbose] [--searchForVuln] [--noRedirects] [--insecure] [--noColor] [--quiet] [--output <filename>]
    sech3r [--verbose] [--searchForVuln] [--noRedirects] [--insecure] [--noColor] [--quiet] [--input <filename>] [--output <filename>]
    sech3r -h | --help
    sech3r -V | --version

Options:
    -h --help               Display help, basically this screen.
    -V --version            Display version number.
    <urls>                  Optional URL(s) input from the Command-Line.
    -v --verbose            Show verbose output.
    -s --searchForVuln      Open Default WebBrowser, Googling for Vulnerabilities.
    -r --noRedirects        Do not follow HTTP-redirects.
    -k --insecure           Bypass TLS/SSL verification.
    -c --noColor            No Colours to be used for the Output.
    -q --quiet              Silent Mode, nothing else not even colors.
    -i --input <filename>   Take URLs from a file, Single URL per line
    -o --output <filename>  Save output to a file, a JSON output of headers

Examples:
    sech3r demo.testfire.net
    sech3r demo.testfire.net -i in.json
    sech3r demo.testfire.net -vs -o out.json
    sech3r demo.testfire.net -vr
    sech3r demo.testfire.net -c
    sech3r demo.testfire.net -q
    sech3r -vsirc
```


## TODOs

- Additional Header Assesments for better output

----

</> with <3 --naryal2580