#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
بوت الاستغفار - Istighfar Reminder Bot
"""

import os
import random
import asyncio
import logging
from datetime import datetime
from telegram import Bot
from telegram.error import TelegramError

# إعداد السجلات
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ═══════════════════════════════════════════════════════
# ⚙️ الإعدادات
# ═══════════════════════════════════════════════════════

BOT_TOKEN = os.getenv('BOT_TOKEN', '8192965268:AAHkuM6mGOeLkjBDG7dEasgX72TwotTqFCY')
CHANNEL_ID = os.getenv('CHANNEL_ID', '@TasbihAlert')
INTERVAL_SECONDS = int(os.getenv('INTERVAL_SECONDS', 3600))  # ساعة

# ═══════════════════════════════════════════════════════
# 📿 قائمة الاستغفارات
# ═══════════════════════════════════════════════════════

ISTIGHFAR_LIST = [
    "أَسْتَغْفِرُ اللَّهَ",
    "أَسْتَغْفِرُ اللَّهَ وَأَتُوبُ إِلَيْهِ",
    "أَسْتَغْفِرُ اللَّهَ الْعَظِيمَ",
    "أَسْتَغْفِرُ اللَّهَ الْعَظِيمَ وَأَتُوبُ إِلَيْهِ",
    "أَسْتَغْفِرُ اللَّهَ الَّذِي لَا إِلَهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ وَأَتُوبُ إِلَيْهِ",
    "رَبِّ اغْفِرْ لِي وَتُبْ عَلَيَّ إِنَّكَ أَنْتَ التَّوَّابُ الرَّحِيمُ",
    "اللَّهُمَّ أَنْتَ رَبِّي لَا إِلَهَ إِلَّا أَنْتَ، خَلَقْتَنِي وَأَنَا عَبْدُكَ، وَأَنَا عَلَى عَهْدِكَ وَوَعْدِكَ مَا اسْتَطَعْتُ، أَعُوذُ بِكَ مِنْ شَرِّ مَا صَنَعْتُ، أَبُوءُ لَكَ بِنِعْمَتِكَ عَلَيَّ، وَأَبُوءُ بِذَنْبِي فَاغْفِرْ لِي فَإِنَّهُ لَا يَغْفِرُ الذُّنُوبَ إِلَّا أَنْتَ",
    "اللَّهُمَّ اغْفِرْ لِي ذَنْبِي كُلَّهُ، دِقَّهُ وَجِلَّهُ، وَأَوَّلَهُ وَآخِرَهُ، وَعَلَانِيَتَهُ وَسِرَّهُ",
    "رَبَّنَا ظَلَمْنَا أَنْفُسَنَا وَإِنْ لَمْ تَغْفِرْ لَنَا وَتَرْحَمْنَا لَنَكُونَنَّ مِنَ الْخَاسِرِينَ",
    "لَا إِلَهَ إِلَّا أَنْتَ سُبْحَانَكَ إِنِّي كُنْتُ مِنَ الظَّالِمِينَ",
    "رَبِّ إِنِّي ظَلَمْتُ نَفْسِي فَاغْفِرْ لِي",
    "سُبْحَانَكَ اللَّهُمَّ وَبِحَمْدِكَ، أَشْهَدُ أَنْ لَا إِلَهَ إِلَّا أَنْتَ، أَسْتَغْفِرُكَ وَأَتُوبُ إِلَيْكَ",
    "سُبْحَانَ اللَّهِ وَبِحَمْدِهِ، أَسْتَغْفِرُ اللَّهَ وَأَتُوبُ إِلَيْهِ",
    "اللَّهُمَّ اغْفِرْ لِي وَارْحَمْنِي وَارْزُقْنِي",
]

# ═══════════════════════════════════════════════════════
# 🎨 تنسيق الرسالة
# ═══════════════════════════════════════════════════════

def format_message(istighfar: str) -> str:
    """تنسيق رسالة الاستغفار"""
    
    emojis = ["📿", "🤲", "💫", "✨", "🕌", "☪️", "💚", "🌟"]
    emoji = random.choice(emojis)
    
    message = f"""
 {istighfar}

"""
    return message

# ═══════════════════════════════════════════════════════
# 📤 إرسال الرسالة
# ═══════════════════════════════════════════════════════

async def send_istighfar(bot: Bot) -> bool:
    """إرسال رسالة استغفار إلى القناة"""
    try:
        istighfar = random.choice(ISTIGHFAR_LIST)
        message = format_message(istighfar)
        
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=message,
            parse_mode='Markdown'
        )
        
        logger.info(f"✅ تم إرسال الاستغفار")
        return True
        
    except TelegramError as e:
        logger.error(f"❌ خطأ: {e}")
        return False

# ═══════════════════════════════════════════════════════
# 🔄 الحلقة الرئيسية
# ═══════════════════════════════════════════════════════

async def main():
    """الدالة الرئيسية"""
    
    print("📿 بوت الاستغفار يعمل...")
    
    if BOT_TOKEN == 'YOUR_BOT_TOKEN_HERE':
        logger.error("❌ عيّن BOT_TOKEN!")
        return
    
    bot = Bot(token=BOT_TOKEN)
    
    try:
        bot_info = await bot.get_me()
        logger.info(f"✅ متصل: @{bot_info.username}")
    except TelegramError as e:
        logger.error(f"❌ فشل الاتصال: {e}")
        return
    
    logger.info(f"📡 القناة: {CHANNEL_ID}")
    logger.info(f"⏱️ كل {INTERVAL_SECONDS//60} دقيقة")
    
    while True:
        try:
            await send_istighfar(bot)
            await asyncio.sleep(INTERVAL_SECONDS)
        except asyncio.CancelledError:
            break
        except Exception as e:
            logger.error(f"❌ خطأ: {e}")
            await asyncio.sleep(60)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 تم الإيقاف")
