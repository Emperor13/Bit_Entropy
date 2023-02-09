# ───────────────────────────────import modules─────────────────────────────────────────────────────────── #
from tkinter import *
from tkinter import messagebox
from requests.exceptions import ConnectionError
from PIL import Image, ImageTk
from embit.descriptor import Descriptor
from embit.networks import NETWORKS
from embit import bip39, bip32
from embit import ec
import hashlib
from binascii import hexlify
import tkinter as tk
import subprocess
import requests
import json
import os
import keyGen
import recovery
import non_bip32
import set_RPC
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
root = Tk()
root.title("Bit Entropy") 
root.geometry('995x566')  
root.minsize(995, 566)  
root.maxsize(995, 566)  
icon = PhotoImage(file=r"resources/icon.png")
root.wm_iconphoto(False, icon)
root.iconbitmap(bitmap=r'favicon.ico')
minibg = '#FAF7F0'
bgcolor = "#98A8F8"
fontcolor = '#272323'
mainbg = '#A4BDF7'
seedbg = '#FAF7F0'
textBoxColor = '#D9D9D9'
root.configure(background=mainbg)  
# ────────────────────────────────────import image for status────────────────────────────────────────────────────── #
onImage = PhotoImage(file=r'resources/status_on.png')
offImage = PhotoImage(file=r'resources/status_off.png')
onLabel = Button(root, image=onImage, border=0, bg=mainbg,
                 activebackground=mainbg)
offLabel = Button(root, image=offImage, border=0, bg=mainbg,
                  activebackground=mainbg)
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
# ────────────────────────────────────import image────────────────────────────────────────────────────── #
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
walletImage1 = r'resources/buttons/wallet_menu/wallet1.png'
walletImage2 = r'resources/buttons/wallet_menu/wallet2.png'
multiSigImage1 = r'resources/buttons/multisig1.png'
multiSigImage2 = r'resources/buttons/multisig2.png'
timelockImage1 = r'resources/buttons/timelock1.png'
timelockImage2 = r'resources/buttons/timelock2.png'
broadcastImage1 = r'resources/buttons/broadcast1.png'
broadcastImage2 = r'resources/buttons/broadcast2.png'
newwalletImage1 = r'resources/buttons/wallet_menu/new_wallet.png'
newwalletImage2 = r'resources/buttons/wallet_menu/new_wallet2.png'
recoveryImage1 = r'resources/buttons/wallet_menu/recovery.png'
recoveryImage2 = r'resources/buttons/wallet_menu/recovery2.png'
masterImage1 = r'resources/buttons/wallet_menu/master.png'
masterImage2 = r'resources/buttons/wallet_menu/master2.png'
homeImage1 = r'resources/buttons/home1.png'
homeImage2 = r'resources/buttons/home2.png'
textboxImage = PhotoImage(file=r'resources/text/textbox.png')
textboxImage2 = PhotoImage(file=r'resources/text/textbox2.png')
pointerImage = PhotoImage(file=r'resources/pointer.png')
writeDownImage = PhotoImage(file=r'resources/confirm.png')
conSeedImage = PhotoImage(
    file=r'resources/background/mnemonic/confirmseed.png')
nextImage = PhotoImage(file=r'resources/buttons/next.png')
settingImage = PhotoImage(file=r'resources/settings.png')
bgImage = PhotoImage(file=r'resources/background/first_page.png')
menuImage = PhotoImage(file=r'resources/background/menu1.png')
menuImage2 = PhotoImage(file=r'resources/background/menu2.png')
submitImage = PhotoImage(file=r'resources/buttons/MultiSig/Submit.png')
recoveImg = PhotoImage(
    file=r'resources/background/Recovery_Phrase/Group 44.png')
importImg = PhotoImage(file=r'resources/buttons/import.png')
copyImage = PhotoImage(file=r'resources/text/copy.png')
homeImage = PhotoImage(file=r'resources/background/home.png')
buttonImg = PhotoImage(file=r'resources/connect.png')
# ────────────────────────────────────create Label, Button, Text, Entry────────────────────────────────────────────────────── #
recoveryBg = Label(root, image=recoveImg, bd=0, bg=mainbg)
p2pkhbox = Label(root, image=textboxImage, bd=0, bg=seedbg)
p2pkhbox2 = Label(root, image=textboxImage, bd=0, bg=seedbg)
p2pkhbox3 = Label(root, image=textboxImage, bd=0, bg=seedbg)
p2wpkhbox = Label(root, image=textboxImage, bd=0, bg=seedbg)
p2wpkhbox2 = Label(root, image=textboxImage, bd=0, bg=seedbg)
p2wpkhbox3 = Label(root, image=textboxImage, bd=0, bg=seedbg)
p2trbox = Label(root, image=textboxImage, bd=0, bg=seedbg)
p2trbox2 = Label(root, image=textboxImage, bd=0, bg=seedbg)
p2trbox3 = Label(root, image=textboxImage, bd=0, bg=seedbg)
pubkeybox = Label(root, image=textboxImage2, bd=0, bg=seedbg)
pubkeybox2 = Label(root, image=textboxImage2, bd=0, bg=seedbg)
pubkeybox3 = Label(root, image=textboxImage2, bd=0, bg=seedbg)
prikeybox = Label(root, image=textboxImage2, bd=0, bg=seedbg)
prikeybox2 = Label(root, image=textboxImage2, bd=0, bg=seedbg)
prikeybox3 = Label(root, image=textboxImage2, bd=0, bg=seedbg)
non_prikeybox = Label(root, image=textboxImage2, bd=0, bg=seedbg)
non_pubkeybox = Label(root, image=textboxImage2, bd=0, bg=seedbg)
homebg = Label(root, image=homeImage, bd=0, bg=mainbg)

setting = Button(root, image=settingImage, border=0,
                 bg=mainbg, activebackground=mainbg, command=lambda: login_node())
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
copy_pubkey = Button(root, image=copyImage, bd=0, bg=seedbg,
                     activebackground=seedbg)
copy_pubkey2 = Button(root, image=copyImage, bd=0, bg=seedbg,
                      activebackground=seedbg)
copy_pubkey3 = Button(root, image=copyImage, bd=0, bg=seedbg,
                      activebackground=seedbg)
copy_prvkey = Button(root, image=copyImage, bd=0, bg=seedbg,
                     activebackground=seedbg)
copy_prvkey2 = Button(root, image=copyImage, bd=0, bg=seedbg,
                      activebackground=seedbg)
copy_prvkey3 = Button(root, image=copyImage, bd=0, bg=seedbg,
                      activebackground=seedbg)
copy_non_prvkey = Button(root, image=copyImage, bd=0, bg=seedbg,
                         activebackground=seedbg)
copy_non_pubkey = Button(root, image=copyImage, bd=0, bg=seedbg,
                         activebackground=seedbg)

recovery_text = Text(root, border=0, bg=minibg, font=(
    'Grandstander', 14), padx=10, pady=10, fg=fontcolor, wrap=WORD)
generated = Text(root, border=0, bg=minibg, font=(
    'Grandstander', 14), padx=10, pady=10, fg=fontcolor, wrap=WORD)
input_text = Text(root, border=0, bg=minibg, font=(
    'Grandstander', 14), padx=10, pady=10, fg=fontcolor, wrap=WORD)
p2pkhTextBox = Text(root, border=0, bg=textBoxColor, font=(
    'Grandstander', 9), fg=fontcolor)
p2pkhTextBox2 = Text(root, border=0, bg=textBoxColor, font=(
    'Grandstander', 9), fg=fontcolor)
p2pkhTextBox3 = Text(root, border=0, bg=textBoxColor, font=(
    'Grandstander', 9), fg=fontcolor)
p2wpkhTextBox = Text(root, border=0, bg=textBoxColor, font=(
    'Grandstander', 9), fg=fontcolor)
p2wpkhTextBox2 = Text(root, border=0, bg=textBoxColor, font=(
    'Grandstander', 9), fg=fontcolor)
p2wpkhTextBox3 = Text(root, border=0, bg=textBoxColor, font=(
    'Grandstander', 9), fg=fontcolor)
p2trTextBox = Text(root, border=0, bg=textBoxColor, font=(
    'Grandstander', 9), fg=fontcolor)
p2trTextBox2 = Text(root, border=0, bg=textBoxColor, font=(
    'Grandstander', 9), fg=fontcolor)
p2trTextBox3 = Text(root, border=0, bg=textBoxColor, font=(
    'Grandstander', 9), fg=fontcolor)
pubkeyTextBox = Text(root, border=0, bg=textBoxColor, font=(
    'Grandstander', 9), fg=fontcolor)
pubkeyTextBox2 = Text(root, border=0, bg=textBoxColor, font=(
    'Grandstander', 9), fg=fontcolor)
pubkeyTextBox3 = Text(root, border=0, bg=textBoxColor, font=(
    'Grandstander', 9), fg=fontcolor)
prvkeyTextBox = Text(root, border=0, bg=textBoxColor, font=(
    'Grandstander', 9), fg=fontcolor)
prvkeyTextBox2 = Text(root, border=0, bg=textBoxColor, font=(
    'Grandstander', 9), fg=fontcolor)
prvkeyTextBox3 = Text(root, border=0, bg=textBoxColor, font=(
    'Grandstander', 9), fg=fontcolor)
rand_prvkey = Text(root, border=0, bg=textBoxColor, font=(
    'Grandstander', 9), fg=fontcolor)
rand_pubkey = Text(root, border=0, bg=textBoxColor, font=(
    'Grandstander', 9), fg=fontcolor)


user_input = Entry(root, border=0, bg=textBoxColor,
                   font=('Grandstander', 11), fg=fontcolor)
pass_input = Entry(root, border=0, show='*', bg=textBoxColor,
                   font=('Grandstander', 11), fg=fontcolor)

setting.place(x=916, y=17)

connectImage = PhotoImage(file=r'resources/connectNode.png')

connect = Label(root, image=connectImage, bd=0, bg=mainbg)
connect.lower()

noteImg = PhotoImage(file=r'resources/note.png')
note = Label(root, image=noteImg, bd=0, bg=mainbg)


def login_node():
    global count1
    count1 = count1 + 1
    if count1 > 1:
        count1 = 0
    if count1 == 1:
        connect.place(x=348, y=109)
        note.place(x=706, y=115)
        user_input.place(x=400, y=279, width=213, height=20)
        pass_input.place(x=400, y=346, width=213, height=20)
        connect_button.place(x=449, y=392)
        close_home()
        close_menu()
        close_mnemonic()
        close_wallet_buttons()
        close_recovery_seed_menu()
        set_RPC.write_json_file('', '')
    else:
        close_login_node()

def close_login_node():
    connect.place_forget()
    note.place_forget()
    user_input.place_forget()
    pass_input.place_forget()
    connect_button.place_forget()
    wallet_button.config(state='normal')
    multiSig_button.config(state='normal')
    timelock_button.config(state='normal')
    broadcast_button.config(state='normal')


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



def generated_key(key):
    count = 0
    text = key.split(' ')
    keyTest = key.split(' ')
    for i in text:
        # print(i, end=" ")
        generated.insert(INSERT, i + " ")


rseed = []
rawseed = ''


def select_key(num):
    global seed, rawseed
    if num == 12:
        key12 = keyGen.key12()
        rseed.append(key12)
        rawseed = rseed[0]
        print("This is raw!", rawseed)
        print("this is key12: ", key12)
        seed = key12.split(' ')
        print(seed)
        generated_key(key12)
        mnemonic12.place(x=358, y=94)
        pointer.place(x=299, y=223)
        place_generated_key()
        writeDown.place(x=452, y=391)
        key_align()
        clear_seed()
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
        pointer.place(x=299, y=223)
        place_generated_key()
        writeDown.place(x=452, y=391)
        key_align()
        clear_seed()
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
        pointer.place(x=299, y=223)
        place_generated_key()
        writeDown.place(x=452, y=391)
        key_align()
        clear_seed()
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
        pointer.place(x=299, y=223)
        place_generated_key()
        writeDown.place(x=452, y=391)
        key_align()
        clear_seed()
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
        pointer.place(x=299, y=223)
        place_generated_key()
        writeDown.place(x=452, y=391)
        key_align()
        clear_seed()
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


seed_input = Text(root, border=0, bg=minibg, font=(
    'Grandstander', 14), fg=fontcolor, wrap=WORD)


def recovery_seed_menu():
    recoveryBg.place(x=367, y=90)
    importBtn.place(x=526, y=392)
    seed_input.place(x=421, y=216, width=360, height=124)
    clear_seed()
    close_wallet_buttons()


def close_recovery_seed_menu():
    recoveryBg.place_forget()
    importBtn.place_forget()
    recovery_text.place_forget()
    seed_input.place_forget()


def submit():  # Callback function for SUBMIT Button
    global seed, count2
    input_text.bind('<Control-v>', lambda _: 'break')
    print(seed)
    text_input = input_text.get('1.0', 'end-1c')
    text_input_list = text_input.split(' ')
    generated.place_forget()
    print(rawseed)
    if text_input_list.__eq__(seed):
        print("Yep!")
        input_text.place_forget()
        confirm.place_forget()
        next_button.place_forget()
        input_text.delete('1.0', END)
        open_home()
        p2pkh_from_seed(True, text_input)
        p2wpkh_from_seed(True, text_input)
        p2tr_from_seed(True, text_input)
        master_pubkey(True, text_input)
        master_prvkey(True, text_input)

        home.place(x=64, y=169)
    elif text_input.__eq__(''):
        messagebox.showinfo("Error!", "Input cannot be empty!")
    else:
        messagebox.showinfo("Error!", "Seed incorrect!")
    close_mnemonic()
    writeDown.place_forget()


submitButton = Button(root, image=submitImage, bd=0,
                      bg=seedbg, activebackground=seedbg, command=submit)
next_button = Button(root, image=nextImage, border=0,
                     bg=seedbg, activebackground=seedbg, command=submit)
# ──────────────────────────────────────Status Check──────────────────────────────────────────────────── #
status = tk.Label(root, text="Checking...", border=0, bg=mainbg,
                  activebackground=mainbg, font=('Grandstander', 14))


def check_connection():
    user = user_input.get()
    password = pass_input.get()
    if os.path.exists('setup_connect.json') == False:
        login_node()

    if (user == '') & (password == ''):
        print("user and password empty")
    else:
        set_RPC.write_json_file(user, password)

    read = set_RPC.read_json_file("setup_connect.json")
    rpc_user = read["username"]
    rpc_password = read["password"]
    print(read["username"])
    print(read["password"])
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
            onLabel.place(x=931, y=515)
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
            close_login_node()
        else:
            messagebox.showinfo("Error", "Connection Fail!!")
            status.config(text="Disconnected")
            offLabel.place(x=931, y=515)
            onLabel.place_forget()
    except ConnectionError:
        messagebox.showinfo("Error", "Connection Fail!!")
        status.config(text="Disconnected")
        offLabel.place(x=931, y=515)
        onLabel.place_forget()

def recheck():
    root.after(1000, check_connection())
    status.config(text="Checking...")


connect_button = Button(root, image=buttonImg, bd=0, bg=seedbg,
                        activebackground=seedbg, command=lambda: check_connection())


def close_Screen():
    loading.place_forget()




def gtc(dtxt):
    root.clipboard_clear()
    root.clipboard_append(dtxt)


def setformat_p2tr(masterkey: str) -> str:
    Frist = masterkey[:13]
    Last = masterkey[-13:]
    result = Frist + "........." + Last
    return result


def p2pkh_from_seed(ch, seed):
    if ch == True:
        seed = rawseed
        p2pkh = recovery.recovery_from_seed(seed, 0)
        print(p2pkh)
        list1 = []

        for i in p2pkh:
            # format = setformat_p2tr(i)
            list1.append(i)

        p2pkhTextBox.insert(INSERT, list1[0])
        p2pkhTextBox.config(state='disabled')

        p2pkhTextBox2.insert(INSERT, list1[1])
        p2pkhTextBox2.config(state='disabled')

        p2pkhTextBox3.insert(INSERT, list1[2])
        p2pkhTextBox3.config(state='disabled')

        copy_p2pkh.config(command=lambda: gtc(p2pkh[0]))
        copy_p2pkh2.config(command=lambda: gtc(p2pkh[1]))
        copy_p2pkh3.config(command=lambda: gtc(p2pkh[2]))
    else:
        print("P2PKH FAIL!!!")


def p2pkh_from_masterKey(ch, masterKey):
    if ch == True:
        masterKey = master_key_input.get('1.0', 'end-1c')
        p2pkh = recovery.recovery_from_master_Publickey(masterKey, 0)
        print(p2pkh)
        list1 = []

        for i in p2pkh:
            # format = setformat_p2tr(i)
            list1.append(i)

        p2pkhTextBox.insert(INSERT, list1[0])
        p2pkhTextBox.config(state='disabled')

        p2pkhTextBox2.insert(INSERT, list1[1])
        p2pkhTextBox2.config(state='disabled')

        p2pkhTextBox3.insert(INSERT, list1[2])
        p2pkhTextBox3.config(state='disabled')

        copy_p2pkh.config(command=lambda: gtc(p2pkh[0]))
        copy_p2pkh2.config(command=lambda: gtc(p2pkh[1]))
        copy_p2pkh3.config(command=lambda: gtc(p2pkh[2]))
    else:
        print("P2PKH FAIL!!!")


def p2wpkh_from_masterKey(ch, masterKey):
    if ch == True:
        masterKey = master_key_input.get('1.0', 'end-1c')
        p2wpkh = recovery.recovery_from_master_Publickey(masterKey, 1)
        print(p2wpkh)
        list1 = []

        for i in p2wpkh:
            # format = setformat_p2tr(i)
            list1.append(i)

        p2wpkhTextBox.insert(INSERT, list1[0])
        p2wpkhTextBox.config(state='disabled')

        p2wpkhTextBox2.insert(INSERT, list1[1])
        p2wpkhTextBox2.config(state='disabled')

        p2wpkhTextBox3.insert(INSERT, list1[2])
        p2wpkhTextBox3.config(state='disabled')

        copy_p2wpkh.config(command=lambda: gtc(p2wpkh[0]))
        copy_p2wpkh2.config(command=lambda: gtc(p2wpkh[1]))
        copy_p2wpkh3.config(command=lambda: gtc(p2wpkh[2]))
    else:
        print("P2PKH FAIL!!!")


def p2tr_from_masterKey(ch, masterKey):
    if ch == True:
        masterKey = master_key_input.get('1.0', 'end-1c')
        p2tr = recovery.recovery_from_master_Publickey(masterKey, 2)
        print(p2tr)
        list1 = []

        for i in p2tr:
            # format = setformat_p2tr(i)
            list1.append(i)

        p2trTextBox.insert(INSERT, list1[0])
        p2trTextBox.config(state='disabled')

        p2trTextBox2.insert(INSERT, list1[1])
        p2trTextBox2.config(state='disabled')

        p2trTextBox3.insert(INSERT, list1[2])
        p2trTextBox3.config(state='disabled')

        copy_p2tr.config(command=lambda: gtc(p2tr[0]))
        copy_p2tr2.config(command=lambda: gtc(p2tr[1]))
        copy_p2tr3.config(command=lambda: gtc(p2tr[2]))
    else:
        print("p2tr FAIL!!!")


def p2wpkh_from_seed(ch, seed):
    if ch == True:
        seed = rawseed
        p2wpkh = recovery.recovery_from_seed(seed, 1)
        print(p2wpkh)
        list1 = []

        for i in p2wpkh:
            # format = setformat_p2tr(i)
            list1.append(i)

        p2wpkhTextBox.insert(INSERT, list1[0])
        p2wpkhTextBox.config(state='disabled')

        p2wpkhTextBox2.insert(INSERT, list1[1])
        p2wpkhTextBox2.config(state='disabled')

        p2wpkhTextBox3.insert(INSERT, list1[2])
        p2wpkhTextBox3.config(state='disabled')

        copy_p2wpkh.config(command=lambda: gtc(p2wpkh[0]))
        copy_p2wpkh2.config(command=lambda: gtc(p2wpkh[1]))
        copy_p2wpkh3.config(command=lambda: gtc(p2wpkh[2]))
    else:
        print("P2WPKH FAIL!!!")


def p2tr_from_seed(ch, seed):
    if ch == True:
        seed = rawseed
        p2tr = recovery.recovery_from_seed(seed, 2)
        print(p2tr)
        list1 = []

        for i in p2tr:
            format = setformat_p2tr(i)
            list1.append(format)

        p2trTextBox.insert(INSERT, list1[0])
        p2trTextBox.config(state='disabled')

        p2trTextBox2.insert(INSERT, list1[1])
        p2trTextBox2.config(state='disabled')

        p2trTextBox3.insert(INSERT, list1[2])
        p2trTextBox3.config(state='disabled')

        copy_p2tr.config(command=lambda: gtc(p2tr[0]))
        copy_p2tr2.config(command=lambda: gtc(p2tr[1]))
        copy_p2tr3.config(command=lambda: gtc(p2tr[2]))
    else:
        print("P2TR FAIL!!!")


def master_pubkey(ch, seed):
    seed = rawseed
    if ch == True:
        pubkey = recovery.create_masterkey_from_seed(seed)
        print(pubkey)
        x = str(pubkey[1][0])
        z = str(pubkey[1][1])
        y = str(pubkey[1][2])

        xpub = setformat_p2tr(x)
        zpub = setformat_p2tr(z)
        ypub = setformat_p2tr(y)

        pubkeyTextBox.insert(INSERT, xpub)
        pubkeyTextBox.config(state='disabled')

        pubkeyTextBox2.insert(INSERT, zpub)
        pubkeyTextBox2.config(state='disabled')

        pubkeyTextBox3.insert(INSERT, ypub)
        pubkeyTextBox3.config(state='disabled')

        copy_pubkey.config(command=lambda: gtc(x))
        copy_pubkey2.config(command=lambda: gtc(z))
        copy_pubkey3.config(command=lambda: gtc(y))
    else:
        print("Fail!!")


def master_prvkey(ch, seed):
    seed = rawseed
    if ch == True:
        prvkey = recovery.create_masterkey_from_seed(seed)
        print(prvkey)
        x = str(prvkey[0][0])
        z = str(prvkey[0][1])
        y = str(prvkey[0][2])

        xprv = setformat_p2tr(x)
        zprv = setformat_p2tr(z)
        yprv = setformat_p2tr(y)

        prvkeyTextBox.insert(INSERT, xprv)
        prvkeyTextBox.config(state='disabled')

        prvkeyTextBox2.insert(INSERT, zprv)
        prvkeyTextBox2.config(state='disabled')

        prvkeyTextBox3.insert(INSERT, yprv)
        prvkeyTextBox3.config(state='disabled')

        copy_prvkey.config(command=lambda: gtc(x))
        copy_prvkey2.config(command=lambda: gtc(z))
        copy_prvkey3.config(command=lambda: gtc(y))
    else:
        print("Fail!!")


randImg = PhotoImage(file=r'resources/buttons/random.png')


def rand_non_bip32(ch):
    rand_prvkey.config(state='normal')
    rand_pubkey.config(state='normal')

    rand_prvkey.delete('1.0', END)
    rand_pubkey.delete('1.0', END)
    print("Clear!!")
    if ch == True:
        Entropy = non_bip32.random_entropy()
        wif = non_bip32.create_wif(Entropy)
        print("Private Key: ", wif)
        prv = ec.PrivateKey.from_wif(wif)
        pub = prv.get_public_key()
        print('Public Key: %s' % pub, '/n')

        rand_prv = setformat_p2tr(str(prv))
        rand_pub = setformat_p2tr(str(pub))

        rand_prvkey.insert(INSERT, rand_prv)
        rand_prvkey.config(state='disabled')

        rand_pubkey.insert(INSERT, rand_pub)
        rand_pubkey.config(state='disabled')

        copy_non_prvkey.config(command=lambda: gtc(prv))
        copy_non_pubkey.config(command=lambda: gtc(pub))
    else:
        rand_prvkey.config(state='NORMAL')
        rand_pubkey.config(state='NORMAL')

        rand_prvkey.delete('1.0', END)
        rand_pubkey.delete('1.0', END)
        print("Fail!!")


master_key_input = Text(root, border=0, bg=minibg, font=(
    'Grandstander', 14), fg=fontcolor, wrap=WORD)

use_masterleyImg = PhotoImage(
    file=r'resources/background/Use_MasterKey/Group 45.png')
use_masterleyBg = Label(root, image=use_masterleyImg, bd=0, bg=mainbg)
use_masterleyBg.lower()
importBtn2 = Button(root, image=importImg, bd=0,
                    bg=seedbg, activebackground=seedbg, command=lambda: recovery_masterKey())


def recovery_masterKey_menu():
    use_masterleyBg.place(x=367, y=90)
    importBtn2.place(x=526, y=392)
    master_key_input.place(x=421, y=216, width=360, height=124)
    clear_seed()
    close_wallet_buttons()


def close_recovery_masterKey_menu():
    use_masterleyBg.place_forget()
    importBtn2.place_forget()
    master_key_input.place_forget()


def recovery_masterKey():
    global master_key
    master_key = master_key_input.get('1.0', END)
    check_type_master_key()
    p2pkh_from_masterKey(True, master_key)
    p2wpkh_from_masterKey(True, master_key)
    p2tr_from_masterKey(True, master_key)
    open_home()


def recovery_seed():
    global rawseed
    rawseed = seed_input.get('1.0', END)
    print(rawseed)
    p2pkh_from_seed(True, rawseed)
    p2wpkh_from_seed(True, rawseed)
    p2tr_from_seed(True, rawseed)
    master_pubkey(True, rawseed)
    master_prvkey(True, rawseed)
    open_home()


importBtn = Button(root, image=importImg, bd=0,
                   bg=seedbg, activebackground=seedbg, command=lambda: recovery_seed())
rand_button = Button(root, image=randImg, bd=0, bg=seedbg,
                     activebackground=seedbg, command=lambda: rand_non_bip32(True))



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



def wallet_menu():
    pointer.place(x=312, y=228)
    menu.place(x=363, y=151)
    newwallet_button.place(x=385, y=196)
    recovery_button.place(x=385, y=292)
    master_button.place(x=385, y=388)
    recoveryBg.place_forget()
    recovery_text.place_forget()
    importBtn.place_forget()
    submitButton.place_forget()
    confirm.place_forget()
    close_menu()
    close_mnemonic()
    close_home()
    generated.place_forget()
    next_button.place_forget()
    writeDown.place_forget()
    input_text.place_forget()


def open_menu_wallet():
    global count1, count2
    count1 = count1 + 1
    if count1 > 1:
        count1 = 0
    if count1 == 1:
        generated.config(state=NORMAL)
        generated.delete("1.0", END)
        wallet_menu()
        close_recovery_seed_menu()
        close_login_node()
        pointer.place_forget()
        count2 = 0
    else:
        pointer.place_forget()
        close_wallet_buttons()


def clear_seed():
    p2pkhTextBox.config(state='normal')
    p2pkhTextBox2.config(state='normal')
    p2pkhTextBox3.config(state='normal')
    p2wpkhTextBox.config(state='normal')
    p2wpkhTextBox2.config(state='normal')
    p2wpkhTextBox3.config(state='normal')
    p2trTextBox.config(state='normal')
    p2trTextBox2.config(state='normal')
    p2trTextBox3.config(state='normal')
    pubkeyTextBox.config(state='normal')
    pubkeyTextBox2.config(state='normal')
    pubkeyTextBox3.config(state='normal')
    prvkeyTextBox.config(state='normal')
    prvkeyTextBox2.config(state='normal')
    prvkeyTextBox3.config(state='normal')
    seed_input.config(state='normal')
    rand_prvkey.config(state='normal')
    rand_pubkey.config(state='normal')
    p2pkhTextBox.delete('1.0', END)
    p2pkhTextBox2.delete('1.0', END)
    p2pkhTextBox3.delete('1.0', END)
    p2wpkhTextBox.delete('1.0', END)
    p2wpkhTextBox2.delete('1.0', END)
    p2wpkhTextBox3.delete('1.0', END)
    p2trTextBox.delete('1.0', END)
    p2trTextBox2.delete('1.0', END)
    p2trTextBox3.delete('1.0', END)
    pubkeyTextBox.delete('1.0', END)
    pubkeyTextBox2.delete('1.0', END)
    pubkeyTextBox3.delete('1.0', END)
    prvkeyTextBox.delete('1.0', END)
    prvkeyTextBox2.delete('1.0', END)
    prvkeyTextBox3.delete('1.0', END)
    rand_prvkey.delete('1.0', END)
    rand_pubkey.delete('1.0', END)
    seed_input.delete('1.0', END)


def open_generated_wallet():
    global count2, count1, rseed
    count2 = count2 + 1

    if count2 > 1:
        count2 = 0

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

    p2pkhbox.place_forget()
    p2pkhbox2.place_forget()
    p2pkhbox3.place_forget()
    p2wpkhbox.place_forget()
    p2wpkhbox2.place_forget()
    p2wpkhbox3.place_forget()
    p2trbox.place_forget()
    p2trbox2.place_forget()
    p2trbox3.place_forget()
    pubkeybox.place_forget()
    pubkeybox2.place_forget()
    pubkeybox3.place_forget()
    prikeybox.place_forget()
    prikeybox2.place_forget()
    prikeybox3.place_forget()
    non_prikeybox.place_forget()
    non_pubkeybox.place_forget()

    p2pkhTextBox.place_forget()
    p2pkhTextBox2.place_forget()
    p2pkhTextBox3.place_forget()
    p2wpkhTextBox.place_forget()
    p2wpkhTextBox2.place_forget()
    p2wpkhTextBox3.place_forget()
    p2trTextBox.place_forget()
    p2trTextBox2.place_forget()
    p2trTextBox3.place_forget()
    pubkeyTextBox.place_forget()
    pubkeyTextBox2.place_forget()
    pubkeyTextBox3.place_forget()
    prvkeyTextBox.place_forget()
    prvkeyTextBox2.place_forget()
    prvkeyTextBox3.place_forget()
    rand_prvkey.place_forget()
    rand_pubkey.place_forget()

    pointer.place_forget()
    copy_p2pkh.place_forget()
    copy_p2pkh2.place_forget()
    copy_p2pkh3.place_forget()
    copy_p2wpkh.place_forget()
    copy_p2wpkh2.place_forget()
    copy_p2wpkh3.place_forget()
    copy_p2tr.place_forget()
    copy_p2tr2.place_forget()
    copy_p2tr3.place_forget()
    copy_pubkey.place_forget()
    copy_pubkey2.place_forget()
    copy_pubkey3.place_forget()
    copy_prvkey.place_forget()
    copy_prvkey2.place_forget()
    copy_prvkey3.place_forget()
    copy_non_prvkey.place_forget()
    copy_non_pubkey.place_forget()
    rand_button.place_forget()


def home_menu():
    homebg.lower()
    homebg.place(x=361, y=82)
    home.place(x=64, y=169)

    p2pkhbox.place(x=381, y=144)
    p2pkhbox2.place(x=381, y=177)
    p2pkhbox3.place(x=381, y=208)
    p2wpkhbox.place(x=381, y=269)
    p2wpkhbox2.place(x=381, y=300)
    p2wpkhbox3.place(x=381, y=334)
    p2trbox.place(x=381, y=393)
    p2trbox2.place(x=381, y=426)
    p2trbox3.place(x=381, y=458)
    pubkeybox.place(x=688, y=269)
    pubkeybox2.place(x=688, y=300)
    pubkeybox3.place(x=688, y=334)
    prikeybox.place(x=688, y=144)
    prikeybox2.place(x=688, y=177)
    prikeybox3.place(x=688, y=208)
    non_prikeybox.place(x=688, y=403)
    non_pubkeybox.place(x=688, y=445)

    p2pkhTextBox.place(x=388, y=147, width=235, height=18)
    p2pkhTextBox2.place(x=388, y=180, width=235, height=18)
    p2pkhTextBox3.place(x=388, y=211, width=235, height=18)
    p2wpkhTextBox.place(x=388, y=272, width=235, height=18)
    p2wpkhTextBox2.place(x=388, y=303, width=235, height=18)
    p2wpkhTextBox3.place(x=388, y=337, width=235, height=18)
    p2trTextBox.place(x=388, y=396, width=235, height=18)
    p2trTextBox2.place(x=388, y=429, width=235, height=18)
    p2trTextBox3.place(x=388, y=461, width=235, height=18)
    pubkeyTextBox.place(x=694, y=272, width=218, height=18)
    pubkeyTextBox2.place(x=694, y=303, width=218, height=18)
    pubkeyTextBox3.place(x=694, y=337, width=218, height=18)
    prvkeyTextBox.place(x=694, y=147, width=218, height=18)
    prvkeyTextBox2.place(x=694, y=180, width=218, height=18)
    prvkeyTextBox3.place(x=694, y=211, width=218, height=18)
    rand_prvkey.place(x=694, y=406, width=218, height=18)
    rand_pubkey.place(x=694, y=448, width=218, height=18)

    copy_p2pkh.place(x=634, y=147)
    copy_p2pkh2.place(x=634, y=180)
    copy_p2pkh3.place(x=634, y=211)
    copy_p2wpkh.place(x=634, y=272)
    copy_p2wpkh2.place(x=634, y=303)
    copy_p2wpkh3.place(x=634, y=337)
    copy_p2tr.place(x=634, y=396)
    copy_p2tr2.place(x=634, y=429)
    copy_p2tr3.place(x=634, y=461)
    copy_pubkey.place(x=919, y=272)
    copy_pubkey2.place(x=919, y=303)
    copy_pubkey3.place(x=919, y=337)
    copy_prvkey.place(x=919, y=147)
    copy_prvkey2.place(x=919, y=180)
    copy_prvkey3.place(x=919, y=211)
    copy_non_prvkey.place(x=919, y=406)
    copy_non_pubkey.place(x=919, y=448)

    rand_button.place(x=751, y=475)
    submitButton.place_forget()
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
    pointer.place_forget()
    close_recovery_seed_menu()
    close_recovery_masterKey_menu()


def check_type_master_key():
    global master_key
    master_key = master_key_input.get('1.0', 'end-1c')
    type = master_key[:4]

    if type == 'xpub':
        pubkeyTextBox.insert(INSERT, master_key)
        print('xpub')
    elif type == 'zpub':
        pubkeyTextBox2.insert(INSERT, master_key)
        print('zpub')
    elif type == 'ypub':
        pubkeyTextBox3.insert(INSERT, master_key)
        print('ypub')
    else:
        print('Master Publick Key incorrect!')
        

def open_home():
    global count1, count2
    count2 = count2 + 1
    if count2 > 1:
        count2 = 0

    if count2 == 1:
        home_menu()
        count1 = 0
    else:
        close_home()


def open_multisig():
    print()



bg = Label(root, image=bgImage, border=0, bg=mainbg)
bg.place(x=51, y=32) 

pointer = Label(root, image=pointerImage, border=0, bg=mainbg)

menu = Label(root, image=menuImage, border=0, bg=mainbg)
count1 = 0

menu2 = Label(root, image=menuImage2, border=0, bg=mainbg)
count2 = 0

button12 = Btn(root, img1=word_12Image1, img2=word_12Image2,
               command=lambda: select_key(12))

button15 = Btn(root, img1=word_15Image1, img2=word_15Image2,
               command=lambda: select_key(15))

button18 = Btn(root, img1=word_18Image1, img2=word_18Image2,
               command=lambda: select_key(18))

button21 = Btn(root, img1=word_21Image1, img2=word_21Image2,
               command=lambda: select_key(21))

button24 = Btn(root, img1=word_24Image1, img2=word_24Image2,
               command=lambda: select_key(24))

wallet_button = Btn(root, img1=walletImage1, img2=walletImage2,
                    command=lambda: open_menu_wallet())
wallet_button.place(x=64, y=220)  

multiSig_button = Btn(root, img1=multiSigImage1, img2=multiSigImage2, )
multiSig_button.place(x=64, y=272)  

timelock_button = Btn(root, img1=timelockImage1, img2=timelockImage2)
timelock_button.place(x=64, y=324)  

broadcast_button = Btn(root, img1=broadcastImage1, img2=broadcastImage2)
broadcast_button.place(x=64, y=376)  

newwallet_button = Btn(root, img1=newwalletImage1,
                       img2=newwalletImage2, command=lambda: open_generated_wallet())

recovery_button = Btn(root, img1=recoveryImage1,
                      img2=recoveryImage2, command=lambda: recovery_seed_menu())

master_button = Btn(root, img1=masterImage1, img2=masterImage2,
                    command=lambda: recovery_masterKey_menu())

loadingImage = PhotoImage(file=r'resources/background/loading.png')
loading = Label(root, image=loadingImage, border=0)

writeDown = Button(root, image=writeDownImage, border=0, bg='#FAF7F0',
                   activebackground='#FAF7F0', command=lambda: confirm_seed())

confirm = Label(root, image=conSeedImage, border=0, bg=mainbg)
confirm.lower()

status = tk.Label(root, text="Sychronizing...", border=0, bg=mainbg,
                  activebackground=mainbg, font=('Grandstander', 14))
status.place(x=780, y=518)
offLabel.place(x=931, y=515)
home = Btn(root, img1=homeImage1, img2=homeImage2, command=lambda: open_home())

check_connection()
root.mainloop()
