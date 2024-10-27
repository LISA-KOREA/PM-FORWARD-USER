from pyrogram import Client, filters

# Replace with your actual API ID, API Hash, and Bot Token
api_id = "20950013"
api_hash = "1ec2d7a690f80cf556f8e491d76013aa"
session_string = "AQE_q_0AmDmM-8yp8JJ3VYMgss8kL3lNVDha5Dt5xUTAjU7W_X2Lw8boCeE1NLqELaP_SYI9tf5Z7Tezssn1isMYUp_Mtsv1bU_efzEqAuWAdL2ysWP4d1vYRnwj1JgpCd6mn3DxfTCrGZdlzfQ5s3PP8sC-7uGC3OM2-0YUZU0hMuFyTUZRSnwAqIUVVcipBnVfcpG1yF_gyDancDhPATg009V5zIo6K-nTW1hMe4PJldxlgYWsLIZ1M57mZRCXK0XzDgz64UJQUseQCH0Qju6rDeVRoVFH48-KZ1QcNnFUwooGq7ls3_R3ZNX240O5tYqayjYUoMyCbl2biI0fh9QxdAaTQQAAAAGz1XOfAA"
group_chat_id = "-1002266891348"  # Replace with your group chat ID

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Forward all messages received in private chat to the specified group
@app.on_message(filters.private)
async def forward_to_group(client, message):
    await message.forward(group_chat_id)



# Run the bot
app.run()
