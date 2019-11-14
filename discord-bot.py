import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello! My name is Squeaky Robutt, and I\'m a robutt designed to give help & advice on mental health.')

    if message.content.startswith('!autism'):
        await message.channel.send('''Autism is a developmental disorder characterized by difficulties with social interaction and communication, and by restricted and repetitive behavior.
        As a robot, I also have some difficulties with interaction, and some restricted and repetitive behaviours, so I still think you're swell :)''')

    if message.content.startswith('!depression'):
        await message.channel.send('''Being depressed isn't your fault, you aren't a collection of poorly written python \'if\' statements like me.
        The NHS has some resources on clinical depression: https://www.nhs.uk/conditions/clinical-depression/ You can book a GP appointment to discuss your issues with a doctor.
        Remember to call someone if you feel a danger to yourself, or ring the Samaritans if it\'s really serious.''')

client.run('NjQ0MjU0NjE0NjMxMzUwMjgz.XcxXCw.8yRQjVY6bUQWhyb1D0Fd3yw_Jxg')