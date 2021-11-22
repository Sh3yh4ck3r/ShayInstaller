
clear
trap 'printf "\n";stop;exit 1' 2


dependencies() {

command -v php > /dev/null 2>&1 || { echo >&2 "I require php but it's not installed. Install it. Aborting."; exit 1; }
command -v curl > /dev/null 2>&1 || { echo >&2 "I require curl but it's not installed. Install it. Aborting."; exit 1; }

}

menu() {

printf "  [\e[0m\e[1;77m01\e[0m\e[1;92m]\e[0m\e[1;93m Nmap\e[0m       \e[1
    \e[1"
printf "92m[\e[0m\e[1;77m02\e[0m\e[1;92m]\e[0m\e[1;93m Hydra\e[0m       \e[1
    \e[1"
printf "92m[\e[0m\e[1;77m03\e[0m\e[1;92m]\e[0m\e[1;93m Metasploit\e[0m       \e[1
    \e[1" 
printf "92m[\e[0m\e[1;78m04\e[0m\e[1;92m]\e[0m\e[1;93m Routersploit\e[0m       \e[1
    \e[1"
printf "92m[\e[0m\e[1;78m05\e[0m\e[1;92m]\e[0m\e[1;93m ShellPhish\e[0m       \e[1
    \e[1"
printf "92m[\e[0m\e[1;78m06\e[0m\e[1;92m]\e[0m\e[1;93m Weeman\e[0m       \e[1
    \e[1"
printf "92m[\e[0m\e[1;78m06\e[0m\e[1;92m]\e[0m\e[1;93m Ubuntu-in-termux\e[0m       \e[1
    \e[1"
read -p $'\n\e[1;92m[\e[0m\e[1;77m~\e[0m\e[1;92m] Choose an option: \e[0m\en' option


if [[ $option == 1 || $option == 01 ]]; then
     printf"=======Nmap Install======="
        sleep 2
pkg update -y 
pkg install -y nmap 
python Shay-installer.py

elif [[ $option == 2 || $option == 02 ]]; then
 printf "========Hydra Install=========="
         sleep 2
pkg update -y
pkg install -y hydra

elif [[ $option == 3 || $option == 03 ]]; then
 printf " =========Metasploit Install========="
  sleep 2
pkg install -y wget
wget https://Auxilus.github.io/metasploit.sh
bash metasploit.sh
metasploit-framework
gem install bundle --pre
bundle config build.nokogiri --use-system-libraries
bundle install
elif [[ $option == 4 || $option == 04 ]]; then
printf " =========Insta-Hack Install========="
  sleep 2
pkg update -y
pkg install -y git
pkg install -y python
pkg install -y nano
pip install requests
pip install beautifulsoup4
git clone https://github.com/avramit/instahack.git
elif [[ $option == 5 || $option == 05 ]]; then
printf " =========ShellPhish Install========"
 sleep 2
pkg update -y
pkg install -y git
pkg install -y python
git clone https://github.com/thelinuxchoice/shellphish
cd shellphish
bash shellphish.sh
elif [[ $option == 6 || $option == 06 ]]; then
printf " ========Weeman Install========"
 sleep 2 
pkg update -y
pkg install -y python2
pkg install -y git
git clone https://github.com/evait-security/weeman.git
cd weeman
chmod +x weeman.py
elif [[ $option == 7 || $option == 07 ]]; then
printf " ========Termux-ubuntu=========="
 sleep 2 
apt-get update && apt-get upgrade -y
apt-get install wget -y
apt-get install proot -y
apt-get install git -y
cd
git clone https://github.com/MFDGaming/ubuntu-in-termux.git
cd ubuntu-in-termux
chmod +x ubuntu.sh
./ubuntu.sh -y
./startubuntu.sh

elif [[ $option == 00 ]]; then
exit 1

else
printf "\e[1;93m [!] Invalid option!\e[0m\n"
sleep 1
clear
menu
fi
}

banner() {
    printf "
    
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
"
    }
banners() {
    printf "
    =======Special thanks to: 
    =======The_Linus_Choice for : shellphish
    =======We are in this together.
================================================
-changing the credits of a codedoesn't make you coder- The_Linus_Choice
================================================
    =======And thanks to all the othere devs
    
    "
sleep 3 
  clear
}
banners
banner
dependencies
menu

