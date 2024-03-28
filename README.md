# Dynamic-gaps
auto sizing gaps, with each window added to a workspace gaps are adjusted.
i made this script as for using my ultrawide monitor so things like single 
workspace's with a single application will render in a more readable way

![hippo](https://github.com/squid-slime/Dynamic-gaps/blob/main/ezgif-5-94de7735f5.gif)
![hippo](https://github.com/squid-slime/Dynamic-gaps/blob/main/2024-03-28%2018-08-46.gif)

--------------------------------------------------------------------------
download and install python-i3ipc
download/copy file ending in .py extention from ![here](https://github.com/squid-slime/Dynamic-gaps/blob/main/dynamic_gaps.py)
put the file somewhere safe, i use /home/user/.config/sway/scripts/file.py
add `exec python /path/to/script.py` to your sway config.
login into sway, profit.

--------------------------------------------------------------------------
customise by adding more windows or adjusting hoz, ver and inner values 
within the .py file.
also notifcations can be enabled within the script for depugging.
