import os
import traceback

import discord
from discord.ext import commands

def read_token_from_env():
    token_from_env = os.getenv('AMSC_BOT_TOKEN')
    if not token_from_env:
        raise Exception('Token not found in environment variables')
    
    print(f'Token from env: {token_from_env[:3]}...')
    return token_from_env

def initialize_bot():    
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True 
    intents.guilds = True
    bot = commands.Bot(command_prefix='>', intents=intents)
    return bot

def main():
    try:
        TOKEN = read_token_from_env()
        bot = initialize_bot()
        
        @bot.command(name='ping')
        async def ping(ctx):
            print('Ping command received')
            await ctx.send('Pong!')
            
        @bot.command(name='start')
        async def start(ctx):
            print('Start command received')
            await ctx.send('<start-server>')
            
        @bot.command(name='stop')
        async def stop(ctx):
            print('Stop command received')
            await ctx.send('<stop-server>')
        
        bot.run(TOKEN)

    except Exception as e:
        print(e, 'Run failed')
        print(f'\n{traceback.format_exc()}')

    finally:
        print('Bot has stopped running')

if __name__ == '__main__':
    main()