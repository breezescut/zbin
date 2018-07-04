
import os
from moviepy.video.VideoClip import TextClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

# 一个简单的类结构，存储视频的原名，转换后名称和匹配的字幕名称
class xvideo(object):
    video_path = ""
    origin_name = ""
    new_name = ""
    srt_file = ""


xgenerator = lambda txt: TextClip(txt, font='Georgia-Regular',
                                fontsize=30, color='black')

outpath = r"D:\WorkHome\CodeHome\Python\UW_Machine_Learing\UW_ML_Course3\ml-classification_bilibili"

# 将输入的视频和字幕进行合并压制
def convert_video(srtfile, xgenerator, invideo, outvideo):
    sub = SubtitlesClip(srtfile, xgenerator)
    # sub.set_position(("center", "bottom"), relative=True)
    myvideo = VideoFileClip(invideo)
    final = CompositeVideoClip([myvideo, sub.set_position((0.2, 0.8), relative=True)])
    final.to_videofile(outvideo, fps=myvideo.fps)


# 根据输入的视频信息生成为规定的输出视频文件名
# 如第一周第一单元的课程需要在原视频名加上前缀“W1_M1_”
def trans_filename(v_path):
    base_name = os.path.basename(v_path)
    path_name = os.path.dirname(v_path)

    item_path = path_name.split("\\")

    week = "W" + item_path[-2][0:2]
    module = "M" + item_path[-1][0:2]
    pref = week + "_" + module + "_"

    out_video = outpath + "\\" + pref + base_name
    return out_video



# 从指定的目录中搜索所有相关的视频名
def get_video_list(xpath):
    f_list = os.walk(xpath)
    video_lst = []
    for idx in f_list:
        sub_f_list = idx[2]
        for iidx in sub_f_list:
            if iidx.find("mp4") != -1:
                video_path = idx[0]
                video_lst.append(video_path + "\\" + iidx)
    return video_lst
        

# 从指定目录中根据输入的视频名搜索对应字幕文件，优先匹配中文字幕，其次是英文字幕
def get_srt_info(v_path):
    base_name = os.path.basename(v_path)
    path_name = os.path.dirname(v_path)

    v_name = base_name.split(".")[0]
    f_list = list(os.walk(path_name))

    srt_zh = ""
    srt_en = ""
    print(path_name, v_name)
    print(f_list[0][2])
    for it in f_list[0][2]:
        print("srt check %s" % it)
        items = it.split(".")
        if items[-1] != "srt" or items[0] != v_name:
            continue
        # elif items[-2] == "zh-CN":
        #     srt_zh = path_name + "\\" + it
        elif items[-2] == "en":
            srt_en = path_name + "\\" + it
    # if srt_zh != "":
    #     return srt_zh
    # else:
    return srt_en

def video_proc():
    xpath = r"D:\WorkHome\CodeHome\Python\UW_Machine_Learing\UW_ML_Course3\ml-classification"
    v_done = xpath + r"\v.done"

    print("hello")
    d_dict = dict() 
    xvideo_list = get_video_list(xpath)
    print(xvideo_list)
    vfd = open(v_done, 'r+')
    for line in vfd.readlines():
        line = line.strip()
        d_dict[line] = 1
        print("%s had been processed" % line)
    for xidx in xvideo_list:
        v_name = xidx.split("\\")[-1]
        print("get %s" % v_name)
        if v_name in d_dict:
            print("skip %s" % v_name)
            continue
        srt_file = get_srt_info(xidx)
        xout = trans_filename(xidx)
        print("start convert, srtfile[%s], input[%s], output[%s]" % (srt_file, xidx, xout))
        convert_video(srt_file, xgenerator, xidx, xout)
        vfd.write(v_name + "\n")
        vfd.flush()
    vfd.close()

def unit_test():
    test_path = r"D:\WorkHome\CodeHome\Python\UW_Machine_Learing\UW_ML_Course3\ml-classification"
    v_lst = get_video_list(test_path)

    invideo = v_lst[0]

    srtfile = get_srt_info(invideo)
    outvideo = trans_filename(invideo)

    convert_video(srtfile, xgenerator, invideo, outvideo)