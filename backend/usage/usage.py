from ultralytics import YOLO 
model = YOLO('backend\\weights\\best.pt')

def count_trees(image_path):
    results = model(image_path, verbose=False)
    tree_count = len(results[0].boxes)
    return tree_count
