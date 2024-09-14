import netCDF4 as nc
import pandas as pd
import numpy as np


def nc_to_csv(nc_file_path, csv_file_path):
    # 打开.nc文件
    dataset = nc.Dataset(nc_file_path)

    # 提取时间信息并转换格式
    time_var = dataset.variables['time']
    real_time = nc.num2date(time_var[:], time_var.units)

    time_data = []
    for i in range(len(real_time)):
        time_str = f"{real_time[i].year}/{real_time[i].month:02d}/{real_time[i].day:02d} {real_time[i].hour:02d}:{real_time[i].minute:02d}"
        time_data.append(time_str)

    time_data = np.array(time_data)
    print(time_data)
    # 提取维度信息
    latitude = dataset.variables['latitude'][:]
    longitude = dataset.variables['longitude'][:]
    expver = dataset.variables['expver'][:]

    # 创建网格
    lon, lat, t, exp = np.meshgrid(longitude, latitude, time_data, expver, indexing='ij')

    # 展平网格
    lon = lon.flatten()
    lat = lat.flatten()
    t = t.flatten()
    exp = exp.flatten()

    # 提取数据
    data_dict = {
        'longitude': lon,
        'latitude': lat,
        'time': t,
        'expver': exp
    }

    # 处理每个变量
    variables = ['u10', 'v10', 'd2m', 't2m', 'e', 'mx2t', 'mn2t', 'sp', 'tcc', 'tp']
    for var in variables:
        data = dataset.variables[var][:]

        # 打印变量的名称和维度信息
        print(f"Variable: {var}, Dimensions: {data.shape}")

        if data.ndim == 4:  # 如果变量有四个维度（time, expver, lat, lon）
            data = data.reshape(-1)  # 展平数据
            data_dict[var] = data
        else:
            raise ValueError(f"Unexpected number of dimensions for variable {var}")

    # 将数据转换为DataFrame
    df = pd.DataFrame(data_dict)

    # 保存为.csv文件
    df.to_csv(csv_file_path, index=False)

# 示例使用
nc_file_path = 'C:/Users/zihanli/Desktop/adaptor_mars.nc'
csv_file_path = 'C:/Users/zihanli/Desktop/test.csv'
nc_to_csv(nc_file_path, csv_file_path)

