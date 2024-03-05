from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
async def quest_button():
    markup = InlineKeyboardMarkup(row_width=1)
    b=InlineKeyboardButton('Quastions', callback_data='question')
    b1 = InlineKeyboardButton('Check for bad user', callback_data='bad')
    b2=InlineKeyboardButton('Registration', callback_data='reg')
    b3 = InlineKeyboardButton('View profiles', callback_data='view')
    b4 = InlineKeyboardButton('Referral menu', callback_data='ferral')
    b5 = InlineKeyboardButton('Advanced level', callback_data='advanced')
    b6 = InlineKeyboardButton('Upper Int level', callback_data='upperInt')
    b7 = InlineKeyboardButton('Intermediate level',callback_data='inter')
    b8 = InlineKeyboardButton('Elementary level',callback_data='ele')
    b9 = InlineKeyboardButton('Beginners level',callback_data='begin')
    markup.add(b,b1,b2,b3,b4,b5,b6,b7,b8,b9)
    return markup



async def question_for_food_type(var1,var2,var3,var4):
    markup = InlineKeyboardMarkup(row_width=1)
    air=InlineKeyboardButton(var1, callback_data='aa'+var1)
    car=InlineKeyboardButton(var2, callback_data='cc'+var2)
    bus=InlineKeyboardButton(var3, callback_data='bb'+var3)
    train=InlineKeyboardButton(var4, callback_data='tt'+var4)
    markup.add(air,car,bus,train)
    return markup


async def type_fruit(var1,var2,ex):
    markup = InlineKeyboardMarkup()
    air1=InlineKeyboardButton(var1, callback_data='@'+','+var1+','+ex)
    air2=InlineKeyboardButton(var2, callback_data='ю'+','+var2+','+ex)
    markup.add(air1,air2)
    return markup


async def type_vegetable(var1,var2,ex):
    markup = InlineKeyboardMarkup()
    car1=InlineKeyboardButton(var1, callback_data='$'+','+var1+','+ex)
    car2=InlineKeyboardButton(var2, callback_data='%'+','+var2+','+ex)
    markup.add(car1,car2)
    return markup


async def type_cherry(var1,var2,ex):
    markup = InlineKeyboardMarkup()
    train1=InlineKeyboardButton(var1, callback_data='{'+','+var1+','+ex)
    train2=InlineKeyboardButton(var2, callback_data='^'+','+var2+','+ex)
    markup.add(train1,train2)
    return markup


async def type_meat(var1,var2,ex):
    markup = InlineKeyboardMarkup()
    bus1=InlineKeyboardButton(var1, callback_data='я'+','+var1+','+ex)
    bus2=InlineKeyboardButton(var2,callback_data='&'+','+var2+','+ex)
    markup.add(bus1,bus2)
    return markup


async def yes_no(var1, var2,ex):
    markup = InlineKeyboardMarkup()
    yesbutton = InlineKeyboardButton(var1, callback_data='yes'+','+ex)
    nobutton = InlineKeyboardButton(var2, callback_data='no'+','+ex)
    markup.add(yesbutton, nobutton)
    return markup

async def like_dislike(user):
    markup = InlineKeyboardMarkup(row_width=1)
    qb1 = InlineKeyboardButton("Like👍", callback_data=f'Like_{user}')
    qb2 = InlineKeyboardButton("Dislike👎", callback_data=f'Dislike_{user}')
    markup.add(qb1, qb2)
    return markup

async def generate_link():
    markup = InlineKeyboardMarkup(row_width=1)
    a = InlineKeyboardButton("Generate Link🧬", callback_data='generate_link')
    b = InlineKeyboardButton("See referrals🫣", callback_data='jjj')
    c = InlineKeyboardButton("Balance💴", callback_data='balance')
    markup.add(a, b, c)
    return markup

async def save(link):
    markup = InlineKeyboardMarkup()
    a = InlineKeyboardButton("Save", callback_data=f'save,{link}')
    markup.add(a)
    return markup