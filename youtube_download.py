# importing the module
from pytube import YouTube
import argparse

def get_audio():
    link = args.link
    
    try:
        yt = YouTube(link)
    except:
        print("Connection Error!")
    
    yt.streams.filter(progressive=True, only_audio=True)
    audio = yt.streams.get_by_itag(22)
    
    try:
        audio.download(SAVE_PATH)
    except:
        print("Connection Error!")
    print("Task Completed!")
    
def get_video():
    link = args.link
    
    try:
        yt = YouTube(link)
    except:
        print("Connection Error!")
       
    yt.streams.filter(progressive=True, file_extension="mp4")
    video = yt.streams.get_by_itag(22)
    
    try:
        video.download(SAVE_PATH)
    except:
        print("Connection Error!")
    print("Task Completed!")
    
parser = argparse.ArgumentParser(description="testing")
parser.add_argument('--link', type=str, required=True, help='put the link')

subparser = parser.add_subparsers(title='actions')
subparser.required = True
subparser.dest='command'
audio = subparser.add_parser('audio', add_help=False,help='Get audio from youtube')
video = subparser.add_parser('video', add_help=False, help='Get video from youtube')
# audio = subparser.add_parser('audio', parents=[parser], add_help=False,help='Get audio from youtube')
# video = subparser.add_parser('video', parents[parser], add_help=False, help='Get video from youtube')

args = parser.parse_args()

if args.command == 'audio':
    get_audio()
elif args.command == 'video':
    get_video()

# where to  save
# SAVE_PATH = "/home/ahmad/Downloads/"
SAVE_PATH = "/home/pc/Documents/"

