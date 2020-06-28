# https://www.mscto.com/ai/271799.html
from torchvision import transforms, utils, datasets
from torch.utils.data import Dataset, DataLoader
from torch.autograd import Variable
import torch.optim as optim
import torch.nn as nn
from PIL import Image
import numpy as np
import torch
import glob
import os

# 定义DataTransform
data_transform = transforms.Compose([
    transforms.Resize(84),
    transforms.CenterCrop(84),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],  # 均值和标准方差参考AlexNet
                         std=[0.229, 0.224, 0.225])
])


def sort(cat_path, dog_path, output_path):
	cat = [i.replace('\\', '/')+',0' for i in glob.glob(cat_path+'*.jpg')]
	dog = [i.replace('\\', '/')+',1' for i in glob.glob(dog_path+'*.jpg')]
	with open(output_path+'label.txt', 'a') as f:
    	for i in cat+dog:
        	f.write(i+'\n')


# 重定义Dataset
class MyDataSet(Dataset):
    def __init__(self, txt_path, data_transforms):
        self.imgPathArr, self.labelArr, self.transforms = [], [], data_transforms
        with open(txt_path, 'rb') as f:
            for line in f.readlines():
                file_arr = str(line.strip(), encoding='utf-8').split(",")
                self.imgPathArr.append(file_arr[0])
                self.labelArr.append(file_arr[1])

    def __getitem__(self, index):
        label = np.array(int(self.labelArr[index]))
        pil_img = Image.open(self.imgPathArr[index])
        data = self.transforms(pil_img) if self.transforms else torch.from_numpy(np.asarray(pil_img))
        return data, label

    def __len__(self):
        return len(self.imgPathArr)


# CNN
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Sequential(nn.Conv2d(3, 16, 5, 1, 2), nn.ReLU(), nn.MaxPool2d(2))
        self.conv2 = nn.Sequential(nn.Conv2d(16, 32, 5, 1, 2), nn.ReLU(), nn.MaxPool2d(2))
        self.out = nn.Linear(32 * 21 * 21, 2)

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)
        output = self.out(x)
        return output, x


def main():
	train, test = './data/train/', './data/test/'
    train_dataset = MyDataSet('label.txt', data_transform)
    train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True, num_workers=4)
    test_dataset = MyDataSet('label.txt', data_transform)
    test_loader = DataLoader(test_dataset, batch_size=4, shuffle=True, num_workers=4)

    net = Net()
    cirterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.0001, momentum=0.9)

    # Train
    try:
        for epoch in range(3):
            running_loss = 0.0
            for i, data in enumerate(train_loader, 0):
                inputs, labels = data
                inputs, labels = Variable(inputs), Variable(labels.long())
                outputs = net(inputs)[0]
                loss = cirterion(outputs, labels)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                running_loss += loss.item()

                if i % 100 == 99:
                    print('[%d %5d] loss: %.3f' % (epoch+1, i+1, running_loss/100))
                    running_loss = 0.0
    finally:
        print('finished training!')
        torch.save(net.state_dict(), 'net_params.pkl')

    # Test
    correct, total = 0, 0
    for data in test_loader:
        images, labels = data
        images, labels = Variable(images), Variable(labels)
        outputs = net(images)[0]
        predicted = torch.max(outputs.data, 1)[1].data.numpy()
        total += labels.size(0)
        correct += (predicted == labels.numpy()).sum()
        print(f'Accuracy of the network on the 2000 test images: {100*correct/total}%')


if __name__ == '__main__':
    main()
