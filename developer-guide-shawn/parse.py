#!/usr/bin/env python

import os

readme = "README"

def blank_to_dash(s):
    return s.strip().replace(" ", "-")



class Chapter:
    def __init__(self, session, name, index = 0):
        self.session = session.strip()
        self.name = name.strip()
        self.content = []
        self.index = index
        print("new chapter: {}/{}".format(session, name))

    @property
    def file(self):
        return os.path.join(blank_to_dash(self.session), blank_to_dash(self.name)+'.md')

    @property
    def summary(self):
        name = self.session if self.name == readme else self.name
        return " " * self.index * 2 + "* [{}]({})".format(name, self.file)

    def write(self):
        if self.content and any([c.strip() for c in self.content]):
            if os.path.dirname(self.file):
                os.makedirs(os.path.dirname(self.file), exist_ok=True)
            print("write file {}: \n```\n{}\n```\n".format(self.file, "\n".join(self.content)))
            with open(self.file, "w") as fd:
                fd.write("\n".join(self.content))

    def append(self, line):
        self.content.append(line)


def main():
    with open('hackmd.md', 'r') as fd:
        lines = fd.read().split("\n")

    book = []
    indent = False
    chapter = None
    session = ""

    for line in lines:
        if line.startswith("## "):
            if chapter:
                book.append(chapter)
                chapter.write()
                chapter = None

            session = line.split(" ", 1)[1]
            chapter = Chapter(session, readme)
            continue

        if line.startswith("### "):
            if chapter:
                book.append(chapter)
                chapter.write()
                chapter = None

            chapter = line.split(" ", 1)[1]
            chapter = Chapter(session, chapter, 1)
            continue

        if line.startswith("---"):
            if chapter:
                book.append(chapter)
                chapter.write()
                chapter = None
            continue

        if chapter:
            chapter.append(line)

    for b in book:
        print(b.summary)


if __name__ == '__main__':
    main()