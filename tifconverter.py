import cv2, os

base_path = "./docs/upload/"
new_path = "./docs/upload/"

for infile in os.listdir(base_path):
    print("file : " + infile)
    filename = infile.split('.')[0]

    ret, images = cv2.imreadmulti(base_path + infile, [], cv2.IMREAD_ANYCOLOR)

    for idx, img in enumerate(images):
        #print(idx, img)
        if img.mean() < 255:
            print(idx, img)
            cv2.imwrite(f'static/upload/{filename}_{idx+1}.png', img)


    # outfile = infile.split('.')[0] + '.jpg'
    # cv2.imwrite(new_path+outfile,read,[int(cv2.IMWRITE_JPEG_QUALITY), 200])

# dst = cv2.resize(img, dsize=(640, 480), interpolation=cv2.INTER_AREA)


# tif 중에서 빈화면 아닌건 png나 다른 확장자로 변환후 -> html에서 불러와야함

