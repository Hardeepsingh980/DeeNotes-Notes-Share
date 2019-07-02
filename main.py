## ----------------------- Import Modules ----------------------------------------
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
from tkinter import colorchooser
import os
import socket
import _thread
##--------------------------------------------------------------------------




##---------------------- Variables ---------------------------------------
menu_counter = 2
cur_note = -1
bg_color = 'light green'
##--------------------------------------------------------------------------




##-------------------------------- Class Main_ --------------------------------
class Main_():

    ##-------------------------------- About Function -------------------------------------------
    def about(self):
        mb.showinfo('About Us','This is the exclusive distribution of DeeNotes created by Hardeep Singh. This Application was developed with Python Language. This for Created for the students who face problems in taking notes. So, this application was created to help the students share the notes with other fellow students.')
    ##------------------------------------------------------------------------------------------------


    

    ##-------------------------------- Change Background --------------------------------------
    def tcolor(self):
        global bg_color
        clr = colorchooser.askcolor(title='Select Color')
        co = clr[1]        
        bg_color = co
        bg_label1['bg'] = bg_color
        menu_bg['bg'] = bg_color
        logo_bg['bg'] = bg_color
        menu_frame['bg'] = bg_color
        log_img['bg'] = bg_color
        log_in_as['bg'] = bg_color
        name['bg'] = bg_color
        log_bg['bg'] = bg_color
        upload_l['bg'] = bg_color
        down_l['bg'] = bg_color
        setting_l['bg'] = bg_color
        about_l['bg'] = bg_color
        home_l['bg'] = bg_color
        set_bg['bg'] = bg_color
    ##-------------------------------------------------------------------------------------------------


    

    ##------------------------------------ Setting Window --------------------------------------------
    def setting_func(self):
        global set_bg
        set_ = Toplevel()
        set_.geometry('300x300')
        set_.resizable(0,0)
        set_.title('Settings')
        set_bg = Label(set_, text='Settings', bg=bg_color, font=('',20),width=300,relief='groove')
        set_bg.pack()
        Label(set_, text='Change Background', font=('',13)).place(x=10,y=50)
        Button(set_, text='Select',font=('',13),command=self.tcolor).place(x=200,y=45)
    ##------------------------------------------------------------------------------------------------------


    

    ##------------------------------ Delete Notes Function ---------------------------------------------
    def delete_func(self):
         global cur_note
         dir_l = os.listdir('Notes')
         use = dir_l[cur_note]
         os.remove(f'Notes/{use}')
         dir_l = os.listdir('Notes')
         c = 0
         for i in dir_l:
             os.rename(f'Notes/{i}',f'Notes/{c}.txt')
             c+=1

         self.next_func()
         mb.showinfo('Success','Note Deleted Successfully.')
    ##--------------------------------------------------------------------------------------------------------
        




    

    ##------------------------ Upload Notes Function ---------------------------------
    def upload_n_func(self):
        user = name_entry.get()
        title = title_entry.get()
        data = text_u.get(1.0,END)
        if user != '' and title != '' and data != '':
            to_write = f'post!@!{user}@!{title}@!{data}'
            s.send(to_write.encode('utf-8'))
            mb.showinfo('Success','Notes Successfully Uploaded.')
            self.home_func()
        else:
            mb.showerror('Fill','Fill All The Columns.')
    ##---------------------------------------------------------------------------------------


            

    

    ##------------------------------------ Home Function ---------------------------------------
    def home_func(self):
        global menu_counter
        user_label.place(x=60,y=51)
        title_label.place(x=60,y=75)
        text_.place(x=10,y=100)
        frame.place(x=10,y=50)
        log_a_label.place(x=13,y=52)
        dots_b.place(x=320,y=60)
        next_b.place(x=200,y=395)
        pre_b.place(x=5,y=395)
        name_label.place(x=1000)
        name_entry.place(x=1000)
        title_u_label.place(x=1000)
        title_entry.place(x=1000)
        text_u_label.place(x=1000)
        text_u.place(x=1000)
        attach_u.place(x=1000)
        upload_u_b.place(x=1000)
        cancel_u_b.place(x=1000)
        upload_l.place(x=1000,y=1000)
        down_l.place(x=1000,y=1000)
        setting_l.place(x=1000,y=1000)
        about_l.place(x=1000,y=1000)
        menu_frame.place(x=1000,y=1000)
        log_img.place(x=1000,y=1000)
        home_l.place(x=1000)
        name.place(x=1000,y=1000)
        log_bg.place(x=1000,y=1000)
        log_in_as.place(x=1000,y=1000)
        comp_label.place(x=1000)
        menu_counter+=1
    ##------------------------------------------------------------------------------------------------

    

    ##------------------------------- Attach Notes Functions ---------------------------------------
    def attach_func(self):
        returned = filedialog.askopenfile(initialdir='E:\\', title='Select file to open')
        if returned != None:
            for line in returned:
                text_u.insert(END, line)
            returned.close()
    #------------------------------------------------------------------------------------------------------
            
    
    ##---------------- Upload Note Function ---------------------------------
    def upload_note_func(self):
        global menu_counter
        user_label.place(x=1000)
        title_label.place(x=1000)
        text_.place(x=1000)
        frame.place(x=1000)
        log_a_label.place(x=1000)
        dots_b.place(x=1000)
        menu_frame.place(x=1000,y=1000)
        log_img.place(x=1000,y=1000)
        log_in_as.place(x=1000,y=1000)
        name.place(x=1000,y=1000)
        log_bg.place(x=1000,y=1000)
        upload_l.place(x=1000,y=1000)
        down_l.place(x=1000,y=1000)
        setting_l.place(x=1000,y=1000)
        about_l.place(x=1000,y=1000)
        next_b.place(x=1000)
        pre_b.place(x=1000)
        menu_counter+=1
        name_label.place(x=20,y=50)
        name_entry.place(x=90,y=50)
        title_u_label.place(x=20,y=90)
        title_entry.place(x=90,y=90)
        text_u_label.place(x=20,y=150)
        text_u.place(x=20,y=180)
        attach_u.place(x=220,y=150)
        upload_u_b.place(x=170,y=420)
        cancel_u_b.place(x=240,y=420)
        home_l.place(x=1000)
        comp_label.place(x=1000)
    ##---------------------------------------------------------------------------------------




        

    ##----------------------- Download Notes Function --------------------------------    
    def download_notes_func(self):
         f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
         if f is None:
            return
         global cur_note
         dir_l = os.listdir('Notes')
         use = dir_l[cur_note]
         file = open(f'Notes/{use}','r')
         data_l = file.read(10000).split('@!')
         user = data_l[0]
         title = data_l[1]
         note_data = data_l[2]
         to_write =f'{user} \n\nTitle :  {title}\n\n{note_data}'                
         f.write(to_write)
         f.close
    ##---------------------------------------------------------------------------------------




        
    ##----------------------- Next Function ---------------------------------------------------
    def next_func(self):
        try:
            global cur_note
            dir_l = os.listdir('Notes')
            use = dir_l[cur_note+1]
            f = open(f'Notes/{use}','r')
            data_l = f.read(10000).split('@!')
            user = data_l[0]
            title = data_l[1]
            note_data = data_l[2]
            user_label['text'] = user
            title_label['text'] = 'Title : '+title
            text_.delete(1.0,END)
            text_.insert(INSERT, note_data)
            cur_note += 1
        except:
            global all_caught
            user_label.place(x=1000)
            title_label.place(x=1000)
            text_.place(x=1000)
            frame.place(x=1000)
            comp_label.place(x=10,y=100)
            log_a_label.place(x=1000)
            dots_b.place(x=1000)
    ##-----------------------------------------------------------------------------------------------

            



    ##-------------------------------------- Previous Function -----------------------------------------
    def prev_func(self):
        try:
            global cur_note
            if cur_note <=  0:
                return
                
            else:
                dir_l = os.listdir('Notes')
                use = dir_l[cur_note-1]
                f = open(f'Notes/{use}','r')
                data_l = f.read(10000).split('@!')
                user = data_l[0]
                title = data_l[1]
                note_data = data_l[2]
                user_label['text'] = user
                title_label['text'] = 'Title : '+title
                text_.delete(1.0,END)
                text_.insert(INSERT, note_data)
                cur_note -= 1
        except:
            pass
    ##--------------------------------------------------------------------------------------------------------



        
    #----------------------------------------------- Menu Function --------------------------------------------------------------
    def menu_func(self):
        global menu_counter
        if menu_counter%2 != 0:
            menu_frame.place(x=1000,y=1000)
            log_img.place(x=1000,y=1000)
            log_in_as.place(x=1000,y=1000)
            name.place(x=1000,y=1000)
            log_bg.place(x=1000,y=1000)
            upload_l.place(x=1000,y=1000)
            down_l.place(x=1000,y=1000)
            setting_l.place(x=1000,y=1000)
            about_l.place(x=1000,y=1000)
            home_l.place(x=1000)            
        else:
            menu_frame.place(x=0,y=38)
            log_bg.place(x=0,y=38)
            log_img.place(x=10,y=50)
            log_in_as.place(x=10,y=120)
            name.place(x=5,y=145)
            home_l.place(x=5,y=180)
            upload_l.place(x=5,y=220)
            down_l.place(x=5,y=260)
            setting_l.place(x=5,y=310)
            about_l.place(x=5,y=350)
        menu_counter+=1
    ##-----------------------------------------------------------------------------------------------------------------------------------




    ## ----------------------------- Contructor Function --------------------------------------------------------------------------------    
    def __init__(self):
        global bg_label1,menu_bg,logo_bg
        win = Tk()
        win.geometry('350x450')
        win.resizable(0,0)
        win.title('DeeNotes')
        win.configure(bg='white')
        bg_label1 = Label(win, text='',width=35,bg=bg_color,font=('',20),relief='groove')
        bg_label1.pack()
        menu_img = PhotoImage(file='resources/menu.png')        
        menu_bg = Button(win, image=menu_img,bg=bg_color,bd=0,command=self.menu_func)
        menu_bg.place(x=10,y=9)
        logo_img = PhotoImage(file='resources/logo.png')
        logo_bg = Label(win, image=logo_img,bg=bg_color)
        logo_bg.place(x=240,y=9)


        ## Canvas
        global user_label, title_label, text_,frame,comp_label,log_a_label,dots_b, next_b, pre_b
        frame = Label(win, text='',bg='white',width=14,relief='groove',font=('',30))
        frame.place(x=10,y=50)
        log_a_img = PhotoImage(file='resources/log_a.png')
        log_a_label = Label(win, image=log_a_img,bg='white')
        log_a_label.place(x=13,y=52)        
        user_label = Label(win,text='',bg='white',font=('',13))
        user_label.place(x=60,y=51)
        title_label = Label(win, text='',bg='white',font=('',11,'italic'))
        title_label.place(x=60,y=75)
        text_ = Text(win,font=('',13),wrap='word',width=36,bd=2,height=15)
        text_.place(x=10,y=100)
        dots_img = PhotoImage(file='resources/dots.png')
        dots_b = Button(win, image=dots_img,bd=0,bg='white')
        dots_b.place(x=320,y=60)
        pop = Menu(win, tearoff=0)    
        pop.add_command(label='Download Notes',command=self.download_notes_func)
        pop.add_separator()
        pop.add_command(label='Delete',command=self.delete_func)
        pop.add_separator()
        pop.add_command(label='Report Notes')
        self.next_func()
        def do(event):
            try:
                pop.tk_popup(event.x_root,event.y_root,0)
            finally:
                pop.grab_release
        dots_b.bind('<Button-1>',do)
        next_img = PhotoImage(file='resources/next.png')
        next_b = Button(win, image=next_img,text='Next Note ',bg='white',bd=0,compound='right',font=('',13,'bold'),command=self.next_func)
        next_b.place(x=200,y=395)
        pre_img = PhotoImage(file='resources/prev.png')
        pre_b = Button(win, image=pre_img,text=' Previous Note',bg='white',bd=0,compound='left',font=('',13,'bold'),command=self.prev_func)
        pre_b.place(x=5,y=395)
        comp_img = PhotoImage(file='resources/comp.png')
        comp_label = Label(win, image=comp_img)


        ## Upload Canvas
        global name_label, name_entry,title_u_label, title_entry,text_u_label,text_u,attach_u,upload_u_b,cancel_u_b
        name_label = Label(win, text='Name : ',bg='white',font=('',13,'bold'))
        name_entry = Entry(win,font=('',13),bd=2 )
        title_u_label = Label(win, text='Title : ',bg='white',font=('',13,'bold'))
        title_entry = Entry(win,font=('',13),bd=2 )
        text_u_label = Label(win, text='Write Notes : ',font=('',13,'bold'),bg='white')
        text_u = Text(win, font=('',13,'bold'),width=34,bd=2,height=12,wrap = 'word')
        attach_img = PhotoImage(file='resources/attach.png')
        attach_u = Button(win, image=attach_img,text='Attach Notes',bd=0,compound='left',font=('',10),bg='white',command=self.attach_func)
        upload_u_b = Button(win, text='Upload',bg='Green',fg='white',bd=0,font=('',11),command=self.upload_n_func)
        cancel_u_b = Button(win, text='Cancel',bg='Red',fg='white',bd=0,font=('',11),command=self.home_func)


        ## Menu Bar
        global menu_frame,log_img, log_in_as,name,log_bg,upload_l,down_l,setting_l,about_l,home_l
        menu_frame = Label(win,bg=bg_color,width=20,height=27,relief='groove')
        log_bg = Label(win,bg=bg_color,width=20,height=9,relief='groove')
        login_img =PhotoImage(file='resources/login.png')
        log_img = Label(win,image=login_img,bg=bg_color)
        log_in_as = Label(win, text='Logged In As : ',bg=bg_color,font=('',13))
        name = Label(win, text='Hardeep Singh',bg=bg_color,font=('',13,'bold'))
        home_img = PhotoImage(file='resources/home.png')
        home_l = Button(win, image=home_img,text='Home',font=('',13),bg=bg_color,bd=0,compound='left',command=self.home_func)
        upload_img = PhotoImage(file='resources/upload.png')
        upload_l = Button(win,image=upload_img,text='Upload Notes',bg=bg_color,bd=0,compound='left',font=('',13),command=self.upload_note_func)
        down_img = PhotoImage(file='resources/download.png')
        down_l = Button(win, image=down_img,text='Downloaded \nNotes',font=('',13),bg=bg_color,bd=0,compound='left')
        setting_img = PhotoImage(file='resources/setting.png')
        setting_l = Button(win, image=setting_img,text='Settings',font=('',13),bg=bg_color,bd=0,compound='left',command=self.setting_func)
        about_img = PhotoImage(file='resources/about.png')
        about_l = Button(win, image=about_img,text='About',font=('',13),bg=bg_color,bd=0,compound='left',command=self.about)


        ## Mainloop
        win.mainloop()
    ##-------------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------------



def recv_msg():
    while True:
        msg = s.recv(10000000).decode('utf-8')
        len_l = len(os.listdir('Notes'))
        f = open(f'Notes/{len_l}.txt','w')
        f.write(msg)
        f.close()



def create_socket():
    global s
    s = socket.socket()
    s.connect(('localhost',5000))
    _thread.start_new_thread(recv_msg,())

## Object For Main_ Class
_thread.start_new_thread(create_socket,())
DeeNotes = Main_()

