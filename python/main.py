try:
    import random
    import re
    import requests
    from bs4 import BeautifulSoup
    import os
    import tkinter
    import tkinter.messagebox as messagebox
    import tkinter.simpledialog as simpledialog
    import traceback
except ImportError:
    print("読み込みに失敗しました")

try:

    def login_password_type():
        try:
            tkinter.Tk().withdraw()
            password = simpledialog.askstring('パスワード入力', 'パスワードを入力してください')
            password = int(password)
            if password == 6251:
                print("ログインしました!")
            else:
                tkinter.Tk().withdraw()
                messagebox.showinfo("パスワードが違います", "ログインに失敗しました")
                login_password_type()
        except TypeError:
            pass

    login_password_type()

    def file_sonzai():
        if os.path.isfile("URL_List.txt") == True:
            os.remove("URL_List.txt")
        else:
            pass

    file_sonzai()

    file_name = 0
    yuip = 0
    N = 0
    os.system("cls")
    wawawa = ""

    with open("URL_List.txt", "x") as f:
        f.close()

    os.makedirs("image", exist_ok=True)

    URL = "https://nikkanerog.com/blog-entry-18183.html"
    requess = requests.get(url=URL)
    soup = BeautifulSoup(requess.content, "html.parser")
    elems = soup.find_all(src=re.compile("https://blog-imgs-145.fc2.com/"))

    def image_acquisition(file_name, yuip, N, wawawa, elems):

        for elem in elems:
            with open("URL_List.txt", "a") as Link:
                Link.write(elem.attrs["src"] + "\n")
                print(elem.attrs["src"])
                N = N + 1
                Link.close()
        print(N)

    image_acquisition(file_name, yuip, N, wawawa, elems)

    def install_image(elems, filename):
        for elem in elems:
            with open("URL_List.txt", "r", encoding="UTF-8") as f:
                URL_List = elem.attrs["src"]
                aaaa = requests.get(URL_List)
                url = aaaa.content
                wawa = str(wawawa + random.choice(
                    "abcdefghijklmnopqrstu123456789zyxwABCDEFGHIJKLMNOPQRSTUVWXYZ"))
                file_name = wawa + ".png"
                with open(filename + "/" + file_name, "wb") as aaa:
                    aaa.write(url)

    def make_image_keep():
        try:
            tkinter.Tk().withdraw()
            filename = simpledialog.askstring("filename", "ファイル名を入力してください")
            filename = "image/" + filename
            os.makedirs(filename)
            install_image(elems=elems, filename=filename)
        except FileExistsError:
            tkinter.Tk().withdraw()
            messagebox.showinfo(
                'error!', f'そのファイル{filename}名は存在していますほかの名前にしてください!')
            make_image_keep()

    make_image_keep()

    def end_move():
        tkinter.Tk().withdraw()
        messagebox.showinfo("complete", "処理が完了しました!")

        os.remove("URL_List.txt")

    end_move()

except KeyboardInterrupt:
    pass
