class Event: 
    def __init__(self, name): 
        self.name = name 

    def __str__(self): 
        return self.name 

class Widget: 
    def __init__(self, parent=None): 
        self.parent = parent 

    def handle(self, event): 
        handler = 'handle_{event}'.format(event=event) 
        if hasattr(self, handler): 
            method = getattr(self, handler) 
            method(event) 
        elif self.parent is not None: 
            self.parent.handle(event) 
        elif hasattr(self, 'handle_default'): 
            self.handle_default(event) 

class MainWindow(Widget): 
    def handle_close(self, event): 
        print('MainWindow: {event}'.format(event=event))

    def handle_default(self, event): 
        print('MainWindow Default: {event}'.format(event=event))

class SendDialog(Widget): 
    def handle_paint(self, event): 
        print('SendDialog: {event}'.format(event=event))

class MsgText(Widget): 
    def handle_down(self, event): 
        print('MsgText: {event}'.format(event=event)) 

def main(): 
    mw = MainWindow() 
    sd = SendDialog(mw) 
    msg = MsgText(sd) 

    for e in ('down', 'paint', 'unhandled', 'close'): 
        evt = Event(e) 
        print('Sending event -{evt}- to MainWindow'.format(evt=evt))
        mw.handle(evt) 
        print('Sending event -{evt}- to SendDialog'.format(evt=evt))
        sd.handle(evt) 
        print('Sending event -{evt}- to MsgText'.format(evt=evt))
        msg.handle(evt) 

if __name__ == '__main__': 
    main()
