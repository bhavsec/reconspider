import os
import re
import sys
from requests import get

if sys.version_info[0] > 2:
    from .update_log import changes
    from .colors import run, que, good, bad, info, end, green

else:
    from update_log import changes
    from colors import run, que, good, bad, info, end, green

def update():
    print('\n%s Checking for updates..' % run)
    latestCommit = get('https://raw.githubusercontent.com/bhavsec/reconspider/master/core/update_log.py').text

    if changes not in latestCommit:  # just a hack to see if a new version is available
        changelog = re.search(r"changes = '''(.*?)'''", latestCommit)
        changelog = changelog.group(1).split(';')  # splitting the changes to form a list
        print('\n%s A new version of ReconSpider is available.' % good)
        print('\n%s Changes:' % info)
        for change in changelog:  # print changes
            print('%s>%s %s' % (green, end, change))

        currentPath = os.getcwd().split('/')  # if you know it, you know it
        folder = currentPath[-1]  # current directory name
        path = '/'.join(currentPath)  # current directory path

        if sys.version_info[0] > 2:
            choice = input('\n%s Would you like to update? [Y/n] ' % que).lower()

        else:
            choice = raw_input('\n%s Would you like to update? [Y/n] ' % que).lower()


        if choice == 'y':
            print('\n%s Updating ReconSpider..' % run)
            os.system('git clone --quiet https://github.com/bhavsec/reconspider %s' % (folder))
            os.system('cp -r %s/%s/* %s && rm -r %s/%s/ 2>/dev/null' % (path, folder, path, path, folder))
            print('\n%s Update successful!' % good)
            sys.exit()
        else:
            print('\n%s Update Canceled!' % bad)

    else:
        print('\n%s ReconSpider is up to date!' % good)
