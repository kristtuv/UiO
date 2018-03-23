#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                                                                               #
# Part of mandatory assignment 2 in                                             #
# INF5860 - Machine Learning for Image analysis                                 #
# University of Oslo                                                            #
#                                                                               #
#                                                                               #
# Ole-Johan Skrede    olejohas at ifi dot uio dot no                            #
# 2018.03.01                                                                    #
#                                                                               #
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

"""Define the dense neural network model"""

import numpy as np
import sys
from IPython import get_ipython
# sys.path.remove('/usr/local/lib/python2.7/site-packages')
from scipy.stats import truncnorm


def one_hot(Y, num_classes):
    """Perform one-hot encoding on input Y.

    It is assumed that Y is a 1D numpy array of length m_b (batch_size) with integer values in
    range [0, num_classes-1]. The encoded matrix Y_tilde will be a [num_classes, m_b] shaped matrix
    with values

                   | 1,  if Y[i] = j
    Y_tilde[i,j] = |
                   | 0,  else
    """
    m = len(Y)
    Y_tilde = np.zeros((num_classes, m))
    Y_tilde[Y, np.arange(m)] = 1
    return Y_tilde


def initialization(conf):
    """Initialize the parameters of the network.

    Args:
        layer_dimensions: A list of length L+1 with the number of nodes in each layer, including
                          the input layer, all hidden layers, and the output layer.
    Returns:
        params: A dictionary with initialized parameters for all parameters (weights and biases) in
                the network.
    """
    # TODO: Task 1
    layer_dimensions = conf['layer_dimensions']
    L = len(layer_dimensions)


    params = {}
    for l in range(1, L):
       
        W = np.random.normal(0.0, np.sqrt(2.0/layer_dimensions[l-1]), size=(layer_dimensions[l-1], layer_dimensions[l]))

        b = np.zeros((layer_dimensions[l], 1) )
        # b = np.zeros((1, layer_dimensions[l]))

        params['W_{}'.format(l)] = W
        params['b_{}'.format(l)] = b
    

    return params

def activation(Z, activation_function):
    """Compute a non-linear activation function.

    Args:
        Z: numpy array of floats with shape [n, m]
    Returns:
        numpy array of floats with shape [n, m]
    """
    # TODO: Task 2 a)
    if activation_function == 'relu':
        return (Z >= 0) * Z 
    else:
        print("Error: Unimplemented derivative of activation function: {}", activation_function)
        return None


def softmax(Z):
    """Compute and return the softmax of the input.

    To improve numerical stability, we do the following

    1: Subtract Z from max(Z) in the exponentials
    2: Take the logarithm of the whole softmax, and then take the exponential of that in the end

    Args:
        Z: numpy array of floats with shape [n, m]
    Returns:
        numpy array of floats with shape [n, m]
    """
    # TODO: Task 2 b)
    Z -= np.max(Z)
    S = np.exp(Z - np.log(np.sum(np.exp(Z), axis=0)))
    return S


def forward(conf, X_batch, params, is_training):
    """One forward step.

    Args:
        conf: Configuration dictionary.
        X_batch: float numpy array with shape [n^[0], batch_size]. Input image batch.
        params: python dict with weight and bias parameters for each layer.
        is_training: Boolean to indicate if we are training or not. This function can namely be
                     used for inference only, in which case we do not need to store the features
                     values.

    Returns:
        Y_proposed: float numpy array with shape [n^[L], batch_size]. The output predictions of the
                    network, where n^[L] is the number of prediction classes. For each input i in
                    the batch, Y_proposed[c, i] gives the probability that input i belongs to class
                    c.
        features: Dictionary with
                - the linear combinations Z^[l] = W^[l]a^[l-1] + b^[l] for l in [1, L].
                - the activations A^[l] = activation(Z^[l]) for l in [1, L].
               We cache them in order to use them when computing gradients in the backpropagation.
    """
    # TODO: Task 2 c)
    # layer_dims = conf['layer_dimensions']
    # L = len(layer_dims)
    # act_func = conf['activation_function']

    # features = {}
    # features['A_0'] = X_batch 

    # for i in range(1,L):
    #     print("forward:", i)
    #     W = params['W_'+ str(i)]
    #     b = params['b_' + str(i)]
    #     A = features['A_' + str(i-1)]
    #     # Z = np.dot(A, W.T) + b
    #     print("A", A.shape)
    #     print("W", W.shape)
    #     print("b", b.shape)
    #     Z = np.dot(W.T, A) + b 
    #     features['Z_' + str(i)] = Z.round(2)

    #     if i != (L-1):
    #         A_next = activation(Z, act_func)
    #         features['A_'+ str(i)] = A_next
    #     else:
    #         A_next = softmax(Z)
    #         features['A_' + str(i)] = A_next
    #         Y_proposed = A_next





    layer_dimensions = conf['layer_dimensions']
    L = len(layer_dimensions)
    activation_function = conf['activation_function']

    features = {}
    features['A_0'] = X_batch

    for l in range(1, L-1):
        W = params['W_{}'.format(l)]
        b = params['b_{}'.format(l)]
        A = features['A_{}'.format(l-1)]

        # Z = np.dot(A, W.T) + b
        Z = np.dot(W.T, A) + b
        features['Z_{}'.format(l)] = Z
        features['A_{}'.format(l)] =  activation(Z, activation_function)

    #Last step, trying to avoid if-tests in the for-loop
    W = params['W_{}'.format(L-1)]
    b = params['b_{}'.format(L-1)]
    A = features['A_{}'.format(L-2)]
    
    Z = np.dot(W.T, A) + b
    features['Z_{}'.format(L-1)] = Z.round(2)

    Y_proposed = softmax(Z)
    features['A_{}'.format(L-1)] = Y_proposed

    return Y_proposed, features


def cross_entropy_cost(Y_proposed, Y_reference):
    """Compute the cross entropy cost function.

    Args:
        Y_proposed: numpy array of floats with shape [n_y, m].
        Y_reference: numpy array of floats with shape [n_y, m]. Collection of one-hot encoded
                     true input labels

    Returns:
        cost: Scalar float: 1/m * sum_i^m sum_j^n y_reference_ij log y_proposed_ij
        num_correct: Scalar integer
    """
    # TODO: Task 3
    m = Y_reference.shape[1]
    cost = -1.0/m * np.sum(Y_reference*np.log(Y_proposed))
    num_correct = np.sum(np.argmax(Y_proposed, axis=0) == np.argmax(Y_reference, axis=0))
    return cost, num_correct


def activation_derivative(Z, activation_function):
    """Compute the gradient of the activation function.

    Args:
        Z: numpy array of floats with shape [n, m]
    Returns:
        numpy array of floats with shape [n, m]
    """
    # TODO: Task 4 a)
    if activation_function == 'relu':
        return (Z >= 0) * 1
    else:
        print("Error: Unimplemented derivative of activation function: {}", activation_function)
        return None


def backward(conf, Y_proposed, Y_reference, params, features):
    """Update parameters using backpropagation algorithm.

    Args:
        conf: Configuration dictionary.
        Y_proposed: numpy array of floats with shape [n_y, m].
        features: Dictionary with matrices from the forward propagation. Contains
                - the linear combinations Z^[l] = W^[l]a^[l-1] + b^[l] for l in [1, L].
                - the activations A^[l] = activation(Z^[l]) for l in [1, L].
        params: Dictionary with values of the trainable parameters.
                - the weights W^[l] for l in [1, L].
                - the biases b^[l] for l in [1, L].
    Returns:
        grad_params: Dictionary with matrices that is to be used in the parameter update. Contains
                - the gradient of the weights, grad_W^[l] for l in [1, L].
                - the gradient of the biases grad_b^[l] for l in [1, L].
    """
    # TODO: Task 4 b)
    grad_params = {}
    L = len(conf['layer_dimensions']) - 1
    m = Y_proposed.shape[1]
    
    J_L = Y_proposed - Y_reference
    dw = 1.0/m*np.dot(features['A_{}'.format(L-1)], J_L.T)
    db = 1.0/m*np.dot(J_L, np.ones((m,1))) 
    grad_params['grad_W_{}'.format(L)] = dw
    grad_params['grad_b_{}'.format(L)] = db

    for l in reversed(range(1, L)):
        J_l = activation_derivative(features['Z_{}'.format(l)], 'relu') * np.dot(params['W_{}'.format(l + 1)], J_L)
        dw = 1.0/m*np.dot(features['A_{}'.format(l - 1)], J_l.T)
        db = 1.0/m*np.dot(J_l, np.ones((m,1))) 
        grad_params['grad_W_{}'.format(l)] = dw
        grad_params['grad_b_{}'.format(l)] = db
        J_L = J_l
    return grad_params


def gradient_descent_update(conf, params, grad_params):
    """Update the parameters in params according to the gradient descent update routine.

    Args:
        conf: Configuration dictionary
        params: Parameter dictionary with W and b for all layers
        grad_params: Parameter dictionary with b gradients, and W gradients for all
                     layers.
    Returns:
        updated_params: Updated parameter dictionary.
    """
    # TODO: Task 5
    lamda = conf['learning_rate']
    updated_params = {}
    keys = sorted(params.keys())
    dkeys = sorted(grad_params.keys())
    for key, dkey in zip(keys, dkeys):
        updated_params[key] = params.get(key) - lamda*grad_params.get(dkey)
   

    
    return updated_params

if __name__ == '__main__':

    # from tests import task_2c
    from tests import task_3
    Y_proposed, Y_batch, expected_cost_value, expected_num_correct = task_3()
    cost_value, num_correct = cross_entropy_cost(Y_proposed, Y_batch)
    print(Y_proposed)
    print(Y_batch)
    # conf, X_batch, params, expected_Z_1, expected_A_1, expected_Z_2, expected_Y_proposed = task_2c()
    # Y_proposed, features = forward(conf, X_batch, params, is_training=True)
    # for key in features:
    #     print (key)
    #     for y in features[key]:
    #         print(y)
    # print(expected_Z_1)
    # print(expected_Z_2)
    # print(expected_A_1)
    # print(expected_Z_1)
    # print(expected_Z_1)
