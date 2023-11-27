from pytube import YouTube
import argparse
import os, time

# import tkinter as tk
# def create_and_get_user_input():
#     user_input = ""

#     def get_user_input():
#         nonlocal user_input
#         user_input = entry.get()
#         if user_input:
#             print(f"You entered: {user_input}")
#         root.destroy()

#     root = tk.Tk()
#     root.title("User Input Example")

#     label = tk.Label(root, text="Enter some text:")
#     label.pack(pady=10)

#     entry = tk.Entry(root)
#     entry.pack(pady=10)

#     button = tk.Button(root, text="Get User Input", command=get_user_input)
#     button.pack(pady=20)

#     root.mainloop()

#     return user_input

def take_user_input():
    parser = argparse.ArgumentParser(description='yt-downloader')
    parser.add_argument('user_input', type=str, help='Enter the URL of video')
    args = parser.parse_args()
    return args.user_input

def download_yt_video(yt_link):
    try:
        curr_dir = os.getcwd()
        yt = YouTube(yt_link)
        # print('title: ', yt.title)
        yd = yt.streams.get_highest_resolution()
        yd.download(os.path.join(curr_dir,'yt_videos'))
        # print('download complete')
    except Exception as e:
        print("an error occured: ", e)


if __name__ == '__main__':
    # yt_link = create_and_get_user_input()
    start = time.time()
    yt_link = take_user_input()
    download_yt_video(yt_link)
    # python yt_download.py "https://www.youtube.com/watch?v=e-TuBq5QTO0&ab_channel=TimesMusic"  run file in terminal
    end = time.time()
    print("time taken: ",round(end-start,2))




