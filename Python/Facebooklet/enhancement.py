from Tkinter import*
import facebooklet
import time

def main_notes_window(window, dic_info, dic_status, dic_wall, name_list, \
                      notes_list):
    '''The previous window is destoryed. The main notes window is the main 
       window that shows all the notes of every member of facebooklet.'''
    # This code destroy's the pervious window created
    window.destroy()
    
    # Creating a new Tk window called notes_window
    notes_window = Tk()
    notes_window.title('Facebooklet | Notes')
    
    # Creating a frame in the notes_winow called header_window that only display
    # the headers
    header_frame = Frame(notes_window, bg = '#5F04B4')
    header_frame.grid(row = 0, columnspan = 3)
    
    # Creating a frame in the notes_winow called frame 
    frame = Frame(notes_window)
    frame.grid(row = 1, rowspan = 3, columnspan = 3)
    
    # Creating a frame in the notes_window called notes_frame that only displays 
    # notes entered by the user
    notes_frame = Frame(notes_window)
    notes_frame.grid(row = 4, rowspan = 4, columnspan = 2)
        
    # HEADER
    # Creating Labels that display headers in the notes_window and in the frame 
    # header_frame, headers like, 'facebooklet', 'Home', 'Friends', 'Inbox', 
    facebooklet_logo_label = Label(header_frame, text = ' facebooklet ', \
                                   bg = '#5F04B4', \
                                   font = ("Courier", 16, 'bold'), \
                                   fg= 'white', width = 14, height = 2)
    facebooklet_logo_label.grid(row = 0, column = 0)
    
    home_label = Label(header_frame, text = 'Home', \
                       font = ("Arial", 11, 'bold'), bg = '#5F04B4', \
                       fg = 'white', width = 8, height = 2, anchor = W, \
                       justify = LEFT)
    home_label.grid(row = 0, column = 1)
    
    friends_label = Label(header_frame, text = 'Friends', \
                          font = ("Arial", 11, 'bold'), bg = '#5F04B4', \
                          fg = 'white', width = 82, height = 2, anchor = W, \
                          justify = LEFT)
    friends_label.grid(row = 0, column = 3)
    
    
    #Creating a profile_button to display the profile window back to the user
    profile_command = lambda: facebooklet.profile_window(notes_window, \
                        dic_info, dic_status, dic_wall, name_list, notes_list)
    profile_button = Button(header_frame, text = 'Profile', \
                            font = ("Arial", 11, 'bold'), bg = '#5F04B4', \
                            fg = 'white', anchor=W, justify=LEFT, \
                            command = profile_command)
    profile_button.grid(row = 0, column = 2)
    
    space_label = Label(frame)
    space_label.grid(row = 0, columnspan = 5)
    
    #Creating a add_note_button that takes the user to a window were they add a 
    #note
    text1_label = Label(frame, text = 'Notes', anchor=W, justify=LEFT, \
                        width = 50,font = ('Arial', 16, 'bold'))
    text1_label.grid(row = 1, column = 0)
       
    add_note_command = lambda: note_editor_window(notes_window, dic_info, \
                                                  dic_status, dic_wall, \
                                                  name_list, notes_list)
    add_note_button = Button(frame, text = '+  Write a New Note', \
                             command = add_note_command)
    add_note_button.grid(row = 1, column = 3)
    
    # Displays Label message if there are note added by the user, that is if \
    # the notes_list is a empty list
    if notes_list == []:
        space_label = Label(frame, height = 20, text = 'There are currently' + \
        ' 0 note. To add a note click "Write a New Note"')
        space_label.grid(row = 2, column = 0)
    
    # Frist creating a variable for to display the local time to display it after
    # Go through the loop in a list called notes_list that stores the notes 
    # messages typed by the user at all times and we know that the first index 
    # at note is the name so we create a variable for that and the next index in 
    # the message
    localtime = time.asctime(time.localtime(time.time()))
    for note in notes_list:
        membername = note[0]
        message = note[1]
        
        # Go through the loop of the message and the message is divided into two 
        # the first index is the title and the second index is the body so we 
        # create a variable name for each 
        for i in message:
            title = message[0]
            body = message[1]
        
        # Now that we know the NAME of the current member and their TITLE message 
        # and their BODY message
        # For each we create a Label to display them seperately 
        title_label = Label(notes_frame, text = title)
        title_label.pack()
        
        membername_label = Label(notes_frame, text = 'by ' + \
                                 membername.upper() + '. ' + localtime + '.')
        membername_label.pack()
        
        body_label = Label(notes_frame, text = body)
        body_label.pack()
    
    notes_window.mainloop()

def note_editor_window(window, dic_info, dic_status, dic_wall, name_list, \
                       notes_list):
    '''The notes editor is a window where text entries to edit for the Notes 
       are being saved.'''
    
    # Creating a new_window called notes_editory window
    notes_editor_window = Tk()
    notes_editor_window.title('Facebooklet | Write a Note')
    
    frame = Frame(notes_editor_window)
    frame.pack()          
    
    # Creating a Label called note that appears in the notes_frame only
    note = LabelFrame(frame, padx = 5, pady = 5)
    note.grid(row = 0, column = 0, padx = 10, pady = 10)
    
    # Creating a Label that displays the message 'Title' and then created a Text 
    # for the user to enter in the title of their note
    title_label = Label(note, text = "Title:", anchor = W, justify = LEFT, \
                        width = 44)
    title_label.pack()
    
    title_text = Text(note, height = 2, width = 50, bg = '#E3CEF6')
    title_text.pack()
    
    # Creating a Label that displays the message 'Body' and then created a Text 
    # for the user to enter in the body of their note    
    body_label = Label(note, text="Body:", anchor=W, justify=LEFT, width = 44)
    body_label.pack()
    
    body_text = Text(note, height = 15, width = 50, bg = '#E3CEF6')
    body_text.pack()

    # Creating a Label that displays a text of dashes to separtor 
    separator_label = Label(note, \
        text= '_________________________________________________________', \
        fg = 'lightgray')
    separator_label.pack()
    
    # Creating a publish_button that calls a function notes_data_structure
    publish_command = lambda: notes_data_structure(window, \
                                                   notes_editor_window, \
                                                   dic_info, dic_status, \
                                                   dic_wall, name_list, \
                                                   notes_list, title_text, \
                                                   body_text)
    publish_button = Button(note, text= 'Publish', command = publish_command)
    publish_button.pack()
    
    notes_editor_window.mainloop()
    
def notes_data_structure(window, notes_editor_window, dic_info, dic_status, \
                         dic_wall, name_list, notes_list, title_name, body):
    '''Destorys the note editor window. Creates a new storage for notes that 
       are being typed in title_name and body into the list notes_list.'''
    
    # Get's the last updated of the membername
    membername = name_list[-1]
    
    # Creates a new note storage created by member and appends it to notes_list
    notes = [membername, [title_name.get(1.0, END), body.get(1.0, END)]]
    notes_list.append(notes)
    
    # This destroys the notes_editor_window opened
    notes_editor_window.destroy()
    
    # Call the function main_notes_window
    main_notes_window(window, dic_info, dic_status, dic_wall, name_list, \
                      notes_list)
    
def status_window(window, dic_info, dic_status, dic_wall, name_list, \
                  notes_list):
    '''Previous window destoryed. This window shows all the updated status of 
       each member on facebooklet.'''
    
    # This code destroy's the previous window created
    window.destroy()
    
    # Creating a status_window that displays the updated status of all members
    status_window = Tk()
    status_window.title('Facebooklet | Updated Status')
    
    # Creating a header_frame that displays only the headers in the window
    header_frame = Frame(status_window, bg = '#5F04B4')
    header_frame.grid(row = 0, columnspan = 5)

    space_label = Label(status_window)
    space_label.grid(row = 1, column = 0)
    
    # Creating a status_frame that displays only the status of all members
    status_frame = Frame(status_window)
    status_frame.grid(row = 4, columnspan = 4)
    
    # HEADER
    # Creating Labels that display headers in the status_window and in the frame 
    # header_frame, headers like, 'facebooklet', 'Home', 'Friends', 'Inbox', 
    facebooklet_logo_label = Label(header_frame, text = ' facebooklet ', \
                                   bg = '#5F04B4', \
                                   font = ("Courier", 16, 'bold'), \
                                   fg = 'white', width = 14, height = 2)
    facebooklet_logo_label.grid(row = 0, column = 0)
    
    home_label = Label(header_frame, text = 'Home', \
                       font = ("Arial", 11, 'bold'),  bg = '#5F04B4', \
                       fg = 'white', width = 8, height = 2, anchor=W, \
                       justify=LEFT)
    home_label.grid(row = 0, column = 1)
    
    friends_label = Label(header_frame, text = 'Friends', \
                          font = ("Arial", 11, 'bold'), bg = '#5F04B4', \
                          fg = 'white', width = 60, height = 2, anchor = W, \
                          justify = LEFT)
    friends_label.grid(row = 0, column = 3)
    
    # Creating a profile_button to display the profile window back to the user
    profile_command = lambda: facebooklet.profile_window(status_window, \
                                                         dic_info, dic_status, \
                                                         dic_wall, name_list, \
                                                         notes_list)
    profile_button = Button(header_frame, text = 'Profile', \
                            font = ("Arial", 11, 'bold'), bg = '#5F04B4', \
                            fg = 'white', anchor=W, justify=LEFT, \
                            command = profile_command)
    profile_button.grid(row = 0, column = 2)
    
    text_label = Label(status_window, text = 'All Members > Status Updates', \
                       font = ('Arial', 16, 'bold'), anchor=W, justify=LEFT)
    text_label.grid(row = 2, column = 0)
    
    # Creating a Label that displays the number of members updated their status
    status = dic_status.keys()

    num_of_status = Label(status_window, text = 'You have ' + str(len(status)) \
                          + ' members with recent status updates', anchor=W, \
                          justify=LEFT)
    num_of_status.grid(row = 3, column = 1)
    
    # Go through the keys in dic_status dictonary and print the name of the 
    # membername with their status in a LABEL
    for keys in dic_status.keys():
        value = dic_status[keys]
        status = keys + ' is ' + value
        
        show_membername_label = Label(status_frame, text = keys, font = \
                                      ('Arial', 14, 'bold'))
        show_membername_label.pack()
        
        show_status_label = Label(status_frame, text = status, anchor=W, \
                                  justify=LEFT)
        show_status_label.pack()

    status_window.mainloop()