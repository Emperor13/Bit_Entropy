# ───────────────────────────────import modules─────────────────────────────────────────────────────────── #
from tkinter import *
from tkinter import messagebox
from requests.exceptions import ConnectionError
from PIL import Image, ImageTk
from embit.descriptor import Descriptor
from embit.networks import NETWORKS
from embit import bip39, bip32
from binascii import hexlify
import tkinter as tk
import subprocess
import requests
import json
import os
import keyGen
import recovery
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
root = Tk()
root.title("Bit Entropy")  # CFD9ED
root.geometry('995x566')  # กำหนดขนาดของวินโดว Width x Height
root.minsize(995, 566)  # กำหนดขนาดเล็กสุดของวินโดว width, height
root.maxsize(995, 566)  # กำหนดขนาดใหญ่สุดของวินโดว width, height
# icon = PhotoImage(file=r"resources\icon.png")
# root.wm_iconphoto(False, icon)
root.iconbitmap(bitmap=r'favicon.ico')

# ────────────────────────────────────main colors────────────────────────────────────────────────────── #

minibg = '#FAF7F0'
bgcolor = "#98A8F8"
fontcolor = '#272323'
mainbg = '#A4BDF7'
seedbg = '#FAF7F0'

root.configure(background=mainbg)  # กำหนดสีของพื้นหลัง
# ────────────────────────────────────import image for status────────────────────────────────────────────────────── #
onImage = PhotoImage(file=r'resources/status_on.png')
offImage = PhotoImage(file=r'resources/status_off.png')
onLabel = Button(root, image=onImage, border=0, bg=mainbg,
                 activebackground=mainbg, command=lambda: recheck())
offLabel = Button(root, image=offImage, border=0, bg=mainbg,
                  activebackground=mainbg, command=lambda: recheck())
# def Broadcast_Transaction():
# ────────────────────────────────────import image for mnemonic────────────────────────────────────────────────────── #
mnemonic12_image = PhotoImage(file=r'resources/background/mnemonic/12word.png')
mnemonic12 = Label(root, image=mnemonic12_image, border=0, bg=mainbg)
mnemonic12.lower()

mnemonic15_image = PhotoImage(file=r'resources/background/mnemonic/15word.png')
mnemonic15 = Label(root, image=mnemonic15_image, border=0, bg=mainbg)
mnemonic15.lower()

mnemonic18_image = PhotoImage(file=r'resources/background/mnemonic/18word.png')
mnemonic18 = Label(root, image=mnemonic18_image, border=0, bg=mainbg)
mnemonic18.lower()

mnemonic21_image = PhotoImage(file=r'resources/background/mnemonic/21word.png')
mnemonic21 = Label(root, image=mnemonic21_image, border=0, bg=mainbg)
mnemonic21.lower()

mnemonic24_image = PhotoImage(file=r'resources/background/mnemonic/24word.png')
mnemonic24 = Label(root, image=mnemonic24_image, border=0, bg=mainbg)
mnemonic24.lower()
# ────────────────────────────────────import image for buttons────────────────────────────────────────────────────── #
word_12Image1 = r'resources/buttons/multiSig_menu/12word1.png'
word_12Image2 = r'resources/buttons/multiSig_menu/12word2.png'
word_15Image1 = r'resources/buttons/multiSig_menu/15word1.png'
word_15Image2 = r'resources/buttons/multiSig_menu/15word2.png'
word_18Image1 = r'resources/buttons/multiSig_menu/18word1.png'
word_18Image2 = r'resources/buttons/multiSig_menu/18word2.png'
word_21Image1 = r'resources/buttons/multiSig_menu/21word1.png'
word_21Image2 = r'resources/buttons/multiSig_menu/21word2.png'
word_24Image1 = r'resources/buttons/multiSig_menu/24word1.png'
word_24Image2 = r'resources/buttons/multiSig_menu/24word2.png'
walletImage1 = r'resources\buttons\wallet_menu\wallet1.png'
walletImage2 = r'resources\buttons\wallet_menu\wallet2.png'
multiSigImage1 = r'resources/buttons/multisig1.png'
multiSigImage2 = r'resources/buttons/multisig2.png'
timelockImage1 = r'resources/buttons/timelock1.png'
timelockImage2 = r'resources/buttons/timelock2.png'
broadcastImage1 = r'resources/buttons/broadcast1.png'
broadcastImage2 = r'resources/buttons/broadcast2.png'
newwalletImage1 = r'resources\buttons\wallet_menu\new_wallet.png'
newwalletImage2 = r'resources\buttons\wallet_menu\new_wallet2.png'
recoveryImage1 = r'resources\buttons\wallet_menu\recovery.png'
recoveryImage2 = r'resources\buttons\wallet_menu\recovery2.png'
masterImage1 = r'resources\buttons\wallet_menu\master.png'
masterImage2 = r'resources\buttons\wallet_menu\master2.png'
pointerImage = PhotoImage(file=r'resources/pointer.png')
writeDownImage = PhotoImage(file=r'resources/confirm.png')
conSeedImage = PhotoImage(
    file=r'resources/background/mnemonic/confirmseed.png')
nextImage = PhotoImage(file=r'resources/buttons/next.png')
settingImage = PhotoImage(file=r'resources\settings.png')
setting = Button(root, image=settingImage, border=0,
                 bg=mainbg, activebackground=mainbg)
setting.place(x=916, y=17)

homeImage1 = r'resources\buttons\home1.png'
homeImage2 = r'resources\buttons\home2.png'


# ────────────────────────────────────import image for backgrounds────────────────────────────────────────────────────── #
bgImage = PhotoImage(file=r'resources/background/first_page.png')
menuImage = PhotoImage(file=r'resources/background/menu1.png')
menuImage2 = PhotoImage(file=r'resources/background/menu2.png')
# ───────────────────────────────|Close Functions|───────────────────────────────────────── #


def close_menu():
    menu2.place_forget()
    button12.place_forget()
    button15.place_forget()
    button18.place_forget()
    button21.place_forget()
    button24.place_forget()


def close_mnemonic():
    mnemonic12.place_forget()
    mnemonic15.place_forget()
    mnemonic18.place_forget()
    mnemonic21.place_forget()
    mnemonic24.place_forget()


def close_wallet_buttons():
    menu.place_forget()
    newwallet_button.place_forget()
    recovery_button.place_forget()
    master_button.place_forget()

# ────────────────────────────────────────────────────────────────────────────────────────── #
# ───────────────────────────────|Place Functions|───────────────────────────────────────── #


def place_buttons():
    button12.place(x=387, y=116)  # -- กำหนดตำแหน่งของปุ่ม 12 word
    button15.place(x=387, y=187)  # -- กำหนดตำแหน่งของปุ่ม 15 word
    button18.place(x=387, y=258)  # -- กำหนดตำแหน่งของปุ่ม 18 word
    button21.place(x=387, y=329)  # -- กำหนดตำแหน่งของปุ่ม 21 word
    button24.place(x=387, y=400)  # -- กำหนดตำแหน่งของปุ่ม 24 word


def place_generated_key():
    generated.place(x=410,
                    y=214,
                    width=366,
                    height=141
                    )


def key_align():
    generated.config(state='disabled')
    generated.tag_configure("center", justify='center')

    # generated.tag_add("center", 1.0, "end")
# ──────────────────────────────────────Generating Key──────────────────────────────────────────────────── #
generated = Text(root, border=0, bg=minibg, font=(
    'Grandstander', 14), padx=10, pady=10, fg=fontcolor, wrap=WORD)
input_text = Text(root, border=0, bg=minibg, font=(
    'Grandstander', 14), padx=10, pady=10, fg=fontcolor, wrap=WORD)


def generated_key(key):
    count = 0
    text = key.split(' ')
    keyTest = key.split(' ')
    for i in text:
        # print(i, end=" ")
        generated.insert(INSERT, i+" ")
        count += 1
        if count == 4:
            print()
            generated.insert(END, '\n')
            count = 0


# seed = ''
# seed_list = seed.split(' ')
rseed = []
rawseed = ''


def select_key(num):
    global seed, rawseed
    if num == 12:
        key12 = keyGen.key12()
        rseed.append(key12)
        rawseed = rseed[0]
        print("This is raw!",rawseed)
        print("this is key12: ", key12)
        seed = key12.split(' ')
        print(seed)
        generated_key(key12)
        mnemonic12.place(x=358, y=94)
        pointer.place(x=299,y=223)
        place_generated_key()
        writeDown.place(x=452, y=391)
        key_align()
  
        close_menu()
        generated.bind('<Control-c>', lambda _: 'break')
    elif num == 15:
        key15 = keyGen.key15()
        rseed.append(key15)
        rawseed = rseed[0]
        print("this is key15: ", key15)
        seed = key15.split(' ')
        generated_key(key15)
        mnemonic15.place(x=358, y=94)
        pointer.place(x=299,y=223)
        place_generated_key()
        writeDown.place(x=452, y=391)
        key_align()

        close_menu()
        generated.bind('<Control-c>', lambda _: 'break')
    elif num == 18:
        key18 = keyGen.key18()
        rseed.append(key18)
        rawseed = rseed[0]
        print("this is key18: ", key18)
        seed = key18.split(' ')
        generated_key(key18)
        mnemonic18.place(x=358, y=94)
        pointer.place(x=299,y=223)
        place_generated_key()
        writeDown.place(x=452, y=391)
        key_align()

        close_menu()
        generated.bind('<Control-c>', lambda _: 'break')
    elif num == 21:
        key21 = keyGen.key21()
        rseed.append(key21)
        rawseed = rseed[0]
        print("this is key21: ", key21)
        seed = key21.split(' ')
        generated_key(key21)
        mnemonic21.place(x=358, y=94)
        pointer.place(x=299,y=223)
        place_generated_key()
        writeDown.place(x=452, y=391)
        key_align()

        close_menu()
        generated.bind('<Control-c>', lambda _: 'break')
    elif num == 24:
        key24 = keyGen.key24()
        rseed.append(key24)
        rawseed = rseed[0]
        print("this is key24: ", key24)
        seed = key24.split(' ')
        generated_key(key24)
        mnemonic24.place(x=358, y=94)
        pointer.place(x=299,y=223)
        place_generated_key()
        writeDown.place(x=452, y=391)
        key_align()
  
        close_menu()
        generated.bind('<Control-c>', lambda _: 'break')


def confirm_seed():
    generated.place_forget()
    input_text.place(x=409, y=244,
                     width=363, height=132)

    confirm.place(x=358, y=94)
    next_button.place(x=530, y=404)
    close_mnemonic()
    writeDown.place_forget()
    


sub = False


def submit():  # Callback function for SUBMIT Button
    global seed, count2, sub
    text = generated.get('1.0', 'end-2c')
    textSplit = text.split(' ')
    print(seed)
    text_input = input_text.get('1.0', 'end-1c')
    text_input_list = text_input.split(' ')
    generated.place_forget()
    input_text.bind('<Control-v>', lambda _: 'break')
    print(rawseed)
    if text_input_list.__eq__(seed):
        print("Yep!")
        input_text.place_forget()
        confirm.place_forget()
        next_button.place_forget()
        input_text.delete('1.0', END)
        open_home()
        p2pkh_from_seed(True)
        p2wpkh_from_seed(True)
        p2tr_from_seed(True)
        home.place(x=64, y=169)
    elif text_input.__eq__(''):
        messagebox.showinfo("Error!", "Input cannot be empty!")
    else:
        messagebox.showinfo("Error!", "Seed incorrect!")
    close_mnemonic()
    writeDown.place_forget()


next_button = Button(root, image=nextImage, border=0,
                     bg=seedbg, activebackground=seedbg, command=submit)
# ──────────────────────────────────────Status Check──────────────────────────────────────────────────── #


def check_connection():
    rpc_user = 'apirak12'
    rpc_password = 'api123'
    rpc_port = 8332
    auth = requests.auth.HTTPBasicAuth(rpc_user, rpc_password)
    headers = {'content-type': 'application/json'}
    url = f'http://localhost:{rpc_port}/'
    method = 'getblockchaininfo'
    params = []
    payload = {
        'method': method,
        'params': params,
        'jsonrpc': '2.0',
        'id': 0,
    }
    try:
        response = requests.post(url, data=json.dumps(
            payload), headers=headers, auth=auth)
        if response.status_code == 200:
            status.config(text="Connected")
            onLabel.place(x=907, y=486)
            offLabel.place_forget()
            block_height_method = 'getblockcount'
            block_height_params = []
            block_height_payload = {
                'method': block_height_method,
                'params': block_height_params,
                'jsonrpc': '2.0',
                'id': 0,
            }
            block_height_response = requests.post(url, data=json.dumps(
                block_height_payload), headers=headers, auth=auth)
            block_height = block_height_response.json()['result']
            status.config(text="%s Block" % block_height)
        else:
            status.config(text="Disconnected")
            offLabel.place(x=931, y=507)
    except ConnectionError:
        status.config(text="Disconnected")
        offLabel.place(x=931, y=507)


def recheck():
    root.after(1000, check_connection)
    status.config(text="Checking...")


def close_Screen():
    loading.place_forget()

# ────────────────────────────────────Balance Check────────────────────────────────────────────────────── #

print(rawseed)
def gtc(dtxt):
    root.clipboard_clear()
    root.clipboard_append(dtxt)

def setformat_p2tr(masterkey):
    Frist = masterkey[:13]
    Last = masterkey[-13:]
    result = Frist + "........." + Last
    return result


textboxImage = PhotoImage(file=r'resources\text\textbox.png')
p2pkhbox = Label(root, image=textboxImage, bd=0, bg=seedbg)
p2pkhbox2 = Label(root, image=textboxImage, bd=0, bg=seedbg)
p2pkhbox3 = Label(root, image=textboxImage, bd=0, bg=seedbg)

p2wpkhbox = Label(root, image=textboxImage, bd=0, bg=seedbg)
p2wpkhbox2 = Label(root, image=textboxImage, bd=0, bg=seedbg)
p2wpkhbox3 = Label(root, image=textboxImage, bd=0, bg=seedbg)

p2trbox = Label(root, image=textboxImage, bd=0, bg=seedbg)
p2trbox2 = Label(root, image=textboxImage, bd=0, bg=seedbg)
p2trbox3 = Label(root, image=textboxImage, bd=0, bg=seedbg)

p2pkhTextBox = Text(root, border=0, bg='#D9D9D9', font=(
    'Grandstander', 9), fg=fontcolor)
p2pkhTextBox2 = Text(root, border=0, bg='#D9D9D9', font=(
    'Grandstander', 9), fg=fontcolor)
p2pkhTextBox3 = Text(root, border=0, bg='#D9D9D9', font=(
    'Grandstander', 9), fg=fontcolor)

p2wpkhTextBox = Text(root, border=0, bg='#D9D9D9', font=(
    'Grandstander', 9), fg=fontcolor)
p2wpkhTextBox2 = Text(root, border=0, bg='#D9D9D9', font=(
    'Grandstander', 9), fg=fontcolor)
p2wpkhTextBox3 = Text(root, border=0, bg='#D9D9D9', font=(
    'Grandstander', 9), fg=fontcolor)

p2trTextBox = Text(root, border=0, bg='#D9D9D9', font=(
    'Grandstander', 9), fg=fontcolor)
p2trTextBox2 = Text(root, border=0, bg='#D9D9D9', font=(
    'Grandstander', 9), fg=fontcolor)
p2trTextBox3 = Text(root, border=0, bg='#D9D9D9', font=(
    'Grandstander', 9), fg=fontcolor)

copyImage = PhotoImage(file=r'resources\text\copy.png')

copy_p2pkh = Button(root, image=copyImage, bd=0, bg=seedbg,
                        activebackground=seedbg)
copy_p2pkh2 = Button(root, image=copyImage, bd=0, bg=seedbg,
                        activebackground=seedbg)
copy_p2pkh3 = Button(root, image=copyImage, bd=0, bg=seedbg,
                        activebackground=seedbg)

copy_p2wpkh = Button(root, image=copyImage, bd=0, bg=seedbg,
                        activebackground=seedbg)
copy_p2wpkh2 = Button(root, image=copyImage, bd=0, bg=seedbg,
                        activebackground=seedbg)
copy_p2wpkh3 = Button(root, image=copyImage, bd=0, bg=seedbg,
                        activebackground=seedbg)

copy_p2tr = Button(root, image=copyImage, bd=0, bg=seedbg,
                        activebackground=seedbg)
copy_p2tr2 = Button(root, image=copyImage, bd=0, bg=seedbg,
                        activebackground=seedbg)
copy_p2tr3 = Button(root, image=copyImage, bd=0, bg=seedbg,
                        activebackground=seedbg)

def p2pkh_from_seed(ch):
    if ch == True:
        
        p2pkh = recovery.recovery_from_seed(rawseed, 0)
        print(p2pkh)
        list1 = []
        p2pkhbox.lower()

        for i in p2pkh:
            format = setformat_p2tr(i)
            list1.append(format)

        p2pkhTextBox.insert(INSERT, list1[0])
        p2pkhTextBox.config(state='disabled')

        p2pkhTextBox2.insert(INSERT, list1[1])
        p2pkhTextBox2.config(state='disabled')

        p2pkhTextBox3.insert(INSERT, list1[2])
        p2pkhTextBox3.config(state='disabled')
        
        copy_p2pkh.config(command= lambda: gtc(p2pkh[0]))
        copy_p2pkh2.config(command= lambda: gtc(p2pkh[1]))
        copy_p2pkh3.config(command= lambda: gtc(p2pkh[2]))
    else: 
        print("FAIL!!!")

def p2wpkh_from_seed(ch):
    if ch == True:

        p2wpkh = recovery.recovery_from_seed(rawseed, 1)
        print(p2wpkh)
        list1 = []
        p2wpkhbox.lower()

        for i in p2wpkh:
            format = setformat_p2tr(i)
            list1.append(format)

        p2wpkhTextBox.insert(INSERT, list1[0])
        p2wpkhTextBox.config(state='disabled')

        p2wpkhTextBox2.insert(INSERT, list1[1])
        p2wpkhTextBox2.config(state='disabled')

        p2wpkhTextBox3.insert(INSERT, list1[2])
        p2wpkhTextBox3.config(state='disabled')
        
        copy_p2wpkh.config(command= lambda: gtc(p2wpkh[0]))
        copy_p2wpkh2.config(command= lambda: gtc(p2wpkh[1]))
        copy_p2wpkh3.config(command= lambda: gtc(p2wpkh[2]))
    else: 
        print("FAIL!!!")

def p2tr_from_seed(ch):
    if ch == True:

        p2tr = recovery.recovery_from_seed(rawseed, 2)
        print(p2tr)
        list1 = []
        p2trbox.lower()

        for i in p2tr:
            format = setformat_p2tr(i)
            list1.append(format)

        p2trTextBox.insert(INSERT, list1[0])
        p2trTextBox.config(state='disabled')

        p2trTextBox2.insert(INSERT, list1[1])
        p2trTextBox2.config(state='disabled')

        p2trTextBox3.insert(INSERT, list1[2])
        p2trTextBox3.config(state='disabled')
        
        copy_p2tr.config(command= lambda: gtc(p2tr[0]))
        copy_p2tr2.config(command= lambda: gtc(p2tr[1]))
        copy_p2tr3.config(command= lambda: gtc(p2tr[2]))
    else: 
        print("FAIL!!!")

# ─────────────────────────────────Hovering Effect───────────────────────────────────────────────────────── #
class Btn(Button):
    def __init__(self, root, img1, img2, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.img = ImageTk.PhotoImage(Image.open(img1))
        self.img2 = ImageTk.PhotoImage(Image.open(img2))

        self.config(image=self.img, bg=bgcolor, bd=0, activebackground=bgcolor)

        self.bind('<Enter>', self.enter)
        self.bind('<Leave>', self.leave)

    def enter(self, event):
        self.config(image=self.img2, bg=bgcolor,
                    bd=0, activebackground=bgcolor)

    def leave(self, event):
        self.config(image=self.img, bg=bgcolor, bd=0, activebackground=bgcolor)
# ────────────────────────────────────Open Menu────────────────────────────────────────────────────── #


def open_menu_wallet():
    global count1, count2
    count1 = count1 + 1
    # print("wallet",count1)
    # print("multiSig",count2)
    if count1 > 1:
        count1 = 0
    # count clicks 1 = open ,2 = close
    if count1 == 1:
        generated.config(state=NORMAL)
        generated.delete("1.0", END)
        pointer.place(x=312, y=228)
        menu.place(x=363, y=151)
        newwallet_button.place(x=385, y=196)
        recovery_button.place(x=385, y=292)
        master_button.place(x=385, y=388)
        confirm.place_forget()
        close_menu()
        close_mnemonic()
        close_home()
        generated.place_forget()
        next_button.place_forget()
        writeDown.place_forget()
        input_text.place_forget()
        count2 = 0
    else:
        pointer.place_forget()
        close_wallet_buttons()


def open_generated_wallet():
    global count2, count1
    count2 = count2 + 1
    # print("multiSig",count2)
    # print("wallet", count1)
    if count2 > 1:
        count2 = 0
    # count clicks 1 = open ,2 = close
    if count2 == 1:
        pointer.place(x=312, y=228)
        pointer.bind('<Button-1>', lambda x: open_menu_wallet())
        menu2.place(x=365, y=90)
        place_buttons()
        close_wallet_buttons()
        count1 = 0

    else:
        close_menu()


def close_home():
    homebg.place_forget()
    p2pkh_label.place_forget()
    p2wpkh_label.place_forget()
    p2tr_label.place_forget()

    p2pkhbox.place_forget()
    p2pkhbox2.place_forget()
    p2pkhbox3.place_forget()
    p2wpkhbox.place_forget()
    p2wpkhbox2.place_forget()
    p2wpkhbox3.place_forget()
    p2trbox.place_forget()
    p2trbox2.place_forget()
    p2trbox3.place_forget()

    p2pkhTextBox.place_forget()
    p2pkhTextBox2.place_forget()
    p2pkhTextBox3.place_forget()
    p2wpkhTextBox.place_forget()
    p2wpkhTextBox2.place_forget()
    p2wpkhTextBox3.place_forget()
    p2trTextBox.place_forget()
    p2trTextBox2.place_forget()
    p2trTextBox3.place_forget()

    copy_p2pkh.place_forget()
    copy_p2pkh2.place_forget()
    copy_p2pkh3.place_forget()
    copy_p2wpkh.place_forget()
    copy_p2wpkh2.place_forget()
    copy_p2wpkh3.place_forget()
    copy_p2tr.place_forget()
    copy_p2tr2.place_forget()
    copy_p2tr3.place_forget()


homeImage = PhotoImage(file=r'resources\background\home.png')
homebg = Label(root, image=homeImage, bd=0, bg=mainbg)

p2pkh_label = Label(root, text='Pay to Public key Hash (P2PKH)', font=(
    'Grandstander', 13), bg=seedbg, bd=0)

p2wpkh_label = Label(root, text='Pay to Witness Public Key Hash (P2WPKH)', font=(
    'Grandstander', 13), bg=seedbg, bd=0)

p2tr_label = Label(root, text='Pay to Taproot (P2TR)', font=(
    'Grandstander', 13), bg=seedbg, bd=0)


def open_home():
    global count1, count2
    count2 = count2 + 1
    if count2 > 1:
        count2 = 0

    if count2 == 1:
        homebg.lower()
        homebg.place(x=361, y=82)
        home.place(x=64, y=169)
        p2pkh_label.place(x=381, y=92)
        p2wpkh_label.place(x=381, y=217)
        p2tr_label.place(x=381, y=341)

        p2pkhbox.place(x=381, y=123)
        p2pkhbox2.place(x=381, y=156)
        p2pkhbox3.place(x=381, y=187)
        p2wpkhbox.place(x=381, y=248)
        p2wpkhbox2.place(x=381, y=281)
        p2wpkhbox3.place(x=381, y=313)
        p2trbox.place(x=381, y=372)
        p2trbox2.place(x=381, y=405)
        p2trbox3.place(x=381, y=437)

        p2pkhTextBox.place(x=388, y=126, width=239, height=18)
        p2pkhTextBox2.place(x=388, y=159, width=239, height=18)
        p2pkhTextBox3.place(x=388, y=190, width=239, height=18)
        p2wpkhTextBox.place(x=388, y=251, width=239, height=18)
        p2wpkhTextBox2.place(x=388, y=284, width=239, height=18)
        p2wpkhTextBox3.place(x=388, y=316, width=239, height=18)
        p2trTextBox.place(x=388, y=375, width=239, height=18)
        p2trTextBox2.place(x=388, y=408, width=239, height=18)
        p2trTextBox3.place(x=388, y=440, width=239, height=18)

        copy_p2pkh.place(x=634, y=127)
        copy_p2pkh2.place(x=634, y=160)
        copy_p2pkh3.place(x=634, y=191)
        copy_p2wpkh.place(x=634, y=252)
        copy_p2wpkh2.place(x=634, y=285)
        copy_p2wpkh3.place(x=634, y=317)
        copy_p2tr.place(x=634, y=376)
        copy_p2tr2.place(x=634, y=409)
        copy_p2tr3.place(x=634, y=440)
        menu.place_forget()
        pointer.place_forget()
        confirm.place_forget()
        close_menu()
        close_wallet_buttons()   
        close_mnemonic()
        generated.place_forget()
        next_button.place_forget()
        writeDown.place_forget()
        input_text.place_forget()
        count1 = 0
    else:
        close_home()


def open_multisig():
    print()


# ────────────────────────────────────Buttons───────────────────────────────────────────────────── #
# background settings
bg = Label(root, image=bgImage, border=0, bg=mainbg)
bg.place(x=51, y=32)  # -- กำหนดตำแหน่ง
# pointer
pointer = Label(root, image=pointerImage, border=0, bg=mainbg)
# wallet menu settings
menu = Label(root, image=menuImage, border=0, bg=mainbg)
count1 = 0
# multiSig menu settings
menu2 = Label(root, image=menuImage2, border=0, bg=mainbg)
count2 = 0
# 12word button settings
button12 = Btn(root, img1=word_12Image1, img2=word_12Image2,
               command=lambda: select_key(12))
# 15word button settings
button15 = Btn(root, img1=word_15Image1, img2=word_15Image2,
               command=lambda: select_key(15))
# 18word button settings
button18 = Btn(root, img1=word_18Image1, img2=word_18Image2,
               command=lambda: select_key(18))
# 21word button settings
button21 = Btn(root, img1=word_21Image1, img2=word_21Image2,
               command=lambda: select_key(21))
# 24word button settings
button24 = Btn(root, img1=word_24Image1, img2=word_24Image2,
               command=lambda: select_key(24))
# wallet button settings
wallet_button = Btn(root, img1=walletImage1, img2=walletImage2,
                    command=lambda: open_menu_wallet())
wallet_button.place(x=64, y=220)  # -- กำหนดตำแหน่ง
# MultiSig Button
multiSig_button = Btn(root, img1=multiSigImage1, img2=multiSigImage2, )
multiSig_button.place(x=64, y=272)  # -- กำหนดตำแหน่ง
# Time locked button
timelock_button = Btn(root, img1=timelockImage1, img2=timelockImage2)
timelock_button.place(x=64, y=324)  # -- กำหนดตำแหน่ง
# broadcast button
broadcast_button = Btn(root, img1=broadcastImage1, img2=broadcastImage2)
broadcast_button.place(x=64, y=376)  # -- กำหนดตำแหน่ง
# new wallet button
newwallet_button = Btn(root, img1=newwalletImage1,
                       img2=newwalletImage2, command=lambda: open_generated_wallet())
# Recovery button
recovery_button = Btn(root, img1=recoveryImage1, img2=recoveryImage2)
# Master key button
master_button = Btn(root, img1=masterImage1, img2=masterImage2)
# Loading Image
loadingImage = PhotoImage(file=r'resources/background/loading.png')
loading = Label(root, image=loadingImage, border=0)
# Confirm button
writeDown = Button(root, image=writeDownImage, border=0, bg='#FAF7F0',
                   activebackground='#FAF7F0', command=lambda: confirm_seed())
# confirm bg
confirm = Label(root, image=conSeedImage, border=0, bg=mainbg)
confirm.lower()

# status checking
status = tk.Label(root, text="Checking...", border=0, bg=mainbg,
                  activebackground=mainbg, font=('Grandstander', 14))
#status.place(x=780, y=506)

home = Btn(root, img1=homeImage1, img2=homeImage2, command=lambda: open_home())

# root.after(2000, check_connection)

root.mainloop()
