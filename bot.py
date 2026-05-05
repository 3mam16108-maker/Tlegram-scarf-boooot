from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8744675125:AAFayAq8Z28QMEO9PsxR1JptC60ZDMu2zYY"

# القائمة الرئيسية
def main_menu():
    keyboard = [
        [InlineKeyboardButton("📍 عنوان المكتب", callback_data="1")],
        [InlineKeyboardButton("📞 وسائل التواصل", callback_data="2")],
        [InlineKeyboardButton("🚚 وسائل الشحن والتوصيل", callback_data="3")],
        [InlineKeyboardButton("💳 طرق الدفع", callback_data="4")],
        [InlineKeyboardButton("💰 قائمه الاسعار", callback_data="5")],
        [InlineKeyboardButton("🛒 نظام تجار الاون لاين", callback_data="6")]
    ]
    return InlineKeyboardMarkup(keyboard)

# زر الرجوع
def back_button():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 رجوع", callback_data="back")]
    ])

# رسالة البداية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "اهلا بيك فى مكتب الولاء Scarf 👋\nاخبرنى كيف يمكننى مساعدتك",
        reply_markup=main_menu()
    )

# التعامل مع الأزرار
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "1":
        text = """عنوان مكتب الولاء Scarf هو
ميت القرشي - ميت غمر
- محافظه الدقهليه"""

    elif data == "2":
        text = """وسائل التواصل مع المكتب هى
1 قناه التليجرام : https://t.me/alwalascarf
2 جروب الوتساب : https://chat.whatsapp.com/DtOKFz4AXF70QfAOamzlXE?mode=gi_t
3 رقم التواصل : 01030842917
ا/ مسعد"""

    elif data == "3":
        text = """يوجد لدينا العديد من وسائل التوصيل ومنها
1 شركه شحن ايرجينت
2 شركه شحن البراق
3 شركه شحن J&T Express
4 شحن عن طريق البريد المصرى

تتراوح مده التوصيل من يومين الى ثلاثه ايام"""

    elif data == "4":
        text = """يتوفر لدينا العديد من طرق الدفع ومنها
1 حسابات بنكيه
2 محافظ اليكترونيه
3 عند الاستلام بعربون 300ج"""

    elif data == "5":
        text = "قائمة الأسعار تم عرضها بالكامل 👇"

    elif data == "6":
        text = """نظام التعامل مع تجار الاون لاين:
حجز لمدة 10 أيام
زيادة 5ج على القطعة
اقل كمية 2 دسته"""

    elif data == "back":
        # بدل edit → نبعت رسالة جديدة
        await query.message.reply_text(
            "اهلا بيك فى مكتب الولاء Scarf 👋\nاخبرنى كيف يمكننى مساعدتك",
            reply_markup=main_menu()
        )
        return

    # 👇 دي أهم سطر: بعتنا رسالة جديدة بدل ما نعدل القديمة
    await query.message.reply_text(text, reply_markup=back_button())

    # (اختياري) نشيل الأزرار من الرسالة القديمة بس
    try:
        await query.edit_message_reply_markup(reply_markup=None)
    except:
        pass


# تشغيل البوت
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

print("Bot is running...")
app.run_polling()