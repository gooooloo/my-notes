import glob
import os
import time
import shutil
from os.path import basename, join, dirname, abspath, isdir, sep
from urllib import parse
from os.path import basename, join, dirname, abspath, isdir, sep
import re


def docmd(cmd):
    print(cmd)
    os.system(cmd)


def nogit(fn):
    with open(fn, mode="r") as f:
        firstline = f.readline()

    return firstline == '#nogit\n'

def ingit(fn):
    return not nogit(fn)


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


def get_used_imgs_in_git():
    img_list = set()
    md_list = [abspath(fn) for fn in glob.glob(join('**', '*.md'), recursive=True) if not basename(fn).startswith('_') and basename(fn) != 'README.md' and ingit(fn)]
    for md in md_list:
        with open(md, 'r') as f:
            lines = f.readlines()
        for postfix in ('png', 'jpg', 'svg'):
            sublines = [l for l in lines if f'.{postfix}' in l]
            for line in sublines:
                p = f'\(.*{postfix}\)'
                x = re.search(p, line)
                if x:
                    x= x.group()[1:-1]
                    x = join(dirname(md), x)
                    img_list.add(abspath(x))
    return img_list


def update_img():
    img_list = get_used_imgs_in_git()

    for postfix in ('png', 'jpg', 'svg'):
        for fn in glob.glob(join('**', f'*.{postfix}')):
            x = abspath(fn)
            if x in img_list:
                x = x.replace(' ', '\ ')
                docmd(f'git add {x}')
            else:
                gi = join(dirname(fn), '.gitignore')
                with open(gi, 'a') as f:
                    print(basename(x), file=f)
                docmd(f'git add {gi}')


if __name__ == '__main__':
    auto_git_add()
    update_sidebar()
    update_img()
