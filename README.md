# Keyword Reply Cog for Red

This repository contains a simple Red Discord bot cog that replies when specific words appear in selected Discord channels.

## Features
- Add/remove channels in Discord with commands
- Add/remove trigger words and replies in Discord with commands
- Replies when configured keywords are found

## Setup
1. Put the folder named `keywordreply` into your Red bot's `cogs` directory.
2. Load the cog with:
   - `[p]load keywordreply`
3. Configure channels and words with commands in Discord.

## Install from GitHub
Once this repo is pushed to GitHub, you can install it in Red with:

- `[p]cog install <your-github-repo-url>`
- `[p]load keywordreply`

## Commands
- `[p]keywordreply channel add #channel`
- `[p]keywordreply channel remove #channel`
- `[p]keywordreply channel list`
- `[p]keywordreply trigger add #channel keyword your reply text`
- `[p]keywordreply trigger remove #channel keyword`
- `[p]keywordreply trigger list #channel`
