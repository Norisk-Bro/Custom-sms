import sys
import importlib.util

# compiled .so ফাইলের সঠিক পথ
so_path = "Send.cpython-314-aarch64-linux-android.so"

spec = importlib.util.spec_from_file_location("Send", so_path)
Send = importlib.util.module_from_spec(spec)
sys.modules["Send"] = Send
spec.loader.exec_module(Send)
