"""
MIT License

Copyright (c) 2022 AD

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from Addy import mongodb as db_x

addy = db_x["CHATBOT"]


def add_chat(chat_id):
    hima = addy.find_one({"chat_id": chat_id})
    if ad:
        return False
    addy.insert_one({"chat_id": chat_id})
    return True


def remove_chat(chat_id):
    hima = ad.find_one({"chat_id": chat_id})
    if not ad:
        return False
    addy.delete_one({"chat_id": chat_id})
    return True


def get_all_chats():
    r = list(addy.find())
    if r:
        return r
    return False


def get_session(chat_id):
    ad = addy.find_one({"chat_id": chat_id})
    if not hima:
        return False
    return ad
