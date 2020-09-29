import discord
from discord.ext import commands
from discord import Embed
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import asyncio 
import requests
import random
import shutil
from os import system






client = commands.Bot( command_prefix = '$' )
bad_words = ['хуй','ты еблан?','ты даун?','ты конч?','ты уёбок','ты чмо','ты конч','ты даун','ты еблан','уебись нахуй','сдохни от спида','ебаная шлюха','ебать ты тупой',
'ебать ты днище','тупой блять','нытик ебаный','мать жива?','педрила','животное ебливое','гандон сука','хуйца сосни','хуйца сосни школьница','днище ебаное','соси хуй',
'соси письку','соси дно тупорылое','глотни хуйца','ебланище','ебланище тупое','хуй соси','хуй соси еблан','ппиздец ты даун','тупой еблан','сын шлюхи','гандон ебаный',
'пиздец','нахуй','ебать','уебись','еблан','ебаное','гандон','гондон','ебаный','Хуесос','Залупа','Залупа','захуярить','нихуя','Нехуй','Ни хуя себе','Охуевать','Охуенно',
'Похую','Соси хуй','Хуёво','Пизда','Хуй его знает','Хуеплёт','Хуета','иди нахуй','даун тупой','даун','хуй забей','пиздец тупой','пиздец ты тупой','пиздец тупоой',
'пиздец ты тупоой','пиздец я тупой','нахуй иди','нахуй иди даун','нахуй вали','нахуй проваливай','нахуй сука','нахуй блять','ебать я тупой','ебать я тупоой','хуй знает',
'хуйня','это все хуйня','иди нахуй чмо','сосни хуйца','сосни хуйцы школьница']
#@
client.remove_command('help') # Удаляем изначальную команду "help" 

#ошибки

#command error
@client.event
async def on_command(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send( f'{ ctx.author.name }, укажи аргумент' )

#нет такой команды 

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send( f'{ ctx.author.name }, Такой команды не существует!' )

#clear error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument ):
		await ctx.send( f'{ ctx.author.name }, пожалуйста, укажи количество сообщений для удаления.')


#@client.event
#async def on_ready():
    #играет
    #await client.change_presence(activity=discord.Game(name="on {len(client.guilds')} servers | $help")
    #стримит
    #await client.change_presence(activity=discord.Streaming(name="My Stream", url=My_twich_url))
    # слушает
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="моргена"))
    # смотрит
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="за сервером COFFIMIXA"))
    #print("Ready")

#async def ch_pr():
    #await client.wait_until_ready()

    #statuses = ["a game", f"on {len(client.guilds)} servers | $help0", "discord.py"]

    #while not client.is_closed():

        #status = random.choice(statuses)
        #await client.change_presence(activity=discord.Game(name=status))

        #await asyncio.sleep(10)
        

#client.loop.create_task(ch_pr())
#client.run()


    

#random

@client.event
async def on_ready():
	print("The bot is ready!")
	
@client.command(pass_context = True)
async def random_10(ctx):
	await ctx.send(random.randint(1,11))
@client.command(pass_context = True)
async def random_20(ctx):
	await ctx.send(random.randint(1,21))
@client.command(pass_context = True)
async def random_30(ctx):
	await ctx.send(random.randint(1,31))
@client.command(pass_context = True)
async def random_40(ctx):
	await ctx.send(random.randint(1,41))
@client.command(pass_context = True)
async def random_50(ctx):
	await ctx.send(random.randint(1,51))
@client.command(pass_context = True)
async def random_60(ctx):
	await ctx.send(random.randint(1,61))
@client.command(pass_context = True)
async def random_70(ctx):
	await ctx.send(random.randint(1,71))
@client.command(pass_context = True)
async def random_80(ctx):
	await ctx.send(random.randint(1,81))
@client.command(pass_context = True)
async def random_90(ctx):
	await ctx.send(random.randint(1,91))
@client.command(pass_context = True)
async def random_100(ctx):
	await ctx.send(random.randint(1,101))



#roli
@client.event

async def on_member_join( member ):
	channel = client.get_channel( 585550248504721419 )

	role = discord.utils.get( member.guild.roles, id = 759687650100641822 )

	await member.add_roles( role )
	await channel.send( embed = discord.Embed( description = f'Пользователь ``{ member.name }``, Залетел к нам!', color = 0x0c0c0c,) )



#BOT_MESSEGE!!!!!!!!!!!!!!!!!!!!

@client.command()
async def send( ctx, member: discord.Member ):
	await member.send( f'{ member.name }, привет от { ctx.author.name } ' )

#BOT_MESSEGE!!!!!!!!!!!!!!!!!!!!


#clear message
@client.command(pass_context = True, aliases=['cl','CL'])
@commands.has_permissions( administrator = True )

async def clear( ctx, amount = 10000 ):
	await ctx.channel.purge( limit = amount )
	await ctx.send(embed = discord.Embed(description = f':white_check_mark: Удалено {amount} сообщений', color = 0x0c0c0c, ) )

# Kick
@client.command(pass_context = True, aliases=['KICK'])
@commands.has_permissions( administrator = True )
 
async def kick( ctx, member: discord.Member, *, reason = None ):
    await ctx.channel.purge( limit = 1 )
    await member.kick( reason = reason )
 
    emb = discord.Embed( title = 'Информация о кике', description = f'{ member.name.title() }, был кикнут в связи c нарушением правил',
    color = 0x979c9f )
 
    emb.set_author( name = member, icon_url = member.avatar_url )
    emb.set_footer( text = f'Был кикнут администратором { ctx.message.author.name }', icon_url = ctx.author.avatar_url )
 
    await ctx.send( embed = emb )
    

#ban
@client.command( pass_context = True, aliases=['BAN'] )
@commands.has_permissions( administrator = True )

async def ban( ctx, member: discord.Member, *, reason = None ):
	emb = discord.Embed( title = 'Ban', color = discord.Color.red())
	await ctx.channel.purge( limit = 1 )

	await member.ban( reason = reason )

	emb.set_author( name = member, icon_url = member.avatar_url )
	emb.add_field( name = 	'забанен ' , value = 'игрок : {}'.format(member.mention) )
	emb.set_footer( text = 'Был забанен Администратором {}'.format(ctx.author.name ), icon_url = ctx.author.avatar_url )

	await ctx.send( embed = emb )

#unban
@client.command(pass_context=True, aliases=['UNBAN'])
async def unban(ctx, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split("#")

	for banned_entry in banned_users:
		user = banned_entry.user
	if (user.name, user.discriminator) == (member_name, member_discriminator):
		await ctx.guild.unban(user)
		await ctx.send( f"{user} разбанен")
		return



#отправить сообщения 
@client.command()
async def maniak( ctx, member: discord.Member ):
	await member.send(f'{ member.name}, привет не хочешь ли ты поиграть в маньяка? пиши на сервере COFFIMIXA или мне в лс { ctx.author.name }' )


# filter
@client.event
async def on_message( message, ):
	await client.process_commands( message )

	msg = message.content.lower()

	if msg in bad_words:
		await message.delete()
		await message.author.send( f'{ message.author.name }, давай без мата!!! Если так будет дальше, то Админ тебя забанит!')


#commandhelp
@client.command()
async def help( ctx ):
    emb = discord.Embed( 
        title = 'КОМАНДЫ :clipboard:',
        color = 0x7aa13d
     )
 
    emb.add_field( name = '**ДЛЯ МУЗЫКИ**', value = '''
        :robot:$join ; $j ; $joi :robot:   добавить бота в голосовой канал 
        :headphones:$play; $p; $pl ссылка :headphones: - воспроизвести музыку 
        :robot:$leave ; $le :robot:-     убрать бота из голосового канала 
        :pause_button:$pause ; $p ; $pau :pause_button: - поставить бота на паузу 
        :record_button:$resume ; $r ; $res :record_button: - снять с паузы бота 
        :stop_button:$stop ; $s ; $st :stop_button: - остановить музыку 
        :musical_note:$q ссылка :musical_note: - поставить музыку в очередь 
        :track_next: $next ; $n ; $nex:track_next:  - следующая музыка в очереди 
        ''' )
 
    emb.add_field( name = '**КОМАНДЫ ДЛЯ ИГРОКОВ**', value = '''
        :woman_detective:$maniak @user:woman_detective: - позвать играть в маньяка 
        :1234:$random_10:1234: - рандомное число (20,30,40,50,60,70,80,90,100)
        :robot:$maps:robot:  - в следующих обновлениях 
        ''' )
    emb.add_field( name = '**КОМАНДЫ ДЛЯ АДМИНОВ**', value = '''
        :face_with_symbols_over_mouth:$ban ; $BAN @user:face_with_symbols_over_mouth: - БАН 
        :rage:$kick ; $KICK @user:rage: - КИК 
        :innocent:$unban ; $UNBAN user#2134:innocent: - разбанить 
        :wastebasket:$clear ; $cl ; $CL  число :wastebasket:- очистить чат 
        ''' )

 
    await ctx.send( embed = emb )

@client.command()
async def ip_info( ctx, arg ):
    response = requests.get( f'http://ipinfo.io/{ arg }/json' )
 
    user_ip = response.json()[ 'ip' ]
    user_city = response.json()[ 'city' ]
    user_region = response.json()[ 'region' ]
    user_country = response.json()[ 'country' ]
    user_location = response.json()[ 'loc' ]
    user_org = response.json()[ 'org' ]
    user_timezone = response.json()[ 'timezone' ]
 
    global all_info
    all_info = f'\n<INFO>\nIP : { user_ip }\nCity : { user_city }\nRegion : { user_region }\nCountry : { user_country }\nLocation : { user_location }\nOrganization : { user_org }\nTime zone : { user_timezone }'
 
    await ctx.author.send( all_info )


@client.command( pass_context = True )
#.hello
async def hello( ctx ):
	author = ctx.message.author

	await ctx.send( f'Привет {author.mention} я бот COFFIMIXA! Что хотел спросить? напиши !helpd' )

# voice chat

#1

@client.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")

    await ctx.send(f"Бот присоеденился к голосовому каналу {channel}")


@client.command(pass_context=True, aliases=['l', 'le'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"Бот покинул голосовой канал: {channel}")
        await ctx.send(f"покинул голосовой канал {channel}")
    else:
        print("Bot was told to leave voice channel, but was not in one")
        await ctx.send("Бот не находился ни в одном голосовом канале")


@client.command(pass_context=True, aliases=['p', 'pl'])
async def play(ctx, url: str):

    def check_queue():
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("Queue"))
            length = len(os.listdir(DIR))
            still_q = length - 1
            try:
                first_file = os.listdir(DIR)[0]
            except:
                print("No more queued song(s)\n")
                queues.clear()
                return
            main_location = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first_file)
            if length != 0:
                print("Song done, playing next queued\n")
                print(f"Songs still in queue: {still_q}")
                song_there = os.path.isfile("song.mp3")
                if song_there:
                    os.remove("song.mp3")
                shutil.move(song_path, main_location)
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, 'song.mp3')

                voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.07

            else:
                queues.clear()
                return

        else:
            queues.clear()
            print("No songs were queued before the ending of the last song\n")



    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            queues.clear()
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("Ошибка: воспроизведение музыки")
        return


    Queue_infile = os.path.isdir("./Queue")
    try:
        Queue_folder = "./Queue"
        if Queue_infile is True:
            print("Removed old Queue Folder")
            shutil.rmtree(Queue_folder)
    except:
        print("No old Queue folder")

    await ctx.send("Песня грузиться...")

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([url])
    except:
        print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if Spotify URL)")
        c_path = os.path.dirname(os.path.realpath(__file__))
        system("spotdl -f " + '"' + c_path + '"' + " -s " + url)

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit("-", 2)
    await ctx.send(f"Играет музыка: {nname[0]}")
    print("playing\n")


@client.command(pass_context=True, aliases=['pa', 'pau'])
async def pause(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music paused")
        voice.pause()
        await ctx.send("музыка на паузе")
    else:
        print("Music not playing failed pause")
        await ctx.send("Музыка не играет, неудачная пауза")


@client.command(pass_context=True, aliases=['r', 'res'])
async def resume(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print("Resumed music")
        voice.resume()
        await ctx.send("снята с паузы")
    else:
        print("Music is not paused")
        await ctx.send("нет музыки на паузе")


@client.command(pass_context=True, aliases=['s', 'st'])
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    queues.clear()

    queue_infile = os.path.isdir("./Queue")
    if queue_infile is True:
        shutil.rmtree("./Queue")

    if voice and voice.is_playing():
        print("Music stopped")
        voice.stop()
        await ctx.send("музыка остановилась")
    else:
        print("No music playing failed to stop")
        await ctx.send("Ни одна играющая музыка не прекращалась")


queues = {}

@client.command(pass_context=True, aliases=['q', 'que'])
async def queue(ctx, url: str):
    Queue_infile = os.path.isdir("./Queue")
    if Queue_infile is False:
        os.mkdir("Queue")
    DIR = os.path.abspath(os.path.realpath("Queue"))
    q_num = len(os.listdir(DIR))
    q_num += 1
    add_queue = True
    while add_queue:
        if q_num in queues:
            q_num += 1
        else:
            add_queue = False
            queues[q_num] = q_num
            queue_path = os.path.abspath(os.path.realpath("Queue") + f"\song{q_num}.%(ext)s")

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'outtmpl': queue_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([url])
    except:
        print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if Spotify URL)")
        q_path = os.path.abspath(os.path.realpath("Queue"))
        system(f"spotdl -ff song{q_num} -f " + '"' + q_path + '"' + " -s " + url)


    await ctx.send("добавлена в очередь , " + str(q_num) + " в очереди")

    print("Song added to queue\n")


@client.command(pass_context=True, aliases=['n', 'nex'])
async def next(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Playing Next Song")
        voice.stop()
        await ctx.send("следующая музыка")
    else:
        print("No music playing")
        await ctx.send("нет следующей музыки ")



    
    


token = os.environ.get('BOT_TOKEN')
