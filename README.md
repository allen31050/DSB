# 2018 Data Science Bowl

##```train.py``` 
Overall training process

##```net```
The main network

```net/resnet50_mask_rcnn/model.py```  
main network overview  

```net/resnet50_mask_rcnn/layer```  
features passing through (1)rpn, (2)rcnn and (3)mask layers in sequence  

```net/resnet50_mask_rcnn/configuration.py```  
Parameters

##```annotate.py```
Data processing before training (Note that data are kept offline)

##```submit.py```
make a submission after training (Note that results are kept offline)

code modified from: https://www.kaggle.com/c/data-science-bowl-2018/discussion/49692#282662