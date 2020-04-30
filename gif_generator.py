import imageio
import os
import sys

#get input from system
file_name = sys.argv[1]
clip = os.path.abspath(file_name)


def gif_maker(inputPath, targetFormat):
    output_path = os.path.splitext(inputPath)[0]+targetFormat
    print(f"converting {inputPath} \n to {output_path}")

    reader = imageio.get_reader(inputPath)
    #read metadata from source video to determine fps
    fps = reader.get_meta_data()['fps']
    writer = imageio.get_writer(output_path,fps = fps)
    
    for frames in reader:
        writer.append_data(frames)
        # print(f'frame{frames}')

    print('done')
    writer.close()

gif_maker(clip,'.gif')
