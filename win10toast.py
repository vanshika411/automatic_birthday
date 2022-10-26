# ##################################
# standard library
import logging
import threading
from os import path
from time import sleep
from pkg_resources import Requirement
class ToastNotifier(object):
    """# def __init__(self):
   # "Initialize."""
        # message_map = {WM_DESTROY: self.on_destroy, }
    def __init__(self):
        """Initialize."""
        self._thread = None

        # # Register the window class.
        # self.wc = WNDCLASS()
        # self.hinst = self.wc.hInstance = GetModuleHandle(None)
        # self.wc.lpszClassName = str("PythonTaskbar")  # must be a string
        # self.wc.lpfnWndProc = message_map  # could also specify a wndproc.
        # try:
        #     self.classAtom = RegisterClass(self.wc)
        # except:
        #     pass #not sure of this

    def _show_toast(self, title="Notification", msg="Message deleivered",
                    icon_path=None, duration=5):
        def show_toast(self, title, msg,icon_path, duration):
            """Notification settings."""
 
    def show_toast(self,title="Notification",msg="Here comes the message"):
        (self.wc.lpszClassName, None)
        return None

    def show_toast(self, title="Notification", msg= "Here comes the message",
                    icon_path=None, duration=5, threaded=False):
        """Notification settings.
        :title: notification title
        :msg: notification message
        :icon_path: path to the .ico file to custom notification
        :duration: delay in seconds before notification self-destruction
        """
        if not threaded:
            self._show_toast(title, msg, icon_path, duration)
        else:
            if self.notification_active():
                # We have an active notification, let is finish so we don't spam them
                return False

            self._thread = threading.Thread(target=self._show_toast, args=(title, msg, icon_path, duration))
            self._thread.start()
        return True

    def notification_active(self):
        """See if we have an active notification showing"""
        if self._thread != None and self._thread.is_alive():
            # We have an active notification, let is finish we don't spam them
            return True
        return False

    def on_destroy(self, hwnd, msg, wparam, lparam):
        """Clean after notification ended."""