import os

def menu():
    print(""".
################################################
.########.#    # ###### #     # #    #    ##
.#       .#    #      #  #   #  #    #   # #
.####### .######    #     # #   ######  #  #
       # .#    #     #     #    #    # #######
.####### .#    # #### #    #    #    #     #
##############################################

      #________________________________#
        Sh3yh4ck3r .. =====.: Group 
        coming soon.. =====.: channel
        First Ver. by =====.: Sh3yh4ck3r
        N0D3__Gr0up  ======.: Creators
             ********************
             ********************
             
         More Tools will be coming soon....
         
             ********************
       #_p_l_e_a_s_e__S_u_p_p_o_r_t__u_s_#
==========================================
[1] Install Nmap 
[2] Hydra
[3] Metasploit 
[4] Instagram Bruteforcer (instahack)
[5] Install routersploit
------------------------------------------
==========================================
[00] Exit
==========================================
""")

loop = True

while loop:
    menu()
    ask = input("~: ")
    if ask == "1":
        print("===You about to install Nmap===")
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y nmap")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] nmap installed successfully :)")
        rmenu = input("[?] Start Nmap? (y/n): ")
        if rmenu == "y":
            os.system("nmap www.nmap.com")
        print("====================================")
        rmenu = input("[?] Back to Selection? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif ask == "2":
        print("===you about to install Hydra===")
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y hydra")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] hydra installed successfully :)")
        rmenu = input("[?] Start Hydra? (y/n): ")
        if rmenu == "y":
            os.system("hydra")
        print("====================================")
        rmenu = input("[?] back to Selection? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
  
    elif ask == "3":
        print("===You about to install Metasploit===")
        os.system("pkg install -y wget")
        os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
        os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
        os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
        os.system("cd /data/data/com.termux/files/home && bundle install")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Metasploit installed successfully :)")
        rmenu = input("[?] Start Metasploit? (y/n): ")
        if rmenu == "y":
            os.system("msfconsole")
        print("====================================")
        rmenu = input("[?] back to Selection? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
   
    
    elif ask == "4":
        print("===You about to install InstaHack===")
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pkg install -y nano")
        os.system("pip install requests")
        os.system("pip install beautifulsoup4")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
        print("====================================")
        print("[+] Instahack installed successfully :)")
        rmenu = input("[?] Start IntaHack? (y/n): ")
        if rmenu == "y":
            os.system("python hackinsta.py")
        print("====================================")
        rmenu = input("[?] back to Selection? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
        
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            print("====================================")
            print("[+] routersploit installed successfully :)")
            rmenu = input("[?] Start routersploit? (y/n): ")
        if rmenu == "y":
            os.system("python2 rsf.py")
            print("[+] Go to routersploit folder and type 'python2 rsf.py' to start.")
            print("====================================")
            rmenu = input("[?] back to Selection? (y/n): ")
            if rmenu == "y":
                menu()
            else:
                break
    elif ask == "00":
        os.system("clear")
        print("""
        ===Thank you For Using My Tool===
               ====#black poison#=====
                   ==Sh3yh4ck3r==
   _t_h_a_n_k_s___F_o_r___t_h_e___S_u_p_p_o_r_t_
        """)
        break
