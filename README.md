# SéCh3r v3.0
A Security HTTP-Header Checker.  # Make it Dry!

#### NOTE: Present Headers does not mean it is secure.

## What? Why? Where? How?

### What is This?

> This is a tool, written by [naryal2580](https://google.com#q=naryal2580) or, [Captain Nick Lucifer](https://duckduckgo.com?q=naryal2580). It is a tool to determine the presence of Security  HTTP-Headers of a URL.

### Why is This?

> This is written in `python3` to check if `Security HTTP-Headers are present` also, to check if `Version Disclosure is present`. 

### Where is This?

> This is right here! 😁 You can just simply `git clone https://github.com/naryal2580/sech3r`, and use it within Inter-net or, an Intra-net.

### How does This work?

> It makes a `GET` HTTP-Request to the given URL. And, then parses the HTTP-Response Headers. [blah^2^] Check `sech3r -v` flag to know what is happening.

## Features

- Cool Command Line Interface.
- Some good and, satisfying colors.
- Others, discover it yourself!

## Installation
Follow the steps provided to Install this tool.

### Linux
```bash
make install
```

### Other Platform

```
echo "Will update, As Soon As Possible."
```

## Usage

```
$ sech3r -h
        __       ____
 ()  _ / () |)    __/ ,_
 /\ |/|     |/\     \/  |
/(_)|_/\___/|  |/\__/   |/

Usage:
    sech3r [--verbose] [--searchForVuln] [--noRedirects] [--noColor]
    sech3r <url> [--verbose] [--searchForVuln] [--noRedirects] [--noColor]
    sech3r -h | --help
    sech3r -V | --version

Options:
    -h --help           Display help, basically this screen.
    -V --version        Display version number.
    <url>               Optional URL input from the Command-Line.
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

## Output

```
        __       ____
 ()  _ / () |)    __/ ,_
 /\ |/|     |/\     \/  |
/(_)|_/\___/|  |/\__/   |/  v3.0  by --naryal2580
[*] Started [at] 1.8.2019│19:23:38
[<] URL: demo.testfire.net
[*] Requesting to: http://demo.testfire.net/
[!] Non-HTTPS request: Someone else can interact.
[-] Version Disclosure Present: Apache-Coyote/1.1
[-] Referrer-Policy: Not Present!
[-] X-XSS-Protection: Not Present!
[-] Content-Security-Policy: Not Present!
[-] X-Frame-Options: Not Present!
[-] Strict-Transport-Security: Not Present!
[-] X-Content-Type-Options: Not Present!
[-] X-Permitted-Cross-Domain-Policies: Not Present!
[-] Public-Key-Pins: Not Present!
[-] Expect-CT: Not Present!
[-] Feature-Policy: Not Present!
[-] Report-To: Not Present!
[-] NEL: Not Present!
[*] Halted [at] 1.8.2019│19:23:38
```
// An Asciinema demo will be added soon.



\-\-
</> with ❤️ & ✌️ --naryal2580