import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
my_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]],
                         dtype=torch.float32,
                         requires_grad=True,
                         device=device)
print(my_tensor)
print(my_tensor.requires_grad)
print(my_tensor.dtype)
print(my_tensor.device)
print(my_tensor.shape)
#%% initialization methods
x = torch.empty(size=(3,4))
print(x)
x = torch.zeros(size=(3,4))
print(x)
x = torch.randn(size=(3,4)) # numbers from 0 to 1
print(x)
x = torch.ones(size=(3,4))
print(x)
x = torch.eye(3,3) # diagonal ones [ 'I' matrix ]
print(x)
x = torch.arange(start=0, end=4,step=0.1, dtype=torch.float32)
print(x)
x = torch.linspace(start=0.1, end=1, steps=10)
print(x)
x = torch.empty(size=(3,4)).normal_(mean=0, std=1)
print(x)
x = torch.empty(size=(3,4)).uniform_(0, 1)
print(x)
x = torch.diag(torch.ones(3))
print(x)
#%% how to initialize and convert tensors to other types (int, float, double)
tensor = torch.arange(4)
print(tensor.bool()) # boolean
print(tensor.short()) # int16
print(tensor.long()) # int64 (important)
print(tensor.half()) # float64
print(tensor.float()) # float32 (super important)
print(tensor.double()) #float64
#%% how to convert numpy array to tensor and the opposite
import numpy as np
np_array = np.zeros((5, 5))
print(np_array)
numpay_to_tensor = torch.from_numpy(np_array)
print(numpay_to_tensor)
tensor_to_numpy = numpay_to_tensor.numpy()
print(tensor_to_numpy)
#%% tensor math & comparison operation
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
y = torch.tensor([[54, 6, 88], [10, 45, 61]])
# element wise mult
z = x * y
print(z)
# addition
x_plus_y = x + y
x_plus__y = torch.add(x, y)
print(x_plus_y)
# subtraction
x_sub_y = x - y
x_sub__y = torch.sub(x, y)
print(x_sub__y)
#division
x_div_y = torch.div(x, y)
print(x_div_y)
x_div__y = torch.true_divide(x, y)
print(x_div__y)
# inplace operation
t = torch.tensor([[1, 2, 3], [4, 5, 6]])
t.add_(x)
print(t)
t += x
print(t)
# exponentiation
z = x.pow(2)
z_ = x ** 2
print(z)
# simple comparison
z = x < 0
print(z)
z = x > 0
print(z)
# matrix multiplication
x1 = torch.rand((2, 5))
x2 = torch.rand((5, 3))
x3 = torch.mm(x1, x2)
x3_ = x1.mm(x2)
print(x3)
# matrix exponentation
x = torch.randn(5, 5)
x.matrix_power(3)
print(x)
# dot product
x = torch.tensor([1, 2, 3])
y = torch.tensor([54, 6, 88])
z = torch.dot(x, y)
print(z)
# other useful tensor operations
sum_x = torch.sum(x, dim=0)
print(sum_x)
values, indices = torch.max(x, dim=0)
print(values, indices)
values, indices = torch.min(x, dim=0)
print(values, indices)
abs_x = torch.abs(x)
print(abs_x)
z = torch.argmax(x, dim=0) # same as torch.max, but it's give only the index
print(z)
z = torch.argmin(x, dim=0)
print(z)
mean_x = torch.mean(x.float(), dim=0) # it takes only float values
print(mean_x)
z = torch.eq(x.float(), y.float()) # # it takes only float values
print(z)
sorted_y, indices = torch.sort(y, dim=0, descending=True)
print(sorted_y)
z = torch.clamp(x.float(), min=0, max=1) # values are under 0 becomes 0 & values are upper 1 becomes 1
print(z)
x = torch.tensor([1, 0, 0, 1, 0, 0, 1], dtype=torch.bool)
z = torch.any(x, dim=0)
print(z)
z = torch.all(x, dim=0)
print(z)
#%% tensor indexing
batch_size = 10
features = 25
x = torch.randn(batch_size, features)
print(x[0].shape) # give me the features of the first batch
print(x[:, 0].shape) # give me the first feature of all the batches
print(x[2, 0:10].shape) # give me the first 10 features of the third batch
# fancy indexing
x = torch.arange(5,15)
index = [2, 5, 8]
print(x[index])
x = torch.rand(3, 5)
rows = torch.tensor([1, 0])
cols = torch.tensor([4, 0])
print(x[rows, cols])
# more advanced indexing
x = torch.arange(10)
print(x[(x > 2) & (x < 5)]) # '|' for 'or', '&' for 'and'
print(x[x.remainder(2) == 0]) # divide all the values on 2 and give the even values
# other useful operations
print(torch.where(x > 5, x, x**2)) # if x > 5 give me x, if it's not, then give me x**2
print(torch.tensor([1,5,2,3,4,8,6,7,9,10]).unique()) # ranking the tensor [1,2,3,4,5,....]
print(x.ndimension()) # give the dimension of the tensor
print(x.numel()) # give the number of elements in the tensor
#%% tensor reshaping
x = torch.arange(60)
x_5x2x3x2 = x.view(5, 2, 3, 2) # reshaping the 1 dimensional tensor to 4
x__5x2x3x2 = x.reshape(5, 2, 3, 2)
x___5x2x3x2 = x.contiguous().view(60)
print(x_5x2x3x2.shape)
print(x___5x2x3x2.shape)
x1 = torch.rand(2, 5)
x2 = torch.rand(2, 5)
print(torch.cat((x1, x2), dim=0).shape) # to Concatenation the two tensors
z = x1.view(-1) # to flatten the tensor to be only one row
print(z)
batch = 64
x = torch.rand((batch, 2, 5))
z = x.view(batch, -1) # to marge the dimensions
print(z.shape)
z = x.permute(0, 2, 1) # to switching between the dimensions
print(z.shape)
x = torch.arange(10)
print(x.unsqueeze(0).shape) # to add dimension [1] to the left (row)
print(x.unsqueeze(1).shape)# to add dimension [1] ro the right (column)
x = torch.arange(10).unsqueeze(0).unsqueeze(2) # 1x10x1 dimensions
print(x.shape)
z = x.squeeze(0) # it remove only the dim that is equal to 1
print(z.shape)