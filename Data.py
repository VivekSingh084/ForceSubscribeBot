from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {},

Welcome to {}

I can force your group's users to join a particular chat. 
The chat can be a group or channel. It can be private or public.

Use below buttons to learn more !

By @AnonymousSupport 
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="๐  Return Home ๐ ", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("How to use me ๐ค", callback_data="help"),
            InlineKeyboardButton("๐ค About Me ๐ค", callback_data="about")
        ],
        [InlineKeyboardButton("๐ More Amazing bots ๐", url="https://t.me/AnonymousSupport")],
        [InlineKeyboardButton("๐ Support Group ๐", url="https://t.me/AnonymousRobotSupport")],
    ]

    # Help Message
    HELP = """
1) Add me as **Admin** to a group.

2) Add me to the particular chat as **Admin** where you want to force your users to join. It can be any group or channel, public or private.

3) Use /fsub chat_id/username to make me functional. Use /id if you need chat id.
Example : `/fsub -1001756847896 or `/forcesubscribe -1001756847896

4) [Optional] Use /settings to change settings!

5) Everything's Done. Leave the rest to me.

โจ **แดแด แดษชสแดสสแด แดแดแดแดแดษดแดsโ** โจ

/fsub - See current status of force subscribe chat
/fsub chat_id/username - Force users to join the particular chat
/settings - Change Force Subscribe Settings
/id - Get the chat id of any group or channel
/about - About Me
/help - Send This Message
/start - Starts the Bot

**Note** - You can also use `/forcesubscribe` instead of `/fsub`
    """

    # About Message
    ABOUT = """
**About This Bot** 

A telegram force subscribe bot by @AnonymousSupport

Source Code : [Force Subscribe](https://github.com/AnonymousBoy1025/ForceSubscribeBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : [Anonymous Boy](telegram.me/anonymous_was_bot)
    """
