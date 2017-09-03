# CMP 规划思路

## 1. 背景
CMP 全称 "Connection Management Platform", 属于爱立信的 SLP 产品线中的
关键平台, 所有接入SLP产品线应用的设备统一由 CMP 平台进行连接管理(Connection Management), 
属性管理(MetaData Management),设备能力管理(Device Ability Management)和
设备状态管理(Device Status Management), CMP 中的事件中心(Event Hub)负责
收集 Device 上发的事件.

## 2. 概念解释

### 2.1 设备



后端应用可以通过在 Event Hub 中注册监听某类事件, 当某类
事件到达后自动触发应用启动预设行为.

Eg1.智能家居场景中, 当门被打开后, 智能家居应用
通过在 Event Hub 中监听"门打开"事件触发开灯, 开窗帘等行为. 

Eg2. 智慧农业场景中, 当某个湿度传感器侦测到湿度过低(土壤干燥), 上发该事件到
Event Hub, 在 Event Hub 中注册监听该事件的智慧农业应用监听到该事件后自动触发
预配置行为.

