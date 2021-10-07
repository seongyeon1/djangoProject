import cv2, os

base_path = "./docs/upload/"

for infile in os.listdir(base_path):
    print("file : " + infile)
    filename = infile.split('.')[0]

    ret, images = cv2.imreadmulti(base_path + infile, [], cv2.IMREAD_ANYCOLOR)

    for idx, img in enumerate(images):
        #print(idx, img)
        if img.mean() < 255:
            # print(idx, img)
            img_resized = cv2.resize(img, dsize=(1000, 1000), interpolation=cv2.INTER_AREA)
            img_cut = img_resized[50:950, 50:950]
            img_final = cv2.resize(img_cut, dsize=(640, 480), interpolation=cv2.INTER_AREA)
            cv2.imwrite(f'static/upload/{filename}_{idx+1}.png', img_final)

# tif 중에서 빈화면 아닌건 png나 다른 확장자로 변환후 -> html에서 불러와야함

