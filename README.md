# Keyword Reply Cog for Red

This repository contains a simple Red Discord bot cog that replies when specific words appear in selected Discord channels.

## Features
- Watches specific channels by ID
- Replies when configured keywords are found
- Easy to edit for your own triggers and responses

## Setup
1. Put the folder named `keywordreply` into your Red bot's `cogs` directory.
2. Load the cog with:
   - `[p]load keywordreply`
3. Edit the channel IDs and keywords in the cog file.

## Install from GitHub
Once this repo is pushed to GitHub, you can install it in Red with:

- `[p]cog install <your-github-repo-url>`
- `[p]load keywordreply`

## Editing the cog
Open [keywordreply/keywordreply.py](keywordreply/keywordreply.py) and replace the example channel IDs and keyword replies with your own.
