import rclpy
from wei_executor.weiExecutorNode import weiExecNode
peelerPos = [264.584, -29.413,	284.376, 372.338, 0.0, 651.621]
sealerPos = [231.788, -27.154, 313.011, 342.317, 0.0, 683.702]
cyclops_ext = [262.550, 20.608, 119.290, 662.570, 0.0, 574.367]
rclpy.init()
minimal_client = weiExecNode()
rclpy.spin(minimal_client)
minimal_client.send_move(cyclops_ext,sealerPos)
minimal_client.send_move(sealerPos,peelerPos)
minimal_client.send_move(cyclops_ext,sealerPos)
