from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

til = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'π·πΊ Russian', callback_data = "ru"),
		InlineKeyboardButton(text = 'πΊπΈ English', callback_data = 'en')
	],
	[
		InlineKeyboardButton(text = 'πΊπΏ Uzbek', callback_data = 'uz'),
		InlineKeyboardButton(text = 'π«π· French', callback_data = 'fr')
	],
	[ 
		InlineKeyboardButton(text = 'π¦πͺ Arabic', callback_data = 'ar'),
		InlineKeyboardButton(text = 'π¨π³ Chinese', callback_data = 'zh-cn')
	],
	],

	)