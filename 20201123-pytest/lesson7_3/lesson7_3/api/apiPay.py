import setting
from tools.logger import GetLogger
logger=GetLogger().get_logger()
class ApiPay:
    def __init__(self):
        logger.info('即将开始获取支付订单接口的url')
        self.url = setting.JUMP_URL
        logger.info('支付订单接口的url是{}'.format(self.url))
    def pay(self,session):

        # 对302接口禁止重定向 allow_redirects=False
        logger.info('开始发送支付订单接口的请求')
        resp = session.get(self.url,allow_redirects=False)
        # 提取响应头中的location,对location后面的地址发起请求，
        # 然后获取响应，以便testcase中做断言
        logger.info('获取到支付订单的接口响应是{}'.format(resp.headers))
        logger.info('开始获取支付订单接口的响应头信息中的locationlocation{}，并对其发起请求'.format(resp.headers['location']))
        resp_pay = session.get(resp.headers['location'])
        logger.info('获取支付订单接口location请求的响应：{}'.format(resp_pay.text))
        return resp_pay
