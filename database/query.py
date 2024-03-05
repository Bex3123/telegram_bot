CREATE_TG_USER_TABLE="""CREATE TABLE IF NOT EXISTS telegram_users(
id INTEGER PRIMARY KEY,
telegram_user_id INTEGER,
first_name CHAR(20),
UNIQUE (telegram_user_id))"""

ALTER_R_USER_TABLE = """
ALTER TABLE telegram_users ADD COLUMN REFERENCE_LINK TEXT
"""

ALTER_B_USER_TABLE = """
ALTER TABLE telegram_users ADD COLUMN BALANCE INTEGER
"""


INSERT_TG_USER_TABLE="""INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?)"""

CREATE_ANSWER_TABLE = '''
CREATE TABLE IF NOT EXISTS answers(
id INTEGER PRIMARY KEY,
telegram_user_id INTEGER,
first_name CHAR(20),
transport_type CHAR(20) ,
model CHAR(20),
experience CHAR(20),
UNIQUE(telegram_user_id)
)
'''
INSERT_ANSWER_TABLE = '''
INSERT OR IGNORE INTO answers  VALUES (?,?, ?, ?, ?,?)
'''

CREATE_BAN_TABLE = '''
CREATE TABLE IF NOT EXISTS bans(
id INTEGER PRIMARY KEY,
tg_id INTEGER,
first_name CHAR(20),
countt INTEGER,
UNIQUE(tg_id)
)'''
INSERT_BAN_TABLE = '''
INSERT OR IGNORE INTO bans  VALUES (?,?,?,?)
'''

SELECT_BAN_TABLE_COUNT = '''
SELECT countt FROM bans WHERE tg_id=?
'''
UPDATE_BAN_TABLE_COUNT = '''
UPDATE bans SET countt=countt+1 WHERE tg_id=?
'''

DELETE_USER = '''
DELETE FROM bans WHERE tg_id=?
'''

SELECT_USER_FROM_BAN = '''
SELECT tg_id,first_name,countt FROM bans'''

CREATE_REGISTER_TABLE = '''
CREATE TABLE IF NOT EXISTS registers(
id INTEGER PRIMARY KEY,
tg_id INTEGER,
nickname CHAR(20),
biography TEXT,
age INTEGER,
zodiac CHAR(20),
gender CHAR(20),
best_color CHAR(20),
photo TEXT,
UNIQUE (tg_id)
)
'''

INSERT_REGISTER_TABLE = '''
INSERT OR IGNORE INTO registers VALUES (?,?,?,?,?,?,?,?,?)'''

SELECT_REGISTER_TABLE = '''
SELECT tg_id FROM registers WHERE tg_id=?'''

SELECT_INFO_REGISTER_TABLE = '''
SELECT tg_id,nickname,biography,age,zodiac,gender,best_color,photo FROM registers WHERE tg_id=?'''

SELECT_ALL_INFO_REGISTER_TABLE = '''
SELECT * FROM registers'''


CREATE_LIKE_DISLIKE_TABLE = '''
CREATE TABLE IF NOT EXISTS like_dislike(
ID INTEGER PRIMARY KEY,
user_tg_id INTEGER,
liker_tg_id INTEGER,
like_dislike CHAR(20),
UNIQUE (user_tg_id, liker_tg_id)
)'''
INSERT_LIKE_DISLIKE_TABLE = '''
INSERT INTO like_dislike VALUES (?,?,?,?)'''

FILTER_LEFT_JOIN = '''
SELECT * FROM registers
LEFT JOIN like_dislike ON registers.tg_id = like_dislike.user_tg_id
AND like_dislike.liker_tg_id = ?
WHERE like_dislike.ID IS NULL
AND registers.tg_id != ?'''


CREATE_REFERRAL_TABLE = """
CREATE TABLE IF NOT EXISTS referral 
(
ID INTEGER PRIMARY KEY,
OWNER_TG_ID INTEGER,
REFERRAL_TG_ID INTEGER,
UNIQUE (OWNER_TG_ID, REFERRAL_TG_ID)
)
"""

DOUBLE_SELECT_REFERRAL_USER_QUERY = """
SELECT
    COALESCE(telegram_users.BALANCE, 0) as BALANCE,
    COUNT(referral.ID) as total_referrals
FROM
    telegram_users
LEFT JOIN
    referral ON telegram_users.telegram_user_id = referral.OWNER_TG_ID
WHERE
    telegram_users.telegram_user_id = ?
"""

SELECT_ALL_USER_TL_USERS = '''
SELECT * FROM telegram_users WHERE telegram_user_id=?'''

UPDATE_USER_TL_USERS_LINK = '''UPDATE telegram_users SET REFERENCE_LINK=? WHERE telegram_user_id=?'''

SELECT_BY_LINK_TG_USERS = '''SELECT * FROM telegram_users WHERE REFERENCE_LINK=?'''

INSERT_REFERRAL_TABLE = '''
INSERT INTO referral VALUES (?,?,?)'''

UPDATE_USER_TL_USERS_BALANCE = '''UPDATE telegram_users SET BALANCE=COALESCE(BALANCE,0)+100 WHERE telegram_user_id=?'''

SELECT_TG_ID_USER_TABLE = '''
SELECT telegram_user_id FROM telegram_users WHERE telegram_user_id=?'''

SELECT_REFERRALS_REFERRAL_TABLE = '''
SELECT REFERRAL_TG_ID FROM referral WHERE OWNER_TG_ID=?'''

SELECT_BALANCE_TL_USERS = '''
SELECT COALESCE(BALANCE,0) FROM telegram_users WHERE telegram_user_id=?'''


CREATE_ENGLISH_LEVEL_LEARN_TABLE = '''CREATE TABLE IF NOT EXISTS eng_level_table(
id INTEGER PRIMARY KEY,
link TEXT,
UNIQUE(link))'''


INSERT_ENGLISH_LEVEL_LEARN_TABLE = '''INSERT OR IGNORE INTO eng_level_table VALUES (?,?)'''

CREATE_ENGLISH_LEVEL_LEARN_TABLE_B2 = '''CREATE TABLE IF NOT EXISTS eng_level_table_b2(
id INTEGER PRIMARY KEY,
link TEXT,
UNIQUE(link))'''

INSERT_ENGLISH_LEVEL_LEARN_TABLE_B2 = '''INSERT OR IGNORE INTO eng_level_table_b2 VALUES (?,?)'''

CREATE_ENGLISH_LEVEL_LEARN_TABLE_B1 = '''CREATE TABLE IF NOT EXISTS eng_level_table_b1(
id INTEGER PRIMARY KEY,
link TEXT,
UNIQUE(link))'''

INSERT_ENGLISH_LEVEL_LEARN_TABLE_B1 = '''INSERT OR IGNORE INTO eng_level_table_b1 VALUES (?,?)'''

CREATE_ENGLISH_LEVEL_LEARN_TABLE_A2 = '''CREATE TABLE IF NOT EXISTS eng_level_table_a2(
id INTEGER PRIMARY KEY,
link TEXT,
UNIQUE(link))'''

INSERT_ENGLISH_LEVEL_LEARN_TABLE_A2 = '''INSERT OR IGNORE INTO eng_level_table_a2 VALUES (?,?)'''

CREATE_ENGLISH_LEVEL_LEARN_TABLE_A1 = '''CREATE TABLE IF NOT EXISTS eng_level_table_a1(
id INTEGER PRIMARY KEY,
link TEXT,
UNIQUE(link))'''

INSERT_ENGLISH_LEVEL_LEARN_TABLE_A1 = '''INSERT OR IGNORE INTO eng_level_table_a1 VALUES (?,?)'''

CREATE_FAVOURITE_ENGLISH_LEVEL_LEARN_TABLE = '''CREATE TABLE IF NOT EXISTS favourite_eng_level_table(
id INTEGER PRIMARY KEY,
tg_user_id INTEGER,
link TEXT)'''

INSERT_FAVOURITE_ENGLISH_LEVEL_LEARN_TABLE = '''INSERT INTO favourite_eng_level_table VALUES (?,?,?)'''

SELECT_FAV_ENG_LEVEL_TABLE = '''SELECT id FROM favourite_eng_level_table WHERE tg_user_id=? AND link=?'''
