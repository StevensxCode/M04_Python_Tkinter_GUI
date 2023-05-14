root = tk.Tk()
root.title('GPA Calculator')

# create frames
self.column_headers = Frame(root)
self.class1_frame = Frame(root)
self.class2_frame = Frame(root)
self.class3_frame = Frame(root)
self.class4_frame = Frame(root)
self.enterClasses_frame = Frame(root)
self.deposit_frame = Frame(root)

self.column_header = Label(self.column_headers, \
                           text='Credit Hours                        Grade', fg='black')
self.column_header.pack(side='left')

self.class1label = Label(self.class1_frame, \
                         text='Class 1:', fg='black')
self.class1label.pack(side='left')
self.creditHours1 = Entry(self.class1_frame)
self.creditHours1.pack(side='left')
self.grade1 = Entry(self.class1_frame)
self.grade1.pack(side='left')

self.class2label = Label(self.class2_frame, \
                         text='Class 2:', fg='black')
self.class2label.pack(side='left')
self.creditHours2 = Entry(self.class2_frame)
self.creditHours2.pack(side='left')
self.grade2 = Entry(self.class2_frame)
self.grade2.pack(side='left')

self.class3label = Label(self.class3_frame, \
                         text='Class 3:', fg='black')
self.class3label.pack(side='left')
self.creditHours3 = Entry(self.class3_frame)
self.creditHours3.pack(side='left')
self.grade3 = Entry(self.class3_frame)
self.grade3.pack(side='left')

self.class4label = Label(self.class4_frame, \
                         text='Class 4:', fg='black')
self.class4label.pack(side='left')
self.creditHours4 = Entry(self.class4_frame)
self.creditHours4.pack(side='left')
self.grade4 = Entry(self.class4_frame)
self.grade4.pack(side='left')

self.enterClasses = Button(self.enterClasses_frame, text='Submit Classes', bg='blue', \
                           fg='white')
self.enterClasses.pack(side='left')

# pack frames
self.column_headers.pack()
self.class1_frame.pack()
self.class2_frame.pack()
self.class3_frame.pack()
self.class4_frame.pack()
self.enterClasses_frame.pack()

root.mainloop()