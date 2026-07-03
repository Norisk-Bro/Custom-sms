import Freesms # এটি আপনার .so ফাইলটিকে লোড করবে

# এবার আপনার মেইন ফাংশনটি কল করুন যা দিয়ে টুলটি চালু হবে
try:
    Freesms.send_sms()
except AttributeError:
    print("Error: Could not find send_sms function in the module.")
