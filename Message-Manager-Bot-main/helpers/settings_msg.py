# (c) @AbirHasan2005

from database.access_database import mongodb
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def show_settings(message: Message):
    """ Pass a Editable Message by of Bot Client to Edit it with Settings Buttons & Message! """
    # Primary Markup Button
    markup = [[InlineKeyboardButton("🔰 Setup Custom Filters 🔰", callback_data="setCustomFilters")]]
    # Setup for Blocked Words
    blocked_words = await mongodb.get_blocked_words(message.chat.id)
    block_specific_words_button = [InlineKeyboardButton("Block Specific Words", callback_data="blockWords")]
    if blocked_words is not None:
        block_specific_words_button.append(InlineKeyboardButton("Show 👀", callback_data="showBlockedWords"))
    # Setup for Blocked Extensions
    blocked_extensions = await mongodb.get_blocked_exts(message.chat.id)
    block_specific_extensions_button = [InlineKeyboardButton("Block File Extensions", callback_data="blockFileExtensions")]
    if blocked_extensions is not None:
        block_specific_extensions_button.append(InlineKeyboardButton("Show 👀", callback_data="showBlockedExtensions"))
    # Append All Buttons Together
    markup.append(block_specific_words_button)
    markup.append(block_specific_extensions_button)
    markup.append([InlineKeyboardButton(f"Delete Service Messages {'✅' if (await mongodb.allowServiceMessageDelete(message.chat.id)) is True else '❌'}", callback_data="allowServiceMessagesDelete")])
    markup.append([InlineKeyboardButton("Close ❎", callback_data="closeMeh")])
    # Show Via Message Markup Buttons
    await message.edit(
        text="Here You Can Set Settings for this Chat:",
        reply_markup=InlineKeyboardMarkup(markup)
    )