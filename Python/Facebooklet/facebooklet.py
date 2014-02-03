from Tkinter import *
from PIL import ImageTk
import Image
import tkFileDialog
import time
import enhancement

def settings_window(window, dic_info, dic_status, dic_wall, name_list, \
                    notes_list):
    '''Destorys previous window. Settings window is a window where the user 
    asked to input any additional information that they want to update in their 
    information. These additional information are stored into dic_info, 
    dic_status, dic_wall, and notes_list. The last member of the list name_list 
    is the current member which is display under the facbooklet header.'''
    
    window.destroy()
    # This code destroy's the previous window created
    
    # Creating setting_window that lets the user modify their information
    settings_window = Tk()
    settings_window.title('Facebooklet | Settings')
    
    # Creating a header_frame that only display headers in this frame
    header_frame = Frame(settings_window, bg = '#5F04B4')
    header_frame.pack()
    
    frame = Frame(settings_window, bg = 'white')
    frame.pack()
    
    # Creating labels that displays text like 'facebooklet', 'Home', 'Friends', 
    # 'Inbox', in the header_frame only

    
    facebooklet_label1 = Label(header_frame, text = ' facebooklet ', \
                               bg = '#5F04B4', font = ("Courier", 16, 'bold'), \
                               foreground = 'white', width = 14, height = 2)
    facebooklet_label1.grid(row = 0, column = 0)
    
    facebooklet_label2 = Label(header_frame, text = 'Home', \
                                font = ("Arial", 11, 'bold'), bg = '#5F04B4', \
                                foreground = 'white', width = 8, height = 2, \
                                anchor = W, justify = LEFT)
    facebooklet_label2.grid(row = 0, column = 1)
    
    # Creating a profile_button that once the user is done saving changes to 
    # their information this button takes their user to new window which then 
    # displays all the information they have updated      
    profile_command = lambda: profile_window(settings_window, dic_info, \
                                dic_status, dic_wall, name_list, notes_list)
    facebooklet_label3 = Button(header_frame, text = 'Profile', \
                                font = ("Arial", 11, 'bold'), bg = '#5F04B4', \
                                foreground = 'white', \
                                anchor = W, justify = LEFT, \
                                command = profile_command)
    facebooklet_label3.grid(row = 0, column = 2)
    
    facebooklet_label4 = Label(header_frame, text = '   Friends', \
                                font = ("Arial", 11, 'bold'), bg = '#5F04B4', \
                                foreground = 'white', width = 60, height = 2, \
                                anchor = W, justify = LEFT)
    facebooklet_label4.grid(row = 0, column = 3)  
    
    # Creating labels that displays text like 'Settings', 'Networks', 
    # 'Notifications, 'Mobile', 'Language'
    name = name_list[-1]
    capital_name = name[0].upper() + name[1:].lower()
    
    empty_label = Label(frame, bg = 'white')
    empty_label.grid(row=1, columnspan=5)
    
    account_label = Label(frame, text = capital_name + "'s Account", \
                          bg = 'white', fg = '#5F04B4', \
                          font = ('Arial', '16', 'bold'), anchor = W, \
                          justify = LEFT)
    account_label.grid(row = 2, columnspan = 5)
    
    empty_label2 = Label(frame, bg = 'white')
    empty_label2.grid(row=3, columnspan=5)
    
    settings_label = Label(frame, text = 'Settings', bg = '#5F04B4', \
                           fg = 'white', width = 20, relief = 'groove')
    settings_label.grid(row = 4, column = 0)
    
    networks_label = Label(frame, text = 'Networks', bg = '#E3CEF6', \
                           width = 15, relief = 'groove')
    networks_label.grid(row = 4, column = 1)
    
    notifications_label = Label(frame, text = 'Notifications', bg = '#E3CEF6', \
                                width = 20, relief = 'groove')
    notifications_label.grid(row = 4, column = 2)
    
    mobile_label = Label(frame, text = 'Mobile', bg = '#E3CEF6', width = 20, \
                         relief = 'groove')
    mobile_label.grid(row = 4, column = 3)
      
    language_label = Label(frame, text = 'Language', bg = '#E3CEF6', \
                           width = 20, relief = 'groove')
    language_label.grid(row = 4, column = 4)
    
    space_label = Label(frame, bg = 'white')
    space_label.grid(row = 5, column = 0) 
    
    # Creating widgets like a Label, and Button for the user to UPLOAD a picture
    # they want to display it in their facebook and a Label displays the name 
    # of the picture they choose
    picture_label = Label(frame, text = 'My Picture:', fg = '#5F04B4', \
                          bg = 'white')
    picture_label.grid(row = 8, column = 1)
    
    picname = StringVar()
    picname_label = Label(frame, textvariable = picname, relief = 'groove', \
                          width = 20, bg = '#E3CEF6', fg = '#5F04B4')
    picname_label.grid(row = 8, column = 2)
    
    upload_command = lambda: open_new_pic(filename, picname)
    upload_picture_button = Button(frame, text = 'Upload Picture', \
                                   command = upload_command, bg = '#E3CEF6')
    upload_picture_button.grid(row = 8, column = 3)

    space_label = Label(frame, bg = 'white')
    space_label.grid(row = 9, column = 0)
    
    # Creating widgets like a Label, and Entry for the user to enter their
    # information that they want to display it in facebook such as what SEX you 
    # are, what is your NETWORKS, and your BIRDTHDAY DATE
    information_label = Label(frame, text = ' Information ', bg = '#5F04B4', \
                              fg = 'white', width = 15)
    information_label.grid(row = 10, column = 0)
    
    sex_label = Label(frame, text = 'Sex:', fg = '#5F04B4', bg = 'white')
    sex_label.grid(row = 12, column = 1)

    sex_entry = Entry(frame, bg = '#E3CEF6')
    sex_entry.grid(row = 12, column = 2)
    
    networks_label = Label(frame, text = 'Networks:', fg = '#5F04B4', \
                           bg = 'white')
    networks_label.grid(row = 14, column = 1)
    
    networks_entry = Entry(frame, bg = '#E3CEF6')
    networks_entry.grid(row = 14, column = 2)

    birthday_label = Label(frame, text = 'Birthday Date:', fg = '#5F04B4', \
                           bg = 'white')
    birthday_label.grid(row = 16, column = 1)
    
    birthday_entry = Entry(frame, bg = '#E3CEF6')
    birthday_entry.grid(row = 16, column = 2)
 
    space_label = Label(frame, bg = 'white')
    space_label.grid(row = 17, column = 0)
    
    space_label = Label(frame, bg = 'white')
    space_label.grid(row = 18, column = 0)
    
    # Creating widgets like a Label, Entry, and Button for the user to enter 
    # any friends that they would like to add in their friends lists in facebook
    friends_label = Label(frame, text = 'Your Friends:', bg = '#5F04B4', \
                          fg = 'white', width = 15)
    friends_label.grid(row = 19, column = 0)
    
    add_friends_label = Label(frame, text = 'Add Friends:', fg = '#5F04B4', \
                              bg = 'white')
    add_friends_label.grid(row = 20, column = 1)
    
    add_friends_entry = Entry(frame, bg = '#E3CEF6')
    add_friends_entry.grid(row = 20, column = 2)
    
    add = StringVar()
    add_command = lambda: add_friends(dic_info, add_friends_entry, add, \
                                      name_list)
    add_friends_button = Button(frame, text = 'Add', \
                                command = add_command, bg = '#E3CEF6')
    add_friends_button.grid(row = 20, column = 3)
    
    show_add_friends_label = Label(frame, textvariable = add, fg = '#5F04B4', \
                                   bg = 'white')
    show_add_friends_label.grid(row = 20, column = 4)
    
    # Creating widgets like a Label, Entry, and Button for the user to enter 
    # any friends that they would like to delete in their friends lists
    delete_friends_label = Label(frame, text = 'Delete Friends:', \
                                 fg = '#5F04B4', bg = 'white')
    delete_friends_label.grid(row = 21, column = 1)
    
    delete = StringVar()
    delete_friends_entry = Entry(frame, bg = '#E3CEF6')
    delete_friends_entry.grid(row = 21, column = 2)
    
    delete_command = lambda: delete_friends(dic_info, delete_friends_entry, \
                                            delete, name_list)
    delete_friends_button = Button(frame, text = 'Delete', \
                                   command = delete_command, bg = '#E3CEF6')
    delete_friends_button.grid(row = 21, column = 3)
    
    show_delete_friends_label = Label(frame, textvariable = delete, \
                                      fg = '#5F04B4', bg = 'white')
    show_delete_friends_label.grid(row = 21, column = 4)   
    
    # Creating data structure Button that saves all changes the user updated
    save_command = lambda: save_changes(dic_info, networks_entry, sex_entry, \
                                        birthday_entry, filename, name_list)
    save_button = Button(frame, text = 'Save Changes', command = save_command, \
                         bg = '#E3CEF6')
    save_button.grid(row = 17, column = 3)
    
    # Creating a Delete Button for any reason the user wants to delete their 
    # account in facebook
    deletemember = StringVar()
    delete_command2 = lambda: delete_member_window(settings_window, dic_info, \
                                                  dic_status, dic_wall, \
                                                  name_list, notes_list)
    deletemember_button = Button(frame, text = 'Delete Account', \
                                 command = delete_command2, bg = '#E3CEF6')
    deletemember_button.grid(row = 22, column = 3)
    
    empty_label = Label(frame, bg = 'white')
    empty_label.grid(row=23, columnspan=5)
    
    filename = []
    dic_info[name.lower()] = [networks_entry.get(), sex_entry.get(), \
                              birthday_entry.get(), [], filename]
    
    settings_window.mainloop()
    
def profile_window(window, dic_info, dic_status, dic_wall, name_list, \
                   notes_list):
    '''Destorys previous window. Profile window is a window where everything 
       that has been stored into the dictionaries dic_info, dic_status, 
       dic_wall, notes_list are displayed into widgets. The last member of the 
       list name_list is the current member is being displayed under the 
       facebooklet header.'''
    
    # This code destroy's the pervious window opened
    window.destroy()
        
    # Creating a new window called profile_window
    profile_window = Tk()
    profile_window.title('facebooklet | Profile')
    
    # Creating Menu Bar called 'Applications' in the profile_window 
    menubar = Menu(profile_window)
    filemenu = Menu(menubar)
    
    menubar.add_cascade(label = "Applications", menu= filemenu)
    
    filemenu.add_command(label = "Notes", command = lambda : \
        enhancement.main_notes_window(profile_window, dic_info, dic_status, \
                                      dic_wall, name_list, notes_list))
    filemenu.add_separator()   
                     
    filemenu.add_command(label = "Status", command = lambda : \
        enhancement.status_window(profile_window, dic_info, dic_status, \
                                  dic_wall, name_list, notes_list))
    
    # FRAMES
    # Creating a list of frames to arrange the layout of the facebooklet in a 
    # more organized way

    # Displays Header Frame
    header_frame = Frame(profile_window, bg = '#5F04B4')
    header_frame.grid(row = 0, columnspan = 7)
    
    # Displays Membername frame
    name_frame = Frame(profile_window)
    name_frame.grid(row = 2, rowspan = 1, column = 1)
    
    # Display Picture frame
    pic_frame = Frame(profile_window)
    pic_frame.grid(row = 2, rowspan = 4, column = 0, columnspan = 1)

    # Status frame
    status_frame = Frame(profile_window)
    status_frame.grid(row = 3, rowspan = 2, column = 1, columnspan = 5)
    
    space_label = Label(profile_window)
    space_label.grid(row = 7, columnspan = 7)
    
    # Displays Information box frame
    info_frame = Frame(profile_window)
    info_frame.grid(row = 8, rowspan = 7, column = 0, columnspan = 1)
    
    # Displays Friends box frame
    friends_frame = Frame(profile_window)
    friends_frame.grid(row = 16, column = 0, columnspan = 1)
    
    # Displays Wall Text frame
    wall_text_frame = Frame(profile_window)
    wall_text_frame.grid(row = 8, rowspan = 5, column = 1, columnspan = 5)
    
    # Creating Labels in the hearder_frame that displays text like, 
    # 'facebooklet', 'Home', Profile', 'Friends'
    facebooklet_logo_label = Label(header_frame, text = ' facebooklet ', \
        bg = '#5F04B4', font = ("Courier", 16, 'bold'),  fg = 'white', \
        width = 12, height = 2)
    facebooklet_logo_label.grid(row = 0, column = 0)
    
    home_label = Label(header_frame, text = 'Home', \
                                font = ("Arial", 11, 'bold'),  bg = '#5F04B4', \
                                foreground = 'white', width = 10, height = 2, \
                                anchor = W, justify = LEFT)
    home_label.grid(row = 0, column = 1)
   
    profile_label = Label(header_frame, text = 'Profile', \
                                font = ("Arial", 11, 'bold'), bg = '#5F04B4', \
                                foreground = 'white', width = 10, height = 2, \
                                anchor = W, justify = LEFT)
    profile_label.grid(row = 0, column = 2)
    
    friends_label = Label(header_frame, text = 'Friends', \
                                font = ("Arial", 11, 'bold'), bg = '#5F04B4', \
                                foreground = 'white', width = 30, height = 2, \
                                anchor = W, justify = LEFT)
    friends_label.grid(row = 0, column = 3)
    
    # Creating a Button for the user to go back to their settings and change any 
    # information they want to update it in their profile
    settings_button = Button(header_frame, text = 'Settings', \
                             font = ("Arial", 11, 'bold'), bg = '#5F04B4', \
                    fg = 'white', width = 12, height = 1, command = \
                    lambda: settings_window(profile_window, \
                        dic_info, dic_status, dic_wall, name_list, notes_list))
    settings_button.grid(row = 0, column = 4)
    
    # SEARCH FRIEND
    # Creating a Label, and Entry, for the user to enter a member NAME which 
    # could be their friend name or any other member NAME that they want to 
    # search and see their profile
    search_friend_label = Label(header_frame, text = 'Search: ', \
                                font = ("Arial", 11, 'bold'), \
                                bg = '#5F04B4', fg = 'white', height = 1)
    search_friend_label.grid(row = 0, column = 5)
    
    membername_entry = Entry(header_frame)
    membername_entry.grid(row = 0, column = 6)
    
    # Creating a Label called show_search_label that displays a message if the 
    # user has searched a valid name or not and a search_friend_button to calls 
    # the function search_friends
    search = StringVar()
    show_search_label = Label(profile_window, textvariable = search, font = \
                              ("Arial", 14, 'bold'), fg = 'red')
    show_search_label.grid(row = 1, column = 5)

    search_command = lambda: search_friends(dic_info, membername_entry, sex, \
                                            networks, birthday, friends, \
                                            membername, search, dic_status, \
                                            status, dic_wall, wall1, wall2, \
                                            wall3, image_label, name_list)
    search_friend_button = Button(header_frame, text = 'X', \
                                  font = ("Arial", 11, 'bold'), \
                                  bg = '#5F04B4', fg = 'white', height = 1, \
                                  command = search_command)
    search_friend_button.grid(row = 0, column = 7)
    
    # Creating a Label called show_membername_label that displays the Currnet 
    # Member's name 
    membername = StringVar()
    show_membername_label = Label(name_frame, textvariable = membername, \
                                  font = ('Arial', 18, 'bold'), anchor = W, \
                                  justify = LEFT, width = 15)
    show_membername_label.grid(row = 0, column = 0)
    
    # PICTURE
    # Creating a Label called image_label that displays the picture the user 
    # uploaded
    image_label = Label(pic_frame, width = 20, height = 10, text = \
        'My picture', relief = 'groove', fg = '#5F04B4')
    image_label.grid(row = 0, column = 0)    
    
    # INFORMATION
    # Creating a new frame called information_frame in the profile_window that 
    # would display the users information of NETWORKS, BIRTHDAY DATE, and SEX
    information_frame = LabelFrame(info_frame)
    information_frame.grid(row = 4, column = 0)
    
    information_label = Label(information_frame, text = ' Information ', \
                              bg = '#5F04B4',fg = 'white', width = 20)
    information_label.pack()
    
    # Creating a Label called display_networks_label that displays the users 
    # information of NETWORKS inside the information_frame
    networks_label = Label(information_frame, text = 'Networks:', \
                           fg = '#5F04B4')
    networks_label.pack()
    
    networks = StringVar()
    display_networks_label = Label(information_frame, textvariable = networks)
    display_networks_label.pack()
        
    # Creating a Label called display_birthday_label that displays the users 
    # information of BIRTHDAY DATE inside the information_frame
    birthday_label = Label(information_frame, text = 'Birthday Date:', \
                           fg = '#5F04B4')
    birthday_label.pack()
    
    birthday = StringVar() 
    display_birthday_label = Label(information_frame, textvariable = birthday)
    display_birthday_label.pack()
    
    # Creating a Label called display_sex_label that displays the users 
    # information of SEX inside the information_frame
    sex_label = Label(information_frame, text = 'Sex:', fg = '#5F04B4')
    sex_label.pack()
    
    sex = StringVar() 
    display_sex_label = Label(information_frame, textvariable = sex)
    display_sex_label.pack()
    
    # FRIENDS
    # Creating a new frame called friends_frame that would display the list of 
    # friends the user has
    friends_frame = LabelFrame(friends_frame)
    friends_frame.grid(row = 6, column = 0)
    
    friends_label = Label(friends_frame, text = 'Your Friends ', fg = 'white', \
                          bg = '#5F04B4', width = 20)
    friends_label.pack()
    
    # Creating a Label called friends_list_label the displays a list of friends 
    # that the user has added 
    friends = StringVar()
    friends_list_label = Label(friends_frame, textvariable = friends)
    friends_list_label.pack()
    
    # Creating a Label called show_status_label that displays the status of the 
    # user including the their NAME and their status    
    status_label1 = Label(status_frame, text = 'Status:')
    status_label1.pack()
    
    status = StringVar()
    show_status_label = Label(status_frame, textvariable = status, \
                              fg = '#5F04B4')
    show_status_label.pack()   
    
    space_label = Label(status_frame)
    space_label.pack()
    
    # Creating widgets like Label in the status_frame for the user to enter 
    # their status in the status_text and then the share_button would display
    # the users status 
    status_label = Label(status_frame, bg = '#F2F2F2')
    status_label.pack()
    
    status_label2 = Label(status_label, text= "What's on your mind?", \
                          bg = '#E3CEF6', width = 60, anchor = W, \
                          justify = LEFT)
    status_label2.pack()
    
    status_text = Text(status_label, height = 1, width = 65)
    status_text.pack()
    
    share_button = Button(status_label, text = "Share", command = \
            lambda: display_status(name_list, dic_status, status_text, status))
    share_button.pack()
    
    # WALL
    # Creating a new frame in the profile_window called wall_frame  
    wall_frame = LabelFrame(wall_text_frame, text = "Wall", fg = '#5F04B4', \
                            bg= '#F2F2F2')
    wall_frame.pack()
    
    # Creating widgets like Label in the wall_frame for the user to enter 
    # their message in the Text wall_txt and then the Button share_button would 
    # call the funtion post_text to post the message 
    wall_txt_prompt = Label(wall_frame, text="Write something...", width = 60, \
                            bg = '#E3CEF6', anchor = W, justify = LEFT)
    wall_txt_prompt.pack()
    
    wall_txt = Text(wall_frame, height = 3, width = 65)
    wall_txt.pack()
    
    share_button = Button(wall_frame, text = "Share", command = lambda: \
        post_text_on_wall(wall1, wall2, wall3, wall_txt, dic_wall, name_list))
    share_button.pack()
    
    empty_label = Label(wall_frame, bg = '#F2F2F2')
    empty_label.pack()

    # Creating a new frame in the profile_window called my_wall_frame to display 
    # all the wall postings
    space_label = Label(wall_frame, text = 'My Wall')
    space_label.pack()
    
    my_wall_label = LabelFrame(wall_frame)
    my_wall_label.pack()
    
    empty_label2 = Label(wall_frame, bg = '#F2F2F2')
    empty_label2.pack()

    # Creating 3 wall Labels in the my_wall_label frame that displays the
    # message of the user in their profile 
    wall1 = StringVar()
    wall2 = StringVar()
    wall3 = StringVar()
    
    post1_wall = Label(my_wall_label, textvariable = wall1, width = 60, \
                       fg = '#5F04B4', font= ("Arial", 12, 'bold'))
    post1_wall.pack()
    
    post2_wall = Label(my_wall_label, textvariable = wall2, width = 60, \
                       fg = '#5F04B4', font= ("Arial", 12, 'bold'))
    post2_wall.pack()
    
    post3_wall = Label(my_wall_label, textvariable = wall3, width = 60, \
                       fg = '#5F04B4', font= ("Arial", 12, 'bold'))
    post3_wall.pack()
    
    # This button called join_button will call the function settings_window for 
    # the user to create a new account
    join_button = Button(profile_window, text = 'Join facebooklet', command = \
        lambda: join_facebooklet_window(profile_window, dic_info, dic_status, \
                                        dic_wall, name_list, notes_list))
    join_button.grid(row = 21, column = 4)
    
    # Created some Labels that shows some detailed messages of a facebooklet
    text1_label = Label(profile_window, text = '________________________' * 4, \
                   fg = 'gray')
    text1_label.grid(row = 20, columnspan = 7)
    
    text2_label = Label(profile_window, text = 'Facebooklet  2009', \
                        fg = 'gray', height = 2)
    text2_label.grid(row = 21, column = 0)    
    
    displaying_information(dic_info, membername_entry, sex, \
        networks, birthday, friends, membername, search, dic_status, status, \
        dic_wall, wall1, wall2, wall3, image_label, name_list)
            
    profile_window.config(menu=menubar)
    profile_window.mainloop()

def updating_data_structure(dic_info, networks, sex, birthday, filename, \
                            name_list):  
    '''Store the entries from membername, networks, sex, birthday, and filename 
       into the dictionary dic_info of the last member in the list name_list 
       (the current member).'''
    
    # Get the current member NAME
    membername = name_list[-1]
    value = dic_info[membername.lower()]
        
    # If the user entered in an information such as their networks, sex, 
    # birthday, filename, then go through the their values in the dictonary and 
    # remove the previous information of the user and insert updated networks 
    # information of the user and go through this proccess for each information
    if networks.get() != '':
        value.remove(value[0])
        value.insert(0, networks.get())
        
    if sex.get() != '':
        value.remove(value[1])
        value.insert(1, sex.get())
        
    if birthday.get() != '':
        value.remove(value[2])
        value.insert(2, birthday.get())
            
    if filename != []:
        value.pop(4)
        value.insert(4, filename)  
        
def displaying_information(dic_info, membername_entry, sex, networks, \
                           birthday, friends, membername, search, dic_status, \
                           status, dic_wall, text1, text2, text3, image_label, \
                           name_list):
    '''Display the current member from the list name_list to it's entry 
       membername. Search for the current name in the dictionaries dic_info, 
       dic_status, and dic_wall and get it's values. Set the values to it's 
       rightful entries such as sex, networks, birthday, friends, status, text1,
       text2, text3.'''
    
    # First get the NAME of the current member and display it in the profile 
    # window, then get the value of the NAME in the dic_info. Go through the 
    # value and set each index to it's exact particular information. 
    name = name_list[-1]
    capital_name = name[0].upper() + name[1:].lower()
    membername.set(capital_name)
    value = dic_info[name.lower()]
    if value != []:
        networks.set(value[0])
        sex.set(value[1])
        birthday.set(value[2])
        friends.set(value[3])
        
        # If the the user has uploaded a picture in then display that picture in 
        # their profile and if not display a default.jpg in their profile
        if value[4] != []:
            filename = value[4]
            open_known_pic(image_label,filename[0])
        else:
            filename = str('default.jpg')
            open_known_pic(image_label,filename)
      
    # Displaying the Status
    # Go through the keys in dic_status, if the NAME is in the list of keys then 
    # find it's value in the dictonary and display their status in the profile 
    key = dic_status.keys()
    if key.count(name.lower()) == 1:
        values = dic_status[name.lower()]
        status.set(name + ' is ' + values)
    else:
        status.set('')
            
    # Displaying the Wall
    # Go through the keys in dic_wall, if the NAME is in the list of keys then 
    # find its value in the dictonary and display their wall post in the profile 
    key = dic_wall.keys()
    if key.count(name.lower()) == 1:
        value = dic_wall[name.lower()]
        localtime = time.asctime(time.localtime(time.time()))
            
        # If the index at 0 in value list is not empty then set text1 
        # StringVar to be the index at 0 in value list plus the local time
        # Else set the text1 stringvar to be the index at 0 in value list
        if value[0] != '':
            text1.set(value[0] + '\n' + localtime)
        else:
            text1.set(value[0])
            
            if value[1] != '':
                text2.set(value[1] + '\n' + localtime)
            else:
                text2.set(value[1])
                
            if value[2] != '':
                text3.set(value[2] + '\n' + localtime)
            else:
                text3.set(value[2])
    else:
        text1.set('')
        text2.set('')
        text3.set('')
        
def search_friends(dic_info, membername_entry, sex, networks, birthday, \
                   friends, membername, search, dic_status, status, dic_wall, \
                   text1, text2, text3, image_label, name_list):
    '''Search for the name being typed in membername_entry which is saved into 
       StringVar search. The search calls the function displaying_information 
       which goes through the dictionaries dic_info, dic_status, dic_wall and 
       displays all the entries under the name that was searched for such as 
       sex, networks, birthday, friends, status, membername, text1, text2, 
       text3, and image_label. Also, appends the name into name_list making that 
       user as the current member if it is valid. Else if the name is not valid,
       a nonvalid statment appears.'''
    
    search.set('')
    
    name_list.append(membername_entry.get())
    
    # Go through the keys in the dictonary dic_info
    # If the search NAME entered by the user is in the list of keys atleast once 
    # then get the values of the NAME in the dictonary 
    # Now we have the values and we know the order of which information comes, 
    # set each of the information according to it's index in the value list
    # Else if the NAME isn't in the list of keys then show a message saying that 
    # the 'NAME entered can't be found'
    key = dic_info.keys()
    if key.count(membername_entry.get().lower()) == 1:
        displaying_information(dic_info, membername_entry, sex, networks, \
        birthday, friends, membername, search, dic_status, status, dic_wall, \
        text1, text2, text3, image_label, name_list)

    else:
        name_list.pop(-1)
        search.set(membername_entry.get().lower() + ' ' + 'can"t be found')

def post_text_on_wall(text1, text2, text3, wall_txt, dic_wall, name_list):
    '''Post the text from StringVar's text1, text2, text3 that are being typed 
       from text entry wall_txt. Get the current members name from name_list and
       store each StringVar into a list. And lastly, store the membername as a 
       key and the list of StringVar's as a value in the dictionary dic_wall.'''
    
    # Get the current member NAME
    membername = name_list[-1]
    
    # Go through the keys in the dictonary dic_walls and if the NAME is not 
    # in the list of keys then create a item in dic_wall, which has key as 
    # the NAME, name the value as a list of 3 empty strings
    # Else the NAME is in the list of keys then get the value of the NAME in 
    # the dictonary dic_wall
    
    keys = dic_wall.keys()
    if keys.count(membername.lower()) == 0:
        dic_wall[membername.lower()] = ['', '', '']
        value = dic_wall[membername.lower()]
    else:
        value = dic_wall[membername.lower()]
        
    value.insert(0, wall_txt.get(1.0, END))
    # Keep looping until the length of the list value is 3.
    while len(value) != 3:
        localtime = time.asctime(time.localtime(time.time()))
        
        # If the index at 0 in value list is not empty then set text1 
        # StringVar to be the index at 0 in value list plus the local time
        # Else set the text1 stringvar to be the index at 0 in value list
        if value[0] != '':
            text1.set(value[0] + '\n' + localtime)
        else:
            text1.set(value[0])
                
        if value[1] != '':
            text2.set(value[1] + '\n' + localtime)
        else:
            text2.set(value[1])
            
        if value[2] != '':
            text3.set(value[2] + '\n' + localtime)
        else:
            text3.set(value[2])
            
        value.pop(-1)
        
    wall_txt.delete(1.0, END)
    
def add_friends(dic_info, add_friends_entry, add, name_list):
    '''Add a friend by getting the last member of the list name_list 
       (the current member), and matching it's values in the dictionary 
       (dic_info). While it's values is not empty, get the entry of friends to 
       add (add_friends_entry) and match and add. Nonvalid statements are 
       displayed in StringVar add if any list or dictionaries are empty or do 
       not match it's values.'''
    
    # Get the current member NAME
    membername = name_list[-1]
    
    # Check if the user entered FRIEND NAME that is not empty 
    if add_friends_entry.get() != '':
            
        # Check if the user didn't enter their own name as a FRIEND NAME and  
        if membername.lower() != add_friends_entry.get().lower():
            
            # Go through the keys in the dictonary dic_info if the entered 
            # FRIEND NAME by the user is in the list of keys then get the 
            # value of the FRIEND NAME in the dictonary 
            keys = dic_info.keys()
            if keys.count(add_friends_entry.get().lower()) == 1:
                friendname_values = dic_info[add_friends_entry.get().lower()]
                
                # If the value list of the FRIENDS does not have the 
                # membername in it, then append it to the value list
                if friendname_values[3].count(membername.lower()) == 0:
                    friendname_values[3].append(membername.lower())
                    
                    # Now get the value of the membername in the dictonary 
                    # dic_info and append the FRIEND NAME in the value list
                    membername_values = dic_info[membername.lower()]
                    membername_values[3].append(add_friends_entry.get().lower())
                    add.set('You added ' + add_friends_entry.get().lower() + \
                            ' as your friend')
                        
                else:
                    add.set(add_friends_entry.get().lower() + \
                                ' is already your friend')
            else:
                add.set(add_friends_entry.get().lower() + \
                        ' does not exist as a member')
        else:
            add.set('You can"t add yourself as a friend!')
    else:
        add.set('Please enter a friend name to add.')
                
def delete_friends(dic_info, delete_friends_entry, delete, name_list):
    '''Delete a friend by getting the last member of name_list (current member),
       and matching it's values in the dictionary (dic_info). While it's values 
       is not empty, get the entry of friends to delete (delete_friends_entry) 
       and match and delete. Display nonvalid statements in StringVar delete if 
       any list or dictionaries are empty or do not match it's values.'''
    
    # Get the current member NAME  
    membername = name_list[-1]
    membername_values = dic_info[membername.lower()]
    
    # Check if the user entered FRIEND NAME that is not empty and if it is 
    # empty then display a message in delete stringvar
    if delete_friends_entry.get() != '':
        
        # Check if the current member value list is not empty and if it is  
        # empty display a message in delete StringVar
        if membername_values != []:
            
            # Check if the current member value list has the FRIEND NAME in 
            # it and if it does then remove the FRIEND NAME in the value list
            # Else display the message in delete StringVar
            if membername_values[3].count(delete_friends_entry.get().lower()) == 1:
                membername_values[3].remove(delete_friends_entry.get().lower())
                    
                # Get the the FRIEND NAME value in the dic_info dictonary 
                # and remove the current membername from the list too
                friendname_values = dic_info[delete_friends_entry.get().lower()]
                friendname_values[3].remove(membername.lower())
                delete.set(delete_friends_entry.get().lower() + ' \has been deleted.')
            else:
                delete.set(delete_friends_entry.get().lower() + ' is not a friend.')
        else:
            delete.set('You have no friends added to delete.')
    else:
        delete.set('Please enter a friend name to delete.')
        
def open_new_pic(filename, picname):
    '''Use a file dialog to ask the user to choose a file containing a 
    picture.'''
    
    f = tkFileDialog.askopenfilename()
    filename.append(f)
    
    pic_name = filename[0]
    num = pic_name.count('/')
    
    #Keep looping until only one '/' left in the filename of the picture
    while num >= 1:
        slash = pic_name.find('/')
        pic_name = pic_name[slash + 1:]
        num = pic_name.count('/')
    picname.set(pic_name)
        
def delete_member_window(window, dic_info, dic_status, dic_wall, name_list, \
                         notes_list):
    '''Delete the current member by asking the user if they would like their 
       account to be deleted. If yes, the window will call the function 
       delete_member_data to delete the member from the lists/dictionaries 
       name_list, dic_info, dic_status, dic_wall, and notes_list. If not, 
       destory window and resume to settings window.'''
    
    # Creating a delete_window for the user to choose whether they want to 
    # delete their account in facebooklet or not
    delete_window = Tk()
    
    frame = Frame(delete_window)
    frame.pack()
    
    message_label = Label(frame, \
                        text = 'Are you sure you want to Delete your account?')
    message_label.grid(row = 0, column = 1)
    
    # If the user chooses the YES delete account button then the program would 
    # go to the delete_member function and delete all the information saved and 
    # start again from signing up   
    yes_button = Button(frame, text = 'YES', \
                        command = lambda: delete_member_data(window, \
                                                             delete_window, \
                                                             dic_info, \
                                                             dic_status, \
                                                             dic_wall, \
                                                             name_list, \
                                                             notes_list))
    yes_button.grid(row = 1, column = 0)
    
    #If the user chooses the NO delete account button then the program would 
    #destroy this delete_window and resume back to the settings_window
    no_button = Button(frame, text = 'NO', \
                       command = lambda: delete_window.destroy())
    no_button.grid(row = 1, column = 2)

def delete_member_data(window, delete_window, dic_info, dic_status, dic_wall, \
                       name_list, notes_list):
    '''The previous window is destoryed. Delete the current member by getting 
       the last member of the list name_list (the current member) and removing 
       the member name. Also, deleting the member from the dictionaries 
       dic_info, dic_status, dic_wall and a list notes_list. After deleting, 
       the current window is destoryed and directed to the main window of 
       facebooklet.'''
    
    delete_window.destroy()
    
    # Get the current member NAME    
    membername = name_list[-1]
    name_list.remove(membername)
        
    # Delete the membername in dic_info, dic_status, dic_wall
    dic_info.pop(membername.lower())
    
    if dic_status.keys().count(membername.lower()) == 1:
        dic_status.pop(membername)
        
    if dic_wall.keys().count(membername.lower()) == 1:
        dic_wall.pop(membername)
        
    # Go through the keys in the dictonary dic_info and get for each keys in 
    # the dic_info get it's value
    for keys in dic_info.keys():
        values = dic_info[keys]
        
        # values[3] is the index which stores the list of friends each 
        # member has added, so we go through that list and see if any has 
        # added the current member as their friend 
        # If they do have the current membername in their friends list then 
        # remove it if not go to the next keys in the dic_info
        for i in values[3]:
            if i == membername:
                values[3].remove(membername)
    
    # Go through the note in notes_list and if the frist index in note isn't the
    # current membername then append it to the new_notes_list created
    new_notes_list = []
    for note in notes_list:
        if note[0] != membername:
            notes_list.append(note)

    join_facebooklet_window(window, dic_info, dic_status, dic_wall, name_list, \
                            new_notes_list)

def display_status(name_list, dic_status, status_text, status):
    '''Set the StringVar status by getting the current member in the list 
       name_list and the text that is being typed into the entry status_text. 
       Store the current name and it's values from the entry status_text into 
       the dictionary dic_status. Else, if a status is not being entered and 
       nonvalid statement appears. '''
    
    # If the name_list is not empty and that means there is alteast one member 
    # in the facebooklet then get the NAME of the last member in the name_list
    # as the current member
    membername = name_list[-1]
    
    # In the dictonary dic_status make the key as the current member and the 
    # value as status typed by the current member
    # Also set the status StringVar to first the current member name and 
    # then the status they updated 
    if status_text.get(1.0, END) != '\n' :
        dic_status[membername.lower()] = status_text.get(1.0, END)
        status.set(membername + ' is ' + status_text.get(1.0, END))
        status_text.delete(1.0, END)
    else:
        status.set('Please enter a Status: ')
        
def open_known_pic(label, filename):
    '''Scale the picture in file "filename" to PHOTO_SIZE (a global variable)
       and display it in Label label.  PHOTOSIZE is a tuple containing two 
       integers: the width and height in which to display the picture, 
       in pixels.'''
    
    PHOTO_SIZE = (200, 300)

    label.image = Image.open(filename)
    label.image.thumbnail(PHOTO_SIZE, Image.ANTIALIAS)
    update_label(label) 
    
def update_label(label):
    '''Update Label label to re-display its image.  This needs to be called
    any time label's image is changed.'''
    
    photo = ImageTk.PhotoImage(label.image)
    label.config(image = photo)
    label.config(width = photo.width())
    label.config(height = photo.height())

    # Keep a reference to the PhotoImage.  If nothing were to point to it,
    # Python would "garbage collect" it.
    label.photo = photo
    
def join_facebooklet_window(window, dic_info, dic_status, dic_wall, name_list, \
                            notes_list):
    '''Destory previous window. Ask the user to enter a name, and searches if 
       the name exists under the function check_membername_exits through all 
       the dictionaries and lists such as dic_info, dic_status, dic_wall, 
       name_list, notes_list. If the name is taken a nonvalid statement is 
       displayed, if not taken the current window taken to the settings window 
       by the function check_membername_exits.'''
    
    window.destroy()

    # Creating a window called main_window
    join_facebooklet_window = Tk()
    join_facebooklet_window.title('Join Facebooklet')

    frame = Frame(join_facebooklet_window, bg = 'white')
    frame.pack()
    
    # Creating a labels to display text in the main_window
    facebooklet_logo_label = Label(frame, text = 'facebooklet ', \
                                   bg = '#5F04B4', \
                                   font = ("Courier", 45, 'bold'), \
                                   fg = 'white', height = 2)
    facebooklet_logo_label.grid(row = 0, column = 0)
    
    space_label = Label(frame, bg = '#5F04B4', font = ("Courier", 45, 'bold'), \
                        fg = 'white', height = 2, width = 15)
    space_label.grid(row = 0, column = 1)
    
    text3_label = Label(frame, text = 'Sign Up', \
                        font = ("Courier", 15, 'bold'), fg = '#5F04B4', \
                        bg = 'white')
    text3_label.grid(row = 4, column = 0)
    
    text4_label = Label(frame, text = "It's free and anyone can join!", \
                        font = ("Courier", 15, 'bold'), fg = '#5F04B4', \
                        bg = 'white')
    text4_label.grid(row = 5, column = 0)
    
    text4_label = Label(frame, text = 'Name: ',font = ("Courier", 15, 'bold'), \
                        fg = '#5F04B4', bg = 'white')
    text4_label.grid(row = 6, column = 0)
    
    # Creating widgets like a Label, Entry, and Button for the user to enter 
    # a NAME to open an account in facebooklet and to check wether the entered 
    # NAME already exists in facebooklet or not 
    
    membername_entry = Entry(frame)
    membername_entry.grid(row = 6, column = 1)
    
    name = StringVar()
    show_message = Label(frame, textvariable = name, fg = '#5F04B4')
    show_message.grid(row = 7, column = 1)
    
    # Creating a join_button to call the function settings_window 
    join_command2 = lambda: check_membername_exits(membername_entry, name, \
                                                  join_facebooklet_window, \
                                                  dic_info, dic_status, \
                                                  dic_wall, name_list, \
                                                  notes_list)
    join_button = Button(frame, text = 'JOIN', width = 20, height = 2, \
                         bg = '#E3CEF6', fg= '#5F04B4', command = join_command2)
    join_button.grid(row = 7, column = 0)
    join_facebooklet_window.mainloop()
    
def check_membername_exits(membername, message, window, dic_info, dic_status, \
                           dic_wall, name_list, notes_list):
    '''Check if the member name that is being typed into the entry 
       membername_entry is taken by searching through the dictionary dic_info. 
       If the member name is not taken, a valid statement is set to the 
       StringVar membername. Otherwise, a nonvalid statement is given.'''
    
    keys = dic_info.keys()
    
    # If the NAME typed by the user isn't in the keys list let the user open a 
    # account in that NAME and call the function settings_window to create their 
    # profile
    # And if the NAME did not qualify for either of them then display the 
    # appropriate message for that type of error
    if keys.count(membername.get().lower()) == 0 and membername.get() != '':
        name_list.append(membername.get())
        settings_window(window, dic_info, dic_status, dic_wall, name_list, \
                        notes_list)
        
    elif keys.count(membername.get().lower()) == 1:
        message.set('Sorry the name ' + membername.get().lower() + \
                    ' already exists.')
        
    elif membername.get() == '':
        message.set('Enter a name to join Facebooklet!: ')
    
if __name__ == '__main__':
    
    dic_info = {}
    dic_status = {}
    dic_wall = {}
    name_list = []
    notes_list = []
    
    main_window = Tk()
    main_window.title('Welcome to Facebooklet')

    frame = Frame(main_window, bg = 'white')
    frame.pack()
    
    # Creating a labels to display text in the main_window
    facebooklet_logo_label = Label(frame, text = 'facebooklet ', \
                                   bg = '#5F04B4', \
                                   font = ("Courier", 45, 'bold'), \
                                   fg = 'white', height = 2)
    facebooklet_logo_label.grid(row = 0, column = 0)
    
    space_label = Label(frame, bg = '#5F04B4', \
                        font = ("Courier", 45, 'bold'), width = 20, height = 2)
    space_label.grid(row = 0, column = 1)
    
    text1_label = Label(frame, text = 'Facebooklet helps you connect and', \
                        font = ("Courier", 25, 'bold'), fg = '#5F04B4',\
                        bg = 'white')
    text1_label.grid(row = 2, column = 1)
    
    text2_label = Label(frame, text = 'share with the people in your life.', \
                        font = ("Courier", 25, 'bold'), fg = '#5F04B4', \
                        bg = 'white')
    text2_label.grid(row = 3, column = 1)
    
    # Creating a join_button to call the function join_facebooklet_window 
    sign_command = lambda: join_facebooklet_window(main_window, dic_info, \
                                                   dic_status, dic_wall, \
                                                   name_list, notes_list)
    sign_up_button = Button(frame, text = 'Sign Up', width = 20, height = 2, \
                            bg = '#E3CEF6', fg= '#5F04B4', \
                            command = sign_command)
    sign_up_button.grid(row = 4, column = 0)
    
    main_window.mainloop()