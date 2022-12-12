try:
    import random
    import re
    import requests
    from bs4 import BeautifulSoup
    import os
    import time
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
        except ValueError:
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
    # if text kuuhaku true let's in + ! rei https://www.xvideos.com/?k=rem+cosplay

    tkinter.Tk().withdraw()
    URL = simpledialog.askstring("", "input!")
    tkinter.Tk().withdraw()
    URL2 = simpledialog.askstring("", "input!")

    #URL = "https://www.elog-ch.com/porn-2bcosplay-best/"
    requess = requests.get(url=URL)
    soup = BeautifulSoup(requess.content, "html.parser")
    elems = soup.find_all("img", src=re.compile(URL2))
    try:
        print(soup.a.get('src'))
    except AttributeError:
        pass

    if requess.status_code == requests.codes.ok:
        print(requess.status_code)

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
        import time
        for elem in elems:
            with open("URL_List.txt", "r", encoding="UTF-8") as f:
                URL_List = elem.attrs["src"]
                aaaa = requests.get(URL_List)
                url = aaaa.content
                wawa234 = str(wawawa + random.choice(
                    "abcdefghijklmnopqrstu123456789zyxwABCDEFGHIJKLMNOPQRSTUVWXYZ"))
                wawa = str(wawa234 + random.choice(
                    "abcdefghijklmnopqrstu123456789zyxwABCDEFGHIJKLMNOPQRSTUVWXYZ"))
                file_name = wawa + wawa234 + ".png"
                with open(filename + "/" + file_name, "wb") as aaa:
                    time.sleep(0.1)
                    aaa.write(url)

    def make_image_keep(file_name, yuip, N, wawawa, elems):
        try:
            tkinter.Tk().withdraw()
            filename = simpledialog.askstring("filename", "ファイル名を入力してください")
            filename = "image2/" + filename
            os.makedirs(filename)
            install_image(elems=elems, filename=filename)
        except TypeError:
            pass
        except FileExistsError:
            tkinter.Tk().withdraw()
            messagebox.showinfo(
                'error!', f'そのファイル{filename}名は存在していますほかの名前にしてください!')
            make_image_keep()

    make_image_keep(file_name, yuip, N, wawawa, elems)

    def end_move():
        tkinter.Tk().withdraw()
        messagebox.showinfo("complete", "処理が完了しました!")

        os.remove("URL_List.txt")

    end_move()

except KeyboardInterrupt:
    pass


#https://ei.phncdn.com/videos/
