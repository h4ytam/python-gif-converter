import imageio
import os

clip = os.path.abspath('reddit.mp4')


def gifmaker(inputpath, tagetFormat):
    outPath = os.path.splitext(inputpath)[0]+tagetFormat
    print(f'converting {inputpath} \n to {outPath}')

    reader = imageio.get_reader(inputpath)
    fps = reader.get_meta_data()['fps']
    writer = imageio.get_writer(outPath, fps=fps)

    for frames in reader:
        writer.append_data(frames)
        print(f'Frame {frames}')
    print('Done')
    writer.close()


gifmaker(clip, '.gif')
