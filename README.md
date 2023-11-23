## Python Video Thumbnail 
Python Video Thumbnail is a Free and OpenSource thumbnail generator for videos hosted on remote server. It provide an useful API Endpoint to easily integrate this feature in all your apps.

**Requirements**:

 - Python3
 - FFMPEG Library
# How to use
Since this script provide only one GET endpoint, it's pretty easy to use it, lets see how to create a request:

    https://yourserver.ltd/screenshot?video_source=[remote_video]&seconds=[seconds]
  
    https://yourserver.ltd/screenshot?video_source=http://yourvideo.lt/video.mp4&seconds=10

 You just need to change the value of video_source and seconds. As response you'll receive a jpeg image of the video at that specific seconds. That's it.

