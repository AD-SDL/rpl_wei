import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from std_msgs.msg import String

from wei_services.srv import WeiActions
from std_msgs.msg import String


from pf400_module_services.srv import MoveJ 


class weiExecNode(Node):
    def __init__(self):
        super().__init__('weiExecNode')


                                                                
    def send_move(self, posA, posB):
        pf400Client = self.create_client(MoveJ, 'pf400_moveJ')
        while not pf400Client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('pf400 service not available, waiting again...')
        pf400Req = MoveJ.Request()
        pf400Req.joint_positions = posA + posB

        future = pf400Client.call_async(pf400Req)
        rclpy.spin_until_future_complete(self, future)  

    def send_wei_command(self,service,command):
        weiExecutor = self.create_client(WeiActions,service)
        while not weiExecutor.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(service + ' service not available, waiting again...')
        weiReq = WeiActions.Request()
        weiReq.action_request(command)

        future = weiExecutor.call_async(weiReq)
        rclpy.spin_until_future_complete(self, future)  


