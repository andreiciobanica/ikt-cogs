# -*- coding: utf-8 -*-
from redbot.core import commands
from redbot.core.data_manager import cog_data_path
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

import os
import psutil 
import sqlite3

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
        await ctx.send("Așteptați până se încarcă baza de date!")

        GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = str(cog_data_path(self) / "client_secret.json")
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)
        
        file_list = drive.ListFile({'q': "'1jZM6k4Cl4Kb_2CVXse_9ziY3GwJ4KpPR' in parents and trashed=false"}).GetList()
        numefile = file_list[0]['title']
        for file1 in file_list:
            if numefile <= file1['title']:
                numefile = file1['title']
                idfile = file1['id']
        f_ = drive.CreateFile({'id': idfile})
        f_.GetContentFile(numefile)
        await ctx.send("Baza de date s-a încărcat!")

        global ScriptDatabase
        pathdb = os.path.abspath(numefile)
        numedb = os.path.join(os.path.dirname(__file__), numefile)
        if (InstancedDatabase.is_open(pathdb)):
            ScriptDatabase.close
            
        ScriptDatabase = self.InstancedDatabase(numedb)
    
