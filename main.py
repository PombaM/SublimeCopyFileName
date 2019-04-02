import os
import ntpath
import sublime
import sublime_plugin

class CopyFileName(sublime_plugin.TextCommand):
    def run(self, edit):
        # returns file name with full path
        full_file_path = self.view.file_name()
        # get file name
        full_file_name = ntpath.basename(full_file_path)
        # split filename and extension
        file_name, _ = os.path.splitext(full_file_name)
        # set the file name to the os clipboard
        sublime.set_clipboard(file_name)

class CopyPath(sublime_plugin.TextCommand):
    def run(self, edit):
        # returns file name with full path
        full_file_path = self.view.file_name()
        # get file name
        full_file_name = ntpath.basename(full_file_path)
        # split filename and extension
        _, ext = os.path.splitext(full_file_name)
        # set full path name to the os clipboard
        sublime.set_clipboard(full_file_path.replace(ext, ''))

class CopyRelativePath(sublime_plugin.TextCommand):
    def run(self, edit):
        # returns file name with full path
        full_file_path = self.view.file_name()
        # split relative file path and extension
        relative_file_path, _ = os.path.splitext(full_file_path.replace(self.get_active_project_path() + '/', ''))
        # set the file relative path to the os clipboard
        sublime.set_clipboard(relative_file_path)

    # https://gist.github.com/astronaughts/9678368
    def get_active_project_path(self):
	    window = sublime.active_window()
	    folders = window.folders()
	    if len(folders) == 1:
	        return folders[0]
	    else:
	        active_view = window.active_view()
	        active_file_name = active_view.file_name() if active_view else None
	        if not active_file_name:
	            return folders[0] if len(folders) else os.path.expanduser("~")
	        for folder in folders:
	            if active_file_name.startswith(folder):
	                return folder
	        return os.path.dirname(active_file_name)
