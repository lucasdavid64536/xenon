import discord

# https://www.iconfinder.com/iconsets/small-n-flat
message_types = {
    None: ("", "{c}", "", 0x36393e),
    "info": ("Info", "{c}",
             "https://cdn0.iconfinder.com/data/icons/small-n-flat/24/678110-sign-info-512.png", 0x478fce),
    "wait_for": ("Waiting for response", "{c}", "https://cdn4.iconfinder.com/data/icons/small-n-flat/24/bubbles-alt2-512.png", 0x478fce),
    "success": ("Voila!", "{c}", "https://cdn0.iconfinder.com/data/icons/small-n-flat/24/678134-sign-check-512.png",
                0x48ce6c),
    "warning": ("Warning", "{c}",
                "https://cdn0.iconfinder.com/data/icons/small-n-flat/24/678136-shield-warning-512.png",
                0xefbc2f),
    "working": ("Please wait ...", "{c}",
                "https://images-ext-1.discordapp.net/external/AzWR8HxPJ4t4rPA1DagxJkZsOCOMp4OTgwxL3QAjF4U/https/cdn.discordapp.com/emojis/424900448663633920.gif",
                0x36393e),
    "error": ("Error", "{c}", "https://cdn0.iconfinder.com/data/icons/small-n-flat/24/678069-sign-error-512.png",
              0xc64935),
    "perm_error": ("Permissions Error", "{c}",
                   "https://cdn0.iconfinder.com/data/icons/small-n-flat/24/678069-sign-error-512.png",
                   0xc64935),
    "unex_error": ("Error", "**Error Code:**\n```{c}```",
                   "https://cdn0.iconfinder.com/data/icons/small-n-flat/24/678069-sign-error-512.png", 0xc64935)
}


def embed_message(content=None, embed=None, type=None):
    title, content_format, icon, color = message_types.get(type) or message_types.get(None)
    embed = discord.Embed(color=discord.Color(color), description=content_format.format(c=content))
    embed.set_author(name=title, icon_url=icon)

    if isinstance(embed, discord.Embed):
        custom_embed = discord.Embed(color=discord.Color(color))
        custom_embed.set_author(name=title, icon_url=icon)
        embed_data = custom_embed.to_dict()
        embed_data.update(embed.to_dict())
        embed = discord.Embed.from_data(embed_data)

    return {"embed": embed}


def paginate(content, limit):
    result = [""]
    lines = content.splitlines(keepends=True)
    i = 0
    for line in lines:
        if len(result[i]) + len(line) <= limit:
            result[i] += line

        else:
            i += 1
            result[i] = line

    return result