
import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2) # "Poolowanie" - zmniejszanie efektywnego rozmiaru obrazka dwukrotnie
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(400, 250) #16 * 5 * 5
        self.fc2 = nn.Linear(250,160)
        self.fc3 = nn.Linear(160,100)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16*5*5) # 16 * 5 * 5
        x = F.relu(self.fc1(x)) ##Funkcja aktywacji - Rectifier -> f(x) = max(x,0)
        x = F.relu(self.fc2(x))
        x = self.fc3(x) #dodatek
        return x

def load():
    net = Net()
    net.load_state_dict(torch.load('NN/LearnedNetwork.pt'))
    net.eval()
    return net

def prepareImg(images):
    return torchvision.utils.make_grid(images)


def imshow(img):
    img = prepareImg(img)
    img = img / 2 + 0.5     # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()


transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

testset = torchvision.datasets.CIFAR100(root='./data', train=False,
                                       download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=1,
                                         shuffle=False, num_workers=0)

dataiter = iter(testloader)

def test(net):
    images, labels = dataiter.next()

    # print images
    print('Obrazki przedstawiaja: ', ' '.join('%5s' % classes[labels[j]] for j in range(1)))

    print(labels[0])

    ########################################################################
    # Okay, now let us see what the neural network thinks these examples above are:

    outputs = net(images)

    ########################################################################
    # The outputs are energies for the 10 classes.
    # The higher the energy for a class, the more the network
    # thinks that the image is of the particular class.
    # So, let's get the index of the highest energy:
    _, predicted = torch.max(outputs, 1)
    print('Przewidywany wynik: ', ' '.join('%5s' % classes[predicted[j]]
                                           for j in range(1)))
    imshow(torchvision.utils.make_grid(images))


classes = [
    'apple', 'aquarium_fish', 'baby', 'bear', 'beaver', 'bed', 'bee', 'beetle',
    'bicycle', 'bottle', 'bowl', 'boy', 'bridge', 'bus', 'butterfly', 'camel',
    'can', 'castle', 'caterpillar', 'cattle', 'chair', 'chimpanzee', 'clock',
    'cloud', 'cockroach', 'couch', 'crab', 'crocodile', 'cup', 'dinosaur',
    'dolphin', 'elephant', 'flatfish', 'forest', 'fox', 'girl', 'hamster',
    'house', 'kangaroo', 'keyboard', 'lamp', 'lawn_mower', 'leopard', 'lion',
    'lizard', 'lobster', 'man', 'maple_tree', 'motorcycle', 'mountain', 'mouse',
    'mushroom', 'oak_tree', 'orange', 'orchid', 'otter', 'palm_tree', 'pear',
    'pickup_truck', 'pine_tree', 'plain', 'plate', 'poppy', 'porcupine',
    'possum', 'rabbit', 'raccoon', 'ray', 'road', 'rocket', 'rose',
    'sea', 'seal', 'shark', 'shrew', 'skunk', 'skyscraper', 'snail', 'snake',
    'spider', 'squirrel', 'streetcar', 'sunflower', 'sweet_pepper', 'table',
    'tank', 'telephone', 'television', 'tiger', 'tractor', 'train', 'trout',
    'tulip', 'turtle', 'wardrobe', 'whale', 'willow_tree', 'wolf', 'woman',
    'worm'
]



def createimg():
    images, labels = dataiter.next()
    return images

def predictImg(net, images):
    outputs = net(images)
    _, predicted = torch.max(outputs,1)
    return classes[predicted[0]]


def example():
    net = load()
    boy = 0
    girl = 0
    man = 0
    baby = 0
    woman = 0

    for i in range(10000):
        image = createimg()
        result = predictImg(net, image)
        if result == "boy":
            boy +=1
        if (result == "girl"):
            girl+=1
        if result == "baby":
            baby+=1
        if result == "man":
            man +=1
        if result == "woman":
            woman+=1
    print("boys: ", boy)
    print("girls: ", girl)
    print("men: ", man)
    print("women: ", woman)
    print("babies: ", baby)

#example()