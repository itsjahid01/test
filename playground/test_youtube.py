import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
dotagent_dir = os.path.abspath(os.path.join(script_dir, ".."))
sys.path.append(dotagent_dir)


from dotagent.helpers.youtubeSearch import YouTubeSearchTool
from dotagent.helpers.youtubeTranscript import YoutubeTranscriptReader
YoutubeSearch = YouTubeSearchTool()

print(YoutubeSearch.run("Samay Raina"))

loader  = YoutubeTranscriptReader()
docs = loader.load_data(ytlinks=['https://www.youtube.com/watch?v=i3OYlaoj-BM'])

print(docs)

#Requires installing
#pip install youtube_search
#pip install youtube_transcript_api