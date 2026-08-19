from ultralytics import YOLO

DATA_YAML=r"C:\Users\45300\Desktop\Software_C2\data.yaml"

if __name__ == "__main__":
    # 加载预训练权重
    # yolov8n 小模型
    model = YOLO("yolov8n.pt")

    results = model.train(
        data=DATA_YAML,
        epochs=100,               # 训练总轮次
        imgsz=640,                # 输入图像尺寸
        batch=8,                  # 显存16G设8；显存小改为4 / 2
        device="cpu",             # GPU使用0号显卡；无GPU写 device="cpu"
        workers=2,                # windows建议2，防止多线程报错
        patience=15,              # 早停：连续15轮验证集无提升，自动停止训练
        augment=True,             # 开启数据增强，提升泛化能力
        dropout=0.05,             # 防止过拟合
        cos_lr=True,              # 余弦学习率衰减
        lr0=0.01,                 # 初始学习率
        lrf=0.01,
        weight_decay=0.0005,
        plots=True,
        project=r"runs\train",
        name="community_detect",
        exist_ok=False,
        seed=42,
        verbose=True
    )

    print("=" * 50)
    print("训练完成！")
    print(f"best模型路径：runs/train/community_detect/weights/best.pt")
    print(f"last模型路径：runs/train/community_detect/weights/last.pt")
