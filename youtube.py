from __future__ import unicode_literals
import pyperclip as pc
import time
import os
import subprocess

def loop():
    prev_text = ""
    while (1):
        new_text = pc.paste()
        print(new_text)
        if prev_text != new_text:
            if new_text.find("https://www.youtube.com") >= 0:
                print("Now I will work")
                all_links, all_names,length = get_all_links_and_names(new_text)
                for i in range(length):
                    call_idm(all_links[i],all_names[i])
        prev_text = new_text
        time.sleep(1)


#def get_links(text):
#    command=['youtube-dl', 'ytsearch:"' + text+'"', '-g','-f best','--yes-playlist'] #Give the audio+video url for the best quality normally stuck at 720p
#    result=subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True).stdout.split()
#    my_string = "youtube-dl --get-filename -o %(title)s.%(ext)s " + "\"" + text + "\""
#    process = subprocess.Popen(my_string, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#    name = process.stdout.readline() #it returns binary string
#    name = name.decode("utf-8") #here we decode it using utf-8
#    name = name.rstrip("\n\r") #and the name had \n at the end so here we strip it of \n or \r if any
#    print(result)
#    return result[0],name #the url is in a list so give it 0th value
    
def call_idm(video_url,name):
    my_str = "idman "+  "/f " +  "\"" + name + "\" " + "/d " + "\""+ video_url +  "\""
    print(my_str)
    os.system(my_str)

def split_them(strings):
    tokens = strings.decode("utf-8").split('\n')
    my_list = []
    for i in tokens:
        my_list.append(i.rstrip('\r'))
    return my_list

def get_all_links_and_names(url):
    links_command = "youtube-dl -g " + "\""+url+"\"" + " -f best --yes-playlist"
    all_links = split_them(subprocess.check_output(links_command))
    names_command = "youtube-dl --get-filename -o %(title)s.%(ext)s " + "\"" + url + "\""
    all_names = split_them(subprocess.check_output(names_command))
    return all_links, all_names, len(all_links)-1
   


loop()
