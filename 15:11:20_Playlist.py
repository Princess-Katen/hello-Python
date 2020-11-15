#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 13:27:05 2020

@author: tatyanamironova
"""

playlist = {"title": "Katten_drives", 
            "author": "Princess_Katen",
            "songs": [
                {"title": "song1", "artist": ['blue'], "duration": 2.5},
                {"title": "song2", "artist": ['kitty','djcat'], "duration": 5.5},
                {"title": "meowmeow", "artist": ['gardfield'], "duration": 2}
            ]
}

total_length = 0
for song in playlist['songs']:
    total_length += song["duration"]
print(total_length)