#!/usr/bin/env python

import re
import configparser
config = configparser.ConfigParser()
config.optionxform = str # make the parser case-sensitive

from os import walk, makedirs
from os.path import dirname,abspath,join

class PATH:
    ROOT = dirname(abspath(__file__))
    TEMPLATE = join(ROOT,"_template")

def gen(filepath, filename, li, txt):
    package = ""
    txt = txt.split("\n")
    kv = dict(li.items())
    kname = {}

    for pos,i in enumerate(txt):
        line = i.strip()
        if line.startswith("package "):
            package = i.split(" ").pop()
            txt[pos] = "package %s%s"%(package, filename)

        for k,v in kv.items():
            if "type %s "%k in line:
                r = re.compile(r"([\[\*\(\s\]])%s\b"%k)
                kname[r] = r"\1"+v
                txt[pos] = ""
                del kv[k]
                break

        for k,v in kname.items():
            txt[pos] = k.sub(v, txt[pos])


    filepath = filepath[len(PATH.ROOT)+11:]
    outfile = join(PATH.ROOT, package+filename,filepath[filepath.find("/")+1:])
    makedirs(dirname(outfile), exist_ok=True)
    with open(outfile, "w") as f:
        f.write("\n".join(txt))


def main():
    for dirpath, _, file_li in walk(PATH.TEMPLATE):
        for filename in file_li:
            if filename.endswith(".ini"):
                filepath = join(dirpath,filename)
                config.read(filepath)
                gopath = join(dirpath, filename[:-4]+".go")
                with open(gopath) as f:
                    txt = f.read()

                for filename, li in config.items():
                    if len(li):
                        gen(gopath, filename.strip(), li, txt)

if __name__ == "__main__":
    main()
