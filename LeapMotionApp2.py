import Leap, sys, thread, time
from Leap import CircleGesture,KeyTapGesture, ScreenTapGesture, SwipeGesture

class LeapMotionListener(Leap.Listener):
	finger_names = ['Thumb','Index','Middle','Ring','Pinky']
	bone_names = ['Metacarpol', 'Proximal', 'Intermediate', 'Distal']
	state_names =['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

	def on_init(self, controller):
		print "Initialized"

	def on_connect(self,controller):
		print "Motion Sensor Connected"
		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
		controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

	def on_disconnect(self, controller):
		print "Motion Sensor Disconnected"

	def on_exit(self, controller):
		print "Exited"

	def on_frame(self, controller):
		frame = controller.frame()
		for hand in frame.hands:
			handtype = "Left Hand" if hand.is_left else "Right Hand"
			print handtype + "Hand ID:" + str(hand.id)+ " Palm Position" + str(hand.palm_position)
			normal = hand.palm_normal
			direction = hand.direction

			print "pitch: "+str(direction.pitch + Leap.RAD_TO_DEG)+  " Roll: "+str(normal.roll +Leap.RAD_TO_DEG)+ " Yaw: "+str(direction.yaw + Leap.RAD_TO_DEG)


def main():
	listener = LeapMotionListener()
	controller = Leap.Controller()
	controller.add_listener(listener)
	print "Press enter to exit"
	try:
		sys.stdin.readline()
	except keyboardInterrupt:
		pass
	finally:
		controller.remove_listener(listener)

if __name__ == "__main__":
	main()