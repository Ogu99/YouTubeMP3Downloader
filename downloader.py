from pytube import YouTube
from moviepy.editor import *
from os import path
import shutil
import os

HARD_CODED_PATH = '' #Here was originally a path
MP4_PATH = HARD_CODED_PATH + '\\mp4'
MP3_PATH = HARD_CODED_PATH + '\\mp3'

if not path.exists(MP3_PATH):
    os.makedirs(MP3_PATH)

links = []
link = input('YouTube Link eingeben oder \'start\' um download zu starten: ')

while link != 'start':
    video = YouTube(link).streams.first()
    links.append(video)
    print('\nAusgewählter Titel ' + video.title + '\n')
    link = input('YouTube Link eingeben oder \'start\' um download zu starten: ')

for link in links:
    path = MP4_PATH + '\\' + link.title + '.mp4'
    link.download(MP4_PATH)
    video = VideoFileClip(path)
    video.audio.write_audiofile(link.title + '.mp3')
    shutil.move(HARD_CODED_PATH + '\\' + link.title + '.mp3', MP3_PATH + '\\' + link.title + '.mp3')
