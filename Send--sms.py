import sys
import importlib.util
import importlib.machinery

# CPython C-extension loader setup
so_filename = "Send.cpython-314-aarch64-linux-android.so"

loader = importlib.machinery.ExtensionFileLoader("Send", so_filename)
spec = importlib.util.spec_from_loader("Send", loader)
Send = importlib.util.module_from_spec(spec)
sys.modules["Send"] = Send
spec.loader.exec_module(Send)
