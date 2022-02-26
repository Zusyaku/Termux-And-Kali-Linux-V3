# (c) @AbirHasan2005

import os
import time
import asyncio
import aiohttp
from configs import Config
from pyrogram import Client, filters, errors
from core.display_progress import progress_for_pyrogram, humanbytes
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQueryResultArticle, \
    InputTextMessageContent, InlineQuery

Bot = Client(Config.SESSION_NAME, bot_token=Config.BOT_TOKEN, api_id=Config.API_ID, api_hash=Config.API_HASH)


@Bot.on_message(filters.command("start"))
async def start_handler(_, cmd):
    await cmd.reply_text(
        "HI, I am Cloud Uploads Manager Bot!\n\nI can Do a Lot of Things, Check > /help <",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Developer", url="https://t.me/AbirHasan2005"),
                 InlineKeyboardButton("Support Group", url="https://t.me/linux_repo")],
                [InlineKeyboardButton("Bots Channel", url="https://t.me/Discovery_Updates")],
                [InlineKeyboardButton("Bot's Source Code", url="https://github.com/AbirHasan2005/Cloud-UPManager-Bot")]
            ]
        )
    )


@Bot.on_message(filters.command("help"))
async def help_handler(_, cmd):
    await cmd.reply_text(
        Config.HELP_TEXT,
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Support Group", url="https://t.me/linux_repo"),
                 InlineKeyboardButton("Developer", url="https://t.me/AbirHasan2005")],
                [InlineKeyboardButton("Delete GoFile.io File", switch_inline_query_current_chat="!godel ")],
                [InlineKeyboardButton("Delete Streamtape File (Admin Only)",
                                      switch_inline_query_current_chat="!stdel ")],
                [InlineKeyboardButton("Rename Streamtape File (Admin Only)",
                                      switch_inline_query_current_chat="!strename ")],
                [InlineKeyboardButton("Add Remote URL in Streamtape", switch_inline_query_current_chat="!stremote ")],
                [InlineKeyboardButton("Get Status of Streamtape Token", switch_inline_query_current_chat="!show ")],
                [InlineKeyboardButton("Remove Remote URL (Admin Only)", switch_inline_query_current_chat="!strmdel ")],
                [InlineKeyboardButton("Show Configs (Admin Only)", callback_data="showcreds")]
            ]
        )
    )


@Bot.on_message(filters.private & filters.media)
async def _main(_, message):
    await message.reply_text(
        "Where you want to Upload?",
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Upload to GoFile.io", callback_data="uptogofile"),
                 InlineKeyboardButton("Upload to Streamtape", callback_data="uptostreamtape")]
            ]
        ),
        quote=True
    )


@Bot.on_inline_query()
async def answer(bot, query: InlineQuery):
    answers = []
    string = query.query.lower()
    search_query = query.query
    if string == "":
        answers.append(
            InlineQueryResultArticle(
                title="Help & Usage",
                input_message_content=InputTextMessageContent(Config.HELP_TEXT, disable_web_page_preview=True,
                                                              parse_mode="Markdown"),
                description="Documention of How to Use this Bot.",
                thumb_url="https://i.imgur.com/6jZsMYG.png",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Support Group", url="https://t.me/linux_repo"),
                         InlineKeyboardButton("Developer", url="https://t.me/AbirHasan2005")],
                        [InlineKeyboardButton("Delete GoFile.io File", switch_inline_query_current_chat="!godel ")],
                        [InlineKeyboardButton("Delete Streamtape File (Admin Only)",
                                              switch_inline_query_current_chat="!stdel ")],
                        [InlineKeyboardButton("Rename Streamtape File (Admin Only)",
                                              switch_inline_query_current_chat="!strename ")],
                        [InlineKeyboardButton("Add Remote URL in Streamtape",
                                              switch_inline_query_current_chat="!stremote ")],
                        [InlineKeyboardButton("Get Status of Streamtape Token",
                                              switch_inline_query_current_chat="!show ")],
                        [InlineKeyboardButton("Remove Remote URL (Admin Only)",
                                              switch_inline_query_current_chat="!strmdel ")],
                        [InlineKeyboardButton("Show Configs (Admin Only)", callback_data="showcreds")]
                    ]
                )
            )
        )
        await bot.answer_inline_query(
            query.id,
            results=answers,
            switch_pm_text="How to Use Me?",
            switch_pm_parameter="help",
            cache_time=0
        )
    elif search_query.startswith("!stdel"):
        if not int(query.from_user.id) == Config.BOT_OWNER:
            answers.append(
                InlineQueryResultArticle(
                    title="You Can't Do That!",
                    description="This is only for Bot Owner!",
                    input_message_content=InputTextMessageContent(
                        message_text="This is only for Bot Owner!\n\nOnly Developer have Streamtape File Delete Rights!"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("Support Group", url="https://t.me/linux_repo")],
                            [InlineKeyboardButton("Developer", url="https://t.me/linux_repo")]
                        ]
                    )
                )
            )
        else:
            try:
                await asyncio.sleep(5)  # Waiting for 5 Sec for getting Correct User Input!
                async with aiohttp.ClientSession() as session:
                    api_link = "https://api.streamtape.com/file/delete?login={}&key={}&file={}"
                    main_text = None
                    splited = None
                    token = None
                    try:
                        main_text = search_query.split("!stdel ")[1]
                        splited = main_text.split(" ")[0]
                        token = splited.split("/")[4]
                    except IndexError:
                        print("Got IndexError - Skiping [token]")
                        main_text = ""
                        splited = ""
                        token = ""
                    except Exception as error:
                        print(f"Got Error - {error} - Skiping [token]")
                        main_text = ""
                        splited = ""
                        token = ""
                    if token == "":
                        answers.append(
                            InlineQueryResultArticle(
                                title="!stdel [file_link]",
                                description="Put File Link to Delete Streamtape File!",
                                input_message_content=InputTextMessageContent(
                                    message_text="This for Deleting Streamtape File via File Link.\n\n**Format:** `@Cloud_UPManager_Bot !stdel `__[file_link]__",
                                    parse_mode="Markdown",
                                    disable_web_page_preview=True
                                ),
                                reply_markup=InlineKeyboardMarkup(
                                    [
                                        [InlineKeyboardButton("Delete Streamtape File",
                                                              switch_inline_query_current_chat="!stdel ")]
                                    ]
                                )
                            )
                        )
                    else:
                        delete = await session.get(
                            api_link.format(Config.STREAMTAPE_API_USERNAME, Config.STREAMTAPE_API_PASS, token))
                        data = await delete.json()
                        status = data['msg']
                        if status == "OK":
                            answers.append(
                                InlineQueryResultArticle(
                                    title="Deleted File!",
                                    description=f"Deleted [{token}]",
                                    input_message_content=InputTextMessageContent(
                                        message_text=f"**Deleted:** {splited}\n\n**File Token:** `{token}`",
                                        parse_mode="Markdown",
                                        disable_web_page_preview=True
                                    )
                                )
                            )
                            await bot.send_message(chat_id=Config.LOG_CHANNEL,
                                                   text=f"#STREAMTAPE_DELETE:\n\n[{query.from_user.first_name}](tg://user?id={query.from_user.id}) Deleted Streamtape File !!\n\n**File Name:** {splited}\n\n**File Token:** `{token}`",
                                                   parse_mode="Markdown", disable_web_page_preview=True)
                        else:
                            answers.append(
                                InlineQueryResultArticle(title="File Not Deleted!",
                                                         description=f"Can't Delete [{token}]",
                                                         input_message_content=InputTextMessageContent(
                                                             message_text=f"Can't Delete - {splited}\nUsing [{token}]",
                                                             disable_web_page_preview=True, parse_mode="Markdown"))
                            )
            except Exception as err:
                answers.append(
                    InlineQueryResultArticle(title="Something Went Wrong!", description=f"Error: {err}",
                                             input_message_content=InputTextMessageContent(
                                                 message_text=f"Something Went Wrong!\n\n**Error:** `{err}`"),
                                             reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Support Group",
                                                                                                      url="https://t.me/linux_repo")]]))
                )

        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text="Error: Search timed out!",
                switch_pm_parameter="help"
            )
    elif search_query.startswith("!godel"):
        try:
            await asyncio.sleep(5)  # Waiting for 5 Sec for getting Correct User Input!
            async with aiohttp.ClientSession() as session:
                api_link = "https://apiv2.gofile.io/deleteUpload?c={}&ac={}"
                main_text = None
                splited = None
                token = None
                adminCode = None
                try:
                    main_text = search_query.split("!godel ")[1]
                    splited = main_text.split(" ")[0]
                    token = splited.split("/")[4]
                    adminCode = main_text.split(" ", 1)[1]
                except IndexError:
                    print("Got IndexError - Skiping [token] [adminCode]")
                    main_text = ""
                    splited = ""
                    token = ""
                    adminCode = ""
                except Exception as error:
                    print(f"Got Error - {error} - Skiping [token] [adminCode]")
                    main_text = ""
                    splited = ""
                    token = ""
                    adminCode = ""
                if (token == "" or adminCode == ""):
                    answers.append(
                        InlineQueryResultArticle(
                            title="!godel [file_link] [AdminCode]",
                            description="Put File Link to Delete GoFile.io File!",
                            input_message_content=InputTextMessageContent(
                                message_text="This for Deleting GoFile.io File via File Link.\n\n**Format:** `@Cloud_UPManager_Bot !godel `__[file_link] [AdminCode]__",
                                parse_mode="Markdown",
                                disable_web_page_preview=True
                            ),
                            reply_markup=InlineKeyboardMarkup(
                                [
                                    [InlineKeyboardButton("Delete GoFile.io File",
                                                          switch_inline_query_current_chat="!godel ")]
                                ]
                            )
                        )
                    )
                else:
                    response = await session.get(api_link.format(token, adminCode))
                    data_f = await response.json()
                    status = data_f['status']
                    if status == "ok":
                        answers.append(
                            InlineQueryResultArticle(
                                title="Deleted File!",
                                description=f"Deleted [{token}], Using [{adminCode}]",
                                input_message_content=InputTextMessageContent(
                                    message_text=f"**Deleted:** {splited}\n\n**Using AdminCode:** `{adminCode}`\n**File Token:** `{token}`",
                                    parse_mode="Markdown",
                                    disable_web_page_preview=True
                                )
                            )
                        )
                        await bot.send_message(chat_id=Config.LOG_CHANNEL,
                                               text=f"#GOFILE_DELETE:\n\n[{query.from_user.first_name}](tg://user?id={query.from_user.id}) Deleted GoFile.io File !!\n\n**File Name:** {splited}\n\n**AdminCode:** `{adminCode}`\n\n**File Token:** `{token}`",
                                               parse_mode="Markdown", disable_web_page_preview=True)
                    else:
                        answers.append(
                            InlineQueryResultArticle(title="File Not Deleted!",
                                                     description=f"Can't Delete [{token}], Using [{adminCode}]",
                                                     input_message_content=InputTextMessageContent(
                                                         message_text=f"Can't Delete - {splited}\nUsing [{adminCode}]",
                                                         disable_web_page_preview=True, parse_mode="Markdown"))
                        )

        except Exception as err:
            answers.append(
                InlineQueryResultArticle(title="Something Went Wrong!", description=f"Error: {err}",
                                         input_message_content=InputTextMessageContent(
                                             message_text=f"Something Went Wrong!\n\n**Error:** `{err}`"),
                                         reply_markup=InlineKeyboardMarkup(
                                             [[InlineKeyboardButton("Support Group", url="https://t.me/linux_repo")]]))
            )

        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text="Error: Search timed out!",
                switch_pm_parameter="help"
            )
    elif search_query.startswith("!strename"):
        if not int(query.from_user.id) == Config.BOT_OWNER:
            answers.append(
                InlineQueryResultArticle(
                    title="You Can't Do That!",
                    description="This is only for Bot Owner!",
                    input_message_content=InputTextMessageContent(
                        message_text="This is only for Bot Owner!\n\nOnly Developer have Streamtape File Delete Rights!"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("Support Group", url="https://t.me/linux_repo")],
                            [InlineKeyboardButton("Developer", url="https://t.me/linux_repo")]
                        ]
                    )
                )
            )
        else:
            parts = search_query.split(" ", 2)
            try:
                token, new_filename = parts[1], parts[2]
            except IndexError:
                token, new_filename = "", ""
            except Exception as error:
                token, new_filename = "", ""
            if (parts == "") or (token == "") or (new_filename == ""):
                answers.append(
                    InlineQueryResultArticle(
                        title="!strename [token] [new_filename]",
                        description="Put File Token & New File Name to Rename Streamtape File!",
                        input_message_content=InputTextMessageContent(
                            message_text="This for Renaming Streamtape File via File Token & New File Name.\n\n**Format:** `@Cloud_UPManager_Bot !strename `__[token] [new_filename]__",
                            parse_mode="Markdown",
                            disable_web_page_preview=True
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [InlineKeyboardButton("Rename Streamtape File",
                                                      switch_inline_query_current_chat="!stdel ")]
                            ]
                        )
                    )
                )
            else:
                try:
                    await asyncio.sleep(5)  # Waiting for 5 Sec for getting Correct User Input!
                    async with aiohttp.ClientSession() as session:
                        api_link = "https://api.streamtape.com/file/rename?login={}&key={}&file={}&name={}"
                        hit_api = await session.get(
                            api_link.format(Config.STREAMTAPE_API_USERNAME, Config.STREAMTAPE_API_PASS, token,
                                            new_filename))
                        data_f = await hit_api.json()
                        status = data_f['msg']
                        if status == "OK":
                            answers.append(
                                InlineQueryResultArticle(
                                    title="File Renamed!",
                                    description=f"Renamed to {new_filename} using {token}",
                                    input_message_content=InputTextMessageContent(
                                        message_text=f"Successfully Renamed file to - `{new_filename}`\n\nUsing `{token}`",
                                        parse_mode="Markdown", disable_web_page_preview=True)
                                )
                            )
                            await bot.send_message(chat_id=Config.LOG_CHANNEL,
                                                   text=f"#STREAMTAPE_RENAME:\n\n[{query.from_user.first_name}](tg://user?id={query.from_user.id}) Renamed Streamtape File !!\n\n**New File Name:** {new_filename}\n\n**File Token:** `{token}`",
                                                   parse_mode="Markdown", disable_web_page_preview=True)
                        else:
                            answers.append(
                                InlineQueryResultArticle(title="Can't Rename File!",
                                                         description=f"Token: {token} is Invalid!",
                                                         input_message_content=InputTextMessageContent(
                                                             message_text=f"Can't Rename File to - `{new_filename}`\n\nUsing `{token}`",
                                                             parse_mode="Markdown", disable_web_page_preview=True))
                            )
                except Exception as e:
                    answers.append(
                        InlineQueryResultArticle(title="Something Went Wrong!", description=f"Error: {e}",
                                                 input_message_content=InputTextMessageContent(
                                                     message_text=f"Something Went Wrong!\n\n**Error:** `{e}`",
                                                     parse_mode="Markdown", disable_web_page_preview=True))
                    )

        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text="Error: Search timed out!",
                switch_pm_parameter="help"
            )
    elif search_query.startswith("!strmdel"):
        if not int(query.from_user.id) == Config.BOT_OWNER:
            answers.append(
                InlineQueryResultArticle(
                    title="You Can't Do That!",
                    description="This is only for Bot Owner!",
                    input_message_content=InputTextMessageContent(
                        message_text="This is only for Bot Owner!\n\nOnly Developer have Streamtape File Delete Rights!"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("Support Group", url="https://t.me/linux_repo")],
                            [InlineKeyboardButton("Developer", url="https://t.me/linux_repo")]
                        ]
                    )
                )
            )
        token = None
        try:
            token = search_query.split("!strmdel ")[1]
        except IndexError:
            print("Got IndexError - Skiping [token]")
            token = ""
        except Exception as error:
            print(f"Got Error - {error} - Skiping [token]")
        if token == "":
            answers.append(
                InlineQueryResultArticle(
                    title="!strmdel [token]",
                    description="Put Streamtape Remote Token to remove Remote from Streamtape Account!",
                    input_message_content=InputTextMessageContent(
                        message_text="This for Removing Remote URL from Streamtape Account via Remote Token.\n\n**Format:** `@Cloud_UPManager_Bot !strmdel `__[token]__",
                        parse_mode="Markdown",
                        disable_web_page_preview=True
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("Remove Remote from Streamtape",
                                                  switch_inline_query_current_chat="!strmdel ")]
                        ]
                    )
                )
            )
        else:
            try:
                async with aiohttp.ClientSession() as session:
                    api_link = "https://api.streamtape.com/remotedl/remove?login={}&key={}&id={}"
                    hit_api = await session.get(
                        api_link.format(Config.STREAMTAPE_API_USERNAME, Config.STREAMTAPE_API_PASS, token))
                    data_f = await hit_api.json()
                    status = data_f['msg']
                    if status == "OK":
                        answers.append(
                            InlineQueryResultArticle(
                                title="Removed Remote!",
                                description="Remote URL Removed from Streamtape Account!",
                                input_message_content=InputTextMessageContent(
                                    message_text=f"Successfully Removed Remote URL from Streamtape Account!\n\n**Remote Token:** `{token}`",
                                    parse_mode="Markdown", disable_web_page_preview=True)
                            )
                        )
                        await bot.send_message(chat_id=Config.LOG_CHANNEL,
                                               text=f"#REMOTE_URL_REMOVE:\n\n[{query.from_user.first_name}](tg://user?id={query.from_user.id}) Removed Remote URL from Streamtape Account !!\n\n**Remote Token:** `{token}`",
                                               parse_mode="Markdown", disable_web_page_preview=True)
                    else:
                        answers.append(
                            InlineQueryResultArticle(title="Can't Remove Remote URL!",
                                                     description=f"Some Issues with Remote Token!",
                                                     input_message_content=InputTextMessageContent(
                                                         message_text=f"Can't Remove Remote URL!\n\nRemote Token: {token}\nHaving Some Issues.",
                                                         parse_mode="Markdown", disable_web_page_preview=True))
                        )
            except Exception as e:
                answers.append(
                    InlineQueryResultArticle(title="Something Went Wrong!", description=f"Error: {e}",
                                             input_message_content=InputTextMessageContent(
                                                 message_text=f"Something Went Wrong!\n\n**Error:** `{e}`",
                                                 parse_mode="Markdown", disable_web_page_preview=True))
                )

        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text="Error: Search timed out!",
                switch_pm_parameter="help"
            )
    elif search_query.startswith("!stremote"):
        remote_link = None
        try:
            remote_link = search_query.split("!stremote ")[1]
        except IndexError:
            print("Got IndexError - Skiping [download_url]")
            remote_link = ""
        except Exception as error:
            print(f"Got Error - {error} - Skiping [download_url]")
        if remote_link == "":
            answers.append(
                InlineQueryResultArticle(
                    title="!stremote [download_url]",
                    description="Put Direct Download Link to Upload to Streamtape!",
                    input_message_content=InputTextMessageContent(
                        message_text="This for Uploading to Streamtape via Any Direct Download Link.\n\n**Format:** `@Cloud_UPManager_Bot !stremote `__[download_url]__",
                        parse_mode="Markdown",
                        disable_web_page_preview=True
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("Add Remote to Streamtape",
                                                  switch_inline_query_current_chat="!stremote ")]
                        ]
                    )
                )
            )
        else:
            try:
                async with aiohttp.ClientSession() as session:
                    api_link = "https://api.streamtape.com/remotedl/add?login={}&key={}&url={}"
                    hit_api = await session.get(
                        api_link.format(Config.STREAMTAPE_API_USERNAME, Config.STREAMTAPE_API_PASS, remote_link))
                    data_f = await hit_api.json()
                    status = data_f['msg']
                    if status == "OK":
                        token = data_f['result']['id']
                        answers.append(
                            InlineQueryResultArticle(
                                title="URL Added!",
                                description="Remote URL Added to List!",
                                input_message_content=InputTextMessageContent(
                                    message_text=f"Successfully Added Remote URL( {remote_link} ) to Remote List!\n\n**Remote Token:** `{token}`",
                                    parse_mode="Markdown", disable_web_page_preview=True),
                                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Show Status",
                                                                                         switch_inline_query_current_chat=f"!show {token}")]])
                            )
                        )
                        await bot.send_message(chat_id=Config.LOG_CHANNEL,
                                               text=f"#REMOTE_URL_ADD:\n\n[{query.from_user.first_name}](tg://user?id={query.from_user.id}) Added Remote URL to Streamtape Account !!\n\n**Remote URL:** {remote_link}\n\n**Remote Token:** `{token}`",
                                               parse_mode="Markdown", disable_web_page_preview=True)
                    else:
                        answers.append(
                            InlineQueryResultArticle(title="Can't Add Remote URL!",
                                                     description=f"Some Issues with Remote URL!",
                                                     input_message_content=InputTextMessageContent(
                                                         message_text=f"Can't Upload Remote URL!\n\nRemote Link: {remote_link}\nHaving Some Issues.",
                                                         parse_mode="Markdown", disable_web_page_preview=True))
                        )
            except Exception as e:
                answers.append(
                    InlineQueryResultArticle(title="Something Went Wrong!", description=f"Error: {e}",
                                             input_message_content=InputTextMessageContent(
                                                 message_text=f"Something Went Wrong!\n\n**Error:** `{e}`",
                                                 parse_mode="Markdown", disable_web_page_preview=True))
                )

        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text="Error: Search timed out!",
                switch_pm_parameter="help"
            )
    elif search_query.startswith("!show"):
        try:
            input_f = search_query.split("!show ")[1]
        except IndexError:
            print("Got IndexError - Skiping [token]")
            input_f = ""
        except Exception as error:
            print(f"Got Error - {error} - Skiping [token]")
            input_f = ""
        if input_f == "":
            answers.append(
                InlineQueryResultArticle(
                    title="!show [token]",
                    description="Put Streamtape Remote Access Token to Get Current Status of Streamtape Remote!",
                    input_message_content=InputTextMessageContent(
                        message_text="This for Getting Current Status of Streamtape Remote via Streamtape Remote Access Token. \n\n**Format:** `@Cloud_UPManager_Bot !show `__[token]__",
                        parse_mode="Markdown",
                        disable_web_page_preview=True
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("Get Streamtape Remote Status",
                                                  switch_inline_query_current_chat="!show ")]
                        ]
                    )
                )
            )
        else:
            try:
                async with aiohttp.ClientSession() as session:
                    api_link = "https://api.streamtape.com/remotedl/status?login={}&key={}&id={}"
                    hit_api = await session.get(
                        api_link.format(Config.STREAMTAPE_API_USERNAME, Config.STREAMTAPE_API_PASS, input_f))
                    data_f = await hit_api.json()
                    status = data_f['msg']
                    if status == "OK":
                        remote_URL = data_f["result"][f"{input_f}"]["remoteurl"]
                        downloaded = data_f["result"][f"{input_f}"]["bytes_loaded"]
                        total_size = data_f["result"][f"{input_f}"]["bytes_total"]
                        added_at = data_f["result"][f"{input_f}"]["added"]
                        last_update = data_f["result"][f"{input_f}"]["last_update"]
                        url = data_f["result"][f"{input_f}"]["url"]
                        answers.append(
                            InlineQueryResultArticle(
                                title=f"TOKEN: {input_f}",
                                description=f"Uploaded: {humanbytes(downloaded)}, Total: {humanbytes(total_size)}",
                                input_message_content=InputTextMessageContent(
                                    message_text=f"**Token:** `{input_f}`\n**Uploaded:** `{humanbytes(downloaded)}`\n**Total:** `{humanbytes(total_size)}`\n**Added Remote at:** `{added_at}`\n**Last Updated at:** `{last_update}`\n\n**URL:** {url}",
                                    parse_mode="Markdown", disable_web_page_preview=True),
                                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Show Status",
                                                                                         switch_inline_query_current_chat=f"!show {input_f}")]])
                            )
                        )
                    else:
                        answers.append(
                            InlineQueryResultArticle(title="Nothing Found!", description="Nothing ...",
                                                     input_message_content=InputTextMessageContent(
                                                         message_text="Nothing Found ...", parse_mode="Markdown",
                                                         disable_web_page_preview=True))
                        )
            except Exception as e:
                answers.append(
                    InlineQueryResultArticle(title="Something Went Wrong!", description=f"Error: {e}",
                                             input_message_content=InputTextMessageContent(
                                                 message_text=f"Something Went Wrong!\n\n**Error:** `{e}`",
                                                 parse_mode="Markdown", disable_web_page_preview=True))
                )

        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text="Error: Search timed out!",
                switch_pm_parameter="help"
            )


@Bot.on_callback_query()
async def button(bot, data: CallbackQuery):
    cb_data = data.data
    if "uptogofile" in cb_data:
        downloadit = data.message.reply_to_message
        a = await data.message.edit("Downloading to my Server ...", parse_mode="Markdown",
                                    disable_web_page_preview=True)
        dl_loc = Config.DOWNLOAD_DIR + "/" + str(data.from_user.id) + "/"
        if not os.path.isdir(dl_loc):
            os.makedirs(dl_loc)
        c_time = time.time()
        the_media = await bot.download_media(
            message=downloadit,
            file_name=dl_loc,
            progress=progress_for_pyrogram,
            progress_args=(
                "Download kortasi ...",
                a,
                c_time
            )
        )
        await a.delete(True)
        try:
            async with aiohttp.ClientSession() as session:
                server_api = "https://apiv2.gofile.io/getServer"
                datas = await session.get(server_api)
                main_data = await datas.json()
                server = main_data['data']['server']
                a = await data.message.reply_to_message.reply_text(f"**Selected Server:** `{server}`")
                await a.edit("Uploading ...")
                files = {'file': open(the_media, 'rb')}
                URL = "https://" + server + ".gofile.io/uploadFile"
                response = await session.post(URL, data=files)
                data_f = await response.json()
                token = data_f['data']['code']
                download_page = data_f['data']['downloadPage']
                direct_download_link = data_f['data']['directLink']
                filename = data_f['data']['fileName']
                await a.edit(
                    f"**File Name:** `{filename}`\n\n**Download Page:** `{download_page}`\n\n**Direct Download Link:** `{direct_download_link}`",
                    disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Download Page", url=download_page)]]))
                try:
                    os.remove(the_media)
                except:
                    pass
                forwarded_msg = await data.message.reply_to_message.forward(Config.LOG_CHANNEL)
                await bot.send_message(chat_id=Config.LOG_CHANNEL,
                                       text=f"#GOFILE_UPLOAD:\n\n[{data.from_user.first_name}](tg://user?id={data.from_user.id}) Uploaded to GoFile.io !!\n\n**URL:** https://gofile.io/d/{token}",
                                       reply_to_message_id=forwarded_msg.message_id, parse_mode="Markdown",
                                       disable_web_page_preview=True)
        except Exception as err:
            await a.edit(f"Something went wrong!\n\n**Error:** `{err}`")
    elif "uptostreamtape" in cb_data:
        downloadit = data.message.reply_to_message
        a = await data.message.edit("Downloading to my Server ...", parse_mode="Markdown",
                                    disable_web_page_preview=True)
        dl_loc = Config.DOWNLOAD_DIR + "/" + str(data.from_user.id) + "/"
        if not os.path.isdir(dl_loc):
            os.makedirs(dl_loc)
        c_time = time.time()
        the_media = await bot.download_media(
            message=downloadit,
            file_name=dl_loc,
            progress=progress_for_pyrogram,
            progress_args=(
                "Download kortasi ...",
                a,
                c_time
            )
        )
        await a.delete(True)
        async with aiohttp.ClientSession() as session:
            Main_API = "https://api.streamtape.com/file/ul?login={}&key={}"
            hit_api = await session.get(Main_API.format(Config.STREAMTAPE_API_USERNAME, Config.STREAMTAPE_API_PASS))
            json_data = await hit_api.json()
            temp_api = json_data["result"]["url"]
            files = {'file1': open(the_media, 'rb')}
            response = await session.post(temp_api, data=files)
            data_f = await response.json(content_type=None)
            status = data_f["status"]
            download_link = data_f["result"]["url"]
            filename = the_media.split("/")[-1].replace("_", " ")
            try:
                os.remove(the_media)
            except:
                pass

            if not int(status) == 200:
                await data.message.reply_to_message.reply_text(
                    "Something Went Wrong!\n\n**Error:** Server Didn't Accept My Request!", parse_mode="Markdown",
                    disable_web_page_preview=True)
                return
            else:
                await data.message.reply_to_message.reply_text(
                    f"**File Name:** `{filename}`\n\n**Download Link:** `{download_link}`",
                    parse_mode="Markdown",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("Open Link", url=download_link)],
                            [InlineKeyboardButton("Delete File", callback_data="deletestream")]
                        ]
                    )
                )
                forwarded_msg = await data.message.reply_to_message.forward(Config.LOG_CHANNEL)
                await bot.send_message(chat_id=Config.LOG_CHANNEL,
                                       text=f"#STREAMTAPE_UPLOAD:\n\n[{data.from_user.first_name}](tg://user?id={data.from_user.id}) Uploaded to Streamtape !!\n\n**URL:** {download_link}",
                                       reply_to_message_id=forwarded_msg.message_id, parse_mode="Markdown",
                                       disable_web_page_preview=True)

    elif "deletestream" in cb_data:
        data_revive = data.message.text.split("Link: ", 1)[1]
        token = data_revive.split("/")[4]
        async with aiohttp.ClientSession() as session:
            del_api = "https://api.streamtape.com/file/delete?login={}&key={}&file={}"
            data_f = await session.get(
                del_api.format(Config.STREAMTAPE_API_USERNAME, Config.STREAMTAPE_API_PASS, token))
            json_data = await data_f.json()
            status = json_data['msg']
            if status == "OK":
                await data.message.edit(f"File Deleted using `{token}` !!")
                await bot.send_message(chat_id=Config.LOG_CHANNEL,
                                       text=f"#STREAMTAPE_DELETE:\n\n[{data.from_user.first_name}](tg://user?id={data.from_user.id}) Deleted {data_revive}",
                                       parse_mode="Markdown", disable_web_page_preview=True)
            else:
                await data.message.edit("File not Found!")
    elif "showcreds" in cb_data:
        if int(data.from_user.id) == Config.BOT_OWNER:
            await data.message.edit(
                f"Here are your Configs:\n\n`API_ID` - `{str(Config.API_ID)}`\n`API_HASH` - `{Config.API_HASH}`\n`BOT_TOKEN` - `{Config.BOT_TOKEN}`\n`BOT_OWNER` - `{str(Config.BOT_OWNER)}`\n`LOG_CHANNEL` - `{str(Config.LOG_CHANNEL)}`\n`STREAMTAPE_API_USERNAME` - `{Config.STREAMTAPE_API_USERNAME}`\n`STREAMTAPE_API_PASS` - `{Config.STREAMTAPE_API_PASS}`",
                parse_mode="Markdown", disable_web_page_preview=True)
        else:
            await data.message.edit("Only My Admin Can View That!")


Bot.run()
