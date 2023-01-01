import numpy as np

def get_tpr(y,pred,th = 0.5):
    """
    Compute true positive rate of predictions at threshold.

    Args:
        y (np.array): ground truth, size (n_examples)
        pred (np.array): model output, size (n_examples)
        th (float): cutoff value for positive prediction from model
    Returns:
        TPR (float): True Positive Rate of predictions at threshold
    """

    pred_threshold = pred >= th


    TP = np.sum((y == 1) & (pred_threshold == 1))
    FN =  np.sum((y == 1) & (pred_threshold == 0))

    TPR = TP/(TP+FN)    

    return TPR

def get_fpr(y,pred,th = 0.5):
    """
    Compute false positive rate of predictions at threshold.

    Args:
        y (np.array): ground truth, size (n_examples)
        pred (np.array): model output, size (n_examples)
        th (float): cutoff value for positive prediction from model
    Returns:
        FPR (float): False Positive Rate of predictions at threshold
    """

    pred_threshold = pred >= th

    TN = np.sum((y == 0) & (pred_threshold == 0))
    FP =  np.sum((y == 0) & (pred_threshold == 1))

    FPR = FP/(FP+TN)    

    return FPR