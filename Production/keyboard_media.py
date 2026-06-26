'''
Steps:

1.In Windows Command Prompt, run:
    
    pip install hid pywin32

2.In python, run this program (keyboard_media.py). Ensure python has ben added to PATH.

'''
import time
import asyncio
import win32hid
from winrt.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager

VENDOR_ID = 0xFEED
PRODUCT_ID = 