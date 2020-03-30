import pandas as pd
import os
import sys
import argparse
import random

import numpy as np
import cv2

class CSVParser:
    def __init__(self, path):
        self.df = pd.read_csv(path)
        
    def get_row(self, col_in, value):
        row = self.df.loc[self.df[col_in] == value, :].index
        return row.values

    # Get value using col input, col output, value
    def get_value(self, col_out, col_in, value):
        row = self.get_row(col_in, value)
        return self.df.iloc[row][col_out]

    # Get value using row, col
    def get_value(self, row_in, col_in):
        return self.df.iloc[row_in][col_in]


def make_dir(path):
    try:
        if not os.path.isdir(path):
            os.makedirs(os.path.join(path))
    except:
        raise

 

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--csv_path', type=str, default='~/HDD/sdb/datasets/4_DONT/DNTYF_label_full.csv')
    parser.add_argument('--img_path', type=str, default='~/HDD/sdb/datasets/4_DONT/images')

    parser.add_argument('--time_interval', type=int, default=3)

    parser.add_argument('--num', type=int, default=100)
    parser.add_argument('--save_path', type=str, default='~/HDD/sdb/datasets/4_DONT/test')
    parser.add_argument('--mode', type=str, default=None)

    return parser.parse_args()

def main(args):
    
    csv_path = os.path.expanduser(args.csv_path)
    img_path = os.path.expanduser(args.img_path)
    save_path = os.path.expanduser(args.save_path)
    if args.mode == 'touch':
        save_path = os.path.join(save_path, 'touch')
    else:
        save_path = os.path.join(save_path, 'nontouch')
    make_dir(save_path)
    
    csv_parser = CSVParser(csv_path)
    
    # 1. 엑셀파일에서 임의의 영상(row)을 하나 고름
    # row 는 실제 CSV 에서보다 2가 작음. 
    
    for time in range(args.time_interval, 17, 2):
        cnt = 0
        while cnt < args.num:
            rand_row = random.randrange(0, csv_parser.df.shape[0])
            
            # 2. 임의의 row를 고른 이후에, 비디오 이름  확인.
            video_name = csv_parser.get_value(rand_row, 'video_name')
            
            # 3. 임의의 클래스 하나를 선택.(하드코딩)
            if args.mode == 'touch':
                rand_action = random.randrange(5, 13) # 얼굴 만지는 action
            else:
                rand_action = random.randrange(13, 17)
            
            action_periods = csv_parser.get_value(rand_row, rand_action)
            # 3.2. 셀이 NAN값이 아닐 경우에만, 이후 작업 수행
            if action_periods == action_periods:
                action_periods = ''.join([i for i in list(action_periods) if i != ' '])
            
                action_period_list = action_periods.split(',')
            
                # 3.3. 시간이 여러개 적혀있을 경우를 위해, 각각 처리
                for j, action_period in enumerate(action_period_list):
                    action_start, action_end = int(action_period.split('-')[0]), int(action_period.split('-')[1])
                    
                    if action_end - action_start > (args.time_interval*3):
                        # 3.4. 임의의 프레임을 설정한 후, 3채널로 만들기 위한 그룹을 만들어줌. 
                        rand_frame = random.randrange(action_start, action_end-(args.time_interval*2))
                        frame_group = [rand_frame, rand_frame+args.time_interval, rand_frame+(args.time_interval*2)]

                        frame_group = ['{0:06d}'.format(int(frm)) for frm in frame_group]
                        
                        # 3.5. 이미지 3개를 리스트로 구성
                        img_folder = os.path.join(img_path, video_name)

                        img_path_list = []
                        for k in frame_group:
                            new_path = os.path.join(img_folder,(video_name + '_frames' + k + '.png'))
                            img_path_list.append(new_path)

                        
                        stacked_img = np.zeros((224, 224, 3))
                        for n, img_p in enumerate(img_path_list):
                            img = cv2.imread(img_p)
                            
                            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                            gray = cv2.resize(gray, (224,224))
                            stacked_img[:, :, n] = gray
                        
                        stacked_img = stacked_img.astype(np.uint8)

                        # 4. Touching / Non-Touching 폴더에 저장

                        if args.mode == 'touch':
                            cv2.imwrite(os.path.join(save_path,(video_name + '_' + str(time) + '_' + str(cnt) + '_' + str(j) + '.png')) , stacked_img)
                        else:
                            cv2.imwrite(os.path.join(save_path,(video_name + '_' + str(time) + '_' + str(cnt) + '_' + str(j) + '.png')) , stacked_img)

                        cnt += 1
        print('time: ', time, ' cnt: ', cnt)
    

if __name__ == '__main__':
    args = parse_arguments(sys.argv[1:])
    main(args)
