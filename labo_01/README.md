```
sudo apt-get update
sudo apt-get install sense-hat
sudo reboot
```


Run this command in a terminal window;
Code: Select all

sudo nano /boot/config.txt
Scroll to the bottom of the file and add this line;
Code: Select all

dtoverlay=rpi-sense
Then press Ctrl - O followed by Enter to Save, and Ctrl - X to quit.
Then do a reboot. See if that helps.
