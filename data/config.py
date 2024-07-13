from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.str("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
CHANNEL = env.str('CHANNEL')

def get_admin():
    admins = ADMINS
    return admins.split(',')