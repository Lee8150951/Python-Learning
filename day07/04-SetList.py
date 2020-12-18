# P130练习
# 练习8-9
def show_messages(messages_list):
    for mes in messages_list:
        print(mes)
messages = ['China', 'Korea', 'Japan']
show_messages(messages)
# 练习8-10
messages = ['China', 'Korea', 'Japan']
sent_messages = []
def send_messages(message):
    print(message)
    sent_messages.append(message)

def get_messages(messages_list):
    while messages_list:
        message = messages_list.pop()
        send_messages(message)
get_messages(messages)
print(sent_messages)
print(messages)
# 练习8-11 略