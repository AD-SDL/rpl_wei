import subprocess
from pathlib import Path
from argparse import ArgumentParser

from rpl_wei.wei_client_base import WEI
from rpl_wei.data_classes import Module

from ot2_driver.ot2_driver_http import OT2_Driver, OT2_Config


def get_module(module_name: str, wei: WEI) -> Module:
    for mod in wei.workcell.modules:
        if mod.name == module_name:
            return mod


def main(args):
    wei = WEI(args.workflow_config)

    for step in wei.flowdef:
        req_mod = step.module
        module_device = get_module(req_mod, wei)
        ot2 = OT2_Driver(OT2_Config(ip=module_device.config["ip"]))
        for action in step.actions:
            # compile protocol
            protocol_config_path = action.args["config_path"]
            protocol_file_path, resource_file_path = ot2.compile_protocol(protocol_config_path, args.resource_file)

            if not args.simulate:
                # Transfer to OT2
                protocol_id, run_id = ot2.transfer(protocol_file_path)
                print(run_id)
                # Execute
                execute_resp = ot2.execute(run_id)
                print(execute_resp)
            else:
                cmd = f"opentrons_simulate {protocol_file_path}"
                subprocess.run(cmd.split())


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-wc", "--workflow_config", help="Workflow config file", type=Path)
    parser.add_argument(
        "-rf",
        "--resource_file",
        help="OT2 resource file, optional, if provided will track given current state of robot, else will be created with default values ",
        type=Path,
    )
    parser.add_argument("-s", "--simulate", help="Whether or not to simulate the ot2 run", action="store_true")

    args = parser.parse_args()
    main(args)
