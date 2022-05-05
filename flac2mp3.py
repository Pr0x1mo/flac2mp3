# pip install pydub
from pydub import AudioSegment
from pydub.utils import mediainfo
import os
import glob



def convert(mp3folder):

    dirs = Path(mp3folder).glob('**/*.flac')

    for ost in dirs:
        print("\nConverting ", ost, '\n')
        flac_audio = AudioSegment.from_file(ost, "flac")
        flac_audio.export(os.path.splitext(ost)[0] + ".mp3", format="mp3", bitrate="320k", tags=mediainfo(str(ost)).get('TAG', {}))

    print('\n\n')

if __name__ == "__main__":
    convert(r'your_folder_with_flac')
