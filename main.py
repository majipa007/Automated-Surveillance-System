import surveilance as sv

print("Starting the main function")
detector = sv.Object_Detection(capture_index=0)
print("Class Created")
detector()
print("Process Completed")
