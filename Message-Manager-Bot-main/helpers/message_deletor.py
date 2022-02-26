# (c) @AbirHasan2005

async def delete_message(message):
    try:
        await message.delete(True)
    except:
        pass
