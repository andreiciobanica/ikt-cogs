# -*- coding: utf-8 -*-
from redbot.core import commands
from redbot.core.data_manager import cog_data_path
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = cog_data_path("client_secret.json")

import os
import psutil 
import sqlite3

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

global ScriptDatabase

class Diamante(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    class InstancedDatabase(object):
        def __init__(self, databasefile):
            self._connection = sqlite3.connect(databasefile, check_same_thread=False)
            self._cursor = self._connection.cursor()

        def execute(self, sqlquery, queryargs=None):
            if queryargs:
                self._cursor.execute(sqlquery, queryargs)
            else:
                self._cursor.execute(sqlquery)
            return self._cursor

        def commit(self):
            self._connection.commit()

        def close(self):
            self._connection.close()
            return

        def __del__(self):
            self._connection.close()
            
        def is_open(path):
            for proc in psutil.process_iter():
                try:
                    files = proc.get_open_files()
                    if files:
                        for _file in files:
                            if _file.path == path:
                                return True    
                except psutil.NoSuchProcess as err:
                    print(err)
            return False

    @commands.command(name="dbupdate")
    async def dbupdate(self, ctx):
        await ctx.send("AÈ™teptaÈ›i pentru a se Ã®ncÄƒrca baza de date!")
        
        file_list = drive.ListFile({'q': "'1jZM6k4Cl4Kb_2CVXse_9ziY3GwJ4KpPR' in parents and trashed=false"}).GetList()
        numefile = file_list[0]['title']
        for file1 in file_list:
            if numefile <= file1['title']:
                numefile = file1['title']
                idfile = file1['id']
        f_ = drive.CreateFile({'id': idfile})
        f_.GetContentFile(numefile)
        await ctx.send("Baza de date s-a Ã®ncÄƒrcat!")

        global ScriptDatabase
        pathdb = os.path.abspath(numefile)
        numedb = os.path.join(os.path.dirname(__file__), numefile)
        if (is_open(pathdb)):
            ScriptDatabase.close
            
        ScriptDatabase = InstancedDatabase(numedb)
    
