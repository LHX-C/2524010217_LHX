from ultralytics import YOLO

model = YOLO(r"C:\Users\45300\Desktop\Software_C2local\runs\detect\runs\train\community_detect-7\weights\best.pt")

if __name__ == "__main__":
    # ----------------配置----------------
    source = r"C:\Users\45300\Desktop\Software_C2local\images\test\people_electrocar_54.jpg"  #可以是单张图片路径 / 文件夹 / 视频
    conf_threshold = 0.3     #置信度阈值，低于这个不显示框
    iou_threshold = 0.45
    save_result = True       #是否保存画好框的图片
    show_labels = True       #显示类别文字
    show_conf = True         #显示置信度分数

    results = model.predict(
        source=source,
        conf=conf_threshold,
        iou=iou_threshold,
        save=save_result,
        save_txt=False,
        save_conf=False,
        show_labels=show_labels,
        show_conf=show_conf,
        project="./runs/detect",
        name="infer_show"
    )

    print("推理完成！检测效果图保存位置： ./runs/detect/infer_show/")
    # 每一张result里面可以拿到框坐标、类别、置信度
    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            xyxy = box.xyxy[0].tolist()
            # print(f"类别id:{cls},置信度:{conf:.2f},框坐标{xyxy}")
