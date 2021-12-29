"""
Main loop for observer
"""
from subscriber import Subscriber
from publisher import Publisher

if __name__ == '__main__':
    pub = Publisher()
    sub_1 = Subscriber(0)
    sub_2 = Subscriber(1)
    sub_3 = Subscriber(2)

    pub.subscribe(sub_1)
    pub.send_msg('msg_1')

    pub.subscribe(sub_2)
    pub.send_msg('msg_2')

    pub.subscribe(sub_3)
    pub.send_msg('msg_3')
    pub.unsubscribe(sub_1)
    pub.unsubscribe(sub_2)
    pub.unsubscribe(sub_3)

    pub.send_msg()
