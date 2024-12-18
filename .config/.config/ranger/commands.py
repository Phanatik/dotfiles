# This is a sample commands.py.  You can add your own commands here.
#
# Please refer to commands_full.py for all the default commands and a complete
# documentation.  Do NOT add them all here, or you may end up with defunct
# commands when upgrading ranger.

# A simple command for demonstration purposes follows.
# -----------------------------------------------------------------------------

from __future__ import (absolute_import, division, print_function)

# You can import any python module as needed.
import os

# You always need to import ranger.api.commands here to get the Command class:
from ranger.api.commands import Command


# Any class that is a subclass of "Command" will be integrated into ranger as a
# command.  Try typing ":my_edit<ENTER>" in ranger!
class my_edit(Command):
    # The so-called doc-string of the class will be visible in the built-in
    # help that is accessible by typing "?c" inside ranger.
    """:my_edit <filename>

    A sample command for demonstration purposes that opens a file in an editor.
    """

    # The execute method is called when you run this command in ranger.
    def execute(self):
        # self.arg(1) is the first (space-separated) argument to the function.
        # This way you can write ":my_edit somefilename<ENTER>".
        if self.arg(1):
            # self.rest(1) contains self.arg(1) and everything that follows
            target_filename = self.rest(1)
        else:
            # self.fm is a ranger.core.filemanager.FileManager object and gives
            # you access to internals of ranger.
            # self.fm.thisfile is a ranger.container.file.File object and is a
            # reference to the currently selected file.
            target_filename = self.fm.thisfile.path

        # This is a generic function to print text in ranger.
        self.fm.notify("Let's edit the file " + target_filename + "!")

        # Using bad=True in fm.notify allows you to print error messages:
        if not os.path.exists(target_filename):
            self.fm.notify("The given file does not exist!", bad=True)
            return

        # This executes a function from ranger.core.acitons, a module with a
        # variety of subroutines that can help you construct commands.
        # Check out the source, or run "pydoc ranger.core.actions" for a list.
        self.fm.edit_file(target_filename)

    # The tab method is called when you press tab, and should return a list of
    # suggestions that the user will tab through.
    # tabnum is 1 for <TAB> and -1 for <S-TAB> by default
    def tab(self, tabnum):
        # This is a generic tab-completion function that iterates through the
        # content of the current directory.
        return self._tab_directory_content()

class encode(Command):
    """:encode <filename> <directory to extract to>

    A command for encoding audio from a video file into .flac format for import into DaVinci Resolve.
    """    
    # The execute method is called when you run this command in ranger.
    def execute(self):
        import subprocess
        # self.arg(1) is the first (space-separated) argument to the function.
        if self.arg(1):
            # self.rest(1) contains self.arg(1) and everything that follows
            target_filename = self.arg(1)
        else:
            # self.fm is a ranger.core.filemanager.FileManager object and gives
            # you access to internals of ranger.
            # self.fm.thisfile is a ranger.container.file.File object and is a
            # reference to the currently selected file.
            target_filename = self.fm.thisfile.path
	
        extract_path = ""
        # self.arg(1) is the second (space-separated) argument to the function.
        if self.arg(2):
            # self.rest(2) contains self.arg(2) and everything that follows
            extract_path = self.arg(2)

        target_file_root = os.path.splitext(target_filename)[0]
        target_file_ext = os.path.splitext(target_filename)[1]
 
        # Check if archive
        if target_file_ext in [".mkv",".mp4",".flv",".mov"]: 
            # Using bad=True in fm.notify allows you to print error messages:
            if not os.path.exists(target_filename):
                self.fm.notify("The given file does not exist!", bad=True)
                return
            flac_file = "{0}.flac".format(target_file_root)
            if extract_path:
                flac_file = "{0}{1}".format(extract_path,flac_file)
            target_file = '{}'.format(target_filename)
            self.fm.notify(target_filename)
            #shell_text = "echo {}".format(target_file)
            #shell_text = "ffmpeg -i {0} -vn -acodec flac {1}".format(target_file,flac_file)
            
            # THIS WORKS
            shell_text = ['ffmpeg','-i', target_filename,'-vn','-acodec','flac',flac_file]

            # THIS DOES NOT
            #shell_text = ['ffmpeg -i', target_filename,'-vn -acodec flac',flac_file]

        
        # This executes a function from ranger.core.acitons, a module with a
        # variety of subroutines that can help you construct commands.
        # Check out the source, or run "pydoc ranger.core.actions" for a list.
        #self.fm.edit_file(target_filename)
        #self.fm.execute_command(shell_text)
        #subprocess.run(shell_text)
        self.fm.run(shell_text)

class handbrake(Command):
    """:encode <filename> <directory to extract to>

    A command for encoding audio from a video file into .flac format for import into DaVinci Resolve.
    """    
    # The execute method is called when you run this command in ranger.
    def execute(self):
        import subprocess
        # self.arg(1) is the first (space-separated) argument to the function.
        if self.arg(1):
            # self.rest(1) contains self.arg(1) and everything that follows
            target_filename = self.arg(1)
        else:
            # self.fm is a ranger.core.filemanager.FileManager object and gives
            # you access to internals of ranger.
            # self.fm.thisfile is a ranger.container.file.File object and is a
            # reference to the currently selected file.
            target_filename = self.fm.thisfile.path
	
        extract_path = ""
        # self.arg(1) is the second (space-separated) argument to the function.
        if self.arg(2):
            # self.rest(2) contains self.arg(2) and everything that follows
            extract_path = self.arg(2)

        target_file_root = os.path.splitext(target_filename)[0]
        target_file_ext = os.path.splitext(target_filename)[1]
 
        # Check if archive
        if target_file_ext in [".mkv",".flv",".mov"]: 
            # Using bad=True in fm.notify allows you to print error messages:
            if not os.path.exists(target_filename):
                self.fm.notify("The given file does not exist!", bad=True)
                return
            out_file = "{0}.mp4".format(target_file_root)
            if extract_path:
                flac_file = "{0}{1}".format(extract_path,flac_file)
            target_file = '{}'.format(target_filename)
            self.fm.notify(target_filename)
            #shell_text = "echo {}".format(target_file)
            #shell_text = "ffmpeg -i {0} -vn -acodec flac {1}".format(target_file,flac_file)
            
            # THIS WORKS
            shell_text = ['HandBrakeCLI','-i', target_filename,'-e','x264','-o',out_file]

            # THIS DOES NOT
            #shell_text = ['ffmpeg -i', target_filename,'-vn -acodec flac',flac_file]

        
        # This executes a function from ranger.core.acitons, a module with a
        # variety of subroutines that can help you construct commands.
        # Check out the source, or run "pydoc ranger.core.actions" for a list.
        #self.fm.edit_file(target_filename)
        #self.fm.execute_command(shell_text)
        #subprocess.run(shell_text)
        self.fm.run(shell_text)

