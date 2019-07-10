import random

class Perceptron:
    def __init__(self):
        self.dimension=2
        self.lr=0.005 #learning rate
        self.weights=[]
        self.bias=0
        self.m=random.randint(-5,5)
        self.b=random.randint(-5,5)
        for i in range(self.dimension):
            weight=0
            self.weights.append(weight)
    def predict(self,input_data):
        prediction=self.bias
        for i in range(self.dimension):
            prediction+=self.weights[i]*input_data[i] #computing the dot product
        if prediction>=0: #activation function
            prediction=1
        else:
            prediction=-1
        return prediction
    def train(self,epochs,dataset):
        for generation in range(epochs):
            for data in dataset:
                prediction = self.predict(data)
                solution = self.solution(data)
                error = solution - prediction
                print(self.weights, self.bias, error)
                self.bias+=self.lr*error
                for i in range(self.dimension):
                    adjustment=error*data[i]*self.lr
                    self.weights[i]+=adjustment

    def solution(self,data):
        x,y=data
        if self.m*x+self.b>=y: #f(x)<=mx+b -> 1
            return 1
        else:
            return -1

ai=Perceptron()
epochs=3
size_of_dataset=1000
data_set=[]
for i in range(size_of_dataset):
    data_set.append([random.randint(-10,10),random.randint(-10,10)])
ai.train(epochs,data_set)

size_of_testset=1000
succes_counter=0
fail_tracker=[]
for i in range(size_of_testset):
    test_data=[random.randint(-10,10),random.randint(-10,10)]
    guess=ai.predict(test_data)
    sol=ai.solution(test_data)
    if guess==sol:
        succes_counter+=1
    else:
        fail_tracker.append(i)

probability=succes_counter/size_of_testset*100
print('Trained function is: f(x)='+str(ai.m)+'x+'+str(ai.b))
print('The AI got an accuracy of: '+str(probability)+ '%')
print('Thats the approximated function: f(x)='+str(ai.weights[0]/ai.weights[1])+'x+'+str(ai.bias))
print(fail_tracker)




