
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


generator = lambda txt: TextClip(txt, font='Georgia-Regular',
                                fontsize=30, color='grey')

outpath = r"E:\WorkHome\CodeHome\Python\UW_Machine_Learing\UW_ML_Course2\ml_regression_bilibili"

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
    print(v_name)
    for idx, it in enumerate(f_list[0][2]):
        items = it.split(".")
        if items[-1] != "srt" or items[0] != v_name:
            continue
        elif items[-2] == "zh-CN":
            srt_zh = path_name + "\\" + it
        elif items[-2] == "en":
            srt_en = path_name + "\\" + it
    if srt_zh != "":
        return srt_zh
    else:
        return srt_en

def video_proc():
    xpath = ""

    xvideo_list = get_video_list(xpath)

    for xidx in xvideo_list:
        srt_file = get_srt_info(xidx)
        xout = trans_filename(xidx)
        convert_video(srt_file, xgenerator, xidx, xout)