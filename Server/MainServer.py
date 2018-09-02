import KeybaordController
import ServerSocket
import GUI

# Create new threads
thread1 = GUI(1, "Thread-1", 1)
thread2 = GUI(2, "Thread-2", 2)
# Start new Threads
thread1.start()
thread2.start()