from ultralytics import YOLO 
model = YOLO('weights/best.pt')

def count_trees(image_path):
    results = model.predict(image_path)
    tree_count = sum(conf > 0.5 for conf in results[0].boxes.conf)
    return tree_count
