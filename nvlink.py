import torch

# 检查当前设备是否可用
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 获取当前设备上的已分配内存大小
allocated_memory = torch.cuda.memory_allocated(device=device)

print(f"当前设备上已分配的内存大小：{allocated_memory / 1024**3:.2f} GiB")
exit()

import pynvml
###### 没有NVlink

def check_nvlink_support():
    try:
        # 初始化 NVML 库
        pynvml.nvmlInit()

        # 获取系统中 GPU 的数量
        device_count = pynvml.nvmlDeviceGetCount()
        print(device_count)
        # 遍历每个 GPU，检查其是否支持 NVLink
        for i in range(device_count):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            gpu_name = pynvml.nvmlDeviceGetName(handle)
            print(f"GPU {i}: {gpu_name}")

            # 检查 GPU 是否支持 NVLink
            for link in range(pynvml.NVML_NVLINK_MAX_LINKS):
                nvlink_capable = pynvml.nvmlDeviceGetNvLinkCapability(handle, link,
                                                                      pynvml.NVML_NVLINK_CAP_SYSMEM_ACCESS)
                if nvlink_capable == pynvml.NVML_SUCCESS:
                    print(f"  NVLink supported on link {link} of this GPU")
                elif nvlink_capable == pynvml.NVML_ERROR_NOT_SUPPORTED:
                    print(f"  NVLink not supported on link {link} of this GPU")
                else:
                    print(f"  Error checking NVLink capability on link {link}: {nvlink_capable}")

    except pynvml.NVMLError as e:
        print("NVML Error:", e)

    finally:
        # 最后要关闭 NVML 库
        pynvml.nvmlShutdown()


# 调用函数检查 NVLink 支持情况
check_nvlink_support()
