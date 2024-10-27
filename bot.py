from pyrogram import Client, filters


api_id = "20950013"
api_hash = "1ec2d7a690f80cf556f8e491d76013aa"
session_string = ""
group_chat_id = "-1002266891348"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, session_string=session_string)


@app.on_message(filters.private)
async def forward_to_group(client, message):
    await message.forward(group_chat_id)




app.run()
