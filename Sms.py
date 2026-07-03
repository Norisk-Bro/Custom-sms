import Freesms

# আপনার মেইন ফাংশনটি কল করুন
try:
    Freesms.send_sms()
except Exception as e:
    print(f"Error: {e}")
