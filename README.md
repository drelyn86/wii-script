# Wii-Script

## About This Software

The main goal of this project was to develop an easy-to-configure inteface for the Nintendo Wii remote control on Linux-based bluetooth-enabled PCs. The script requires few dependencies and only requires modifying one file to configure.

### Dependencies

This software requires the following software dependencies:

- A GNU/Linux operating system with a loaded uinput module and running bluetooth daemon.
- Python 2.7
- cwiid >= 0.6: https://github.com/abstrakraft/cwiid
- python2-uinput: http://tjjr.fi/sw/python-uinput/

Additionally, the following hardware dependencies need to be met:

- A bluetooth device connected to your PC.
- Wiimote
- Optional:
    + Nintendo Wii sensor bar (needed for infrared functionality)
    + Nunchuk or other Wiimote extensions

### Applications

Developed primarily for personal use, there are only a couple existing configurations right now, though it is trivial to add more.

#### super mario

This configuration was built for joystick emulation of side-scrolling games.

#### l4d2

This configuration was built for the Left 4 Dead 2 game by Valve. As of right now, the game needs to run in Wine, though a Linux release should be coming very soon, and there is reason to believe this software will work without modification once that is released.

To use this configuration, you would need to copy all of the files in the l4d2 config directory to the Steam/SteamApps/common/left\ 4\ dead\ 2/left4dead2/cfg directory. Use of "autoexec.cfg" should be used at your own discretion.

