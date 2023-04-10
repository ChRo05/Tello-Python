import tello_single
from tello_control_ui import TelloUI


def main():

    drone = tello_single.Tello('', 8889)  
    vplayer = TelloUI(drone,"./img/")
    
	# start the Tkinter mainloop
    vplayer.root.mainloop() 

if __name__ == "__main__":
    main()
