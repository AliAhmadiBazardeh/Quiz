import re
import random
import string

def random_lower_alphanumeric():
    """Generate a random string with digits and lowercase letters"""
    chars = string.digits + string.ascii_lowercase
    return ''.join(random.choices(chars, k=5))

def simple_slugify(text):
    text = text.lower()                          # کوچک کردن
    text = re.sub(r'[^\w\s-]', '', text)         # حذف کاراکترهای خاص
    text = re.sub(r'[\s_-]+', '-', text)         # تبدیل فاصله و _ به -
    text = re.sub(r'^-+|-+$', '', text)          # حذف خط تیره از ابتدا و انتها
    return text
