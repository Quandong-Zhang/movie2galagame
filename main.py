def read_srt(t_path):
    with open(t_path+'.srt') as lines:  #一次性读入txt文件，并把内容放在变量lines中
        array=lines.readlines()  #返回的是一个列表，该列表每一个元素是txt文件的每一行
    
    return array

if __name__=="__main__":
    print(read_srt("input"))