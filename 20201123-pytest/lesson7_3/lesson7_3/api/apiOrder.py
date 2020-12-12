import setting
from setting import IP, HEADERS
from tools.logger import GetLogger
logger=GetLogger().get_logger()

class ApiOrder:
    def __init__(self):
        logger.info('开始获取订单提交接口URL')
        self.url = IP + '/mtx/index.php?s=/index/buy/add.html'
        logger.info('订单提交接口的URL是：{}'.format(self.url))


    def order(self,session):
        '''
        发起下订单的请求
        :param session:
        :return:
        '''
        logger.info('开始获取订单提交接口的data')
        data = {
            'goods_id': 1,
            'stock': 1,
            'buy_type': 'goods',
            'address_id': 1290,
            'payment_id': 1,
            'spec': '',

        }
        logger.info('开始发送订单提交请求，请求data是{}，headers是{}'.format(data,HEADERS))
        resp_order = session.post(self.url,data=data,headers=HEADERS)
        logger.info('获取订单提交响应是{}'.format(resp_order.json()))
        # 产生数据->并把数据放到setting当中(注意)
        setting.JUMP_URL = resp_order.json().get('data').get('jump_url')
        logger.info('获取订单提交响应的JUMP_URL是{}'.format(setting.JUMP_URL))
        return resp_order
