
# 2018 Data Science Bowl

## Overall Training Process
```train.py``` 

## Main Network

- Network Overview  
```net/resnet50_mask_rcnn/model.py```  

- Layers
```net/resnet50_mask_rcnn/layer```  
features passing through (1)rpn, (2)rcnn and (3)mask layers in sequence  

- Parameters
```net/resnet50_mask_rcnn/configuration.py```  

## Data Processing
```annotate.py```
Processing before training (Note that data are kept offline)

## Submit
```submit.py```
Make a submission after training (Note that results are kept offline)

## Source
code source and modifications inspired by posts in
https://www.kaggle.com/c/data-science-bowl-2018/discussion/
https://www.kaggle.com/c/data-science-bowl-2018/kernels/