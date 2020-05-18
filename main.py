#!/usr/bin/python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import base64

def getLyrics(lId=2605732):
    clientAppId = open('clientAppId').readline().strip('\n')
    lyricsId = lId
    remoteAddr = r'https://p1.petitlyrics.com/api/GetPetitLyricsData.php'
    postHeaders = {'Content-type': 'application/x-www-form-urlencoded', 'charset': 'utf-8'}
    postData = str('key_lyricsId=' + str(lyricsId) + '&lyricsType=3&terminalType=10&clientAppId=' + clientAppId)
    response = requests.post(remoteAddr, headers=postHeaders, data=postData).content
    soup = BeautifulSoup(response, "xml")
    initialBase64 = str(soup.find('lyricsData'))[12:-13]
    syncLyricXml = str(base64.b64decode(initialBase64), 'utf8')
    return syncLyricXml

if __name__ == "__main__":
    lId = input("Please input Lyric ID from Petit Lyrics: ")
    print(getLyrics(lId=lId))