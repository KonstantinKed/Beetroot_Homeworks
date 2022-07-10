# Task 3
# TV controller

class TVController:

    def __init__(self, channels, N = 0):
        self.channels = channels
        self.N = N


    def first_channel(self, N=0):
        self.N=N
        curr_chan = self.channels[self.N]
        print(curr_chan)


    def last_channel(self):
        curr_chan = self.channels[-1]
        print(curr_chan)

    def turn_channel(self, N):
        self.N = N-1
        print(self.channels[self.N])

    def next_channel(self):
        if 0 <= self.N < (len(self.channels)-1):
            self.N += 1
        else:
            self.N = 0
        curr_chan = self.channels[self.N]
        print(curr_chan)


    def previous_channel(self):
        if 0 <= self.N < (len(self.channels)-1):
            self.N -= 1
        else:
            self.N = (len(self.channels)-1)
        curr_chan = self.channels[self.N]
        print(curr_chan)
        return self.N

    def current_channel(self):
        curr_chan = self.channels[self.N]
        print(curr_chan)

    def is_exist(self, check):
        if isinstance(check, str):
            if check in self.channels:
                print("YES")
        elif isinstance(check, int):  # BTW isinstance(True, int) = True!!! But I use it here to practise isinstance...
            if 0 < check <= len((self.channels)):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")


channels = ["BBC", "Discovery", "TV1000"]

controller = TVController(channels)

controller.first_channel()   # BBC
controller.last_channel()   # TV1000
controller.turn_channel(1)   # BBC
controller.next_channel()     #Discovery
controller.previous_channel()  #BBC
controller.current_channel()   #BBC
controller.next_channel()   #Discovery
controller.next_channel()   #TV1000
controller.next_channel()   #BBC
print("--------")
controller.first_channel()  #BBC
controller.next_channel()  #Discovery
controller.previous_channel() #BBC
controller.is_exist(2.5)
controller.is_exist("BBC")

