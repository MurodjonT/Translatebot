from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

til = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🇷🇺 Russian', callback_data = "ru"),
		InlineKeyboardButton(text = '🇺🇸 English', callback_data = 'en')
	],
	[
		InlineKeyboardButton(text = '🇺🇿 Uzbek', callback_data = 'uz'),
		InlineKeyboardButton(text = '🇫🇷 French', callback_data = 'fr')
	],
	[ 
		InlineKeyboardButton(text = '🇦🇪 Arabic', callback_data = 'ar'),
		InlineKeyboardButton(text = '🇨🇳 Chinese', callback_data = 'zh-cn')
	],
	],

	)