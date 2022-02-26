from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.types import CallbackQuery as cbq
from pyrogram.errors.exceptions.bad_request_400 import MessageEmpty, MessageNotModified
from config import BOT_TOKEN, RESULTS_COUNT, SUDO_CHATS_ID, API_ID, API_HASH
from drive import drive

app = Client(":memory:", bot_token=BOT_TOKEN, api_id=API_ID,
             api_hash=API_HASH)

i = 0
ii = 0
m = None
keyboard = None
data = None
user_id = None


@app.on_message(filters.command("start") & ~filters.edited & filters.chat(SUDO_CHATS_ID))
async def start_command(_, message):
    await message.reply_text("What did you expect to happen? Try /help")


@app.on_message(filters.command("help") & ~filters.edited)
async def help_command(_, message):
    await message.reply_text("/search [Query]")


@app.on_message(filters.command("search") & ~filters.edited & filters.chat(SUDO_CHATS_ID))
async def search(_, message: Message):
    global i, m, data, user_id
    if len(message.command) < 2:
        await message.reply_text('/seach Filename')
        return
    query = message.text.split(' ',maxsplit=1)[1]
    m = await message.reply_text("**Searching....**")
    data = drive.drive_list(query)
    # Anon Admin or That User!
    user_id = 1087968824
    if message.from_user:
        user_id = message.from_user.id

    results = len(data)
    i = 0
    i = i + RESULTS_COUNT

    if results == 0:
        await m.edit(text="Found Literally Nothing.")
        return

    text = f"**Total Results:** __{results}__\n"
    for count in range(min(i, results)):
        if data[count]['type'] == "file":
            text += f"""
📄  [{data[count]['name']}
**Size:** __{data[count]['size']}__
**[Drive Link]({data[count]['drive_url']})** | **[Index Link]({data[count]['url']})**\n"""

        else:
            text += f"""
📂  __{data[count]['name']}__
**[Drive Link]({data[count]['drive_url']})** | **[Index Link]({data[count]['url']})**\n"""
    if len(data) > RESULTS_COUNT:
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="<<   Previous",
                        callback_data="previous"
                    ),
                    InlineKeyboardButton(
                        text="Next   >>",
                        callback_data="next"
                    )
                ],
                [InlineKeyboardButton("Close ⬇️", callback_data="closeMeh")]
            ]
        )
        try:
            await m.edit(text=text, disable_web_page_preview=True, reply_markup=keyboard)
        except (MessageEmpty, MessageNotModified):
            pass
        return
    try:
        await m.edit(text=text, disable_web_page_preview=True)
    except (MessageEmpty, MessageNotModified):
        pass


@app.on_callback_query(filters.regex("previous"))
async def previous_callbacc(_, CallbackQuery: cbq):
    global i, ii, m, data, user_id
    if user_id != CallbackQuery.from_user.id:
        await CallbackQuery.answer("Ser, You are not allowed to access other's Search Results!", show_alert=True)
        return
    if i < RESULTS_COUNT:
        await CallbackQuery.answer(
            "Already at 1st page, Can't go back.",
            show_alert=True
        )
        return
    ii -= RESULTS_COUNT
    i -= RESULTS_COUNT
    text = ""

    for count in range(ii, i):
        try:
            if data[count]['type'] == "file":
                text += f"""
📄  [{data[count]['name']}
**Size:** __{data[count]['size']}__
**[Drive Link]({data[count]['drive_url']})** | **[Index Link]({data[count]['url']})**\n"""

            else:
                text += f"""
📂  __{data[count]['name']}__
**[Drive Link]({data[count]['drive_url']})** | **[Index Link]({data[count]['url']})**\n"""
        except IndexError:
            continue

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="<<   Previous",
                    callback_data="previous"
                ),
                InlineKeyboardButton(
                    text="Next   >>",
                    callback_data="next"
                )
            ],
            [
                InlineKeyboardButton("Close ⬇️", callback_data="closeMeh")
            ]
        ]
    )
    try:
        await m.edit(text=text, disable_web_page_preview=True, reply_markup=keyboard)
    except (MessageEmpty, MessageNotModified):
        pass


@app.on_callback_query(filters.regex("next"))
async def next_callbacc(_, cb: cbq):
    global i, ii, m, data, user_id
    if user_id != cb.from_user.id:
        await cb.answer("Ser, You are not allowed to access other's Search Results!", show_alert=True)
        return
    ii = i
    i += RESULTS_COUNT
    text = ""

    for count in range(ii, i):
        try:
            if data[count]['type'] == "file":
                text += f"""
📄  [{data[count]['name']}
**Size:** __{data[count]['size']}__
**[Drive Link]({data[count]['drive_url']})** | **[Index Link]({data[count]['url']})**\n"""

            else:
                text += f"""
📂  __{data[count]['name']}__
**[Drive Link]({data[count]['drive_url']})** | **[Index Link]({data[count]['url']})**\n"""
        except IndexError:
            continue

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="<<   Previous",
                    callback_data="previous"
                ),
                InlineKeyboardButton(
                    text="Next   >>",
                    callback_data="next"
                )
            ],
            [
                InlineKeyboardButton("Close ⬇️", callback_data="closeMeh")
            ]
        ]
    )
    try:
        await m.edit(text=text, disable_web_page_preview=True, reply_markup=keyboard)
    except (MessageEmpty, MessageNotModified):
        pass


@app.on_callback_query(filters.regex("closeMeh"))
async def close_cb(_, cb: cbq):
    global user_id
    if user_id != cb.from_user.id:
        await cb.answer("Ser, You are not allowed to access other's Search Results!", show_alert=True)
        return
    await cb.message.delete(True)


app.run()
