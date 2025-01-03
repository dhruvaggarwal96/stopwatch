import tkinter as tk

count = 0
stop = False

def start_fuction():
    # print("Started")
    global stop
    stop = False
    update_time()

def stop_fuction():
    global stop
    stop = True
    update_time()

def reset_fuction():
    global count 
    count = 0
    lable2.config(text="00:00:00")

        

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds%3600)//60
    sec = seconds%60
    return f"{hours}:{minutes:02}:{sec:02}"
    
def update_time():
    global count
    # print("update working!")
    if stop == False:
        count = count + 1
        formated_time = format_time(count)
        lable2.config(text=formated_time)
        lable2.after(1000,update_time)
    else:
        print("Stopped")






root = tk.Tk()

root.title("Stopwatch By Dhruv Aggarwal")

lable1 = tk.Label(root,text="Stopwatch",font=(50))
lable1.pack(pady=10)

lable2 = tk.Label(root,text="00:00:00",font=(30))
lable2.pack(pady=10)

start_button = tk.Button(root,text="Start StopWatch",command=start_fuction)
start_button.pack(pady=10)

stop_button = tk.Button(root,text="Stop StopWatch",command=stop_fuction)
stop_button.pack(pady=10)

reset_button = tk.Button(root,text="Reset StopWatch",command=reset_fuction)
reset_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=10)

root.geometry("500x500")

root.resizable(False,False)

root.configure(bg="#f0f0f0")  # Set a light grey background


root.mainloop()