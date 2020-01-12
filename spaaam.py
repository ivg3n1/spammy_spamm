from time import sleep
import keyboard

txt = input("insert txt-->")

coin = [0,1]

while True:
	sleep(0.1)
	if keyboard.is_pressed("]"):
		coin[0],coin[1] = coin[1],coin[0]
		print("pressed")
	if keyboard.is_pressed("["):
		txt = input("input new txt -- >")

	if coin[0] == 1:
		keyboard.write(txt)
		keyboard.press_and_release("enter")
	else:
		pass
 
