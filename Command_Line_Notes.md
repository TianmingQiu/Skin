#Command line tips


- launch skin:
```
$ roscore
$ roslaunch tum_skin_tests_fiad tum_skin_driver_fiad_tsu.launch
```
after successful launch: ``clear offsets; store offsets``
```
$ roslaunch tum_skin_tests_fiad pub_left_arm.launch
```


- run NAO (* check the nao's ip on 10.0.29.1(wireless router))
```
$ roscore
$ roslaunch nao_bringup nao_full_py.launch nao_ip:=10.0.29.2 roscore_ip:=127.0.0.1
$ rosservice call /body_stiffness/enable "{}"
```

- simulation rviz
```
$ rosrun tf static_transform_publisher 0 0 0 0 0 0 1 map my_frame 10
$ rosrun rviz rviz
```

- Transfer package to my laptop:
	1. Cannot locate node in xxxx package, please add CMAKE_PREFIX_PATH  
	There are some libraries in '/opt/ros/indigo/', such as 'lib', 'share' and 'include'  
	'tumskin', 'tumtools'  
	copy against permission: 


	$ sudo cp -r home/ming/Desktop/tum_skin_driver_fiad/ opt/ros/indigo/include/ 


	access against permission: 


	$ sudo chmod -R 777 tum_skin_msgs_fiad/


	2. $ rospack find tum_skin_msgs_fiad
	3. python cannot import naoqi:


	$ export PYTHONPATH=/home/ming/naoqi/naoqi-sdk-2.1.4.13-linux64/lib:${PYTHONPATH}
	$ echo 'export PYTHONPATH=~/naoqi/pynaoqi-python2.7-2.1.2.17-linux64:$PYTHONPATH' >> ~/.bashrc



- check IP port
```
	$ nmap --iflist
	$ sudo netdiscover -r 192.168.0.0/24 -i eth1
```


