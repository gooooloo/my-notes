import glob
import os
import time
import shutil
from os.path import basename, join, dirname, abspath, isdir, sep
from urllib import parse
from os.path import basename, join, dirname, abspath, isdir, sep


def docmd(cmd):
    print(cmd)
    os.system(cmd)


def ingit(fn):
    with open(fn, mode="r") as f:
        firstline = f.readline()

    return firstline == '#git\n'


def auto_git_add():
    for fn in glob.glob(join('*', '**', '.gitignore'), recursive=True):
        os.remove(fn)

    for fn in glob.glob(join('*', '**', '*.md'), recursive=True):
        if ingit(fn):
            fn2 = fn.replace(' ', '\ ') 
            cmd = f"git add {fn2}"
            docmd(cmd)
        else:
            xx = join(dirname(fn), '.gitignore')
            fn2 = basename(fn) + '\n'
            with open(xx, 'a') as f:
                print(fn2, file=f)

    for fn in glob.glob(join('*', '**', '.gitignore'), recursive=True):
        docmd(f"git add {fn}")


def urlencode(s):
    ret = parse.quote(s)
    return ret


def update_sidebar():
    md_list = [abspath(fn) for fn in glob.glob(join('**', '*.md'), recursive=True) if not basename(fn).startswith('_') and basename(fn) != 'README.md' and ingit(fn)]

    root_abs = abspath('.')
    assert all(md.startswith(root_abs) for md in md_list)
    md_list = [md[len(root_abs):] for md in md_list]

    # sorting is critical
    md_list.sort()

    extended_list = []
    extended_set = set()
    for md in md_list:
        x = md.split(sep)
        for i in range(1, len(x) + 1):
            y = tuple(x[:i])
            if y != ('',) and y not in extended_set:
                extended_set.add(y)
                extended_list.append(y)
    
    with open("_sidebar.md", "w") as f:
        print('- [首页](/)', file=f)
        for line in extended_list:
            x = ''
            for _ in range(0, len(line) - 2):
                x += '  '
            x += '- '
            if line[-1].endswith('.md'):
                txt = line[-1][:-3]
                url = '/'.join(line)
                url = urlencode(url)
                x += f'[{txt}]({url})'
            else:
                x += line[-1]
            print(x, file=f)
    
    docmd('git add _sidebar.md')


if __name__ == '__main__':
    auto_git_add()
    update_sidebar()