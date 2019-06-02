#!/usr/bin/env python
# encoding: utf-8
import numpy
import scipy
class neuralNetwork:
    # 初始化神经网络（各层节点数、学习率） --各层节点数、学习率、2个权重矩阵、激活函数
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # 输入层、隐藏层、输出层的节点数量
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        # 学习率
        self.lr = learningrate

        ## 权重矩阵（一列）  --numpy.random.normal
        # 权重数组中的w_i_j，表示链接是从下一层的节点i到节点j --使用正态分布采样权重
        self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))

        # 设置激活函数S -scipy.special.expit(x)
        self.activation_function = lambda x: scipy.special.expit(x)


    # 训练神经网络（训练数据集整理后的输入列表，目标数值列表） --train数据集输入，训练神经网络，调整权重
    def train(self, inputs_list, targets_list):
        # 将输入列表转换为二维数组并转置
        # 将目标列表转换为二维数组并转置
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        # 矩阵点乘法--计算进入隐藏层的信号
        # 激活函数--计算离开隐藏层的信号
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        # 矩阵点乘法--计算进入最终输出层的信号
        # 激活函数--计算离开最终输出层的信号（最终输出）
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        # 隐蔽层和最终层的误差
        # 输入层和隐藏层的误差
        output_errors = targets - final_outputs
        hidden_errors = numpy.dot(self.who.T, output_errors)

        # 为隐藏层和最终层间权重矩阵进行更新
        # 为输入层和隐藏层间权重矩阵进行更新
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))


    # 查询神经网络（测试数据集整理后的输入列表） --训练后，test数据集输入，返回计算得出的检验样本集最终输出
    def query(self, inputs_list):
        # 将输入列表转换为二维数组并转置
        inputs = numpy.array(inputs_list, ndmin=2).T

        # 矩阵点乘法--计算进入隐藏层的信号
        # 激活函数--计算离开隐藏层的信号
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        # 矩阵点乘法--计算进入最终输出层的信号
        # 激活函数--计算离开最终输出层的信号（最终输出）
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        # 返回最终输出列表
        return final_outputs

        pass