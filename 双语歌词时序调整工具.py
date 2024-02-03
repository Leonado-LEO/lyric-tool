import re
import os



#帮助信息
help = '''                                 
这是一个歌词文件时间码处理程序，
适用于带有中文翻译的英文歌，
解决在播放时无法将中文和英文显示在同一页的问题，
详细信息请到 https://github.com/Leonado-LEO/lyric-tool

示例如下：
原文件：
[00:00.000] 作曲 : Alphonso Henderson/Ed Sheeran/Jason Epperson/Andreas Carlsson/Steve Mac/Julia Michaels/Jacob Schulze/Tracy Marrow/George Clinton Jr/Benjamin Levin
[00:00.004]作词 : Alphonso Henderson/Ed Sheeran/Jason Epperson/Andreas Carlsson/Steve Mac/Julia Michaels/Jacob Schulze/Tracy Marrow/George Clinton Jr/Benjamin Levin
[00:00.51]I will always remember the day you kissed my lips
[00:05.64]Light as a feather
[00:08.06]And it went just like this

[by:Cepohalm]
[00:00.51]我永远不会忘记你我相吻的那天
[00:05.64]那吻很轻 很柔
[00:08.06]爱意油然而生


修改后：
[00:00.000] 作曲 : Alphonso Henderson/Ed Sheeran/Jason Epperson/Andreas Carlsson/Steve Mac/Julia Michaels/Jacob Schulze/Tracy Marrow/George Clinton Jr/Benjamin Levin
[00:00.004]作词 : Alphonso Henderson/Ed Sheeran/Jason Epperson/Andreas Carlsson/Steve Mac/Julia Michaels/Jacob Schulze/Tracy Marrow/George Clinton Jr/Benjamin Levin
[00:00.51]I will always remember the day you kissed my lips
[00:05.64]我永远不会忘记你我相吻的那天
[00:05.64]Light as a feather
[00:08.06]那吻很轻 很柔
[00:08.06]And it went just like this
[00:13:06]爱意油然而生

[by:Cepohalm]


详细信息请到 https://github.com/Leonado-LEO/lyric-tool
未经授权，严禁商用！
'''


# 指定文件夹路径
while True:
    folder_path = input ("请输入包含.lrc的文件夹路径，\n直接回车默认当前文件夹\n查看帮助请输入help\n")

    if folder_path == "":
        folder_path = "./"
        break
    elif folder_path == "help":
        print (help)
    else:
        break





def start(lines,file_path):

    # 初始化时间码和索引变量
    current_time = None
    next_time = None
    newline = []
    time_processed = []
    # 遍历每一行
    for i, line in enumerate(lines):
        # 使用正则表达式查找时间码
        time_match = re.search(r'\[\d+:\d+\.\d+\]', line)  #从第一次找到时间码开始
        if time_match:
            for j in range(i + 1, len(lines)):             #之后找到重复的一个时间码，也就是找到对应的歌词翻译
                is_mached = False                          #此处判断此for循环有没有找到对应歌词，如果找到了那么循环结束后不需要给newline加上原句
                if lines[j].find(time_match.group(0)) != -1 :
                    is_mached = True
                    newline += line
                    #print ("3")
                    current_time = time_match.group(0)
                    time_processed += [current_time]         #将处理过的时间存入变量中，防止后面重复写入
                    if j < len(lines)-1:                   #最后一句之前的处理方式
                        next_time_match = re.search(r'\[\d+:\d+\.\d+\]', lines[j+1])
                        if next_time_match:
                            next_time = next_time_match.group(0)
                            newline += next_time + lines[j][len(current_time):]
                            #print ("4")
                            break
                    elif j == len(lines)-1:                #最后一句的处理方式
                        match = re.search(r"\[(\d{2}):(\d{2})\.(\d{2})\]", current_time)
                        if match:
                            minutes = int(match.group(1))
                            seconds = int(match.group(2))
                            milliseconds = int(match.group(3))

                            # 将秒钟加5
                            new_seconds = seconds + 5

                            # 处理秒钟超过60的情况
                            if new_seconds >= 60:
                                minutes += 1
                                seconds -= 60


                            # 格式化新的时间字符串
                            next_time = f"[{minutes:02d}:{new_seconds:02d}:{milliseconds:02d}]"
                            newline += next_time + lines[j][len(current_time):]
                            #print ("5")
                        break
            if is_mached == False and time_match.group() not in time_processed :
                newline += line
                #print ("1")
        else:
            newline += line
            #print ("2")
    # 将修改后的内容写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(newline)




#主进程
count = 0                                 #统计总处理文件数
for filename in os.listdir(folder_path):
    if filename.endswith(".lrc"):
        count += 1
        # 构建完整的文件路径
        file_path = os.path.join(folder_path, filename)

        # 打开 LRC 文件并进行处理
        with open(file_path, "r", encoding='utf-8') as file:
            lines = file.readlines()
            print ("processing  " + filename)
            start(lines,file_path)
            print("sucess")

input (f"完成，共处理{count}个，按任意键退出。")

