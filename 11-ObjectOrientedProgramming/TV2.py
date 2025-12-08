# tv_show.py file
# main program

import TV

def main():
   # object creation
   televizor = TV.TV()
   televizor.show_status()
   televizor.turn_on()
   televizor.show_status()
   televizor.turn_off()
   televizor.show_status()
   televizor.turn_on()
   televizor.set_channel(5)
   televizor.show_status()
   # object usage
   

if __name__ == "__main__":
   main() 