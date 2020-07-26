from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup
import tgcrypto
import pyrogram.errors
app = Client("Postverse", api_id=938340, api_hash="4c47ceee0c51daa3e6608dd728c6148d", bot_token="1131492061:AAEYmA87jCCUVBXwzhBu50fuZJvRmg0Hz0A")
groups = []
admins = [1074490547, 1111847352, 820463901]
@app.on_message(Filters.command(['start']))

def download(client, message):
	message.reply_text("Just Send Me Any Text Message I'll Forward It To All Saved Groups!")

@app.on_message(Filters.text)
def download(client, message):
	count = 1
	user_id = message.from_user.id
	for admin in admins:
		if user_id == admin:
			for grp in groups:
				try:
					msg = message.text
					app.send_message(grp, msg)
					message.reply_text(f'({count}) Message Sent To @{grp}')
					count += 1
				except Exception as e:
							message.reply_text(f"Can't send your message to @{grp} due to this reason👇\n\nERROR: {e}")
app.run()
