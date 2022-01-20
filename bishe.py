import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()

# import some common libraries
import numpy as np
import os, json, cv2, random


# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cbook as cbook


im = cv2.imread("./3.jpg")

cfg = get_cfg()
# add project-specific config (e.g., TensorMask) here if you're not running a model in detectron2's core library
cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
# Find a model from detectron2's model zoo. You can use the https://dl.fbaipublicfiles... url as well
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")
predictor = DefaultPredictor(cfg)
outputs = predictor(im)


v = Visualizer(im[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2)
out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
cv2.imshow('imshow',out.get_image()[:, :, ::-1])
cv2.waitKey(0)


for box in outputs["instances"].pred_boxes.to('cpu'):
    x0 = int(box[0].item())
    y0 = int(box[1].item())
    x1 = int(box[2].item())
    y1 = int(box[3].item())

    width = x1 - x0
    height = y1 - y0
    fig, ax = plt.subplots()
    img = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    im1 = ax.imshow(img)
    patch = patches.Rectangle(
        (x0, y0),
        width,
        height,
        transform=ax.transData
    )
    im1.set_clip_path(patch)
    ax.axis('off')
    plt.show()