import cv2
import os

def video_to_frames(video_file, output_dir):
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 读取视频文件
    cap = cv2.VideoCapture(video_file)

    frame_count = 1
    while True:
        success, frame = cap.read()
        if not success:
            break

        # 保存帧为图片
        frame_file = os.path.join(output_dir, f"{frame_count:06d}.jpg")
        cv2.imwrite(frame_file, frame)
        frame_count += 1

    cap.release()
    print(f"共提取了 {frame_count} 帧")



def get_video_info(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video file")
        return None

    # 获取帧率和帧的大小
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    cap.release()
    return frame_rate, frame_width, frame_height, frame_count

def write_sequence_file(video_path, output_path, sequence_name, image_dir, image_ext):
    info = get_video_info(video_path)
    if info is None:
        return

    frame_rate, width, height, length = info
    with open(output_path, 'w') as file:
        file.write(f"[Sequence]\n")
        file.write(f"name={sequence_name}\n")
        file.write(f"imDir={image_dir}\n")
        file.write(f"frameRate={frame_rate}\n")
        file.write(f"seqLength={length}\n")
        file.write(f"imWidth={width}\n")
        file.write(f"imHeight={height}\n")
        file.write(f"imExt={image_ext}\n")


video_file = 'test33.mp4' 
output_txt = 'MOT15/train/test33/seqinfo.ini'  # 输出文件的路径
sequence_name = 'test33'  # 序列名称
image_dir = 'img1'  # 图像目录
image_ext = '.jpg'  # 图像扩展名

write_sequence_file(video_file, output_txt, sequence_name, image_dir, image_ext)


 # 替换为你的视频文件路径
output_dir = 'MOT15/train/test33/img1'  # 输出图片的目录
video_to_frames(video_file, output_dir)
