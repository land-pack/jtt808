from shortcuts.template import render
from app.split import PositionSplit
from app.split import TerminalAttributeSplit
from app.admin import ConvertBaseRegister

from app.models import PositionTable
from app.models import session
from app.models import Base, engine

Base.metadata.create_all(engine)


# You can write your logic here, and it's you place!
# You can do save & custom response message if you want!
# And you also can ignore all request just like the position view!
def register(terminal_request):
    """
    :param terminal_request: original data format to Dicts from terminal!
    :return: a render which a tuple factory
    you should know what you are doing and which field you need!
    """
    template = 'client_msg_id|client_msg_attr|client_dev_id|client_msg_product|client_content'
    return render(terminal_request, template)


def auth(terminal_request):
    msg_content = 'client_msg_product|client_msg_id|sys_ok'
    template = 'ser_com_rsp|sys_fixed_msg_attr|client_dev_id|sys_product|' + msg_content
    print 'terminal_request', terminal_request
    return render(terminal_request, template)


def position(terminal_request):
    # Load the field which your need to save!
    content = terminal_request['client_content']
    # Do some Resolution according your need!
    position_instance = PositionSplit(content)
    # Get the attribute of the PositionSplit and you'll got a Dict type
    result_dict = position_instance.result
    # Convert the client request data to the new type if you need!
    ConvertBaseRegister(result_dict)
    # Get the data with Dict format!
    position_info = position_instance.result
    print 'position_info', position_info
    # Send to ORM & Save it to Data Base!
    p_i = PositionTable(**position_info)
    session.add(p_i)
    session.commit()


def get_ter_info(terminal_request):
    template = 'get_ter_info|sys_fixed_msg_attr2|client_dev_id|sys_product|'
    print 'terminal_request', terminal_request
    return render(terminal_request, template)


def terminal_info(terminal_request):
    print 'Hey here is my terminal setting', terminal_request


def get_ter_attr(terminal_request):
    msg_content = ''  # Empty message content for checking terminal attribute
    template = 'get_ter_attr|sys_fixed_msg_attr2|client_dev_id|sys_product|'
    return render(terminal_request, template)


def terminal_attr(terminal_request):
    # Just print the terminal response for now!
    print "Hey! It's terminal attribute", terminal_request
    # Load the field which your need to save!
    content = terminal_request['client_content']
    ter_attr_instance = TerminalAttributeSplit(content)
    # Get the attribute of the PositionSplit and you'll got a Dict type
    result_dict = ter_attr_instance.result
    print 'result_dict', result_dict


if __name__ == '__main__':
    """
    The below sample dicts just for test the register!
    """
    request = {'msg_id': (1, 2), 'msg_attr': (0, 2), 'dev_id': (153, 17, 152, 64, 130, 104), 't_product': (0, 1),
               'content': (81, 82), 'crc': (185,)}
    example = auth(request)
    print 'example      :', example
