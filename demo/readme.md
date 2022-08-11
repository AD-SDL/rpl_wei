# Installation 

1. Install [OT2_Driver](https://github.com/KPHippe/ot2_driver.git)

    ```
    git clone https://github.com/KPHippe/ot2_driver.git 
    cd ot2_driver 
    pip install -r requirements.txt 
    pip install -e . 
    ```
1. Install [RPL_WEI](https://github.com/AD-SDL/rpl_wei)
    ```
    # Assuming you have already cloned 
    cd rpl_wei 
    pip insatll -r requirements/requirements.txt
    pip install -e . 
    ```

# Running 
1. Make sure to change hardcoded paths in `workflow_files/demo_wf.yaml` to follow your directory layout. (You can use relative paths if you know where you are going to execute the script, but absolute paths might be better)
1. Run `python demo_client.py -wc workflow_files/demo_wf.yaml`