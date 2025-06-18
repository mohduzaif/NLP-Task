from tkinter import *
from mydb import Database
from myapi import API
from tkinter import messagebox

class NLPApp:

    def __init__(self):

        self.root = Tk()
        self.root.title('NLP Task')
        self.root.geometry('550x600')
        self.root.iconbitmap('resources/favicon.ico')
        self.root.configure(bg='#34495E')

        self.login_gui()

        # make an object of other classes to access his attributes.
        self.db_object = Database()
        self.api_object = API()
        
        self.root.mainloop()


    # this function conatin the functionality of the login.
    def login_gui(self):

        # clear the existing gui
        self.clear_gui()

        # to tell the user to print this heading on the root object GUI
        heading = Label(self.root, text = 'NLP Task App', bg = '#34495E', fg = 'white')

        # to tell tkinter explicitly that add that text to the GUI.
        heading.pack(pady = (35, 35))

        # to adjust the font size of this above text. 
        heading.configure(font = ('verdana', 24, 'bold'))

        # for Email.
        label1 = Label(self.root, text = 'Enter Email', width=20)
        label1.pack(pady=(10, 10))

        self.email = Entry(self.root, width=40)
        self.email.pack(pady=(1, 10), ipady=2)

        # For password
        label2 = Label(self.root, text = 'Enter Password', width=20)
        label2.pack(pady=(10, 10))

        self.password = Entry(self.root, width=40, show='*')
        self.password.pack(pady=(1, 10), ipady=2)

        # for login button
        login_btn = Button(self.root, text='Login', width=20, height=1, command=self.perform_login)
        login_btn.pack(pady=(15, 10))

        # for redirect to register page. 
        label3 = Label(self.root, text='Not a member? Register now')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Register Now', command=self.register_gui)
        redirect_btn.pack(pady=(10, 10))


    # this function conatin the functionality of the register a user.
    def register_gui(self): 
        
        # clear the existing gui
        self.clear_gui()

        # to tell the user to print this heading on the root object GUI
        heading = Label(self.root, text = 'NLP Task App', bg = '#34495E', fg = 'white')

        # to tell tkinter explicitly that add that text to the GUI.
        heading.pack(pady = (35, 35))

        # to adjust the font size of this above text. 
        heading.configure(font = ('verdana', 24, 'bold'))

        # for Name.
        label1 = Label(self.root, text = 'Enter Name', width=20)
        label1.pack(pady=(10, 10))

        self.name = Entry(self.root, width=40)
        self.name.pack(pady=(1, 10), ipady=2)

        # for Email.
        label1 = Label(self.root, text = 'Enter Email', width=20)
        label1.pack(pady=(10, 10))

        self.email = Entry(self.root, width=40)
        self.email.pack(pady=(1, 10), ipady=2)

        # For password
        label2 = Label(self.root, text = 'Enter Password', width=20)
        label2.pack(pady=(10, 10))

        self.password = Entry(self.root, width=40, show='*')
        self.password.pack(pady=(1, 10), ipady=2)

        # for login button
        register_btn = Button(self.root, text='Register', width=20, height=1, command=self.perform_registration)
        register_btn.pack(pady=(15, 10))

        # for redirect to register page. 
        label3 = Label(self.root, text='Already a member? Login now')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Login Now', command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))


    # this function handle the deshboard.
    def deshboard_gui(self):

        self.clear_gui()

        # to tell the user to print this heading on the root object GUI
        heading = Label(self.root, text = 'NLP Task App', bg = '#34495E', fg = 'white')

        # to tell tkinter explicitly that add that text to the GUI.
        heading.pack(pady = (35, 35))

        # to adjust the font size of this above text. 
        heading.configure(font = ('verdana', 24, 'bold'))

        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=2, command=self.sentiment_gui)
        sentiment_btn.pack(pady=10)

        ner_btn = Button(self.root, text='Named Entity Recognition', width=30, height=2, command=self.entity_extraction_gui)
        ner_btn.pack(pady=(15, 10))

        sentiment_similarity_btn = Button(self.root, text='Sementic Similarity between two Text', width=30, height=2, command=self.semantic_similarity_gui)
        sentiment_similarity_btn.pack(pady=(15, 10))


        logout_btn = Button(self.root, text='Logout', command=self.login_gui)
        logout_btn.pack(pady=(10, 10))


    # handle the GUI of sentiment Analysis.
    def sentiment_gui(self):
        
        # clear the existing gui.
        self.clear_gui()

        #heading of the GUI.
        heading = Label(self.root, text = 'NLP Task App', bg = '#34495E', fg = 'white')
        heading.pack(pady = (35, 10))
        heading.configure(font = ('verdana', 24, 'bold'))

        # Topic related GUI
        heading = Label(self.root, text = 'Sentiment Analysis', bg = '#34495E', fg = 'white')
        heading.pack(pady = (10, 35))
        heading.configure(font = ('verdana', 20))

        #Label for the text.
        label1 = Label(self.root, text = 'Enter the Text', width=30)
        label1.pack(pady=(10, 10), ipady=5)

        self.text = Entry(self.root, width=40)
        self.text.pack(pady=(1, 10), ipady=3)

        # for Analyze button
        analyze_btn = Button(self.root, text='Analyze', width=20, height=1)
        analyze_btn.pack(pady=(15, 10))

        # result space for analyze the text
        self.sentiment_result = Label(self.root, text = '', width=30, bg = '#34495E', fg='white')
        self.sentiment_result.pack(pady=(10, 10), ipady=5)
        self.sentiment_result.configure(font = ('verdana', 20))


        # for Analyze button
        go_back_btn = Button(self.root, text='Back To Deshboard', width=20, height=1, command=self.deshboard_gui)
        go_back_btn.pack(pady=(15, 10))


    # handle the GUI of NER.
    def entity_extraction_gui(self):

        # clear the existing gui.
        self.clear_gui()

        #heading of the GUI.
        heading = Label(self.root, text = 'NLP Task App', bg = '#34495E', fg = 'white')
        heading.pack(pady = (35, 10))
        heading.configure(font = ('verdana', 24, 'bold'))

        # Topic related GUI
        heading = Label(self.root, text = 'Entity Extraction(NER)', bg = '#34495E', fg = 'white')
        heading.pack(pady = (10, 35))
        heading.configure(font = ('verdana', 20))

        #Label for the text.
        label1 = Label(self.root, text = 'Enter the Text', width=30)
        label1.pack(pady=(10, 10), ipady=5)

        self.ner_text = Entry(self.root, width=40)
        self.ner_text.pack(pady=(1, 10), ipady=3)

        # for Analyze button
        analyze_btn = Button(self.root, text='Analyze', width=20, height=1)
        analyze_btn.pack(pady=(15, 10))

        # result space for analyze the text
        self.ner_result = Label(self.root, text = '', width=30, bg = '#34495E', fg='white')
        self.ner_result.pack(pady=(10, 10), ipady=5)
        self.ner_result.configure(font = ('verdana', 20))


        # for Analyze button
        go_back_btn = Button(self.root, text='Back To Deshboard', width=20, height=1, command=self.deshboard_gui)
        go_back_btn.pack(pady=(15, 10))


    # handle the GUI of sentiment Similarity.
    def semantic_similarity_gui(self):
                # clear the existing gui.
        self.clear_gui()

        #heading of the GUI.
        heading = Label(self.root, text = 'NLP Task App', bg = '#34495E', fg = 'white')
        heading.pack(pady = (35, 10))
        heading.configure(font = ('verdana', 24, 'bold'))

        # Topic related GUI
        heading = Label(self.root, text = 'Sementic Similarity between two Text', bg = '#34495E', fg = 'white')
        heading.pack(pady = (10, 35))
        heading.configure(font = ('verdana', 20))

        #Label for the text1.
        label1 = Label(self.root, text = 'Enter the Text1', width=30)
        label1.pack(pady=(10, 10), ipady=5)

        self.text1 = Entry(self.root, width=40)
        self.text1.pack(pady=(1, 10), ipady=3)

        #Label for the text2.
        label1 = Label(self.root, text = 'Enter the Text2', width=30)
        label1.pack(pady=(10, 10), ipady=5)

        self.text2 = Entry(self.root, width=40)
        self.text2.pack(pady=(1, 10), ipady=3)

        # for Analyze button
        analyze_btn = Button(self.root, text='Analyze', width=20, height=1, command=self.semantic_similarity_api)
        analyze_btn.pack(pady=(15, 10))

        # result space for analyze the text
        self.semantic_similarity_result = Label(self.root, text = '', width=30, bg = '#34495E', fg='white')
        self.semantic_similarity_result.pack(pady=(10, 10), ipady=5)
        self.semantic_similarity_result.configure(font = ('verdana', 20))


        # for Analyze button
        go_back_btn = Button(self.root, text='Back To Deshboard', width=20, height=1, command=self.deshboard_gui)
        go_back_btn.pack(pady=(15, 10))


    # collect response from api.
    def semantic_similarity_api(self):
        text1 = self.text1.get()
        text2 = self.text2.get()

        response = self.api_object.call_api_sementic_similarity(text1, text2)

        if type(response) == dict:     
            self.sentiment_similarity_result = response
        else:
            messagebox.showerror('Error', 'Server is not working right now, Try later!')
        


    # collect the user data from registration form.
    def perform_registration(self):
        name = self.name.get()
        email = self.email.get()
        password = self.password.get()
        # print(name, email, password)
        # call the add_data function from Database class.
        response = self.db_object.add_data(name, email, password)
        if response == True:
            messagebox.showinfo('Success', 'Registration Successful, You can now Login.')
        else:
            messagebox.showerror('Error', 'Email Already Exist.')


    # perform the login by matching the credentials enter by user.
    def perform_login(self):
        
        email = self.email.get()
        password = self.password.get()
        # print(email, password)

        response = self.db_object.match_credentials(email, password)

        if response == True:
            messagebox.showinfo('Success', 'Login Successful')
            self.deshboard_gui()
        else:
            messagebox.showerror('Error', 'Invalid Email/Password')



    # this function is used to clear the GUI.
    def clear_gui(self):
        # this function pack_slaves catch all the labels present on the root GUI.
        for i in self.root.pack_slaves():
            # destroy function destroy/remove all the labels from the GUI
            i.destroy()


nlp = NLPApp()