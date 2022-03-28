#Developed by wodx @ 26-06-2019
import discord, subprocess, json, os, textwrap, time

#These commands are blacklisted, as they're pretty useless in this project. More can be added.
BLACKLISTED_COMMANDS = [
    'nano', 
    'leafpad',
    'wireshark',
    'zenmap'
]

#Operators which are used to run multiple bash commands at once.
OPERATORS = [';', '&&', '||']

CONFIG = json.loads(open('config/config.json').read())

last_process = None

def error(message):
    return discord.Embed(title='**ERROR**', description=message, colour=discord.Colour.red())

def warning(message):
    return discord.Embed(title='**WARNING**', description=message, colour=0xe7e33c)

def success(message):
    return discord.Embed(title='**SUCCESS**', description=message, colour=discord.Colour.green())

def command_history(command):
    return discord.Embed(title='**%s**' % (time.strftime('%H:%M:%S')), description=command, colour=discord.Colour.blue())

def print_banner():
    print ('''
            ╔═╗╦╔╗ ╔═╗╦═╗  ╔═╗╔═╗╔═╗       { Github: WodXTV }
            ║  ║╠╩╗║╣ ╠╦╝  ╚═╗║╣ ║         { Discord: wodx#0666 }
            ╚═╝╩╚═╝╚═╝╩╚═  ╚═╝╚═╝╚═╝ v1.6  { Twitter: @WodXOfficial }
               Cyber Security Bot
      Submission for Discord Hack Week 2019
        ''')

def main():
    #Bot token check
    token = CONFIG['config']['token']
    if not token or len(token) != 59 or not '.' in token:
        print('[-] Invalid token.')
        exit()

    #OS check
    if not os.name == 'posix':
        print('[-] CiberSec has to be run on a Linux machine.')
        exit()

    print('[*] Starting CiberSec bot...')

    #Creating new client
    client = discord.Client()

    #Ready event
    @client.event
    async def on_ready():
        #Printing banner of CiberSec
        print_banner()

        print('[+] CiberSec is ready to use.')

        await client.change_presence(activity=discord.Game('Discord Hack Week 2019'))
        await client.user.edit(username='CiberSec')
        with open('./resources/CyberSec-logo.png', 'rb') as file:
            await client.user.edit(avatar=file.read())

    #Message event
    @client.event
    async def on_message(event_message):
        global last_process

        #User check
        if event_message.author == client.user:
            return

        #Role check
        has_role = None
        for role in event_message.author.roles:
            if str(role).lower() == 'cibersec user':
                has_role = True
                break
        if not has_role:
            return

        #Channel check
        event_channel = event_message.channel
        if event_channel.id != int(CONFIG['config']['terminal']):
            return

        try:
            command = str(event_message.content)

            #Command analyzing
            for operator in OPERATORS:
                if ' %s ' % (operator) in command:
                    command_split = command.split(' %s ' % (operator))
                    for cmd in command_split:
                        for cmd_blacklisted in BLACKLISTED_COMMANDS:
                            if cmd.startswith(cmd_blacklisted):
                                await event_channel.send(embed=error('The executed command contains a blacklisted command.'))
                                return
            for cmd_blacklisted in BLACKLISTED_COMMANDS:
                if command.lower().startswith(cmd_blacklisted):
                    await event_channel.send(embed=error('The executed command is blacklisted.'))
                    return

            #Clear command
            if 'clear' in command.lower():
                if 'clear history' in command.lower():
                    await client.get_channel(int(CONFIG['config']['history'])).purge(limit=1000)
                    await event_channel.send(embed=success('Command history has been cleared.'))
                else:
                    await event_channel.purge(limit=1000)
                    await event_channel.send(embed=success('Terminal has been cleared.'))
                return

            #Change directory command
            if 'cd ' in command:
                command_split = command.split(' ')
                for i, cmd in enumerate(command_split):
                    if cmd == ' ':
                        continue
                    if cmd.lower() == 'cd':
                        os.chdir(command_split[i + 1])
                        output = 'Changed directory to %s' % (os.getcwd())
                        await event_channel.send('```\n%s\n```' % (output))
                        return
            
            #Cancel command
            if command.lower() == 'cancel':
                if last_process:
                    last_process.kill()
                    last_process = None
                    await event_channel.send(embed=success('Process canceled.'))
                else:
                    await event_channel.send(embed=warning('Not process is running.'))
                return
                            
            #Executing the shell command
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            last_process = process

            #Command output
            output = (process.stdout.read() + process.stderr.read()).decode()

            #Adding command to history
            try:
                await client.get_channel(int(CONFIG['config']['history'])).send(embed=command_history('`\n%s\n`' % (command)))
            except:
                await event_channel.send(embed=error('Command history channel not found.'))
                return

            #Handling +2000 chars output
            if len(output) >= 2000:
                async with event_channel.typing():
                    await event_channel.send(embed=warning('Output is more than 2000 characters long. Please wait while all data is getting transferred.'))
                    for output_piece in [output[i * 1000 : i * 1000 + 1000] for i, _ in enumerate(output[::1000])]:
                        await event_channel.send('```\n%s\n```' % (output_piece))
                    await event_channel.send(embed=success('All data has been transferred.'))
                    return

            #Returning the output
            if output.strip():
                await event_channel.send('```\n%s\n```' % (output))
            else:
                await event_channel.send(embed=error('No output recieved.'))

        except Exception as e:
            await event_channel.send(embed=error('An error occurred: %s' % (e)))
            exit()

    #Making the bot run
    client.run(CONFIG['config']['token'])

if __name__ == '__main__':
    main()