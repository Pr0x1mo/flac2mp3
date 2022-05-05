# pip install fastprogress
# pip install pydub
from pydub import AudioSegment
from pydub.utils import mediainfo
from fastprogress import progress_bar
import os
import glob
from pathlib import Path
from concurrent.futures.process import ProcessPoolExecutor
import concurrent


def convert(mp3folder):
    folder_with_albums = mp3folder  # Path with folders of flac files

    dirs = Path(mp3folder).glob('**/*.flac')
    #print('this is dirs', dirs)
    for ost in dirs:
        print("\nConverting ", ost, '\n')
        flac_audio = AudioSegment.from_file(ost, "flac")
        flac_audio.export(os.path.splitext(ost)[0] + ".mp3", format="mp3", bitrate="320k", tags=mediainfo(str(ost)).get('TAG', {}))

    print('\n\n')

if __name__ == "__main__":
    convert(r'C:\Users\xavie\Desktop\Pinback')