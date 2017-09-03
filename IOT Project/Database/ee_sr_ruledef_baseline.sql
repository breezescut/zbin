/*
Navicat MySQL Data Transfer

Source Server         : FET Demo
Source Server Version : 50633
Source Host           : 47.93.80.117:3306
Source Database       : event

Target Server Type    : MYSQL
Target Server Version : 50633
File Encoding         : 65001

Date: 2017-03-27 19:18:40
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for ee_sr_ruledef
-- ----------------------------
DROP TABLE IF EXISTS `ee_sr_ruledef`;
CREATE TABLE `ee_sr_ruledef` (
  `ruleID` varchar(64) NOT NULL COMMENT '校验类型（如：SubsStatus 判断用户状态，IsBlack 判断黑名单，GetMoney 判断欠费，SubsBrand 判断用户品牌，SubsProduct 判断用户品牌，SubsStopKey 判断用户停机锁）等等。用户在受理业务前需要取该属性值与sa_db_recruleslimit_validvalue表中的validvalue字段做比较，检查是否允许受理该种类型的业务',
  `description` varchar(200) DEFAULT NULL,
  `rules` varchar(20000) DEFAULT NULL COMMENT '规则代码',
  `STATUS` int(11) DEFAULT NULL COMMENT '0：无效，1：有效',
  `statusDate` date DEFAULT NULL,
  `log_oper_id` varchar(16) DEFAULT NULL,
  `log_oper_Date` date DEFAULT NULL,
  `log_oper_type` varchar(32) DEFAULT NULL,
  `ruleType` int(11) DEFAULT NULL COMMENT '业务规则检查\n            取数规则\n            脚本流程\n            业务规则检查服务',
  PRIMARY KEY (`ruleID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ee_sr_ruledef
-- ----------------------------
INSERT INTO `ee_sr_ruledef` VALUES ('0-test1', '事件脚本', 'if (_M.get(\'retCode\').equals(\'ERROR\')) println(\'ERROR...\');var result = _M.get(\'orderid\') * 100 + _M.get(\'oprid\') * 10; println(\'msg = \'+ \'test\');println(\'eval = \'+ result); ', '1', '2016-08-04', 'ee_admin', '2016-08-08', '1', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('0-test2', '测试脚本2', 'if (_M.get(\'retCode\').equals(\'ERROR\')) println(\'ERROR...\');\r\nsetTimeout(0,1000);\r\nvar result = orderid * 100 + oprid * 10; println(\'msg = \'+ \'test\');println(\'eval = \'+ result); ', '1', '2016-08-04', 'jinbo', '2016-08-08', '1', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('1-dscript1', '设备测试脚本', '_D.operate(0,4,1,_M);_D.operate(0,4,3,_M);', '1', '2016-08-04', 'ee_admin', '2016-08-08', '1', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('bedroom.bulb.blue', '变蓝', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'0\');\r\n_M.put(\'green\',\'0\');\r\n_M.put(\'blue\',\'255\');\r\n_D.operate(0,158,96,_M);', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('bedroom.bulb.close', '关灯', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'0\');\r\n_M.put(\'green\',\'0\');\r\n_M.put(\'blue\',\'255\');\r\n_D.operate(0,1,223,_M);', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('bedroom.bulb.cyan', '变青', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'0\');\r\n_M.put(\'green\',\'127\');\r\n_M.put(\'blue\',\'255\');\r\n_D.operate(0,158,96,_M);', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('bedroom.bulb.green', '变绿', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'0\');\r\n_M.put(\'green\',\'255\');\r\n_M.put(\'blue\',\'0\');\r\n_D.operate(0,158,96,_M);\r\n', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('bedroom.bulb.open', '开灯', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'100\');\r\n_M.put(\'green\',\'100\');\r\n_M.put(\'blue\',\'100\');\r\n_D.operate(0,1,223,_M);', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('bedroom.bulb.orange', '变橙', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'255\');\r\n_M.put(\'green\',\'165\');\r\n_M.put(\'blue\',\'0\');\r\n_D.operate(0,158,96,_M);', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('bedroom.bulb.purple', '变紫', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'139\');\r\n_M.put(\'green\',\'0\');\r\n_M.put(\'blue\',\'255\');\r\n_D.operate(0,158,96,_M);', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('bedroom.bulb.red', '变红', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'255\');\r\n_M.put(\'green\',\'0\');\r\n_M.put(\'blue\',\'0\');\r\n_D.operate(0,158,96,_M);', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('bedroom.bulb.yellow', '变黄', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'255\');\r\n_M.put(\'green\',\'255\');\r\n_M.put(\'blue\',\'0\');\r\n_D.operate(0,158,96,_M);', '1', '2016-09-08', 'SceneEvent', '2016-09-08', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('bulb.bule', '变蓝', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'0\');\r\n_M.put(\'green\',\'0\');\r\n_M.put(\'blue\',\'255\');\r\n_D.operate(0,158,96,_M);\r\n_D.operate(0,158,169,_M);\r\n', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('bulb.close', '关灯', '_M.put(\'on_off\',\'0\');\r\n_D.operate(0,1,229,_M);\r\n_D.operate(0,1,223,_M);', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('bulb.cyan', '变青', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'0\');\r\n_M.put(\'green\',\'127\');\r\n_M.put(\'blue\',\'255\');\r\n_D.operate(0,158,96,_M);\r\n_D.operate(0,158,169,_M);\r\n', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('bulb.green', '变绿', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'0\');\r\n_M.put(\'green\',\'255\');\r\n_M.put(\'blue\',\'0\');\r\n_D.operate(0,158,96,_M);\r\n_D.operate(0,158,169,_M);\r\n', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('bulb.open', '开灯', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'100\');\r\n_M.put(\'green\',\'100\');\r\n_M.put(\'blue\',\'100\');\r\n_D.operate(0,1,229,_M);\r\n_D.operate(0,1,223,_M);', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('bulb.orange', '变橙', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'255\');\r\n_M.put(\'green\',\'165\');\r\n_M.put(\'blue\',\'0\');\r\n_D.operate(0,158,96,_M);\r\n_D.operate(0,158,169,_M);\r\n', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('bulb.purple', '变紫', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'139\');\r\n_M.put(\'green\',\'0\');\r\n_M.put(\'blue\',\'255\');\r\n_D.operate(0,158,96,_M);\r\n_D.operate(0,158,169,_M);\r\n', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('bulb.red', '变红', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'255\');\r\n_M.put(\'green\',\'0\');\r\n_M.put(\'blue\',\'0\');\r\n_D.operate(0,158,96,_M);\r\n_D.operate(0,158,169,_M);\r\n', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('bulb.yellow', '变黄', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'255\');\r\n_M.put(\'green\',\'255\');\r\n_M.put(\'blue\',\'0\');\r\n_D.operate(0,158,96,_M);\r\n_D.operate(0,158,169,_M);\r\n', '1', '2016-09-08', 'SceneEvent', '2016-09-08', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('curtian.close', '关窗帘', '_M.put(\'open_degree\',\'255\');\r\n_D.operate(0,1,236,_M);\r\n', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('curtian.open', '开窗帘', '_M.put(\'open_degree\',\'50\');\r\n_D.operate(0,1,236,_M);\r\n', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('fan.close', '关风扇', '_M.put(\'on_off\',\'0\');\r\n_D.operate(0,158,91,_M);', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('fan.open', '开风扇', '_M.put(\'on_off\',\'1\');\r\n_D.operate(0,158,91,_M);', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('fet_chat', '你在忙啥', '_M.put(\'robot_msg\',\'现在不忙，需要帮你什么吗\');\r\n_D.operate(0,1, 221,_M);', '2', '2016-08-05', 'jinbo', '2016-08-09', '1', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('fet_cold', '房间有点冷', 'var win=235; //不知道窗户id多少，乱写的\r\nvar fan=227;\r\nvar botId = _M.get(\'botId\');\r\nif (botId==null) botId=221;\r\n\r\n_D.deviceInfo(fan,_M);\r\nvar fan_onoff = _M.get(\'on_off\');\r\n//println(\'fan_onoff=\'+ fan_onoff);\r\n\r\n_D.deviceInfo(win,_M);\r\nvar on_off_win = _M.get(\'window_optype\');\r\n//println(\'window onoff= \'+ on_off_win);\r\nif (on_off_win==null) on_off_win=1;\r\n\r\nif (fan_onoff==1 && on_off_win==2){\r\n	_M.put(\'robot_msg\',\'我帮你关窗户及风扇\');\r\n	_M.put(\'robot_cmd\',\'108\');\r\n	_D.operate(0,232, botId,_M);\r\n	_D.delay(2000);\r\n\r\n  _M.put(\'window_optype\',\'3\');\r\n	_D.operate(0,232, win,_M);\r\n  _D.delay(2000);\r\n\r\n  _M.put(\'on_off\',\'0\');\r\n	_D.operate(0,232, fan,_M);\r\n  _D.delay(2000);\r\n  //println(\'turn off fan & win\');\r\n} else if(fan_onoff==1){\r\n	_M.put(\'robot_msg\',\'我帮关风扇\');\r\n	_M.put(\'robot_cmd\',\'108\');\r\n	_D.operate(0,232, botId,_M);\r\n  _D.delay(2000);\r\n\r\n  _M.put(\'on_off\',\'0\');\r\n	_D.operate(0,232, fan,_M);\r\n  _D.delay(2000);\r\n  //println(\'turn off fan\');\r\n} else if (on_off_win==2){\r\n	_M.put(\'robot_msg\',\'我帮你关窗户\');\r\n	_M.put(\'robot_cmd\',\'108\');\r\n	_D.operate(0,232, botId,_M);\r\n  _D.delay(2000);\r\n\r\n  _M.put(\'window_optype\',\'3\');\r\n	_D.operate(0,232, win,_M);\r\n  _D.delay(2000);\r\n  //println(\'turn off win\');\r\n} else{\r\n	_M.put(\'robot_msg\',\'窗户和风扇都已经关了，主人，请保重身体，多穿点衣服\');\r\n	_M.put(\'robot_cmd\',\'108\');\r\n	_D.operate(0,232, botId,_M);\r\n  _D.delay(2000);\r\n  //println(\'turn off nothing\');\r\n}', '4', '2016-08-07', 'jinbo', '2016-08-11', '1', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('fet_cold_close.windowAndfan', '有点冷关风扇和窗', 'var win=235; //不知道窗户id多少，乱写的\r\nvar fan=227;\r\nvar botId = _M.get(\'botId\');\r\nif (botId==null) botId=221;\r\n\r\n_D.deviceInfo(fan,_M);\r\nvar fan_onoff = _M.get(\'on_off\');\r\n\r\n_D.deviceInfo(win,_M);\r\nvar on_off_win = _M.get(\'window_optype\');\r\n\r\nif (on_off_win==null) on_off_win=2;\r\n\r\nif (on_off_win==2){\r\n	_M.put(\'robot_msg\',\'那我帮你关窗户\');\r\n	_D.operate(0,232, botId,_M);\r\n	_D.delay(2000);	\r\n\r\n  _M.put(\'robot_msg\',\'\');\r\n	_M.put(\'robot_cmd\',\'108\');\r\n	_D.operate(0,232, botId,_M);\r\n	_D.delay(2000);\r\n\r\n  _M.put(\'robot_cmd\',\'\');\r\n	_M.put(\'window_optype\',\'3\');\r\n	_D.operate(0,232, win,_M);\r\n	_D.delay(2000);\r\n}else if(on_off_win==3){\r\n	_M.put(\'robot_msg\',\'窗户已经关好了啦,那要帮你关风扇吗？\');\r\n	_D.operate(0,232, botId,_M);\r\n	_D.delay(2000);\r\n\r\n  _M.put(\'robot_msg\',\'\');\r\n	_M.put(\'robot_cmd\',\'8\');\r\n	_D.operate(0,232, botId,_M);\r\n	_D.delay(2000);\r\n}else if(fan_onoff==1){\r\n	_M.put(\'robot_msg\',\'没问题,我帮你关电扇\');\r\n	_D.operate(0,232, botId,_M);\r\n  _D.delay(2000);\r\n\r\n  _M.put(\'robot_msg\',\'\');\r\n	_M.put(\'robot_cmd\',\'108\');\r\n	_D.operate(0,232, botId,_M);\r\n	_D.delay(2000);\r\n\r\n  _M.put(\'robot_cmd\',\'\');\r\n  _M.put(\'on_off\',\'0\');\r\n	_D.operate(0,232, fan,_M);\r\n  _D.delay(2000);\r\n}', '1', '2017-03-07', 'SceneEvent', '2017-03-07', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('fet_cold_colse.fan', '不好意思，那麻烦你帮关电扇吧', 'var win=235; //不知道窗户id多少，乱写的\r\nvar fan=227;\r\nvar botId = _M.get(\'botId\');\r\nif (botId==null) botId=221;\r\n\r\n_D.deviceInfo(fan,_M);\r\nvar fan_onoff = _M.get(\'on_off\');\r\n\r\n if(fan_onoff==1){\r\n   _M.put(\'robot_msg\',\'没问题,我帮你关电扇\');\r\n	_D.operate(0,232, botId,_M);\r\n  _D.delay(2000);\r\n\r\n  _M.put(\'robot_msg\',\'\');\r\n	_M.put(\'robot_cmd\',\'108\');\r\n	_D.operate(0,232, botId,_M);\r\n	_D.delay(2000);\r\n\r\n  _M.put(\'robot_cmd\',\'\');\r\n  _M.put(\'on_off\',\'0\');\r\n	_D.operate(0,232, fan,_M);\r\n  _D.delay(2000);\r\n}', '1', '2017-03-07', 'SceneEvent', '2017-03-07', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('fet_dizzy', '我头突然好晕', 'var botId = _M.get(\'botId\');\r\nif (botId==null) botId=221;\r\n_M.put(\'robot_msg\',\'你先坐下来休息一下，我们来看一下身体状况\');\r\n_M.put(\'robot_cmd\',\'108\');\r\n_D.operate(0,1, botId,_M);', '5', '2016-08-08', 'jinbo', '2016-08-12', '1', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('fet_heartevent', '心率事件', 'var botId = _M.get(\'botId\');\r\nif (botId==null) botId=221;\r\n_M.put(\'robot_msg\',\'主人，你的心率好高，需要我联络黄医师吗\');\r\nvar botId = _M.get(\'botId\');\r\n_D.operate(0,1, botId,_M);', '1', '2016-08-31', 'SceneEvent', '2016-08-31', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('fet_help', '帮我联络黄医师，也打开视频让黄医师看到我的状况', 'var botId = _M.get(\'botId\');\r\nif (botId==null) botId=240;\r\n_M.put(\'robot_cmd\',\'240\');\r\n_D.operate(0,botId,botId,_M);\r\n_M.put(\'robot_msg\',\'好,我马上联络他\');\r\n_M.put(\'robot_cmd\',\'108\');\r\n_D.operate(0,botId,botId,_M);\r\nvar houseId = _M.get(\'houseId\');\r\n_D.pushSubsMsg(\'1\',\'01\',\'2\',\'\',\'\',houseId,\'\',_M);\r\n_D.delay(5000);\r\n_M.put(\'robot_msg\',\'黃醫師已經知道你的狀況, 他現在在路上，快到了！\');\r\n_M.put(\'robot_cmd\',\'108\');\r\n_D.operate(0,botId,botId,_M);', '6', '2016-08-09', 'jinbo', '2016-08-13', '1', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('fet_open', '快帮开门好让黄医师进来', 'var botId = _M.get(\'botId\');\r\nif (botId==null) botId=221;\r\nvar door=90;\r\n_M.put(\'robot_msg\',\'主人，门已打开\');\r\n_M.put(\'robot_cmd\',\'108\');\r\n_D.operate(0,1, botId,_M);\r\n_M.put(\'on_off\',\'1\');\r\n_D.operate(0,1, door,_M);', '7', '2016-08-10', 'jinbo', '2016-08-14', '1', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('fet_openevent', '开门事件', '\r\nvar botId = _M.get(\'botId\');\r\nif (botId==null) botId=221;\r\n_M.put(\'robot_msg\',\'你回来啦,今天辛苦了\');\r\n_M.put(\'robot_cmd\',\'1\');\r\n_D.operate(0,1,botId,_M);\r\n_D.delay(2000);\r\n\r\n_M.put(\'robot_msg\',\'\');\r\n_M.put(\'robot_cmd\',\'18\');\r\n_D.operate(0,1,botId,_M);\r\n_M.put(\'robot_cmd\',\'108\');\r\n_D.operate(0,1,botId,_M);\r\n\r\n_M.put(\'robot_msg\',\'\');\r\n_M.put(\'robot_cmd\',\'\');\r\n_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_D.operate(0,232,229,_M);\r\n_D.delay(2000);\r\n\r\n_M.put(\'robot_msg\',\'\');\r\n_M.put(\'robot_cmd\',\'\');\r\n_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_D.operate(0,232,223,_M);\r\n_D.delay(2000);', '1', '2016-08-31', 'SceneEvent', '2016-08-31', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('fet_return', '我回家了', 'var botId = _M.get(\'botId\');\r\nif (botId==null) botId=221;\r\n_M.put(\'robot_msg\',\'主人，好高兴看到你，有什么我可以帮你的\');\r\n_D.operate(0,1, botId,_M);', '1', '2016-08-04', 'jinbo', '2016-08-08', '1', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('fet_stuffy', '空气有点闷', 'var curtain = 236; //不知道窗帘id多少，乱写的\r\nvar win = 235; //不知道窗户id多少，乱写的\r\nvar botId = _M.get(\'botId\');\r\nif (botId==null) botId=240;\r\n//println(\'botid=\'+botId);\r\n\r\n_D.deviceInfo(curtain,_M); \r\nvar curtain_degree = _M.get(\'open_degree\');\r\n//println(\'curtain degree = \'+ curtain_degree);\r\n\r\n_D.deviceInfo(win,_M); \r\nvar on_off_win = _M.get(\'window_optype\');\r\n//println(\'window onoff= \'+ on_off_win);\r\nif (on_off_win==null) on_off_win=3;\r\n\r\nif(on_off_win==3){\r\n	_M.put(\'robot_msg\',\'那我帮你开窗\');\r\n	_M.put(\'robot_cmd\',\'108\');\r\n	_D.operate(0,1,botId,_M);\r\n  _D.delay(2000);\r\n\r\n	//开窗帘后延迟1.5秒停止, 确认255是否是停止\r\n	_M.put(\'open_degree\',\'100\');\r\n	_D.operate(0,232,curtain,_M);\r\n  _D.delay(1500);\r\n	_M.put(\'open_degree\',\'255\');\r\n	_D.operate(0,232,curtain,_M);\r\n\r\n  _M.put(\'window_optype\',\'2\');\r\n  _D.operate(0,232,win,_M);\r\n  //_D.delay(2000);\r\n  //  println(\'open window\');\r\n}else if(on_off_win==2){\r\n	_M.put(\'robot_msg\',\'窗已经开了,那我帮你开风扇\');\r\n	_M.put(\'robot_cmd\',\'108\');\r\n	_D.operate(0,1,botId,_M);\r\n  _D.delay(2000);\r\n\r\n  _M.put(\'on_off\',\'1\');\r\n	_D.operate(0,232, 227,_M);\r\n  //_D.delay(2000);\r\n}else {\r\n	_M.put(\'robot_msg\',\'那我帮你打开风扇\');\r\n	_M.put(\'robot_cmd\',\'108\');\r\n	_D.operate(0,1,botId,_M);\r\n  //_D.delay(2000);\r\n  _M.put(\'on_off\',\'1\');\r\n	_D.operate(0,232, 227,_M);\r\n  //_D.delay(2000);\r\n//  println(\'open fan\');\r\n}', '3', '2016-08-06', 'jinbo', '2016-08-10', '1', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('fet_videoevent', '摄像头事件', 'var botId = _M.get(\'botId\');\r\nif (botId==null) botId=240;\r\n_M.put(\'robot_msg\',\'主人，黄医师已在路上，并连接上小爱的摄像头了，您现在可与黄医师远程对话\');\r\nvar botId = _M.get(\'botId\');\r\n_D.operate(0,botId, botId,_M);', '1', '2016-08-31', 'SceneEvent', '2016-08-31', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('health.warning', '健康预警', '_M.put(\'robot_msg\',\'主人，你的心率好高，需要我联络黄医师吗\');\r\nvar houseId = _M.get(\'houseId\');\r\n_D.healthWarning(\'\', houseId, _M);', '1', '2017-02-22', 'SceneEvent', '2017-02-22', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('home.ok', '家里一切都好吗？', 'var botId = _M.get(\'botId\');\r\nif (botId==null) botId=221;\r\n\r\n_M.put(\'robot_msg\',\'很好呀,有什么我可以帮你吗?\');\r\n_D.operate(0,232, botId,_M);', '1', '2017-03-07', 'SceneEvent', '2017-03-07', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Instruct_1488274593745', '我觉得有点冷', '_D.deviceinfo(2,_M);var open_degree_0=_M.get(\'open_degree\');if(open_degree_0<30){_M.put(\'open_degree\',\'34\');_M.put(\'on_off\',\'0\');_D.operate(0,1,235,_M);_D.delay(500);_M.put(\'on_off\',\'0\');_D.operate(0,1,226,_M);_D.delay(500);}', '1', '2017-02-28', 'Instruct', '2017-02-28', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Instruct_1488871835223', '我很冷，帮关窗', '_D.deviceinfo(227,_M);var on_off_0=_M.get(\'on_off\');if(on_off_0==1){_M.put(\'robot_msg\',\'那我帮你关风扇\');_M.put(\'on_off\',\'0\');_D.operate(3,232,227,_M);_D.delay(500);}', '1', '2017-03-07', 'Instruct', '2017-03-07', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Instruct_1488954468118', '把窗戶關起來', '_D.deviceinfo(227,_M);var on_off_0=_M.get(\'on_off\');if(on_off_0==0){_M.put(\'robot_msg\',好了);_M.put(\'on_off\',\'1\');_D.operate(3,232,227,_M);_D.delay(500);}', '1', '2017-03-08', 'Instruct', '2017-03-08', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('JunitTest1', 'test EventScript', '_D.operate(0,4,1,_M);_D.delay(500);_D.operate(0,4,3,_M);', '1', '2016-08-26', null, '2016-08-26', '1', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('JunitTest2', 'test EventScript', 'modi name', '1', '2016-08-26', null, '2016-08-26', '1', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('living.room.bulb.blue', '变蓝', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'0\');\r\n_M.put(\'green\',\'0\');\r\n_M.put(\'blue\',\'255\');\r\n_D.operate(0,158,169,_M);\r\n', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('living.room.bulb.close', '关灯', '_M.put(\'on_off\',\'0\');\r\n_D.operate(0,1,223,_M);', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('living.room.bulb.cyan', '变青', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'0\');\r\n_M.put(\'green\',\'127\');\r\n_M.put(\'blue\',\'255\');\r\n_D.operate(0,158,169,_M);', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('living.room.bulb.green', '变绿', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'0\');\r\n_M.put(\'green\',\'255\');\r\n_M.put(\'blue\',\'0\');\r\n_D.operate(0,158,169,_M);\r\n', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('living.room.bulb.open', '开灯', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'100\');\r\n_M.put(\'green\',\'100\');\r\n_M.put(\'blue\',\'100\');\r\n_D.operate(0,1,223,_M);', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('living.room.bulb.orange', '变橙', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'255\');\r\n_M.put(\'green\',\'165\');\r\n_M.put(\'blue\',\'0\');\r\n_D.operate(0,158,169,_M);\r\n', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('living.room.bulb.purple', '变紫', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'139\');\r\n_M.put(\'green\',\'0\');\r\n_M.put(\'blue\',\'255\');\r\n_D.operate(0,158,169,_M);\r\n', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('living.room.bulb.red', '变红', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'255\');\r\n_M.put(\'green\',\'0\');\r\n_M.put(\'blue\',\'0\');\r\n_D.operate(0,158,169,_M);\r\n', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('living.room.bulb.yellow', '变黄', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'255\');\r\n_M.put(\'green\',\'255\');\r\n_M.put(\'blue\',\'0\');\r\n_D.operate(0,158,169,_M);', '1', '2016-09-08', 'SceneEvent', '2016-09-08', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('open.door.listen', '开门事件', 'var botId = _M.get(\'botId\');\r\nif (botId==null) botId=240;\r\n_M.put(\'robot_msg\',\'你回来啦,今天辛苦了\');\r\n_M.put(\'robot_cmd\',\'1\');\r\n_D.operate(0,1,botId,_M);\r\n_D.delay(1000);\r\n\r\n_M.put(\'robot_msg\',\'\');\r\n_M.put(\'robot_cmd\',\'18\');\r\n_D.operate(0,1,botId,_M);\r\n_M.put(\'robot_cmd\',\'108\');\r\n_D.operate(0,1,botId,_M);\r\n\r\n_M.put(\'robot_msg\',\'\');\r\n_M.put(\'robot_cmd\',\'\');\r\n_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_D.operate(0,232,229,_M);\r\n_D.delay(2000);\r\n\r\n_M.put(\'robot_msg\',\'\');\r\n_M.put(\'robot_cmd\',\'\');\r\n_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_D.operate(0,232,223,_M);\r\n_D.delay(2000);', '1', '2017-03-03', 'SceneEvent', '2017-03-03', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('pushSubsMsg', '消息推送', '_D.pushSubsMsg(182, 120098, \'消息推送测试\',_M);', '1', '2017-02-20', 'SceneEvent', '2017-02-20', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_1', 'Scene_测试场景(打开开关，然后关掉)', '_M.put(\'on_off\',\'1\');_D.operate(4,0,1_M);_D.delay(500);_M.put(\'on_off\',\'0\');_D.operate(4,0,1_M);', '1', '2016-09-08', 'SceneEvent', '2016-09-08', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_100&1481874590074', 'Scene_回家场景', '_M.put(\'red\',\'0\');_M.put(\'lightness\',\'1\');_M.put(\'blue\',\'0\');_M.put(\'on_off\',\'1\');_M.put(\'green\',\'0\');_D.operate(100,128,1,_M);', '1', '2017-01-04', 'SceneEvent', '2017-01-04', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_100&1481883262512', 'Scene_离家场景', '_M.put(\'red\',\'0\');_M.put(\'lightness\',\'1\');_M.put(\'blue\',\'0\');_M.put(\'on_off\',\'1\');_M.put(\'green\',\'0\');_D.operate(100,128,1,_M);', '1', '2017-01-04', 'SceneEvent', '2017-01-04', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_100&robot', '机器人说话', '_M.put(\'robot_binding_status\',\'0\');\r\n_M.put(\'robot_msg\',\'主人，小爱已完成注册，可以开始服务了\');\r\nvar devid = _M.get(\'devid\');\r\n_D.operate(0,devid,devid,_M);', null, null, null, null, null, null);
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_101&1477536090508', 'Scene_离家场景', '_M.put(\'on_off\',\'0\');_D.operate(101,158,169,_M);_D.delay(500);_M.put(\'on_off\',\'0\');_D.operate(101,158,91,_M);_D.delay(500);_M.put(\'on_off\',\'0\');_D.operate(101,158,96,_M);', '1', '2016-11-23', 'SceneEvent', '2016-11-23', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_101&14775360905081', 'Scene_回家场景', '_M.put(\'red\',\'233\');_M.put(\'lightness\',\'52\');_M.put(\'blue\',\'143\');_M.put(\'on_off\',\'1\');_M.put(\'green\',\'255\');_D.operate(101,158,169,_M);_D.delay(500);_M.put(\'on_off\',\'1\');_D.operate(101,158,91,_M);_D.delay(500);_M.put(\'red\',\'255\');_M.put(\'lightness\',\'25\');_M.put(\'blue\',\'211\');_M.put(\'on_off\',\'1\');_M.put(\'green\',\'177\');_D.operate(101,158,96,_M);', '1', '2016-10-27', 'SceneEvent', '2016-10-27', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_101&1477558266863', 'Scene_睡眠场景', '_M.put(\'red\',\'115\');_M.put(\'lightness\',\'1\');_M.put(\'blue\',\'61\');_M.put(\'on_off\',\'1\');_M.put(\'green\',\'113\');_D.operate(101,158,169,_M);_D.delay(500);_M.put(\'on_off\',\'0\');_D.operate(101,158,96,_M);', '1', '2016-10-27', 'SceneEvent', '2016-10-27', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_101&1477561512299', 'Scene_喝茶', '_M.put(\'red\',\'91\');_M.put(\'lightness\',\'128\');_M.put(\'blue\',\'255\');_M.put(\'on_off\',\'1\');_M.put(\'green\',\'253\');_D.operate(101,158,169,_M);', '1', '2016-10-28', 'SceneEvent', '2016-10-28', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_101&1477562041186', 'Scene_回家场景', '_M.put(\'red\',\'255\');_M.put(\'lightness\',\'1\');_M.put(\'blue\',\'164\');_M.put(\'on_off\',\'1\');_M.put(\'green\',\'254\');_D.operate(101,158,169,_M);_D.delay(500);_M.put(\'on_off\',\'1\');_D.operate(101,158,91,_M);_D.delay(500);_M.put(\'red\',\'209\');_M.put(\'lightness\',\'1\');_M.put(\'blue\',\'255\');_M.put(\'on_off\',\'1\');_M.put(\'green\',\'102\');_D.operate(101,158,96,_M);', '1', '2016-10-27', 'SceneEvent', '2016-10-27', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_101&1477902524702', 'Scene_喝茶', '_M.put(\'red\',\'35\');_M.put(\'lightness\',\'1\');_M.put(\'blue\',\'255\');_M.put(\'on_off\',\'1\');_M.put(\'green\',\'120\');_D.operate(101,158,169,_M);', '1', '2016-10-31', 'SceneEvent', '2016-10-31', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_3&1488957134632', 'Scene_休閒', '_M.put(\'red\',\'134\');_M.put(\'lightness\',\'1\');_M.put(\'blue\',\'104\');_M.put(\'on_off\',\'1\');_M.put(\'green\',\'255\');_D.operate(3,232,229,_M);', '1', '2017-03-08', 'SceneEvent', '2017-03-08', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_3&1488957212548', 'Scene_休息', '_M.put(\'red\',\'231\');_M.put(\'lightness\',\'1\');_M.put(\'blue\',\'84\');_M.put(\'on_off\',\'1\');_M.put(\'green\',\'255\');_D.operate(3,232,229,_M);', '1', '2017-03-08', 'SceneEvent', '2017-03-08', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_4&1476951020156', 'Scene_睡觉觉', '_M.put(\'on_off\',\'0\');_D.operate(4,113,96,_M);', '1', '2016-10-20', 'SceneEvent', '2016-10-20', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_4&1476951020765', 'Scene_春眠不觉晓', '_M.put(\'red\',\'255\');_M.put(\'lightness\',\'42\');_M.put(\'blue\',\'92\');_M.put(\'on_off\',\'1\');_M.put(\'green\',\'92\');_D.operate(4,113,1,_M);', '1', '2016-10-20', 'SceneEvent', '2016-10-20', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_4&1476951842920', 'Scene_YY', '_M.put(\'red\',\'130\');_M.put(\'lightness\',\'14\');_M.put(\'blue\',\'130\');_M.put(\'on_off\',\'1\');_M.put(\'green\',\'130\');_D.operate(4,113,1,_M);', '1', '2016-10-20', 'SceneEvent', '2016-10-20', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_4&1477035542167', 'Scene_清楚', '_M.put(\'open_degree\',\'10\');_D.operate(4,113,20,_M);', '1', '2016-10-21', 'SceneEvent', '2016-10-21', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_4&1477044076049', 'Scene_this', '_M.put(\'red\',\'0\');_M.put(\'lightness\',\'1\');_M.put(\'blue\',\'0\');_M.put(\'on_off\',\'1\');_M.put(\'green\',\'0\');_D.operate(4,128,1,_M);', '1', '2016-10-24', 'SceneEvent', '2016-10-24', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_9&1474617405754', 'Scene_定时', '_M.put(\'open_degree\',\'10\');_D.operate(9,61,20,_M);', '1', '2016-10-27', 'SceneEvent', '2016-10-27', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_9&1474859350063', 'Scene_定时执行', '_M.put(\'open_degree\',\'10\');_D.operate(9,61,20,_M);', '1', '2016-09-26', 'SceneEvent', '2016-09-26', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_9&1476928719311', 'Scene_你是', '_M.put(\'on_off\',\'0\');_D.operate(9,113,62,_M);', '1', '2016-10-20', 'SceneEvent', '2016-10-20', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_leaveHome', '离家场景', '_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'200\');\r\n_M.put(\'red\',\'200\');\r\n_M.put(\'green\',\'200\');\r\n_M.put(\'blue\',\'200\');\r\n_D.operate(0,158,96,_M);\r\n_D.operate(0,158,169,_M);\r\n_D.delay(2000);\r\n_M.put(\'on_off\',\'1\');\r\n_M.put(\'lightness\',\'100\');\r\n_M.put(\'red\',\'200\');\r\n_M.put(\'green\',\'0\');\r\n_M.put(\'blue\',\'0\');\r\n_D.operate(0,158,96,_M);\r\n_D.operate(0,158,169,_M);\r\n_D.delay(2000);\r\n_M.put(\'on_off\',\'0\');\r\n_D.operate(0,158,96,_M);\r\n_D.operate(0,158,169,_M);\r\n', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('Scene_returnHome', 'Scene_回家场景', '', '1', '2016-12-16', 'SceneEvent', '2016-12-16', null, '4');
INSERT INTO `ee_sr_ruledef` VALUES ('security.open', '安防', '_M.put(\'audiovisual_duration\',\'1\');\r\n_M.put(\'audiovisual_alarm\',\'2\');\r\n_D.operate(0,1,163,_M);', '1', '2016-08-31', 'SceneEvent', '2016-08-31', '', '4');
INSERT INTO `ee_sr_ruledef` VALUES ('_D.pushSubsMsg(182, 120098, \'消息推送测试\',_M);', '测试脚本', 'if (_M.get(\'retCode\').equals(\'ERROR\')) println(\'ERROR...\');\r\nsetTimeout(0,1000);\r\nvar result = orderid * 100 + oprid * 10; println(\'msg = \'+ \'test\');println(\'eval = \'+ result); ', '1', '2016-08-04', 'ee_admin', '2016-08-08', '1', '4');