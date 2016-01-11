from shortcuts.template import render
from app.split import PositionSplit
from app.admin import ConvertBaseRegister

from sqlalchemy.orm import sessionmaker
from app.models import PositionTable
from app.models import engine

Base.metadata.bind = engine
DBSession = sessionmaker
session = DBSession()


# You can write your logic here, and it's you place!
# You can do save & custom response message if you want!
# And you also can ignore all request just like the position view!
def register(val):
    """
    :param val: original data format to Dicts from terminal!
    :return: a render which a tuple factory
    you should know what you are doing and which field you need!
    """
    template = 'client_msg_id|client_msg_attr|client_dev_id|client_msg_product|client_content'
    return render(val, template)


def auth(val):
    msg_content = 'client_msg_product|client_msg_id|sys_ok'
    template = 'ser_com_rsp|sys_fixed_msg_attr|client_dev_id|sys_product|' + msg_content
    return render(val, template)


def position(val):
    content = val['client_content']
    position_instance = PositionSplit(content)  # Split the position context if the protocol !
    result_dict = position_instance.result  # you got dict type
    ConvertBaseRegister(result_dict)  # Convert the client request data to the new data!
    # Save to db if you want! here you going!
    for item in position_instance.result:
        print '%s           : %s' % (item, result_dict[item])
    position_info = position_instance.result
    p_i = PositionTable(**position_info)
    session.add(p_i)
    session.commit()
    # session.close()


if __name__ == '__main__':
    """
    The below sample dicts just for test the register!
    """
    request = {'msg_id': (1, 2), 'msg_attr': (0, 2), 'dev_id': (153, 17, 152, 64, 130, 104), 't_product': (0, 1),
               'content': (81, 82), 'crc': (185,)}
    example = auth(request)
    print 'example      :', example
