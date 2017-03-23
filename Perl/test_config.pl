%config = (
        "2"=>"有点闷",
        "3"=>"还是很闷",
        "4"=>"我现在觉得冷",
        "5"=>"窗户关了",
        "6"=>"好呀那就关吧",
        "7"=>"我觉得不太舒服",
        "8"=>"联络医生"
);

%mqttconfig = (
        #open door
        "m1"=>qq|{"devid":"FA113705004B1200","devtype":"26","gwid":"50294D20A98F","msgid":"123","params"[{"contactdetector_alarm":"1","subdevid":"14","subdevtype":"26"}],"reqtype":"update","ts":"1490165886463"}|,
        #close door
        "m2"=>qq|{"devid":"FA113705004B1200","devtype":"26","gwid":"50294D20A98F","msgid":"123","params"[{"contactdetector_alarm":"2","subdevid":"14","subdevtype":"26"}],"reqtype":"update","ts":"1490165886463"}|
);
