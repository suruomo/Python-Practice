import numpy
import scipy.special
class neuralNetwork:
    # 初始化神经网络
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # 设置输入层，隐藏层，输出层结点个数,学习率
        self . inodes = inputnodes
        self . hnodes = hiddennodes
        self . onodes = outputnodes
        # 学习率
        self . lr = learningrate
        # 两个权重矩阵
        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        # 激活函数
        self.activation_function = lambda x: scipy.special.expit(x)
        pass
    # 训练神经网络
    def train(self, inputs_list, targets_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T
        # 1.根据输入，正向传播计算输出
        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)
        # 2.计算反向误差
        # output layer error is the (target - actual)
        output_errors = targets - final_outputs
        # hidden layer error is the output_errors, split by weights,
        hidden_errors = numpy.dot(self.who.T, output_errors)
        # 3.更新权重
        # update the weights for the links between the hidden and output layers
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), hidden_outputs)
        # update the weights for the links between the input and hidden layers
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), inputs)
        pass
    # 输入查询输出
    def query(self, inputs_list):
        # 输入值转置后，行变列
        inputs = numpy.array(inputs_list, ndmin=2).T
        # 1.计算各层输入输出
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)
        # 2.返回输出结果
        return final_outputs
# 设置输入层，隐藏层，输出层结点个数
input_nodes = 3
hidden_nodes = 3
output_nodes = 3
# 学习率是 0.5
learning_rate = 0.3
# 创建一个神经网络实例
n = neuralNetwork(input_nodes,hidden_nodes,output_nodes, learning_rate)
inputlist=[1.0,0.5,0.7]
targetlist=n.query([1.0,0.5,1.1])
print("训练前:",n.query([1.0,0.5,1.1]))
n.train(inputlist,targetlist)
targetlist=n.query([1.0,0.5,1.1])
print("1训练后:",n.query([1.0,0.5,1.1]))