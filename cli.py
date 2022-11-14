import sys
import re
import os
import subprocess

cmd = sys.argv[1]
url = ""
episodes = []
seasons = len(episodes)

links = ""

directory = os.getcwd()
output = os.path.join(directory, 'download.txt')
log = os.path.join(directory, 'download.log')

def formatURL(season = 1, episode = 1):
    _url = url
    _url = re.sub(r'{s}', str(season), _url)
    if season < 10:
        season = "0" + str(season)
    else:
        season = str(season)
    _url = re.sub(r'{S}', season, _url)
    if episode < 10:
        episode = "0" + str(episode)
    else:
        episode = str(episode)
    _url = re.sub(r'{E}', episode, _url)
    return _url

def generate():
    global links
    for season in range(1, seasons + 1):
        for episode in range(1, int(episodes[season - 1]) + 1):
            _url = formatURL(season, episode)
            links = links + _url + "\n"


def writeFile():
    file = open(output, 'w')
    file.write(links)
    file.close()

def start():
    command = "aria2c -c -j1 -i {output} > {log} 2>&1 &".format(output=output, log=log)
    os.system(command)

if cmd == "make":
    url = sys.argv[2]
    episodes = sys.argv[3:]
    seasons = len(episodes)
    generate()
    writeFile()
elif cmd == "start":
    start()
elif cmd == "stop":
    os.system("pkill aria2c")
else:
    print("Bad command")