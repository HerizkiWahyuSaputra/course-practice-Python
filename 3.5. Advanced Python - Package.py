print("=====PACKAGE=====") 
# Package is manageable and reusable for the existing set of files has a good hierarchy
# simply, the module is the same as a file, while the package is the same as a folder

import Music.Playlist.play as Play
import Music.Playlist.pause as Pause
import Music.Playlist.load as Load

Play.play("Naruto - flow")
Pause.pause("Naruto - flow")
Load.load("Naruto - flow")