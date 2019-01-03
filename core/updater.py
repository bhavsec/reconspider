import os
import re
from requests import get
from .update_log import changes

from .colors import run, que, good, info, end, green


def update():
    print('%sChecking for updates..' % run)
    latestCommit = get('https://raw.githubusercontent.com/bhavsec/reconspider/master/core/update_log.py').text

    if changes not in latestCommit:  # just a hack to see if a new version is available
        changelog = re.search(r"changes = '''(.*?)'''", latestCommit)
        changelog = changelog.group(1).split(';')  # splitting the changes to form a list
        print('%s\nA new version of ReconSpider is available.' % good)
        print('%s\nChanges:' % info)
        for change in changelog:  # print changes
            print('%s>%s %s' % (green, end, change))

        currentPath = os.getcwd().split('/')  # if you know it, you know it
        folder = currentPath[-1]  # current directory name
        path = '/'.join(currentPath)  # current directory path
        choice = input('%s\nWould you like to update? [Y/n] ' % que).lower()

        if choice != 'n':
            print('%s\nUpdating ReconSpider..' % run)
            os.system(
                'git clone --quiet https://github.com/bhavsec/reconspider %s' % (folder))
            os.system('cp -r %s/%s/* %s && rm -r %s/%s/ 2>/dev/null' % (path, folder, path, path, folder))
            print('%s\nUpdate successful!' % good)
    else:
        print('%s ReconSpider is up to date!' % good)
